import streamlit as st
import google.generativeai as genai
import os
api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
persona=""" answer user quesion as you are mohamad not like model , and depend this info act ,if ask
        you about your name tell them mohamad rashid and if aked are you mohammad tell yas ,
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
 
        Murtaza's Youtube Channel: he dosn's has
        Murtaza's Email: mohamadrashid828@gmail.com 
        Murtaza's Facebook: he dosn's has
        Murtaza's Instagram: he dosn's has
        Murtaza's Linkdin: https://www.linkedin.com/in/mohamad-rashid-2258a1206?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app
        Murtaza's Github :https://github.com/mohamadrashid828 
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





