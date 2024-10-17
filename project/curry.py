def curry_explicit(arity):
    if arity < 0:
        raise Exception("Arity must be non-negative")

    def decorator(func):
        def inner_curry(*args):
            def next_func(*new_args):
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
    if arity < 0:
        raise Exception("Arity must be non-negative")

    def decorator(func):
        def inner_uncurry(*args):
            if len(args) != arity:
                raise TypeError(f"Expected {arity} arguments, got {len(args)}")
            result = func
            for arg in args:
                result = result(arg)
            return result

        return inner_uncurry

    return decorator
