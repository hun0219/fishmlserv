from typing import Union
from fastapi import FastAPI
import pickle
from src.fishmlserv.model.manager import get_model_path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight:float):
    """
    물고기의 종류 판별기

    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    ### 모델 불러오기
    with open(get_model_path(), "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])

    #fish_class = "몰라"
    fish_class = "빙어"
    if prediction[0] == 1:
        fish_class = "도미"

    return {
                "prediction": fish_class,
                "length": length, 
                "weight": weight
            }

@app.get("/predict_fish")
def fish(length: float, weight: float):
    with open("/home/hun/code/fishmlserv/note/model.pkl", "rb") as f:
        fish_model = pickle.load(f)

        if fish_model.predict([[length, weight]])[0] == 1:
            prediction="도미"
            #print('도미')
        else:
            prediction="빙어"
            #print('빙어')

        return {
                "prediction" : prediction,
                "length" : length,
                "weight" : weight
                }
