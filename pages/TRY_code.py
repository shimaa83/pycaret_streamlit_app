
import streamlit as st
from pycaret.regression import *
from pycaret.classification import *
import pandas as pd
st.set_page_config(layout="wide")
st.markdown("# TRY Code")
def check_problem_type(df,x):
    target_dtype = df[x].dtype
    if pd.api.types.is_numeric_dtype(target_dtype):

         # init setup with normalize = True
         s = setup(df, target = df[x], session_id = 123,normalize = True, normalize_method = 'minmax')
         st.write('avaliables model',models())
         with st.form(key='my_form'):
           model2 = st.text_input("Enter target column name (required)")
        
           submit_button = st.form_submit_button(label='Submit')
    
    # Code to execute when the submit button is clicked
           if submit_button:
             st.write('Keep calm.we are processing your chosen model...........')
             lr = create_model(model2)
             lr_results = pull()
             st.text("Your choose model results:")
             st.text(lr_results)  
    else:
         s = setup(df, target = df[x], session_id = 123)  
         st.write('avaliables model',models())
         with st.form(key='my_form'):
           model2 = st.text_input("Enter target column name (required)")
        
           submit_button = st.form_submit_button(label='Submit')
    
    # Code to execute when the submit button is clicked
           if submit_button:
             st.write('Keep calm.we are processing your chosen model...........')
             lr = create_model(model2)
             lr_results = pull()
             st.text("Your choose model results:")
             st.text(lr_results)    

if st.session_state:
   try:
    df=st.session_state.df
    x=st.session_state.message
    check_problem_type(df,x)
   except AttributeError:  
    st.write("upload your file")
    st.markdown("[Upload file](/Upload)")
   
   
else:
    st.write("upload your file")
    st.markdown("[Upload file](/Upload)")