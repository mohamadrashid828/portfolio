import streamlit as st
import google.generativeai as genai
import os
api_key="AIzaSyBlRXllO5oZcxq-h7YL2z_wHR-70mR2s9w"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
persona="""You are Mohamad AI bot. You help people answer questions about your self (i.e Mohamad),
Answer as if you are responding . dont answer in second or third person.f you don't know they answer you simply say "That's a secret"
 Here is more info about Mohamad Rashid:
 I'm mohammad graduated from Soran computer institute and now I'm studied at Soran University of computer science , and i'm 24 yars old ,
 i have been study about data sceince and AI 
 """
def send_requst(prompt):

    response = model.generate_content(prompt)
    return response.text

colm1,colm2=st.columns(2)
with colm1:
    st.subheader("HI :wave: ")
    st.title("I'm mohammad rashid")
with colm2:
    st.image(r"assets\Mohamad.jpg",use_column_width=True)


st.title(" ")
st.title("Mohammad's AI Bot ")

input=st.text_input("Ask anything about me ")
if  st.button("ASK",use_container_width=400):
    send_requst( persona+ "This is a User"+ input)
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
            st.image(r"assets\Mohamad.jpg",use_column_width=True)
            x=x+1

st.title(" ")
st.title("Please contact me Here")





