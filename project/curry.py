def curry_explicit(arity):
    """
    A decorator that curries a function to the specified arity.

    Args:
        arity (int): The number of arguments the function accepts.

    Raises:
        Exception: If the provided arity is negative.

    Returns:
        function: A decorator that transforms the input function into a curried version.
    """
    if arity < 0:
        raise Exception("Arity must be non-negative")

    def decorator(func):
        """
        Decorator that curries the given function.

        Args:
            func (function): The function to be curried.

        Returns:
            function: The curried version of the input function.
        """

        def inner_curry(*args):
            """
            Inner function that accumulates arguments until the arity is met.

            Args:
                *args: Variable length argument list.

            Returns:
                function or result: Returns the function itself if not enough arguments are provided,
                or the result of the function call when enough arguments are accumulated.
            """

            def next_func(*new_args):
                """
                Function that accepts the next argument.

                Args:
                    *new_args: The next argument to be added.

                Raises:
                    Exception: If more than one argument is provided at once.

                Returns:
                    function: The updated inner_curry function with the new argument.
                """
                if len(new_args) != 1:
                    raise Exception("Only one argument can be provided at a time")
                return inner_curry(*(args + new_args))

            if arity == len(args):
                return func(*args)
            else:
                return next_func

        return inner_curry

    return decorator


def uncurry_explicit(arity):
    """
    A decorator that transforms a curried function into an uncurried function.

    Args:
        arity (int): The number of arguments the function accepts.

    Raises:
        Exception: If the provided arity is negative.

    Returns:
        function: A decorator that transforms the input curried function into an uncurried version.
    """
    if arity < 0:
        raise Exception("Arity must be non-negative")

    def decorator(func):
        """
        Decorator that uncurries the given curried function.

        Args:
            func (function): The curried function to be uncurried.

        Returns:
            function: The uncurried version of the input function.
        """

        def inner_uncurry(*args):
            """
            Function that applies all arguments at once to the curried function.

            Args:
                *args: Variable length argument list.

            Raises:
                TypeError: If the number of arguments does not match the arity.

            Returns:
                Any: The result of applying all arguments to the curried function.
            """
            if len(args) != arity:
                raise TypeError(f"Expected {arity} arguments, got {len(args)}")
            result = func
            for arg in args:
                result = result(arg)
            return result

        return inner_uncurry

    return decorator
