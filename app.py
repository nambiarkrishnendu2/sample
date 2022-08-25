import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_sxw84pnl.json")


# ---- HEADER SECTION ----
with st.container():
    st.title("Dyslexia")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("What you will learn")
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
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with left_column:
        st_lottie(lottie_coding, height=300, key="coding")
        st.subheader("Snapshot:what is Dyslexia is")
        st.write(
            """
            Dyslexia is a learning disability in reading. 
            People with dyslexia have trouble reading at a good pace and without mistakes.
            They may also have a hard time with reading comprehension, spelling, and writing.
            But these challenges aren’t a problem with intelligence.
            Dyslexia is a common condition that makes it hard to work with language. 
            Some experts believe that between 5 and 10 percent of people have it.
            Others say as many as 17 percent of people show signs of reading challenges.
            """
        )
        with left_column:
            st.subheader("Dyslexia signs and symptoms")
            st.write("##")
            st.write(
                """
                Dyslexia impacts people in different ways. 
                So, symptoms might not look the same from one person to another.
                A key sign of dyslexia is trouble decoding words.
                This is the ability to match letters to sounds.
                Kids can also struggle with a more basic skill called phonemic awareness.
                This is the ability to recognize the sounds in words.
                Trouble with phonemic awareness can show up as early as preschool.
                In some people, dyslexia isn’t picked up until later on, when they have trouble with more complex skills. 
                These can include grammar, reading comprehension, reading fluency, sentence structure, and more in-depth writing.
                Some of the signs of dyslexia have to do with emotions and behavior.
                People with dyslexia might avoid reading, both out loud and to themselves. 
                They may even get anxious or frustrated when reading.
                This can happen even after they’ve mastered the basics of reading.
                
                """
        )
        st.image("dyslexia.jpeg")
        with right_column:
            st.subheader("possible causes of dyslexia")
            st.write(
                """
                Researchers haven’t yet pinpointed exactly what causes dyslexia.
                But they do know that genes and brain differences play a role. 
                Here are some of the possible causes of dyslexia:
                Genes and heredity: Dyslexia often runs in families.
                About 40 percent of siblings of people with dyslexia also struggle with reading.
                As many as 49 percent of parents of kids with dyslexia have it, too. 
                Scientists have also found genes linked to problems with reading and processing language.
                Brain anatomy and activity: Brain imaging studies have shown brain differences between people with and without dyslexia.
                These differences happen in areas of the brain involved with key reading skills. 
                Those skills are knowing how sounds are represented in words, and recognizing what written words look like.
                """
        )
        st.image("possible causes.jpeg")
        with left_column:
            st.subheader("How dyslexia is diagonsed")
            st.write("##")
            st.write(
                """
                The only way to know for sure if someone has dyslexia is through a full evaluation, done either at school or privately.
                Having a diagnosis (schools call it an identification) can lead to supports and services at school, and accommodations at college and work.
                There are a few types of professionals who can assess people for dyslexia. 
                These include school psychologists, clinical psychologists, and neuropsychologists. 
                An evaluator will give a series of tests for dyslexia.
                They’ll test in other areas as well to see exactly where any weaknesses and strengths lie.
                School evaluations are free. 
                
                But private ones can be very expensive.
                In some cases, there are ways to get them for free or at a low cost.
                Local universities often have programs in psychology that have clinics where students do their training.
                Teaching hospitals may have research projects where people can get evaluations for free.
                Learning Disabilities Association of America (LDA) has local chapters in every state.
                They may be able to help with finding free or low-cost options.
                
                """
        )
        st.image("dyslexia_diagonized.jpeg")


        
        
       


