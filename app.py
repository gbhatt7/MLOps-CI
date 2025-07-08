import streamlit as st

st.title("Power calculator")

st.write("enter a number to calculate its square, cube, and fifth power.")

n=st.number_input("enter an integer", value=1,step=1)

square=n**2
cube=n**3
fifth=n**5

st.write(f"sqaure of the number {n} is {square}")
st.write(f"cube of the number {n} is {cube}")
st.write(f"fifth power of the number {n} is {fifth}")
