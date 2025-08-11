from src.analytics import weekly_temp_tag

if __name__ == "__main__":
    temps_f = [77, 80.6, 86, 95]
    print("Tag:", weekly_temp_tag(temps_f))
