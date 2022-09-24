from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('BMI Calculator')
option = st.selectbox('Enter your gender',('Male','Female'))
height = st.number_input('Enter Your Height in Meters : ' )
weight = st.number_input('Enter Your Weight in Kgs : ' )
height2= height*height
bmi = float(weight / (height2))
check = st.button('Find BMI')
if(check):
    st.title(f'Your BMI : {bmi}')
    if(bmi>40):
        st.title('BMI Category : Very severly obese and Health risk level : Very high risk.')
    elif(bmi>35):
        st.title('BMI Category : Severly obese and Health risk level : High risk.')
    elif(bmi>30):
        st.title('BMI Category : Moderately obese and Health risk level : Medium risk.')
    elif(bmi>25):
        st.title('BMI Category : Overweight and Health risk level : Enhanced risk.')             
    elif(bmi>18.5):
        st.title('BMI Category : Normal weight and Health risk level : Low risk.')
    else:
        st.title('BMI Category : Underweight and Health risk level : Malnutrition risk.')
