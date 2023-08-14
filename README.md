### Grading Tests for Code Warm-up

Students get credit for this assignment based on how much they did.

The tests and point values are:

| Test file         | Points                 | Total Pts
|-------------------|------------------------|:---------:
| `test_money.py`   | 2 pts each test passed | 10
| `test_banknote.py`| 1 pt each test passed  |  2
| `test_multiply.py`| 1 pt each test passed  |  2

* `test_money` tests init, `__eq__`, and `__add__`.
* `test_banknote` tests serial number and Banknote is a subclass of Money.
* `test_multiply` is **extra credit**. Tests Money \* float and float \* Money.

### How to Test

1. Copy this directory into a `tests` subdir of the student's repo.
   - Or, you can clone the money-tests repo as a Git submodule inside the student's repo:
     ```
     cd code-warmup        (student's repository)
     git submodule add https://github.com/ISP2023/money-tests tests
     ```
   - `git submodule` creates the `tests` directory itself. This command may fail if `tests` already exists.
2. Change into the `tests` subdir of student's code, run "runtests.sh".  
   - If you don't have bash, then run pytest with each `test_*.py` file.


