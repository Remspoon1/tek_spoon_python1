import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Invoking function with a mix of default arguments")
introduction_with_mix_of_default_args('Zebulon')
# Intentionally left the second argument blank to show the default functionality

print("Invoking function that returns value(s)")
product_of_two_num(10,20)

print("Invoking function with arbitrary arguments")
add_all_nums(1,2,3,4,5)

print("Invoking function to double value")
double(12)

print("Invoking recursive function is a function that calls itself")
fib(8)

print("Invoking function to subtract values")
subtract(10,6)

print("Invoking function to determine if palindrome")
palindrome('frog')



