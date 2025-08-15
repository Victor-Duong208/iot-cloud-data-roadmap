from src.analytics import weekly_temp_tag

def test_weekly_temp_tag_default_thresholds():
    assert weekly_temp_tag([77, 80.6, 86, 95]) == "hot"

def test_weekly_temp_tag_custom_thresholds():
    # đặt ngưỡng cao để buộc ra "normal"
    assert weekly_temp_tag([77, 80.6, 86, 95], thresholds=(0.0, 35.0)) == "normal"
