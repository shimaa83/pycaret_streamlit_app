import streamlit as st
st.set_page_config(layout="wide")

st.markdown("# Home")
st.sidebar.markdown("# Home")
st.title('The problem:')
st.markdown('create a general package that simplifies data handling and streamlines the machine learning process')
st.title('Project Goals:')
st.markdown('**:blue[The primary goal of this project is to]:** ')
st.write(" 1. Explore PyCaret to understand its functionality fully. This includes learning how to load data, conduct exploratory data analysis (EDA), train various machine learning models, evaluate their performance, and utilize PyCaret AutoML feature to efficiently identify the best machine learning model for specific datasets.")
st.write(" 2. Develop a general machine learning package that enables users to load data, perform EDA, and train machine learning models. The package should also automatically decide whether to use regressors or classifiers based on the data and allow users to select the models they wish to train.")
st.write(" 3. Use Streamlit to create a user-friendly web app. Streamlit, a Python library, simplifies the creation of interactive web apps. The web app should enable users to upload their data, select the target variable, and choose the machine learning models they want to use.")


