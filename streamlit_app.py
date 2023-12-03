import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
 r = requests.get(url)
 if r.status_code != 200:
    return None
return r.json()
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://app.lottiefiles.com/animation/99dd2dce-f53d-43c4-9bca-ce4f02dfcbee")
# ---- HEADER SECTION ----
with st.container():
 st.subheader("Hi I am Reign Risenheimer C. Egnalig")
 st.title("A Student from Surigao Del Norte State University")
 st.write("I am passionate to learn from this magnificent school")
# ---- WHAT I DO ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
        """
        On my journey of being a student i will show you the beautiful place to learn from this school for people that want to learn from this university:
        REQUIREMENTS TO ENROLL:
        - 2x2 pic
        - birth certificate
        - good moral and report card
        If you have any further question just message me in my Fb acc: Reign Risenheimer Egnalig or my Github Acc.
        """
    )
    st.write("[My Github Account >](https://github.com/Reign0104/Reign.Risenheimer")
    st.write("[My Facebook Account >](https://www.facebook.com/Reignexb.Egnalig/")
 with right_column
     st.lottie(lottie_coding, height=300, key="coding")

