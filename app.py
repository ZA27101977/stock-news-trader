import streamlit as st
import random
from datetime import datetime

# ===============================
# הגדרות ראשוניות
# ===============================
st.set_page_config(page_title="מערכת ניתוח מניות", layout="wide")

st.title("📊 מערכת ניתוח מניות חכמה")
st.write("ניתוח מניות לפי חדשות ודוחות (הדמיה)")

# ===============================
# פונקציית ניתוח (הדמיה)
# ===============================
def analyze_stock(stock):
    score = random.randint(-100, 100)

    if score > 30:
        recommendation = "קנייה"
        sentiment = "חיובי"
    elif score < -30:
        recommendation = "מכירה"
        sentiment = "שלילי"
    else:
        recommendation = "המתנה"
        sentiment = "נייטרלי"

    return {
        "stock": stock,
        "score": score,
        "sentiment": sentiment,
        "recommendation": recommendation,
        "time": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

# ===============================
# קלט מניות
# ===============================
st.subheader("➕ הוספת מניות למעקב")

stocks_input = st.text_input(
    "הכנס סימולי מניות (מופרדים בפסיק)",
    value="AAPL,MSFT,TSLA"
)

stocks = [s.strip().upper() for s in stocks_input.split(",") if s.strip()]

# ===============================
# הפעלת ניתוח
# ===============================
if st.button("🔍 נתח מניות עכשיו"):
    results = []

    for stock in stocks:
        result = analyze_stock(stock)
        results.append(result)

    st.subheader("📈 תוצאות ניתוח")

    for r in results:
        with st.container():
            st.markdown(f"### 🏷️ {r['stock']}")
            st.write(f"🕒 זמן ניתוח: {r['time']}")
            st.write(f"📊 ציון: {r['score']}")
            st.write(f"📰 סנטימנט חדשות: {r['sentiment']}")
            st.write(f"📌 המלצה: **{r['recommendation']}**")

            if r["recommendation"] == "קנייה":
                st.success("המלצה חיובית – שקול קנייה")
            elif r["recommendation"] == "מכירה":
                st.error("המלצה שלילית – שקול מכירה")
            else:
                st.info("אין פעולה מיידית מומלצת")

            st.divider()

# ===============================
# הערת סיום
# ===============================
st.caption("⚠️ מערכת זו היא הדמיה לימודית ואינה ייעוץ השקעות")
