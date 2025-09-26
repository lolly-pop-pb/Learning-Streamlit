import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

st.sidebar.write("HI WELCOME TO THE SIDEBAR")
st.markdown("# Hi there :wave:")
a=np.linspace(0,10,100)
fig1=plt.figure()
plt.plot(a,np.sin(a))
st.write(fig1)
st.pyplot(fig1)

x=np.linspace(0,10,100)
x_bar=np.array([1,2,3,4])
opt=st.sidebar.radio("Select graph", options=("Sin-Cos","Bar","H-Bar"))
if opt=="Sin-Cos":
    st.markdown("<h1 style='text-align: center'>Sin-Cos Chart</h1>", unsafe_allow_html=True)
    fig1=plt.figure()
    plt.style.use('ggplot')
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    st.write(fig1)
elif opt=="Bar":
    st.markdown("<h1 style='text-align: center'>Bar Chart</h1>", unsafe_allow_html=True)
    fig1=plt.figure()
    plt.style.use('ggplot')
    plt.bar(x_bar,x_bar*10)
    st.write(fig1)
else:
    st.markdown("<h1 style='text-align: center'>Horizontal Bar Chart</h1>", unsafe_allow_html=True)
    fig1=plt.figure()
    plt.style.use('ggplot')
    plt.barh(x_bar*10, x_bar)
    st.write(fig1)
    