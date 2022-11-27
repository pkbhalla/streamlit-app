import streamlit as st

st.write("""
# TDS Module 8 Graded Assignment


## For the Multiplication of 2 given numbers using Streamlit and deploying on Heroku
""")
#Input the numbers
first_no = st.number_input("Enter first number")
second_no = st.number_input("Enter second number")
product = first_no*second_no
st.write("The product of given numbers is", str(product))
st.write("By Pratham Bhalla (21f1003052)")
