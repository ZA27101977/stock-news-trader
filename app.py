import streamlit as st
import requests
from datetime import datetime

# ===============================
# הגדרות כלליות
# ===============================
st.set_page_config(page_title="מערכת ניתוח מניות לפי חדשות", layout="wide")
st.title("📊 מערכת ניתוח מניות לפי חדשות בזמן אמת")

API_KEY = st.secrets["NEWS_API_KEY"]

# ===============================
# פונקציה לשליפת חדשות
# ===============================
def get_news(stock):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": stock,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        return []

    return data.get("articles", [])

# ===============================
# ניתוח סנטימנט פשוט
# ===============================
def analyze_sentiment(text):
    positive_words = ["beat", "growth", "profit", "surge", "strong", "record"]
    negative_words = ["miss", "loss", "decline", "drop", "weak", "lawsuit"]

    score = 0
    text = text.lower()

    for w in positive_words:
        if w in text:
            score += 1

    for w in negative_words:
        if w in text:
            score -= 1

    if score > 0:
        return "חיובי", "קנייה"
    elif score < 0:
        return "שלילי", "מכירה"
    else:
        return "נייטרלי", "המתנה"

# ===============================
# קלט משתמש
# ===============================
st.subheader("➕ מניות למעקב")

stocks_input = st.text_input(
    "הכנס סימולי מניות (מופרדים בפסיק)",
    value="AAPL,TSLA,MSFT"
)

stocks = [s.strip().upper() for s in stocks_input.split(",") if s.strip()]

# ===============================
# הפעלת ניתוח
# ===============================
if st.button("🔍 נתח לפי חדשות"):
    for stock in stocks:
        st.markdown(f"## 🏷️ {stock}")

        articles = get_news(stock)

        if not articles:
            st.warning("לא נמצאו חדשות")
            continue

        combined_text = ""

        for a in articles:
            st.write(f"📰 {a['title']}")
            combined_text += a["title"] + " "

        sentiment, recommendation = analyze_sentiment(combined_text)

        st.write(f"📊 סנטימנט כללי: **{sentiment}**")
        st.write(f"📌 המלצה: **{recommendation}**")
        st.write(f"🕒 זמן בדיקה: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

        if recommendation == "קנייה":
            st.success("📈 איתות קנייה על בסיס חדשות")
        elif recommendation == "מכירה":
            st.error("📉 איתות מכירה על בסיס חדשות")
        else:
            st.info("⏸️ אין איתות חזק")

        st.divider()

st.caption("⚠️ המערכת לצורכי לימוד בלבד – אינה ייעוץ השקעות")
