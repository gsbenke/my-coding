import calculator
import pytest

def test1():
    assert calculator.add(2, 2) == 4
def test2(): 
    assert calculator.add(-4, -3) == -7

