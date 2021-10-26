import json
import requests  
import streamlit as st  
from streamlit_lottie import st_lottie  

def app():    
    st.header(":mailbox: Get In Touch With Me!")
    
    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")


    # Local lottie file 
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    # URL lottie 
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
    lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_9wjm14ni.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high", # medium ; high
        renderer="svg", # canvas
        height=400,
        width=700,
        key=None,
    ) 


    contact_form = """
    <form action="https://formsubmit.co/sawhemant41@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    
    lottie_thank_you = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_aldqqeyg.json") 
    st_lottie(
        lottie_thank_you,
        speed=1,
        reverse=False,
        loop=True,
        quality="high", # medium ; high
        renderer="svg", # canvas
        height=100,
        width=700,
        key=None,
    ) 
