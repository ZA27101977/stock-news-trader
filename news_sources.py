import feedparser

NEWS_SOURCES = [
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s={symbol}&region=US&lang=en-US",
]

def fetch_news(symbol: str, limit=5):
    articles = []
    for src in NEWS_SOURCES:
        feed = feedparser.parse(src.format(symbol=symbol))
        for entry in feed.entries[:limit]:
            articles.append(entry.title.lower())
    return articles
