import time

def to_string(seconds: float) -> str:
    """
    Convert a time duration in seconds to a human-readable string format.

    Parameters:
    - seconds (float): The time in seconds to be formatted.

    Returns:
    - str: A formatted string representing the time in a human-readable format.

    Description:
    This function takes a time duration in seconds and formats it into a human-readable string.
    If the duration is greater than or equal to 60 seconds, it converts the time into minutes and seconds.
    It returns a string that represents the time in the format "X minutes and Y seconds" or "Z seconds"
    if the duration is less than 60 seconds.
    """
    if seconds >= 60:
        minutes = int(seconds / 60)
        seconds = int(seconds % 60)
        return (
            f"{minutes} {'minute' if minutes == 1 else 'minutes'} and "
            f"{seconds} {'second' if seconds == 1 else 'seconds'}"
        )
    elif seconds == 1:
        return
    return f"{seconds:.2f} {'second' if seconds == 1 else 'seconds'}"

def timer(func):
    """
    Decorator to measure and print the execution time of a function.

    Parameters:
    - func (callable): The function to be timed.

    Returns:
    - wrapper: A wrapper function that times the execution of the provided function.

    Description:
    This function is a decorator that takes a function as input and returns a new function (wrapper)
    that wraps around the provided function. When the wrapped function is executed, it measures the time
    it takes to run and prints the duration in a human-readable format using the to_string function.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that measures and prints the execution time of the provided function.

        Parameters:
        - *args: Variable-length argument list.
        - **kwargs: Arbitrary keyword arguments.

        Returns:
        - result: The result of the wrapped function.

        Description:
        This wrapper function calculates the elapsed time it takes for the provided function to run.
        It then prints the duration in a human-readable format using the to_string function.
        The wrapped function is executed with the provided arguments and keyword arguments.
        The result of the wrapped function is returned.
        """
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Done in {to_string(elapsed)}")
        return result

    return wrapper
