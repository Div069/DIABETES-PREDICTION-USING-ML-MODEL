# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:17:58 2023

@author: Divyansh
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes.sav' , 'rb'))
with st.sidebar: 
    selected = option_menu('Multiple Disease Prediction Model' , 
                           ['Diabetes Prediction'],
                           icons = ['activity'],
                           default_index = 0)

#Diabetes Pred
if(selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)