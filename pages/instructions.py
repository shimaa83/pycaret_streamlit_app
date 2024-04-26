import streamlit as st
st.set_page_config(layout="wide")

st.sidebar.markdown("# Instructions")

# Write instructions using st.write()
st.write("### Welcome to our application!")
st.write("To get started, please follow these instructions:")
st.write("1. Upload your csv file using the file uploader widget.")
st.write("2. Enter target column name.")
st.write("3. Click on the 'Submit' button to process your data.")
st.write("4. View the results displayed on the screen.")
st.write("5. click on Try code and try ML models.")


# You can also format the instructions using Markdown
st.markdown("### Additional Information:")
st.markdown("- Make sure your data file is in the correct format.")
st.markdown("- Double-check the information you provide before submitting.")
st.markdown("- stay calm it takes time to view results.")


