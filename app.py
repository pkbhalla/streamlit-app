'''import streamlit as st

st.write("""
# TDS Module 8 Graded Assignment


## For the Multiplication of 2 given numbers using Streamlit and deploying on Heroku
""")
#Input the numbers
first_no = st.number_input("Enter first number")
second_no = st.number_input("Enter second number")
product = first_no*second_no
st.write("The product of given numbers is", str(product))
st.write("By Pratham Bhalla (21f1003052)")'''
import streamlit as st

st.write("""
#TDS Week 8 Assignment
## Sum of two numbers and depolying using Heroku""")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")

s = a+b 
st.write("Sum of the two numbers are:",s)
st.write("Credits: 21f1005104")
