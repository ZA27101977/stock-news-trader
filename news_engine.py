import random

def analyze_news(symbol: str) -> dict:
    score = random.randint(-100, 100)

    if score > 30:
        sentiment = "חיובי"
        recommendation = "קנייה"
    elif score < -30:
        sentiment = "שלילי"
        recommendation = "מכירה"
    else:
        sentiment = "ניטרלי"
        recommendation = "המתנה"

    return {
        "symbol": symbol,
        "score": score,
        "sentiment": sentiment,
        "recommendation": recommendation
    }
