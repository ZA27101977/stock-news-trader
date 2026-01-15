import random

# סימולציה של ניתוח חדשות
# (בשלב הבא נחבר לחדשות אמיתיות)

def analyze_news(symbol: str) -> dict:
    sentiment_score = random.randint(-100, 100)

    if sentiment_score > 30:
        sentiment = "Positive"
    elif sentiment_score < -30:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "symbol": symbol,
        "score": sentiment_score,
        "sentiment": sentiment
    }
