import threading


class PoolThread(threading.Thread):
    def __init__(self, pool, number, target=None, args=(), kwargs={}):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._pool = pool
        self._thread_number = number

    def set_task(self, target=None, args=(), kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            self._pool.free_thread(self._thread_number)


class ThreadPool:
    def __init__(self, thread_count):
        self._thread_count = thread_count
        self._threads = [PoolThread(self, _) for _ in range(self._thread_count)]
        self._task_queue = []
        self._disposed = False

    def _setup_task(self, func, args, kwargs):
        for _ in range(self._thread_count):
            if not self._threads[_].is_alive():
                self._threads[_].set_task(func, args, kwargs)
                self._threads[_].start()
                return True
        return False

    def free_thread(self, thread_number):
        self._threads[thread_number] = PoolThread(self, thread_number)
        if len(self._task_queue) > 0:
            self._threads[thread_number].set_task(
                self._task_queue[-1]["func"],
                self._task_queue[-1]["args"],
                self._task_queue[-1]["kwargs"],
            )
            self._task_queue.pop()
            self._threads[thread_number].start()
        elif self._disposed and not self._has_active_tasks():
            self._die()

    def _die(self):
        print("лол что")
        self._threads.clear()
        self._task_queue.clear()
        del self._threads
        del self._task_queue

    def get_threads_amount(self):
        return len(self._threads)

    def _has_active_tasks(self):
        for thread in self._threads:
            if thread.is_alive():
                return True
        return False

    def dispose(self):
        self._disposed = True
        if not self._has_active_tasks() and len(self._task_queue) == 0:
            self._die()

    def enqueue(self, func=None, args=[], kwargs={}):
        if self._disposed:
            raise Exception("Cannot use disposed thread pool")
        if not self._setup_task(func, args, kwargs):
            self._task_queue.append({"func": func, "args": args, "kwargs": kwargs})

    def __str__(self):
        log = ""
        for _ in range(self._thread_count):
            log += (
                "thread "
                + str(_ + 1)
                + " in state "
                + ("working" if self._threads[_].is_alive() else "waiting")
                + ("\n" if _ != self._thread_count - 1 else "")
            )
        return log

    def join(self):
        while self._has_active_tasks():
            ...
