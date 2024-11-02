from collections import OrderedDict


def cache(storage_size):
    """
    A decorator that caches the results of a function call with a limited storage size.

    Args:
        storage_size (int): The maximum number of cached results to store.

    Raises:
        Exception: If the storage size is zero or negative.

    Returns:
        function: A decorator that adds caching to the decorated function.
    """
    if storage_size <= 0:
        raise Exception("Storage size can't be zero or less")
    storage = OrderedDict()

    def decorator(func):
        """
        The decorator that wraps the function to add caching capability.

        Args:
            func (function): The function to be decorated.

        Returns:
            function: The wrapped function with caching.
        """

        def wrapper(*args, **kwargs):
            """
            The wrapper function that checks the cache before executing the function.

            Args:
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.

            Returns:
                Any: The result of the function call, either from cache or computed.
            """
            print(args, kwargs, storage)
            # Searching with 'in' is time-consuming; doing it this way because I'm not sure how else to get ~O(1)
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
