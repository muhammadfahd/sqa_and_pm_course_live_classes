# Pytest - Automation with Python Library

>Pytest is a testing framework for Python that makes it easy to write simple and scalable test cases. It offers features like fixtures, parameterized tests, and detailed error reporting. With Pytest, you can efficiently test your code and ensure its reliability.


## Advantages of Pytest
The advantages of Pytest are as follows −
* Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
* Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
* Pytest allows us to skip a subset of the tests during execution.
* Pytest allows us to run a subset of the entire test suite.
* Pytest is free and open source.
* Because of its simple syntax, pytest is very easy to start with.

## installation
To install the latest version of pytest, execute the following command −

`pip install pytest`

Confirm the installation using the following command to display the help section of pytest.

`pytest -h `

## Identifying Test files and Test Functions
Running pytest without mentioning a filename will run all files of format **test_*.py or *_test.py**in the current directory and subdirectories. Pytest automatically identifies those files as test files. We can make pytest run other filenames by explicitly mentioning them.

## Pytest - Starting With Basic Test
Create a file named test_square.py and add the below code to that file.

```
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11



```
To run the file , execute the following command in the terminal.
`pytest`



Now to run all the tests from all the files (2 files here) we need to run the following command −

`pytest -v`
