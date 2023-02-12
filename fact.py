#!/usr/bin/python3
""" This files contains a factorial file """


def fact(n):
    """ Returns the factorial of a positive number"""
    if (type(n) != int):
        raise TypeError("Wrong type")
    else:
        if (n <= 1):
            return (1)
        else:
            return (n * fact(n-1))
