import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="מערכת ניתוח מניות", layout="wide")
import time

REFRESH_SECONDS = 30
st.caption(f"🔄 רענון אוטומטי כל {REFRESH_SECONDS} שניות")
time.sleep(REFRESH_SECONDS)
st.experimental_rerun()

st.title("📊 מערכת ניתוח מניות – ניתוח בעברית")

NEWS_API_KEY = st.secrets["NEWS_API_KEY"]

def get_news(stock):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": stock,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }
    r = requests.get(url, params=params)
    return r.json().get("articles", [])

def analyze_sentiment(text):
    positive = ["growth", "profit", "strong", "beat", "surge", "record"]
    negative = ["loss", "drop", "weak", "miss", "lawsuit", "decline"]

    score = 0
    t = text.lower()

    for w in positive:
        if w in t:
            score += 1
    for w in negative:
        if w in t:
            score -= 1

    if score > 0:
        return "חדשות חיוביות", "קנייה"
    elif score < 0:
        return "חדשות שליליות", "מכירה"
    else:
        return "חדשות ניטרליות", "המתנה"

stocks_input = st.text_input("הכנס מניות (AAPL,TSLA,MSFT)", "AAPL,TSLA,MSFT")
stocks = [s.strip().upper() for s in stocks_input.split(",") if s.strip()]

if st.button("🔍 ניתוח חדשות"):
    for stock in stocks:
        st.markdown(f"## 🏷️ {stock}")

        articles = get_news(stock)
        if not articles:
            st.warning("לא נמצאו חדשות")
            continue

        combined = ""

        for a in articles:
            st.write("📰", a["title"])
            combined += a["title"] + " "

        sentiment, rec = analyze_sentiment(combined)

        st.write(f"📊 ניתוח: **{sentiment}**")
        st.write(f"📌 המלצה: **{rec}**")
        st.write(f"🕒 {datetime.now().strftime('%d/%m/%Y %H:%M')}")

        if rec == "קנייה":
            st.success("📈 איתות קנייה")
        elif rec == "מכירה":
            st.error("📉 איתות מכירה")
        else:
            st.info("⏸️ ללא פעולה")

        st.divider()

st.caption("⚠️ לצורכי לימוד בלבד – לא ייעוץ השקעות")
