<h1>📘 YourDay — Life Data ETL Tracker</h1>
<p>YourDay is a simple Python-based ETL project that helps you log daily life data and convert it into meaningful metrics such as productivity, energy, and day quality.
</p>


Data Flow Overview (ETL)
User Input (Terminal)
        ↓
Raw Daily Log
        ↓
Transformations & Scoring Logic
        ↓
Daily Metrics Table (SQLite)


Raw data is always preserved.
<h4> All scores are derived and can be recomputed anytime.</h4>

<h2>🧠 Derived Daily Metrics</h2>

From the raw data, the system computes the following metrics.

1️⃣ Sleep Bucket

Categorizes sleep duration:

Sleep Hours	Category
< 6	Poor
6 – 7.5	Average
> 7.5	Great

This is used for qualitative insights.

2️⃣ Sleep Score (0–100)

Sleep score combines duration and quality.

Formula:

Sleep Score =
  (sleep_hours / 8) × 70
+ (sleep_quality / 5) × 30


Why:

Duration matters more than perception
Quality still plays a meaningful role

3️⃣ Mood Score (0–100)

Normalizes mood rating to a percentage.

Formula:
Mood Score = (mood_rate / 5) × 100

4️⃣ Focus Intensity

Represents effective focus, adjusted by mood.

Formula:
Focus Intensity = focus_hours × (mood_rate / 5)

5️⃣ Productivity Score

Measures output potential using sleep, mood, and focus together.

Formula:
Productivity Score =
  focus_hours
× (sleep_score / 100)
× (mood_rate / 5)

6️⃣ Day Score (0–100)

Final aggregate score representing overall day quality.

Formula:
Day Score =
  0.4 × productivity_score
+ 0.3 × sleep_score
+ 0.3 × mood_score

7️⃣ Day Type Classification

Each day is tagged based on its Day Score:

Day Score	Day Type
< 40	Burnout
40 – 70	Average
> 70	Peak

🗄️ Stored Daily Metrics

The following derived fields are stored in SQLite:



<h2>🚀 How to Use</h2>
python user.py


Follow terminal prompts to log your day.
