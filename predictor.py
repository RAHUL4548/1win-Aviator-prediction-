import random
from datetime import datetime

def get_prediction():
    now = datetime.now()
    minute = now.minute
    second = now.second

    # Example logic: real-time multiplier estimation
    if second % 5 == 0:
        return "🟥 x1.8 (Be cautious)"
    elif second % 10 == 0:
        return "🟨 x2.5 (Moderate chance)"
    elif second % 13 == 0:
        return "🟩 x7.2 (High confidence)"
    else:
        return f"🟦 x{round(random.uniform(1.2, 3.0), 2)}"
