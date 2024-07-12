import streamlit as st
import google.generativeai as genai
import os
api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
persona=""" answer user quesion as you are Mohamad not like model , and depend this info act ,if ask
        you about your name tell them mohamad rashid and if aked are you Mohamad tell yas ,
        You are Mohamad AI bot. You help people answer questions about your self (i.e Mohamad)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Mohamad: 
        Mohamad Rashid is an junior flutter developer/analytics in the field of Computer Sceince and NEtwork.
        He runs one of the largest Some application that suitable to teal world in androind opration system,
        hobbyists and students. Mohamad obtained his Deploma degree in
        Network department and later start Bachelor’s  in the field of Computer scince  till now from
        Soran Univercity (Iraq).
        Mohamad worked as a Freelanser  and build own your application
        Mohamad's Youtube Channel: he dosn's has
        Mohamad's Email: mohamadrashid828@gmail.com 
        Mohamad's Facebook: he dosn's has
        Mohamad's Instagram: he dosn's has
        Mohamad's Linkdin: https://www.linkedin.com/in/mohamad-rashid-2258a1206?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app
        Mohamad's Github :https://github.com/mohamadrashid828 """
def send_requst(prompt):

    response = model.generate_content(prompt)
    return response.text

colm1,colm2=st.columns(2)
with colm1:
    st.subheader("HI :wave: ")
    st.title("I'm Mohammad Rashid")
with colm2:
    st.image("assets/Mohamad.jpg",use_column_width=True)


# About Me section
st.header("About Me")
st.write("""
 I am Mohammad rashid , a passionate software developer with experience in various programming languages and technologies. 
I enjoy building innovative solutions and learning new skills to improve my craft.
""")

# My Projects section
st.header("My Projects")
st.write("""
1. **Project 1:** develop a project for Ganarator managment using Flutter/Dart and SQL.
2. **Project 2:** develop a mobile app for car parking managment using flutter/Dart languge and SQLlite.
""")


st.title(" ")
st.title("Mohammad's AI Bot ")

input=st.text_input("Ask anything about me ")
if  st.button("ASK",use_container_width=400):
    x=persona+ "Here is the question that the user asked: "+ input
    print(x)
    send_requst(x)
    st.write(send_requst(input))
st.title(" ")


st.subheader("My Skiles")
st.slider("Python",0,100,50,disabled=True)
st.slider("Dart",0,100,80,disabled=True)
st.slider("Flutter ",0,100,80,disabled=True)

st.slider("Communication",0,100,70,disabled=True)
st.slider("Data science",0,100,30,disabled=True)
st.slider("Machine Learning",0,100,20,disabled=True)
st.slider("SQl",0,100,50,disabled=True)

st.title("Galary")
colls=st.columns(3)
x=0;
for i,coll in enumerate(colls):
    for j in range(3):
        with coll:
            st.image("assets/Mohamad.jpg",use_column_width=True)
            x=x+1



footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 18px;
}
.footer a {
    color: white;
    margin: 0 15px;
    text-decoration: none;
    font-size: 24px;
}

</style>
<div class="footer">
    <p>Contact Me Here</p>
    <a href="https://www.linkedin.com/in/mohamad-rashid-2258a1206?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app" target="_blank" class="linkedin">
        <i class="fab fa-linkedin"></i>
    </a>
    <a href="https://github.com/mohamadrashid828" target="_blank" class="github">
        <i class="fab fa-github"></i>
    </a>
    <a href="https://t.me/m0h4m4d9" target="_blank" class="telegram">
        <i class="fab fa-telegram"></i>
    </a>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# Load font-awesome icons for social media
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)
