from app.db import get_connection

def sleep_bucket(hours):
    if hours < 6:
        return "Poor"
    elif 6 <= hours < 7.5:
        return "Average"
    else:
        return "Great"

def sleep_score(quality,hours):
    sleep_score = (hours / 8) * 70 + (quality / 5) * 30
    return sleep_score

def mood_score(mood_rate):
    return (mood_rate / 5) * 100 

def focus_Score(focus_hours, mood_rate):
    fi= focus_hours * (mood_rate / 5)

    return fi 

def producttivity_score(sleep_score, mood_rate,focus_hours):
    ps= focus_hours *(sleep_score *100) * (mood_rate / 5)

def day_score(sleep_score, ps, mood_score):
    DS= 0.4 * ps+ 0.3 * sleep_score + 0.3 * mood_score

    return DS

def day_type(day_score):
    if day_score < 40 :
        tag= 'burnout'
    elif 40 > day_score < 70:
        tag= 'average'
    else:
        tag= 'peak'
    return tag

