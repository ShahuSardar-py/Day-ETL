CREATE TABLE raw_daily_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date TEXT UNIQUE,
    sleep_hours REAL,
    sleep_quality INTEGER,
    mood_rate INTEGER,
    focus_hours REAL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE daily_metrics (
    log_date TEXT PRIMARY KEY,
    day_of_week TEXT,
    sleep_bucket TEXT,
    mood_score REAL,
    focus_intensity REAl,
    productivity_score REAL,
    day_score REAL,
    dat_type TEXT
);
