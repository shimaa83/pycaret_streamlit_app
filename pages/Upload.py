import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.markdown("# Upload")
st.sidebar.markdown("# Upload file ")
st.write("Please fill out this form to start trainig your model")         
with st.form(key='my_form'):

         
  uploaded_file = st.file_uploader("Choose a file",type=["csv"])
  name = st.text_input("Enter target column name (required)")

  if not name:
       st.warning("Please fill out the required fields")
  submit_button = st.form_submit_button(label='Submit')
    
    # Code to execute when the submit button is clicked
  if submit_button:
        if uploaded_file is not None and name != '':
             st.write(f'File uploaded: {uploaded_file.name}, target column name: {name}')
             df = pd.read_csv(uploaded_file)
             st.write(df)
             target_dtype = df[name].dtype
             if pd.api.types.is_numeric_dtype(target_dtype):
                  st.write("This is a Regression problem.Please wait while we process your data...")
                  from pycaret.regression import *
                  s= setup(df, target = df[name], session_id = 123,normalize = True, normalize_method = 'minmax')
                  best = compare_models() 
                  lb = get_leaderboard()
                  st.write('the leader board for the models',lb)
                  st.write('the best model is:',automl())
                  st.session_state.df = df
                  st.session_state.message = name
                  st.write('Now you can start choose model and show the results by clicking on Try code on the left tab')


              
             else:
                  st.write("This is a Classification model.Please wait while we process your data...")
                  from pycaret.classification import *
                  s = setup(df, target = df[name], session_id = 123)
        # compare baseline models
                  best = compare_models()
                  lb = get_leaderboard()
                  st.write('the leader board for the models',lb)
                  st.write('the best model is:')
                  st.write(lb.iloc[0])
                  st.session_state.df = df
                  st.session_state.message = name
                  st.write('Now you can start choose model and show the results by clicking on Try code on the left tab')

        else:
            st.write('Please upload a file and provide a name.')
     
    
