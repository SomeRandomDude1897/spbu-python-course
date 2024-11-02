import copy
from typing import Callable, Any
from inspect import signature


class Evaluated:
    """
    Wrapper class that encapsulates a function to be evaluated when needed.

    Attributes:
        func (Callable): The function to be evaluated.

    Methods:
        calc() -> Any: Evaluates the stored function and returns the result.
    """

    def __init__(self, func: Callable) -> None:
        """
        Initializes the Evaluated instance with a function.

        Args:
            func (Callable): The function to be evaluated.

        Raises:
            AssertionError: If 'func' is an instance of Isolated, since combining Evaluated and Isolated is not allowed.
        """
        assert not isinstance(
            func, Isolated
        ), "Not possible to combine Evaluated and Isolated"

        self.func = func

    def calc(self) -> Any:
        """
        Evaluates the stored function and returns its result.

        Returns:
            Any: The result of the evaluated function.
        """
        return self.func()


class Isolated:
    """
    Marker class indicating that an argument should be isolated.

    This class can be used to signal that a deep copy should be made of the argument,
    or to prevent unintended side effects from mutable arguments.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of Isolated.
        """
        pass


def smart_args(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that processes function arguments to handle Evaluated and Isolated instances,
    and deep copies mutable arguments to prevent side effects.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The wrapped function with smart argument handling.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function that processes arguments before calling the original function.

        Raises:
            AssertionError: If Evaluated or Isolated instances are used in positional arguments.

        Returns:
            Any: The result of the original function call with processed arguments.
        """
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
