from .analytics import weekly_temp_tag

def main():
    import argparse
    p = argparse.ArgumentParser(description="TempKit: phân loại nhiệt độ tuần (°F).")
    p.add_argument("temps_f", type=float, nargs="+", help="Danh sách nhiệt độ °F")
    p.add_argument("--hot-bound", type=float, default=25.0, help="Ngưỡng 'hot' (°C), mặc định 25.0")
    p.add_argument("--cold-bound", type=float, default=0.0,  help="Ngưỡng 'cold' (°C), mặc định 0.0")
    args = p.parse_args()
    tag = weekly_temp_tag(args.temps_f, thresholds=(args.cold_bound, args.hot_bound))
    print(tag)
if __name__ == "__main__":  # <-- thêm
    main()                  # <-- thêm