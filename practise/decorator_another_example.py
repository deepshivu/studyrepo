import time  # Importing time module for measuring execution time

def timing_decorator(func):
    def wrapper(*args, **kwargs):  # Accepting arguments using *args and **kwargs
        start_time = time.perf_counter()  # Start timing
        result = func(*args, **kwargs)    # Execute the original function
        end_time = time.perf_counter()    # End timing
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to complete.")
        return result  # Return the original function's result
    return wrapper

# Applying the decorator to a sample function
@timing_decorator
def calculate_sum(n):
    total = sum(range(n))
    print(f"Sum of numbers from 0 to {n-1} is {total}")

# Calling the decorated function
calculate_sum(1000000)
