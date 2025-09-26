import streamlit as st

st.markdown("# User Registration")
form1=st.form("Form1")
form1.text_input("First Name")
form1.text_input("Last Name")
form1.text_input("Age")
form1.form_submit_button("Submit")

st.markdown("<h1>Course details</h1>", unsafe_allow_html=True)
with st.form("Form2"):
    st.text_input("Course Title")
    st.form_submit_button("Submit")

st.markdown("<h1 style='text-align: center'>New Form</h1>", unsafe_allow_html=True)
with st.form("Form3"):
    col1, col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email")
    st.text_input("Password")
    st.text_input("Confirm Password")
    st.write("Birthday")
    d,m,y=st.columns(3)
    d.text_input("Day")
    m.text_input("Month")
    y.text_input("Year")
    st.form_submit_button("Submit")
 
st.markdown("<h1 style='text-align: center'>New Form Again</h1>", unsafe_allow_html=True)
with st.form("Form4", clear_on_submit=True):
    col1, col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    f_status=st.form_submit_button("Submit")
    if f_status:
        if f_name=="" and l_name=="":
            st.warning("Fill names")
        else:
            st.success("Submitted successfully")