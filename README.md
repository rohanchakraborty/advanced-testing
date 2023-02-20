# advanced-testing
This repository is for doing some advanced testing

# Setup Project

1. Create and source virtualenv
## Create amd source virtualenv

```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing
```
2. Create scaffold

```bash
touch Makefile && touch test_hello.py && touch hello.py && touch requirements.txt
```
3. Populate the "Makefile"
```bash
install:
		pip install --upgrade pip &&\
				pip install -r requirements.txt

test:
		python -m pytest -vv --cov=hello --cov=hellocli test_hello.pytest

lint:
		pylint --disable=R,C hello.py hellocli.py

all: install lint test
```
### How to debug?

* Print 
* PDB
* Testing