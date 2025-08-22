# src/week04/day01/ds_basics.py
from typing import Iterable, List, Any, Dict
from collections import Counter

def unique_preserve_order(seq: Iterable[Any]) -> List[Any]:
    """O(n), dùng dict giữ thứ tự (Python 3.7+)."""
    return list(dict.fromkeys(seq))

def flatten_once(nested: Iterable[Any]) -> List[Any]:
    """Làm phẳng đúng 1 tầng; O(n + m) với m là tổng phần tử con."""
    out: List[Any] = []
    for x in nested:
        if isinstance(x, (list, tuple)):
            out.extend(x)
        else:
            out.append(x)
    return out

def merge_dicts(left: Dict[Any, Any], right: Dict[Any, Any]) -> Dict[Any, Any]:
    """Gộp dict; right ghi đè; O(len(left)+len(right))."""
    return left | right  # Python 3.9+

def count_occurrences(seq: Iterable[Any]) -> Dict[Any, int]:
    """Đếm tần suất; O(n)."""
    return dict(Counter(seq))
