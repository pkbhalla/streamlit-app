import streamlit as st

st.write("""
# TDS Module 8 Graded Assignment


## For the Multiplication of 2 given numbers using Streamlit and deploying on Heroku
""")

#Input the numbers
first_no = st.number_input("Enter first number",min_value=0.0,max_value=999999999.9)
second_no = st.number_input("Enter second number",min_value=0.0,max_value=999999999.9)
product = first_no*second_no
st.write("The product of given numbers is", product)
st.write("By Pratham Bhalla (21f1003052)")
