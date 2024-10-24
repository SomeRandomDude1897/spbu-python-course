from project.thread_pool import ThreadPool
import time
import threading


def test_thread_states():
    import time

    def sample_task(duration):
        time.sleep(duration)

    pool = ThreadPool(2)
    pool.enqueue(sample_task, args=(1,))
    pool.enqueue(sample_task, args=(1,))
    # Немедленно проверяем состояние потоков
    states_before = [thread.is_alive() for thread in pool._threads]
    assert all(states_before), "Потоки должны быть активными во время выполнения задач"

    # Ожидаем завершения задач
    pool.join()

    states_after = [thread.is_alive() for thread in pool._threads]
    assert not any(
        states_after
    ), "Потоки не должны быть активными после завершения задач"


def test_str_representation():
    pool = ThreadPool(2)

    def amogus():
        time.sleep(1)
        return True

    pool.enqueue(amogus)
    # Метод __str__ должен отражать состояние потоков
    output = str(pool)
    assert (
        "Thread 1 in state working" in output
    ), "Состояние потоков некорректно отображается в __str__"


def test_get_threads_amount():
    pool = ThreadPool(3)

    def amogus():
        time.sleep(1)
        return True

    initial_threads = threading.active_count()
    pool.enqueue(amogus)
    pool.enqueue(amogus)
    pool.enqueue(amogus)
    assert (
        threading.active_count() == initial_threads + 3
    ), "потоков занято правильтное количетсво победа!!!!!!!"
