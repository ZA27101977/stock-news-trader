import streamlit as st
from stocks import DEFAULT_STOCKS
from news_engine import analyze_news

st.set_page_config(page_title="Stock News Trader", layout="centered")

st.title("📈 Stock News Trader")

st.subheader("📋 רשימת מניות במעקב")

stocks = st.multiselect(
    "בחר מניות:",
    options=DEFAULT_STOCKS,
    default=DEFAULT_STOCKS
)

if st.button("🔍 נתח חדשות"):
    st.subheader("📰 תוצאות ניתוח חדשות")

    for stock in stocks:
        result = analyze_news(stock)

        st.write(
            f"**{stock}** | "
            f"Sentiment: {result['sentiment']} | "
            f"Score: {result['score']}"
        )

