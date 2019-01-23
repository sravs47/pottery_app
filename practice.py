# class sravani:
#    def __init__(self,me,nithin):
#        self.me=me
#        self.nithin = nithin
#
#    def myfunc(self):
#        print("my name is " +self.me)
#
# obj1 = sravani("sravani","nithin")
# obj1.myfunc()
#
#
# class test:
#     y = 10
#
# obj2 = test()
#
# print(obj2.y)
#
# class selftesting:
#     def __init__(itsmeself,me,nithin):
#         itsmeself.me = me
#         itsmeself.nithin = nithin
#
#     def testingself(itsmeself):
#         print("printing the values of the class " + itsmeself.nithin)
#
# obj3 = selftesting("sravani","nithin")
# obj3.nithin="venkat"
# obj3.testingself()
#
#
# x = lambda s,t:s+t
#
# print("lambda value",x(5,6))
#

#
# def say_hello(name):
#     print( f'Hello {name}')
#
# def be_awesome(name):
#     print( f"Yo {name}, together we are the awesomest")
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
# greet_bob(be_awesome)

from datetime import datetime
import math,random,time,functools
# def not_during_night(func):
#     def wrapper():
#         if 7<=datetime.now().hour<22:
#             func()
#         else:
#             pass
#     return wrapper
#
# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
# @do_twice
# def say_whee(name):
#     print("Whee!" +name)
#     return name
#
# just = say_whee("sravani")
# print(just)
#
# print(say_whee.__name__)


# -------------------- Syntax for decorators ---------------
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         value = func(*args, **kwargs)
#         return value
#     return wrapper

# def timer(func):
#     """print the runtime of the decorated function """
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args , **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time-start_time
#         print(f'finished {func.__name__!r} in {run_time:.4f} secs')
#         return value
#     return wrapper
#
# @timer
# def waste_some_time(num_times):
#     for i in range(num_times):
#         sum([i**2 for i in range(10000)])
#
# waste_some_time(1)
#
# help(time.perf_counter())

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr+kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper

# @debug
# def make_greeting(name , age = None):
#     if age is None:
#         print(f"Howdy {name}")
#     else :
#         print (f"whoa {name}! {age} already, you are growing up")
#
# make_greeting("Benjamin",50)

# math.factorial = debug(math.factorial)
#
# def approximate_e(terms = 18):
#     return sum(1/math.factorial(n) for n in range(terms))
#
# approximate_e(4)
#
#
# PLUGINS = dict()
#
# def register(func):
#     """Register a function as plug-in"""
#     PLUGINS[func.__name__]=func
#     return func
#
# @register
# def say_hello(name):
#     print(f"Hello {name}")
#
# @register
# def be_awesome(name):
#     print(f"Yo {name}, together we are awesomest!")
#
# def randomly_greet(name):
#     greeter,greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter !r}")
#     return greeter_func(name)

import pytest

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore')=='Semaphore'

def test_raise_exception_on_non_string():
    with pytest.raises(TypeError):
        capital_case(9)

