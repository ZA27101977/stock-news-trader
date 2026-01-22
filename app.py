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
    r = analyze_news(stock)

    if r["recommendation"] == "קנייה":
        st.success(f"{stock} | סנטימנט: {r['sentiment']} | ציון: {r['score']} | המלצה: {r['recommendation']}")
    elif r["recommendation"] == "מכירה":
        st.error(f"{stock} | סנטימנט: {r['sentiment']} | ציון: {r['score']} | המלצה: {r['recommendation']}")
    else:
        st.info(f"{stock} | סנטימנט: {r['sentiment']} | ציון: {r['score']} | המלצה: {r['recommendation']}")

    with st.expander("כותרות רלוונטיות"):
        for h in r["headlines"]:
            st.write("•", h)
