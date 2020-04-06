#!/bin/python3.8

""""
To count the frequency of each letter in the given string and print them in descending order

English alphabets frequencies: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
Spanish and others (laters)
"""

# Importing Libraries
import argparse

def read_string():
    # Setting filename to Argument passed
    #filename = 

    # Read string from argument (if provided)
    with open(filename) as f:
        content = f.readlines()
    raw_content = [x.strip() for x in content]

    # If no argument is provided, wait for the user input string
    # Creating temp file or storing it in the string as the user types.

    # Usage warnings

def measure_frequency():
    # Count the letters from the string and store them in the array or map with location
    
    # Measure the frequency of each letter
    pass

def map_letters():
    # Map with the frequencies of each letter in english (For puzzles)
    pass
    
def print_frequency_string():
    # Print in descending order with no attribute
    
    # Print with English Alphabets equivalent if --map attribute is provided

    # Print the mapped string if --decrypt attribute is provided
    pass


if __name__ = "__main__":
    read_string()
