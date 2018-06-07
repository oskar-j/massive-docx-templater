massive-docx-templater
==========================

[![Requires.io](https://requires.io/github/oskar-j/massive-docx-templater/requirements.svg?branch=master)](https://requires.io/github/oskar-j/massive-docx-templater/requirements?branch=master)
[![Pending Pull-Requests](http://githubbadges.herokuapp.com/oskar-j/massive-docx-templater/pulls.svg?style=flat)](https://github.com/oskar-j/massive-docx-templater/pulls)
[![Github Issues](http://githubbadges.herokuapp.com/oskar-j/massive-docx-templater/issues.svg)](https://github.com/oskar-j/massive-docx-templater/issues)

## Description

Tool which helps to produce multiple **paper** documents, holding name and address information on each of them, 
customized by a *Word* template. Information on addressee is read from the input *Excel* file.

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.
