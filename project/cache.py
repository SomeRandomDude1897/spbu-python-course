from collections import OrderedDict


def cache(storage_size):
    if storage_size <= 0:
        raise Exception("Storage size cant be zero or less")
    storage = OrderedDict()

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(args, kwargs, storage)
            # через in искать долго по времени, делаю так потому что глупый и не знаю как еще за ~O(1)
            try:
                return storage[str(args) + str(kwargs)]
            except:
                val = func(*args, **kwargs)
                if len(storage) + 1 >= storage_size:
                    storage.popitem(last=False)
                storage[str(args) + str(kwargs)] = val
                return val

        return wrapper

    return decorator
