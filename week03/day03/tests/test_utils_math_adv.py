import pytest
from src.utils_math import mean, moving_average, normalize, categorize_temp, to_celsius

@pytest.fixture
def temps_f():
    return [77, 80.6, 86, 95]  # giống các ngày trước

@pytest.mark.parametrize("window,expected", [
    (1, [77, 80.6, 86, 95]),
    (2, [78.8, 83.3, 90.5]),
    (3, [81.2, 87.2]),   # giá trị gần đúng; ta so sánh với tolerance
])
def test_moving_average_various(window, expected):
    xs = [77, 80.6, 86, 95]
    out = moving_average(xs, window)
    assert len(out) == len(expected)
    for a, b in zip(out, expected):
        assert pytest.approx(b, rel=1e-3) == a

def test_moving_average_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1,2,3], 0)

@pytest.mark.parametrize("f_value, expected_c", [
    (32, 0.0),
    (212, 100.0),
    (41, 5.0),
])
def test_to_celsius_exact(f_value, expected_c):
    assert pytest.approx(expected_c, rel=1e-9) == to_celsius(f_value)

@pytest.mark.parametrize("mean_c, thresholds, tag", [
    (-0.1, (0.0, 25.0), "cold"),
    (0.0,  (0.0, 25.0), "normal"),
    (24.99,(0.0, 25.0), "normal"),
    (25.0, (0.0, 25.0), "hot"),
    (20.0, (10.0, 20.0), "hot"),    # đổi ngưỡng để kiểm tra “tiêm ngưỡng”
    (9.9,  (10.0, 20.0), "cold"),
])
def test_categorize_temp_with_thresholds(mean_c, thresholds, tag):
    assert categorize_temp(mean_c, thresholds=thresholds) == tag

def test_normalize_invariants():
    xs = [10, 20, 30]
    out = normalize(xs)
    assert min(out) == 0.0 and max(out) == 1.0
    assert out[0] == 0.0 and out[-1] == 1.0
    # đơn điệu tăng
    assert all(a <= b for a, b in zip(out, out[1:]))
