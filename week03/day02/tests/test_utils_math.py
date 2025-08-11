# Chạy pytest từ thư mục week03/day02 để tự nhận package src
from src.utils_math import mean, moving_average, normalize, to_celsius, categorize_temp
import math
import pytest

def test_mean_basic():
    assert mean([1,2,3,4]) == 2.5

def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])

def test_moving_average_window3():
    assert moving_average([1,2,3,4], 3) == [2.0, 3.0]

def test_normalize_range():
    out = normalize([0,5,10])
    assert out == [0.0, 0.5, 1.0]

def test_temp_pipeline_tag():
    temps_f = [77, 80.6, 86, 95]
    temps_c = [to_celsius(t) for t in temps_f]
    assert categorize_temp(mean(temps_c)) == "hot"
