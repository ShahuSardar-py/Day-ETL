from app.db import get_connection

def upsert_daily_metrics(metrics: dict):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT OR REPLACE INTO daily_metrics (
        log_date,
        day_of_week,
        is_weekend,
        sleep_bucket,
        sleep_score,
        mood_score,
        focus_intensity,
        productivity_score,
        day_score,
        day_type
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    cur.execute(query, (
        metrics["log_date"],
        metrics["day_of_week"],
        metrics["is_weekend"],
        metrics["sleep_bucket"],
        metrics["sleep_score"],
        metrics["mood_score"],
        metrics["focus_intensity"],
        metrics["productivity_score"],
        metrics["day_score"],
        metrics["day_type"]
    ))

    conn.commit()
    conn.close()
