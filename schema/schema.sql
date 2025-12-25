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
    is_weekend INTEGER,

    sleep_bucket TEXT,
    sleep_score REAL,

    mood_score REAL,
    focus_intensity REAL,
    productivity_score REAL,

    day_score REAL,
    day_type TEXT
);

