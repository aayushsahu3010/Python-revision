# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"Function {func.__name__} took {end-start:.4f} seconds")
#         return result
#     return wrapper

# @timer
# def exmaple_function(n):
#     time.sleep(n)
#     return f"Slept for {n} seconds"

# exmaple_function(2)

# import time

# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value = ','.join(str(arg) for arg in args )
#         kwargs_value =','.join(f"{k}={v}" for k,v in kwargs.items())
#         print(f"Calling {func.__name__} with arguments: {args_value} and keyword arguments: {kwargs_value}")
#         return func(*args,**kwargs)

#     return wrapper


# @debug
# def greet(name ,greeting ="hello"):
#      print(f"{greeting}, {name}!")

# @debug
# def add(a,b):
#     return a+b

# print(add(3,5))
# greet("Aayush")


# -------------------------------
import time


def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print("Fetching from cache")
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(6, 5))
print(long_running_function(2, 4))
print(long_running_function(3, 5))