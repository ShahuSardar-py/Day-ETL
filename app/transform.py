from app.db import get_connection
from datetime import datetime

def sleep_bucket(hours):
    if hours < 6:
        return "Poor"
    elif 6 <= hours < 7.5:
        return "Average"
    else:
        return "Great"

def sleep_score(quality, hours):
    return (hours / 8) * 70 + (quality / 5) * 30

def mood_score(mood_rate):
    return (mood_rate / 5) * 100

def focus_score(focus_hours, mood_rate):
    return focus_hours * (mood_rate / 5)

def productivity_score(sleep_score, mood_rate, focus_hours):
    return focus_hours * (sleep_score / 100) * (mood_rate / 5)

def day_score(sleep_score, ps, mood_score):
    return 0.4 * ps + 0.3 * sleep_score + 0.3 * mood_score

def day_type(day_score):
    if day_score < 40:
        return "burnout"
    elif 40 <= day_score < 70:
        return "average"
    else:
        return "peak"

#main transformer function
def transform_raw_log(log: dict) -> dict:
    date_obj = datetime.strptime(log["log_date"], "%Y-%m-%d")

    sb = sleep_bucket(log["sleep_hours"])
    ss = sleep_score(log["sleep_quality"], log["sleep_hours"])
    ms = mood_score(log["mood_rate"])
    fi = focus_score(log["focus_hours"], log["mood_rate"])
    ps = productivity_score(ss, log["mood_rate"], log["focus_hours"])
    ds = day_score(ss, ps, ms)
    dt = day_type(ds)

    return {
        "log_date": log["log_date"],
        "sleep_bucket": sb,
        "sleep_score": round(ss, 2),
        "mood_score": round(ms, 2),
        "focus_intensity": round(fi, 2),
        "productivity_score": round(ps, 2),
        "day_score": round(ds, 2),
        "day_type": dt,
        "day_of_week": date_obj.strftime("%A"),
        "is_weekend": 1 if date_obj.weekday() >= 5 else 0
    }