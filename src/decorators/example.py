"""
Decorator examples - functions that modify the behavior of other functions
"""

import functools
import time


# Simple decorator example
def my_decorator(func):
    """A simple decorator that prints before and after function execution"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper


@my_decorator
def say_hello(name):
    """A simple function to greet someone"""
    return f"Hello, {name}!"


# Decorator with arguments
def repeat(times):
    """A decorator that repeats function execution"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


@repeat(times=3)
def greet(name):
    return f"Hi {name}!"


# Timing decorator
def timer(func):
    """A decorator that measures execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    """Simulate a slow function"""
    time.sleep(1)
    return "Done!"


def example_wrapper(func):
    # Python is an interpreted language, this print statement will execute when the decorator is read
    print("Example wrapper decorator is being applied")
    return func

@example_wrapper
def example_func():
    print("Hello World")


if __name__ == "__main__":
    # Test the decorators
    print("=== Simple Decorator ===")
    print(say_hello("Alice"))
    
    print("\n=== Repeat Decorator ===")
    print(greet("Bob"))
    
    print("\n=== Timer Decorator ===")
    print(slow_function())

    print("\n=== Example Wrapper ===")
    example_func()
