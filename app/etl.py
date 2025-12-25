from app.extract import insert_raw
from app.transorm import transform_raw_log
from app.load import upsert_daily_metrics
from app.db import get_connection

def run_daily_el(rdata:dict):
    insert_raw(data)
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM raw_daily_logs WHERE log_date = ?",
        (rdata["log_date"],)
    )
    row = dict(cur.fetchone())
    conn.close()

    metrics = transform_raw_log(row)
    upsert_daily_metrics(metrics)