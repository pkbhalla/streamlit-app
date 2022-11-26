import streamlit as st

st.write("""
# TDS Module 8 Graded Assignment


## For the Multiplication of 2 given numbers using Streamlit and deploying on Heroku
""")
def body(a):
  b="The product of given numbers is "
  return b+str(a)
#Input the numbers
first_no = st.number_input("Enter first number")
second_no = st.number_input("Enter second number")
product = first_no*second_no
if st.button("Click to get product of 2 numbers"):
  body(product)
#st.write("The product of given numbers is", product)
st.write("By Pratham Bhalla (21f1003052)")
