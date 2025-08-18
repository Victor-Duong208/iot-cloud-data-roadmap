from typing import Iterable, Tuple

def mean(xs: Iterable[float]) -> float:
    xs = list(xs)
    if not xs:
        raise ValueError("xs rỗng")
    return sum(xs) / len(xs)

def to_celsius(t_f: float) -> float:
    return (t_f - 32) * 5/9

def categorize_temp(t_c: float, thresholds: Tuple[float, float] = (0.0, 25.0)) -> str:
    """
    thresholds=(cold_hot_boundary, normal_hot_boundary)
    Mặc định: (<0 -> cold), [0,25) -> normal, >=25 -> hot
    """
    cold_boundary, hot_boundary = thresholds
    if t_c < cold_boundary: return "cold"
    if t_c < hot_boundary:  return "normal"
    return "hot"

def moving_average(xs: list[float], window: int = 3) -> list[float]:
    if window <= 0:
        raise ValueError("window phải > 0")
    return [sum(xs[i:i+window]) / window for i in range(len(xs)-window+1)]

def normalize(xs: list[float]) -> list[float]:
    if not xs: return []
    lo, hi = min(xs), max(xs)
    if hi == lo: return [0.0]*len(xs)
    return [(x - lo)/(hi - lo) for x in xs]
