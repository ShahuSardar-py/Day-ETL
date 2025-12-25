from app.db import get_connection

def upsert_daily_metrics(metrics: dict):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT OR REPLACE INTO daily_metrics (
        log_date,
        sleep_bucket,
        productivity_score,
        energy_score,
        day_of_week,
        is_weekend
    ) VALUES (?, ?, ?, ?, ?, ?)
    """

    cur.execute(query, (
        metrics["log_date"],
        metrics["sleep_bucket"],
        metrics["productivity_score"],
        metrics["energy_score"],
        metrics["day_of_week"],
        metrics["is_weekend"]
    ))

    conn.commit()
    conn.close()
