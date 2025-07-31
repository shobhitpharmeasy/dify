from datetime import datetime


def main() -> dict:
    return {"cur_time": datetime.now().isoformat(sep=" ")}
