from news_sources import fetch_news

POSITIVE_WORDS = ["beat", "growth", "record", "profit", "upgrade", "strong"]
NEGATIVE_WORDS = ["miss", "loss", "downgrade", "weak", "lawsuit", "decline"]

def analyze_news(symbol: str) -> dict:
    articles = fetch_news(symbol)
    score = 0

    for title in articles:
        for w in POSITIVE_WORDS:
            if w in title:
                score += 20
        for w in NEGATIVE_WORDS:
            if w in title:
                score -= 20

    if score > 20:
        sentiment = "חיובי"
        recommendation = "קנייה"
    elif score < -20:
        sentiment = "שלילי"
        recommendation = "מכירה"
    else:
        sentiment = "ניטרלי"
        recommendation = "המתנה"

    return {
        "symbol": symbol,
        "score": score,
        "sentiment": sentiment,
        "recommendation": recommendation,
        "headlines": articles[:3]
    }
