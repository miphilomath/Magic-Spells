#!/bin/env python3.8

'''
To count the frequency of each letter in the given string and print them in descending order

English alphabets frequencies: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
Spanish and others (laters)

Arguments = --mapped, --decrypt and --lang
variables:
    * script_desc
    * 

# In case of same frequency letter print with all version, all possible mappings.
# With no argument and language. English default, with frequency in percentage.
'''
script_desc = \
        """
        This program is used to find the frequency of each letter in the text to help solve the cryptography puzzles.
        Usage: script [--options] [values] [input file/string] 
        """

# Importing Libraries
import argparse

def read_file(filename):
    # To read the content from a file
    # Read string from argument (if provided)
    try:
        with open(filename) as f:
            content = f.readlines()
        content = str([string.strip().replace(' ', '') for string in content])
    except:
        f.close()

def read_string():
    # Read string from user input
    content = sys.stdin.readlines("Enter the text: ")
    return content

def measure_frequency(content):
    # Return the frequency of each letter as a dictionary
    return ({i: content.count(i) for i in set(content)})

def map_letters():
    # Map with the frequencies of each letter in english (For puzzles)
    pass
    
def print_frequency_string(frequency_dict):
    # Sorting the frequency in descending order
    frequency_sorted = {k: v for k, v in sorted(frequency_dict.items(), key=lambda item:item[1], reverse=True)}
    
    # Printing each key value pair per line
    print('Character\tCount\tFrequency')
    for keys,values in frequency_sorted.items():
        print(keys, ':', values)   
        
    # Print with English Alphabets equivalent if --map attribute is provided

    # Print the mapped string if --decrypt attribute is provided
    pass

def main():
    pass

if __name__ == "__main__":

    test_string = \
            """
            YJR SMDERT YP JYOD [IXX;R OD YJR DOC VJSTSVYRT MS,R GPT YJR ,PDY VP,,PM LRUNPSTF ;SUPIY
            """

    # Reading arguments
    parser = argparse.ArgumentParser(description = script_desc)

    # Adding parser arguments
    parser.add_argument("-m", "--map", \
            help = "Prints the frequency of each letter and \
                    the mapped equivalence in the given language")
    parser.add_argument("-d", "--decrypt", \
            help = "Prints the decrypted text with the mapped letters.")
    parser.add_argument("-l", "--lang", \
            help = "Select the language to map and decrypt to")

    args = parser.parse_args()

    # Process arguments
    count_args = len(sys.argv)
    if count_args == 1:
        read_string()




