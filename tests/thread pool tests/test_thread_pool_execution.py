from project.thread_pool import ThreadPool


def test_task_execution():
    result = []

    def sample_task():
        result.append(1)

    pool = ThreadPool(2)
    pool.enqueue(sample_task)
    pool.enqueue(sample_task)
    pool.join()
    assert len(result) == 2, "Не все задачи были выполнены"


def test_task_with_args():
    result = []

    def sample_task(x):
        result.append(x)

    pool = ThreadPool(2)
    pool.enqueue(sample_task, args=(10,))
    pool.enqueue(sample_task, args=(20,))
    pool.join()
    assert result == [10, 20], "Задачи с аргументами выполнены некорректно"


def test_task_with_kwargs():
    result = []

    def sample_task(x=None, y=None):
        result.append((x, y))

    pool = ThreadPool(2)
    pool.enqueue(sample_task, kwargs={"x": 1, "y": 2})
    pool.enqueue(sample_task, kwargs={"x": 3, "y": 4})
    pool.join()
    assert result == [
        (1, 2),
        (3, 4),
    ], "Задачи с именованными аргументами выполнены некорректно"


def test_parallel_execution():
    import time

    def sample_task(duration):
        time.sleep(duration)

    pool = ThreadPool(2)
    start_time = time.time()
    pool.enqueue(sample_task, args=(1,))
    pool.enqueue(sample_task, args=(1,))
    # Ожидаем завершения задач
    pool.join()
    end_time = time.time()
    total_time = end_time - start_time
    assert total_time < 2, "Задачи не выполнялись параллельно"
