from project.thread_pool import ThreadPool
import pytest


def test_dispose():
    pool = ThreadPool(2)
    pool.dispose()
    assert pool._disposed, "ThreadPool не помечен как удаленный после dispose()"


def test_enqueue_after_dispose():
    pool = ThreadPool(2)
    pool.dispose()
    with pytest.raises(Exception) as exc_info:
        pool.enqueue(lambda: None)
    assert "Cannot use disposed thread pool" in str(
        exc_info.value
    ), "Не было исключения при добавлении задачи после dispose()"


def test_dispose_clears_threads():
    pool = ThreadPool(2)
    pool.dispose()
    assert not hasattr(pool, "_threads"), "Список потоков не очищен после dispose()"


def test_dispose_clears_task_queue():
    pool = ThreadPool(2)
    pool.dispose()
    assert not hasattr(pool, "_task_queue"), "Очередь задач не очищена после dispose()"
