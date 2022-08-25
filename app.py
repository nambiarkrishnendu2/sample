import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
#emojis
st.set_page_config(page_title="My webpage",page_icon=":tada:",layout="wide")
st.subheader("Hi, I am Sven :wave:")
st.title("A Data Analayst From Germany")
st.write("I am passionate about finding way to use python and VBA to be more efficient")
st.write("[Learn more >](https://pythonandvba.com)")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return=None
    return r.json()
# load assets 
lottie_coding =load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_fmgfy8rq.json")

# what you will learn
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("what you will learn ")
        st.write("##")
        st.write(
            """
            -Snapshot:What dyslexia is 
            
            -Dyslexia signs and symptoms
            
            -Possible causes of dyslexia
            
            -How dyslexia is diagnosed
            
            if this sounds interesting to you consider checking the link below
            """
        )
        st.write("[Dyslexia checker >](https://suraksha-rajagopalan-dyslexia-app-lkjcee.streamlitapp.com/)")
        
      
