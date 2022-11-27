import streamlit as st

st.write("""
#TDS Week 8 Assignment

## Sum of two numbers and depolying using Heroku""")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")

s = a+b 
st.write("Sum of the two numbers are:",s)
st.write("Credits: 21f1005104")
