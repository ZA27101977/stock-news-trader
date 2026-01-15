import streamlit as st
from stocks import DEFAULT_STOCKS

st.set_page_config(page_title="Stock News Trader", layout="centered")

st.title("📈 Stock News Trader")

st.subheader("📋 רשימת מניות במעקב")

stocks = st.multiselect(
    "בחר מניות:",
    options=DEFAULT_STOCKS,
    default=DEFAULT_STOCKS
)

st.write("מניות פעילות:")
st.write(stocks)

st.success("שלב רשימת מניות פעיל ✅")
