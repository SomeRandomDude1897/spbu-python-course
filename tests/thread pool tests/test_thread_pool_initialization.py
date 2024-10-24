from project.thread_pool import ThreadPool


def test_threadpool_initialization():
    pool_size = 5
    pool = ThreadPool(pool_size)
    assert (
        pool.get_threads_amount() == pool_size
    ), "ThreadPool инициализирован с неверным количеством потоков"


def test_threads_not_alive_initially():
    pool = ThreadPool(3)
    for thread in pool._threads:
        assert (
            not thread.is_alive()
        ), "Потоки не должны быть активными до добавления задач"


def test_task_queue_empty_initially():
    pool = ThreadPool(4)
    assert (
        len(pool._task_queue) == 0
    ), "Очередь задач должна быть пустой при инициализации"
