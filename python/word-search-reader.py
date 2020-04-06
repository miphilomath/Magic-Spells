#!/bin/python3.8

# To read the Word search problem and input the value in a matrix
# Using Open CV to detect the characters

# Libraries Import
import os
import tempfile
import subprocess

def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents

str = ocr('DeepinScreenshot_select-area_20200405204443.png')
print(str)
