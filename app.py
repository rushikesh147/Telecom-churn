# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nh9df_-iNLZVitEbxhEEiZTTNY0IJK1X
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("Classifier.pkl","rb")
Classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])

def predict_note_authentication(account_lenght , voice_messages, intl_plan , intl_mins ,
                 intl_calls, night_mins, night_calls,customer_calls, day_mins,
                 day_calls,eve_mins, eve_calls):
  feat_list = np.array([[account_lenght , voice_messages, intl_plan , intl_mins ,
                   intl_calls, night_mins, night_calls,customer_calls, day_mins,
                   day_calls,eve_mins, eve_calls]], dtype=object)
  prediction=Classifier.predict(feat_list)
  print(prediction)
  if (prediction[0]==0):
    return 'the customers has not churn'
  else:
    return 'the customers has been churned'


def main():
  image2 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScH7E1EXIo1ZphKFXpqkWNFX5OA-JYB8g5tw&usqp=CAU'
  image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT4xf_3hVeSgHEb2YGbvBerVIX_oJJxEZKNWeti8TrSat3-Y-wJyVZAGc1vSt3za4y1TM&usqp=CAU'
  st.image(image,use_column_width=False)

  add_selectbox = st.sidebar.selectbox("How would you like to predict?",("Online", "Batch"))
  st.sidebar.info('''the feature name and order must be in same of below [[account_lenght,voice_messages,intl_mins,intl_calls,night_mins,night_calls,customer_calls,day_mins,day_calls,
       eve_mins, eve_calls,voice_plan_yes,intl_plan_yes]] ''')
  st.sidebar.image(image2)
  st.title("Predicting Customer Churn")
  html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Telecom churn rate ML App </h2>
    </div>
    """
  if add_selectbox == 'Online':
      st.markdown(html_temp,unsafe_allow_html=True)
      account_lenght = st.text_input("account_lenght",key ="account_lenght")
      voice_messages = st.text_input("voice_messages",key ="voice_messages")
      intl_plan = st.selectbox('intl_plan 1 is yes or 0 is No', ['1', '0'])
      intl_mins = st.text_input("intl_mins",key ="intl_mins")
      intl_calls = st.text_input("intl_calls",key ="intl_calls")
      night_mins = st.text_input("night_mins",key ="night_mins")
      night_calls = st.text_input("night_calls",key ="night_calls")
      customer_calls = st.text_input("customer_calls",key ="customer_calls")
      day_mins = st.text_input("day_mins",key ="day_mins")
      day_calls = st.text_input("day_calls",key ="day_calls")
      eve_mins = st.text_input("eve_mins",key ="eve_mins")
      eve_calls = st.text_input("eve_calls",key ="eve_calls")
            
    
      result=""
      if st.button("Predict"):
          result=predict_note_authentication(account_lenght , voice_messages, intl_plan , intl_mins ,
                           intl_calls, night_mins, night_calls,customer_calls, day_mins,
                           day_calls,eve_mins, eve_calls)
      st.success('{}'.format(result))
  if add_selectbox == 'Batch':
    file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
    if file_upload is not None:
      data = pd.read_csv(file_upload,encoding= 'unicode_escape')
      result=Classifier.predict(data)
      st.success('The output is {}'.format(result))
      result1 = pd.DataFrame(result)
      data['churn'] = result1
      data['churn'] = data['churn'].replace(0, 'not churn')
      data['churn'] = data['churn'].replace(1, 'churn')
      st.download_button(label='download csv',data=data.to_csv(),mime='text/csv')

if __name__=='__main__':
    main()