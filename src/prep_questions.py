
from collections.abc import Iterable
import time
from typing import List, Dict, Tuple

'''
📝 Python Software Developer (Test Automation) Prep Kit

Section 1: Python Coding (10 Questions)
Focus: core/intermediate Python, problem-solving, clean code.

'''
# Write a function that returns the first non-repeating character in a string.


def first_non_repeating_char(s: str) -> str:
    char_counts: Dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count == 1:
            return char
    return ''


print(first_non_repeating_char('ssfffgggtppdddqqqiidjjj'))


# Given a list of integers, return the two numbers that add up to a target sum. Optimize for time.


def two_sum(nums: List[int], target: int) -> Tuple[int] | None:
    compliments = {n: i for i, n in enumerate(nums)}
    for i, n in enumerate(nums):
        compliment = target - n
        if compliment in compliments and compliments[compliment] != i:
            return n, compliment
    return None


# Implement a context manager that times how long a block of code takes to run.


class MyTimingContextManager():
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f'duration: {self.end - self.start} seconds.')


def get_func_time():
    def func_to_time():
        time.sleep(5)
        return
    with MyTimingContextManager():
        func_to_time()


get_func_time()

# Explain the difference between @staticmethod, @classmethod, and instance methods. Give examples.
'''
static method refers to a method included in a class whcih is independant of the class or the instance of the class
does not use self or reference class parameters

def add(a, b):
    return a + b

an instance method refers to a method applied to a specific instance of a class
using self

a class method is a method which provides context for, performs operation on a class and not a specific isntance
ex_ listing the methods of a class not the data specific to a given instance
'''

# Write a generator that yields the Fibonacci sequence indefinitely.


def fibonacci():
    a, b = 0, 1
    count = 0
    while count < float('inf'):
        yield a
        a, b = b, a + b
        count += 1


# What’s the difference between is and == in Python? When would you use each?
    '''
    == refers to equlaity
    is refers to identity

    lista = [1,2,3]
    listb = [1,2,3]

    lista == listb # True
    lista is listb # False

    listc = lista
    listc is lista # True
    '''

# Given a dictionary of employee names → salaries, return the top 3 highest-paid employees.


def highest_paid(employee_salaries: Dict[str, int]):
    employee_salary_list: List[Dict[str, str | int]] = [{'name': k, 'salary': v} for k, v in employee_salaries.items()]
    employee_salary_list.sort(key=lambda x: x['salary'], reverse=True)
    return employee_salary_list[:3]


employee_salaries = {
    'bob': 100,
    'kate': 120,
    'john': 85,
    'bill': 200
}


print(highest_paid(employee_salaries))


# Write a function that flattens a nested list (e.g. [[1,2],[3,[4]]] → [1,2,3,4]).


def flatten(xs):
    '''
    recursively call flatten if iterable (because depth of nesting uknnown) else yield item
    '''
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


f = flatten([[1, 2], [3, 4], [5, [6, 7]]])


# Explain how Python’s GIL affects multithreading. When would you prefer multiprocessing?


# Add type hints to this function:


def add_items(a: int | float, b: int | float) -> int | float:
    return a + b
