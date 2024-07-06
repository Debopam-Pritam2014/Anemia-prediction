import streamlit as st
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open('model_rf.pkl','rb'))

st.title('Anemia Prediction')

sex=st.selectbox('Gender',('Male','Female'))

red_pixel=st.number_input('Red Pixel % in the image',min_value=38.0,max_value=55.0,value=38.0,format='%.4f')

green_pixel=st.number_input('Green Pixel % in the image',min_value=25.0,max_value=33.0,value=25.0,format='% .4f')

blue_pixel=st.number_input('Blue Pixel % in the image',min_value=19.0,max_value=30.0,value=19.0, format='% .4f')

hb=st.number_input(' Hemoglobin level (g/dL)',min_value=2.0,max_value=17.0,value=2.0)
sex_inp=None
if sex=='Male':
    sex_inp=1
else:
    sex_inp=0

if st.button('Predict'):
    inp_df=pd.DataFrame({'%Red Pixel':[red_pixel],'%Green pixel':[green_pixel],'%Blue pixel':[blue_pixel],
                         'Hb':[hb],'Sex_Male':[sex_inp]})
    pred=model.predict(inp_df.head(1))
    if pred==0:
        st.header('Anemia Prediction: True')
    else:
        st.header('Anemia Prediction: False')