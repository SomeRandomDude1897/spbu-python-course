import threading
from typing import Callable, Any, List, Dict


class PoolThread(threading.Thread):
    """
    A worker thread that belongs to a thread pool. The thread runs a task when assigned and
    frees itself back to the pool upon task completion.
    """

    def __init__(
        self,
        pool: "ThreadPool",
        number: int,
        target: Callable = None,
        args: tuple = (),
        kwargs: dict = {},
    ):
        """
        Initialize the PoolThread with a thread pool, thread number, and an optional task.

        :param pool: The thread pool managing this thread.
        :param number: The index number of this thread in the pool.
        :param target: The task (function) for the thread to execute.
        :param args: The arguments to pass to the task.
        :param kwargs: The keyword arguments to pass to the task.
        """
        super().__init__()
        self._target: Callable = target
        self._args: tuple = args
        self._kwargs: dict = kwargs
        self._pool: "ThreadPool" = pool
        self._thread_number: int = number

    def set_task(
        self, target: Callable = None, args: tuple = (), kwargs: dict = {}
    ) -> None:
        """
        Set the task (function) for the thread to execute.

        :param target: The task (function) to run.
        :param args: The arguments to pass to the task.
        :param kwargs: The keyword arguments to pass to the task.
        """
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self) -> None:
        """
        Run the assigned task, then free the thread back to the pool.
        """
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            self._pool.free_thread(self._thread_number)


class ThreadPool:
    """
    A thread pool that manages a set of worker threads, which can execute tasks concurrently.
    Tasks can be enqueued, and the pool will manage their execution.
    """

    def __init__(self, thread_count: int):
        """
        Initialize the ThreadPool with a set number of threads.

        :param thread_count: The number of threads in the pool.
        """
        self._thread_count: int = thread_count
        self._threads: List[PoolThread] = [
            PoolThread(self, _) for _ in range(self._thread_count)
        ]
        self._task_queue: List[Dict[str, Any]] = []
        self._disposed: bool = False

    def _setup_task(self, func: Callable, args: tuple, kwargs: dict) -> bool:
        """
        Assign a task to an available thread if one is free.

        :param func: The task (function) to execute.
        :param args: The arguments for the task.
        :param kwargs: The keyword arguments for the task.
        :return: True if a thread was available and the task was assigned, False otherwise.
        """
        for _ in range(self._thread_count):
            if not self._threads[_].is_alive():
                self._threads[_].set_task(func, args, kwargs)
                self._threads[_].start()
                return True
        return False

    def free_thread(self, thread_number: int) -> None:
        """
        Free a thread after it completes its task and assign a new task if one is available in the queue.

        :param thread_number: The index number of the thread that finished its task.
        """
        self._threads[thread_number] = PoolThread(self, thread_number)
        if len(self._task_queue) > 0:
            next_task = self._task_queue.pop()
            self._threads[thread_number].set_task(
                next_task["func"],
                next_task["args"],
                next_task["kwargs"],
            )
            self._threads[thread_number].start()
        elif self._disposed and not self._has_active_tasks():
            self._die()

    def _die(self) -> None:
        """
        Clean up all resources and clear the thread pool when it is disposed.
        """
        self._threads.clear()
        self._task_queue.clear()
        del self._threads
        del self._task_queue

    def get_threads_amount(self) -> int:
        """
        Get the number of threads in the pool.

        :return: The number of threads.
        """
        return len(self._threads)

    def _has_active_tasks(self) -> bool:
        """
        Check if there are any threads currently working on a task.

        :return: True if there are active tasks, False otherwise.
        """
        return any(thread.is_alive() for thread in self._threads)

    def dispose(self) -> None:
        """
        Mark the thread pool for disposal. If there are no active tasks or tasks in the queue,
        the pool will be cleaned up.
        """
        self._disposed = True
        if not self._has_active_tasks() and len(self._task_queue) == 0:
            self._die()

    def enqueue(
        self, func: Callable = None, args: list = [], kwargs: dict = {}
    ) -> None:
        """
        Enqueue a task to be executed by a thread. If no thread is available, the task is added to a queue.

        :param func: The task (function) to execute.
        :param args: The arguments for the task.
        :param kwargs: The keyword arguments for the task.
        """
        if self._disposed:
            raise Exception("Cannot use disposed thread pool")
        if not self._setup_task(func, tuple(args), kwargs):
            self._task_queue.append({"func": func, "args": args, "kwargs": kwargs})

    def __str__(self) -> str:
        """
        Return the current status of all threads in the pool.

        :return: A string representing the status of each thread.
        """
        log = ""
        for i in range(self._thread_count):
            status = "working" if self._threads[i].is_alive() else "waiting"
            log += f"Thread {i + 1} in state {status}"
            if i != self._thread_count - 1:
                log += "\n"
        return log

    def join(self) -> None:
        """
        Wait for all active tasks to complete before exiting.
        """
        while self._has_active_tasks():
            pass
