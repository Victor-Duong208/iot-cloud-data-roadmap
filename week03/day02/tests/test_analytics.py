from src.analytics import weekly_temp_tag

def test_weekly_temp_tag():
    assert weekly_temp_tag([77, 80.6, 86, 95]) == "hot"
