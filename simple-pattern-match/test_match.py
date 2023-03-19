import pytest

from match import *


def test_1_arg():
    assert greet(["Jeff"]) == "Hello, Jeff"


def test_2_args():
    assert greet(["bob", "JULIAN"]) == "Hello, Bob and Julian"


def test_3_args():
    assert greet(["bOb", "juliaN", "jeff"]) == "Hello, Bob, Julian, and Jeff"


def test_bad_arg():
    assert greet(13) == "I don't know how to greet 13!"
