import streamlit as st
import pandas as pd
import pickle
import numpy as np
from streamlit.state.session_state import Serialized

st.markdown(
    """
    <div>
        <center><h1>Medical Cost Predictor</h1></center>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("### Information of the beneficary")

model=open('model_pickle','rb')
model=pickle.load(model)


input = []
# Age
input.append(st.slider('Enter his/her age', 0, 100))

# Sex
S = st.radio("Gender of beneficary",('Male', 'Female'))
if S == 'Male':
    S_result = 0
if S == 'Female':
    S_result = 1
input.append(S_result)

# BMI
input.append(st.text_input('Enter his/her BMI'))

# Children
input.append(st.selectbox('How many children does he/she have', [0, 1, 2, 3, 4, 5]))

# Smoker
D = st.radio('Does he/she smoke', ('Yes', 'No'))
if D == 'Yes':
    D_result = 1
if D == 'No':
    D_result = 0
input.append(D_result)

# Region
R = st.selectbox('Select the region', ('Southwest', 'Southeast', 'Northwest', 'Northeast'))
if R == 'Southwest':
    R_result = 0
if R=='Southeast':
    R_result = 1
if R=='Northwest':
    R_result = 2
if R=='Northwest':
    R_result = 3
input.append(R_result)

# Prediction
try:
    if st.button("Predict"):
        p = model.predict([input])
        st.success(f"The estimated medical cost is ${round(float(p),2)}")
except:
    st.error("Please try again")