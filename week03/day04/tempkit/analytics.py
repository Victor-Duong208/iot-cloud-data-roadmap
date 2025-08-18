from .utils_math import mean, to_celsius, categorize_temp

def weekly_temp_tag(temps_f: list[float], thresholds=(0.0, 25.0)) -> str:
    temps_c = [to_celsius(t) for t in temps_f]
    return categorize_temp(mean(temps_c), thresholds=thresholds)
