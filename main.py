from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

app = FastAPI()

#load a pretrained model
model = YOLO("models/last.pt")#相対パスをコピーして使用

@app.get('/')
async def read_root():
    return{'message':'Fish Detector!'}

@app.post("/detect/")
async def detect(file: UploadFile = File(...)):
    # アップロードされたファイルを読み込む
    image_stream = await file.read()
    image = Image.open(BytesIO(image_stream))
    #image = np.array(image) #ここでnumpyに変換すると色調が変わってしまう。PILのままモデルに通すべき。

    # 物体検出の実行
    results = model(image)

    # 結果の画像を生成
    for r in results:
        im_array = r.plot() 
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image(色調をもとにもどす)


    # 結果の画像をレスポンスとして返す
    img_byte_arr = BytesIO()
    im.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/jpeg")

