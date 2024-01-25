import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import matplotlib as plt 

st.title('Fish Detector')

# 画像アップロード
uploaded_file = st.file_uploader("画像を選択してください", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # アップロードされた画像を表示（サイズを小さく調整）
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロードされた画像", width=250)

    # Detectボタン
    if st.button('魚を探す'):
        # FastAPIエンドポイントに画像を送信
        files = {"file": uploaded_file.getvalue()}
        #response = requests.post("http://127.0.0.1:8000/detect/", files=files)
        response = requests.post("https://fish-detector.onrender.com/detect/", files=files)#renderのURLに変更
        
        # 結果を表示
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="魚がいるといいね", use_column_width=True)
        else:
            st.error("エラーです。残念。")