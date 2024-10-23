from project.thread_pool import ThreadPool


def test_task_queue():
    result = []

    def sample_task(x):
        result.append(x)

    pool = ThreadPool(2)
    # Добавляем больше задач, чем потоков
    for i in range(5):
        pool.enqueue(sample_task, args=(i,))
    # Ожидаем завершения задач
    pool.join()
    assert sorted(result) == [0, 1, 2, 3, 4], "Не все задачи из очереди были выполнены"


def test_task_queue_order():
    result = []

    def sample_task(x):
        result.append(x)

    pool = ThreadPool(2)
    for i in range(5):
        pool.enqueue(sample_task, args=(i,))
    # Ожидаем завершения задач
    pool.join()
    assert result == [0, 1, 2, 3, 4], "Задачи не были выполнены в порядке добавления"
