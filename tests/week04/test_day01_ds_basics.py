# tests/week04/test_day01_ds_basics.py
import pytest
from src.week04.day01.ds_basics import (
    unique_preserve_order, flatten_once, merge_dicts, count_occurrences
)

def test_unique_preserve_order():
    assert unique_preserve_order([1,1,2,3,2,1]) == [1,2,3]
    assert unique_preserve_order(['a','b','a','c']) == ['a','b','c']
    assert unique_preserve_order([]) == []

def test_flatten_once():
    assert flatten_once([[1,2],[3]]) == [1,2,3]
    assert flatten_once([1,[2,3],4]) == [1,2,3,4]
    assert flatten_once([]) == []
    assert flatten_once([[],[1]]) == [1]

def test_merge_dicts():
    assert merge_dicts({"a":1,"b":2}, {"b":9,"c":3}) == {"a":1,"b":9,"c":3}
    assert merge_dicts({}, {"x":1}) == {"x":1}
    assert merge_dicts({"x":1}, {}) == {"x":1}

def test_count_occurrences():
    assert count_occurrences(["a","b","a"]) == {"a":2,"b":1}
    assert count_occurrences([]) == {}
    assert count_occurrences([1,1,1,2]) == {1:3, 2:1}
