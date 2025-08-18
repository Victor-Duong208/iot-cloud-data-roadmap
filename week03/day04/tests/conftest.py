# đưa đường dẫn root repo vào sys.path để chạy: python -m week03.day04.tempkit.cli
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
