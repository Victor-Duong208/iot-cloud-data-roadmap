from .utils_math import mean, to_celsius, categorize_temp

def weekly_temp_tag(temps_f: list[float]) -> str:
    """Đổi F→C, lấy trung bình, phân loại."""
    temps_c = [to_celsius(t) for t in temps_f]
    return categorize_temp(mean(temps_c))
