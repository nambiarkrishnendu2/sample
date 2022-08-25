import streamlit as st
st.set_page_config(page_title="My webpage",page_icon=":tada:",layout="wide")
st.subheader("Hi, I am Sven :wave:")
st.title("A Data Analayst From Germany")
st.write("I am passionate about finding way to use python and VBA to be more efficient")
st.write("[Learn more >](https://pythonandvba.com)")
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
        import json
        import requests
        from streamlit_lottie import st_lottie
        def load_lottie(url: str):
            r=requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
lottie_hello=load_lottieuri("https://assets9.lottiefiles.com/packages/lf20_fmgfy8rq.json")
st.title("Include lottile files in stream lit")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",#medium;high
    renderer="svg",#canavas
    height=None,
    width=None,
    key=None,
)
