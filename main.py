"""
## CCA : coexistence with companion animal

DESCRIPTION

Author: [KNU CSE hackathon_컴둥이](https://URL_TO_YOU))\n
Source: [Github](https://github.com/URL_TO_CODE)
"""


import streamlit as st
from PIL import Image
import time
import Intro
import Quiz
import More_information
# Your imports goes below

# 상단바 tab 이름 설정
st.set_page_config(
page_title="CCA_main",
page_icon="🧊",
layout="wide",
initial_sidebar_state="expanded",
)

# 오른쪽 메뉴버튼 숨기기
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


def main():
    st.title("CCA")
    st.subheader("coexistence with companion animal")

    txt = st.write('''
      If you want to live with a companion animal, you have to know a lot of information.
    Through this quiz, you can evaluate how well you’ve done.
    Furthermore, you can get a baseline for raising your companion animal.
        ''')
    
    st.title("당신의 집사 레벨은?")
    st.subheader("퀴즈를 통해 알아보세요!")
        
    # 이미지
    base_image = Image.open('static/cat01.jpg')
    st.image(base_image, width= 600)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        # 시작버튼
        if st.button('START->'):       ########## onclick 으로 내용 update해야함
            # 다음문제로 넘어가도록 설정
            st.write("Click 'QUIZ' radio Button!!")


if __name__ == "__main__":
    # Using "with" notation
    with st.sidebar:
        st.write("CCA category")
        Kategorie = st.radio(
            "--------------- (o^－^o) --------------",
            ("MAIN","INTRO", "QUIZ", "MORE INFORMATION")
        )
        catdog2_image = Image.open('static/catdog2.jfif')
        st.image(catdog2_image, width= 250)

    if Kategorie == "MAIN":
        main()
    elif Kategorie == "QUIZ":
        Quiz.quiz()
    elif Kategorie == "INTRO":
        Intro.intro()
    elif Kategorie == "MORE INFORMATION":
        More_information.more_information()

