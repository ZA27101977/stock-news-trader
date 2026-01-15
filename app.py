import streamlit as st
from stocks import DEFAULT_STOCKS
from news_engine import analyze_news

st.set_page_config(page_title="מערכת ניתוח מניות", layout="centered")

st.title("📈 מערכת ניתוח מניות לפי חדשות")

st.subheader("📋 מניות במעקב")

stocks = st.multiselect(
    "בחר מניות למעקב:",
    options=DEFAULT_STOCKS,
    default=DEFAULT_STOCKS
)

if st.button("📰 נתח חדשות ודוחות"):
    st.subheader("📊 תוצאות ניתוח")

    for stock in stocks:
        result = analyze_news(stock)

        if result["recommendation"] == "קנייה":
            st.success(
                f"{stock} | סנטימנט: {result['sentiment']} | ציון: {result['score']} | המלצה: {result['recommendation']}"
            )
        elif result["recommendation"] == "מכירה":
            st.error(
                f"{stock} | סנטימנט: {result['sentiment']} | ציון: {result['score']} | המלצה: {result['recommendation']}"
            )
        else:
            st.info(
                f"{stock} | סנטימנט: {result['sentiment']} | ציון: {result['score']} | המלצה: {result['recommendation']}"
            )
