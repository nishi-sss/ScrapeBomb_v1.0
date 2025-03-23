import streamlit as st
import pandas as pd
from scraper.main import scrape_jobs  # ← さっき作った関数をここで呼ぶ予定！

st.title("ScrapeBomb 💣 v1.0")
st.markdown("ポチると爆弾（スクレイピング）が発動します")

# 起爆ボタン
if st.button("💥 起爆する！"):
    df = scrape_jobs()
    st.success("爆弾起爆完了！データを取得しました。")
    st.dataframe(df)

    # ダウンロードボタン
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("📥 CSVをダウンロード", data=csv, file_name="job_list.csv", mime="text/csv")

