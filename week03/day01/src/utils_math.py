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
