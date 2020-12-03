# README #

### What is this repository for? ###

F5 (Shape Security) homework test automation using {python, py.test, selenium-webdriver etc...}

### Installation ###

* Install python 3.9.0 and pip via: https://docs.python-guide.org/en/latest/starting/installation/
* Clone this repo to your local machine
```
git clone git@github.com:your_username/f5py.git
```
* Install framework requirements.txt via cmd window in the repo path on your local machine
```
cd f5py
pip install -r requirements.txt
```
Enjoy! Happy Testing!

### SYNOPSIS ###

See. Try. Ask. Learn. Share. Grow...

Thanks to all the wonderful people out there willing to share their knowledge:

* Python - https://www.python.org/
* Pip - https://pip.pypa.io/
* Python Docs - https://docs.python.org/
* Selenium - http://seleniumhq.org/

And many, many more... Google can be your friend.

### PY.TEST ###

Py.Test is the current test runner for all test case execution, as part of the execution via an IDE or cmd line the framework is setup in a way that will utilize passed in arguments or options.

There are some build it arguments/options you get with py.test modules to include random and parallel
executions.
See: https://pypi.python.org/pypi/pytest-randomly and https://pypi.python.org/pypi/pytest-xdist

To control parallel execution number of threads to 4 tests at once, via a cmd line:
```
py.test -n 4 test_dyanmic.py
```

To create human and machine consumables test results, via a cmd line:
```
py.test test_dynamic.py --junitxml=./reports/results.xml --html=./reports/results.html
```

### FILE STRUCTURE ###

When creating a test suite file the file name should be prefixed with `test_`
To create a file for example tests the file name would be: `test_example.py`

Within the test suite file the test case class should be prefixed with `Test`
For example: `class TestExample`

### REQUIREMENTS ###

* Python 3.9.0 - See Installation Section for further details

### LICENSE ###
(The MIT License)

Copyright (c) M. Millgate

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
