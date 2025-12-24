from app.db import get_connection

def insert_raw(data:dict):
    conn = get_connection()
    cusrsor= conn.cursor()

    query="""
    INSERT INTO raw_daily_logs(
    log_date,
    sleep_hours,
    sleep_quality,
    mood_rate,
    focus_hours,
    notes)
    VALUES(?,?,?,?,?,?)
    """
    cur.execute(query, (
        data["log_date"],
        data["sleep_hours"],
        data["sleep_quality"],
        data["mood_rate"],
        data["focus_hours"],
        data.get("notes")
    ))

    conn.commit()
    conn.close()

    