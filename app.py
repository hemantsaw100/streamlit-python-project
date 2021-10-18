import streamlit as st
from multiapp import MultiApp
from apps import stockwatchlist, binance, contact_form  # import your app modules here
# from PIL import Image # Media access library
# img = Image.open("hemant_dp.png") # Create var img to store img inside it
# st.image(img, width=None) # Display the image

# st.markdown("""
# # Streamlit
# This is my final year Project
# """)

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


app = MultiApp()


# Add all your application here
app.add_app("Page 1. Stock Watchlist", stockwatchlist.app)
app.add_app("Page 2. Binance", binance.app)
app.add_app("Page 3. Contact Us", contact_form.app)

# The main app
app.run()



