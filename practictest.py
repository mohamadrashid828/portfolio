import streamlit as st
import google.generativeai as genai
import os
api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
persona=""" You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 
         
        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.
 
        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
 """
def send_requst(prompt):

    response = model.generate_content(prompt)
    return response.text

colm1,colm2=st.columns(2)
with colm1:
    st.subheader("HI :wave: ")
    st.title("I'm Mohammad Rashid")
with colm2:
    st.image("assets/Mohamad.jpg",use_column_width=True)



st.title(" ")
st.title("Mohammad's AI Bot ")

input=st.text_input("Ask anything about me ")
if  st.button("ASK",use_container_width=400):
    send_requst( persona+ "Here is the question that the user asked: "+ input)
    st.write(send_requst(input))
st.title(" ")


st.subheader("My Skiles")
st.slider("Python",0,100,50)
st.slider("Communication",0,100,70)
st.slider("Data science",0,100,30)
st.slider("Machine Learning",0,100,20)
st.slider("SQl",0,100,50)

st.title("Galary")
st.title(" ")
colls=st.columns(3)
x=0;
for i,coll in enumerate(colls):
    for j in range(3):
        with coll:
            st.image("assets/Mohamad.jpg",use_column_width=True)
            x=x+1

st.title(" ")
st.title("Please contact me Here")





