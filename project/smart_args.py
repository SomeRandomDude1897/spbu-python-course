import copy
from typing import Callable, Any
from inspect import signature


class Evaluated:

    def __init__(self, func: Callable) -> None:
        assert not isinstance(
            func, Isolated
        ), "Not possible to combine Evaluated and Isolated"

        self.func = func

    def calc(self) -> Any:
        return self.func()


class Isolated:

    def __init__(self) -> None:
        pass


def smart_args(func: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(*args: Any, **kwargs: Any) -> Any:

        # Check for Evaluated and Isolated in positional arguments
        for arg in args:
            assert not isinstance(
                arg, (Evaluated, Isolated)
            ), f"Cannot use Evaluated or Isolated with positional arguments."

        sig = signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for key, value in bound_args.arguments.items():
            if isinstance(value, Evaluated):
                bound_args.arguments[key] = value.calc()
            elif isinstance(value, (dict, list)):
                bound_args.arguments[key] = copy.deepcopy(value)

        return func(*bound_args.args, **bound_args.kwargs)

    return wrapper
