#!/bin/bash
echo "Test money"
pytest test_money.py
echo "Test banknote"
pytest test_banknote.py
echo "Test multiply of money - 2 pt extra credit"
pytest test_multiply.py
