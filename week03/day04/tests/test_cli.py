import sys, subprocess

def run_cli(args):
    cmd = [sys.executable, "-m", "week03.day04.tempkit.cli"] + args
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()

def test_cli_default_hot():
    out = run_cli(["77", "80.6", "86", "95"])
    assert out == "hot"

def test_cli_custom_threshold_normal():
    # tăng ngưỡng hot lên 35°C để kết quả giảm xuống "normal"
    out = run_cli(["77", "80.6", "86", "95", "--hot-bound", "35"])
    assert out == "normal"
