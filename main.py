import streamlit as st
import pandas as pd
import numpy as np

import pickle




with open("./xgboost_feature3.pkl","rb") as file:
    model = pickle.load(file)
    
st.title("머신러닝 모델 예측 앱")

st.write("3개의 feature 값을 입력해 주세요.")

def predict(input):
    result = model.predict(input)
    
    return result


with st.form(key='form'):
      
    input1 = st.number_input('첫 번째 값', value=0.0)
    input2 = st.number_input('두 번째 값', value=0.0)
    input3 = st.number_input('세 번째 값', value=0.0)
    
    submit = st.form_submit_button(label='예측하기')
    
    user_input_data = [[input1, input2, input3]]
    
import time
if submit:
    user_input_data=[[input1, input2, input3]]
    
    start = time.time()
    
    result = predict(user_input_data)
    
    end = time.time()
    st.write(f'걸린 시간:{end-start}')
    
    st.write(user_input_data)
    st.write(f'house : {result[0]}')


# 입력값을 배열로 변환
input_data = np.array([[input1, input2, input3]])

# 4. 예측 버튼을 눌렀을 때 예측 수행
if st.button('예측하기'):
    prediction = model.predict(input_data)
    st.write(f"예측 결과: {prediction[0]}")


    print("예측 결과:", prediction)



