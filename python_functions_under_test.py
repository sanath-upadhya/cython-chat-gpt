import inspect
import re
import openai
import time
from cyprompt import cyprompt
import utils as util
import random

@cyprompt(useCode = True,useDoc = True,tests = ["fibonacci(-1) == -1", 
                                                "fibonacci('san') == -1",
                                                "fibonacci(1) == 1" , 
                                                ("st.integers(5, 20)", "fibonacci(n+2) == fibonacci(n+1) + fibonacci(n)")])
def fibonacci(n):
    """
    The function returns the nth fibonacci number
    """
    a,b = (0,1)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b = b,a+b
    return a

@cyprompt(useCode = True,useDoc = True,tests = ["tribonacci(-1) == -1" , 
                                                "tribonacci('san') == -1" , 
                                                ("st.integers(5, 20)", "tribonacci(n+3) == tribonacci(n+2) + tribonacci(n+1) + tribonacci(n)")])
def tribonacci(n):
    """
    The function returns the nth tribonacci number
    """
    a,b,c = (0,1,1)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b,c = b,c,a+b+c
    return a 

def tribonacci_python(n):
    """
    The function returns the nth tribonacci number
    """
    a,b,c = (0,1,1)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b,c = b,c,a+b+c
    return a    

def fibonacci_python(n):
    """
    The function returns the nth fibonacci number
    """
    a,b = (0,1)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b = b,a+b
    return a


@cyprompt(useCode = False,useDoc = True,tests = ["sum_of_integers(2) == 3", 
                                                ("st.integers(5, 20)", "sum_of_integers(n) == n*(n+1)/2")])
def sum_of_integers(n):
    """
    The function returns the summation of n positive integers
    """
    if (not isinstance(n, int)) or (n<0):
        return -1
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

def sum_of_integers_python(n):
    """
    The function returns the summation of n positive integers
    """
    if (not isinstance(n, int)) or (n<0):
        return -1
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

@cyprompt(useCode = False,useDoc = True,tests = ["factorial(1) == 1" , 
                                                 "factorial('san') == -1" ,
                                                 "factorial(-1) == -1" ,
                                                ("st.integers(1, 8)", "factorial(n) == factorial(n-1)*n")])
def factorial(n):
    """
    The function returns the factorial of n
    """
    if (not isinstance(n, int)) or (n<0):
        return -1
    if (n == 0):
        return 1
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial

@cyprompt(useCode = False,useDoc = True,tests = ["pell(1) == 1",
                                                 "pell(-1) == -1",
                                                 "pell('san') == -1",
                                                ("st.integers(2, 8)", "pell(n) == 2*pell(n-1) + pell(n-2)")])
def pell(n):
    """
    The function returns the nth pell number
    """
    a,b = (0,1)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b = b,2*b+a
    return a

def pell_python(n):
    """
    The function returns the nth pell number
    """
    a,b = (0,1)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b = b,2*b+a
    return a

@cyprompt(useCode = False,useDoc = True,tests = ["perrin(1) == 0",
                                                ("st.integers(3, 10)", "perrin(n) == perrin(n-2) + perrin(n-3)")])
def perrin(n):
    """
    The function returns the nth perrin number
    """
    a,b,c = (3,0,2)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b,c = b,c,a+b
    return a 

def perrin_python(n):
    """
    The function returns the nth perrin number
    """
    a,b,c = (3,0,2)
    if (not isinstance(n, int)) or (n<0):
        return -1
    for i in range(n):
        a,b,c = b,c,a+b
    return a 

def factorial_python(n):
    """
    The function returns the factorial of n
    """
    if (not isinstance(n, int)) or (n<0):
        return -1
    if (n == 0):
        return 1
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i

    return factorial

def test_fibonacci(number_of_tests):
    for i in range(0, number_of_tests):
        value = random.randint(0,50)
        content = "Test number: " + str(i+1) + "\n" + "The n value is: " + str(value)
        util.write_to_file(content)
        #Test cython code
        a = fibonacci(value)

        #Test python code
        start = time.time()
        a = fibonacci_python(value)
        end = time.time()
        content = "Time by python code is " + str(end-start)
        print("Time by python code is " + str(end-start))
        util.write_to_file(content)

def test_tribonacci(number_of_tests):
    for i in range(0, number_of_tests):
        value = random.randint(0,50)
        content = "Test number: " + str(i+1) + "\n" + "The n value is: " + str(value)
        util.write_to_file(content)
        #Test cython code
        a = tribonacci(value)

        #Test python code
        start = time.time()
        a = tribonacci_python(value)
        end = time.time()
        content = "Time by python code is " + str(end-start)
        print("Time by python code is " + str(end-start))
        util.write_to_file(content)

def test_factorial(number_of_tests):
    for i in range(0, number_of_tests):
        value = random.randint(0,10)
        content = "Test number: " + str(i+1) + "\n" + "The n value is: " + str(value)
        util.write_to_file(content)
        #Test cython code
        a = factorial(value)

        #Test python code
        start = time.time()
        a = factorial_python(value)
        end = time.time()
        content = "Time by python code is " + str(end-start)
        print("Time by python code is " + str(end-start))
        util.write_to_file(content)

def test_sum_of_integers(number_of_tests):
    for i in range(0, number_of_tests):
        value = random.randint(0,5000)
        content = "Test number: " + str(i+1) + "\n" + "The n value is: " + str(value)
        util.write_to_file(content)
        #Test cython code
        a = sum_of_integers(value)

        #Test python code
        start = time.time()
        a = sum_of_integers_python(value)
        end = time.time()
        content = "Time by python code is " + str(end-start)
        print("Time by python code is " + str(end-start))
        util.write_to_file(content)

def test_pell(number_of_tests):
    for i in range(0, number_of_tests):
        value = random.randint(0,50)
        content = "Test number: " + str(i+1) + "\n" + "The n value is: " + str(value)
        util.write_to_file(content)
        #Test cython code
        a = pell(value)

        #Test python code
        start = time.time()
        a = pell_python(value)
        end = time.time()
        content = "Time by python code is " + str(end-start)
        print("Time by python code is " + str(end-start))
        util.write_to_file(content)

def test_perrin(number_of_tests):
    for i in range(0, number_of_tests):
        value = random.randint(0,50)
        content = "Test number: " + str(i+1) + "\n" + "The n value is: " + str(value)
        util.write_to_file(content)
        #Test cython code
        a = perrin(value)

        #Test python code
        start = time.time()
        a = perrin_python(value)
        end = time.time()
        content = "Time by python code is " + str(end-start)
        print("Time by python code is " + str(end-start))
        util.write_to_file(content)

if __name__ == "__main__":
    #test_fibonacci(1)

    #test_tribonacci(1)

    #test_sum_of_integers(1)

    #test_factorial(1)

    #test_pell(1)

    test_perrin(1)
    pass
    
