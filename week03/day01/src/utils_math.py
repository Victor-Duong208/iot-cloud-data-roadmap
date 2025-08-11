from typing import Iterable

def mean(xs: Iterable[float]) -> float:
    xs = list(xs)
    if not xs:
        raise ValueError("xs rỗng")
    return sum(xs) / len(xs)

def to_celsius(t_f: float) -> float:
    return (t_f - 32) * 5/9

def categorize_temp(t_c: float) -> str:
    if t_c < 0: return "cold"
    if t_c < 25: return "normal"
    return "hot"
def moving_average(xs: list[float], window: int = 3) -> list[float]:
    """Trung bình trượt độ dài 'window'."""
    if window <= 0:
        raise ValueError("window phải > 0")
    out = []
    for i in range(len(xs) - window + 1):
        out.append(sum(xs[i:i+window]) / window)
    return out

def normalize(xs: list[float]) -> list[float]:
    """Chuẩn hoá min-max về [0,1]."""
    if not xs:
        return []
    lo, hi = min(xs), max(xs)
    if hi == lo:
        return [0.0] * len(xs)
    return [(x - lo) / (hi - lo) for x in xs]
