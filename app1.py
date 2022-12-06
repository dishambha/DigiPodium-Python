import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="STUDENTS GUID",
    page_icon="😎",
    layout="wide"
)

st.title("GET ALL YOUR NOTES HERE")
st.info("THIS APP IS BUILD TO KEEP ALL NOTES AND ASSIGNMENT AT ONE PLACE")
df = pd.read_csv("laptop_data.csv")
