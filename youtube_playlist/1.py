import streamlit as st
st.title("This is Title")
st.header("This is Header")
st.subheader("This is Subheader")
st.text("This is text")
st.write("---")

st.markdown("# MATH")
st.latex(r"\begin{matrix} a & b \\c & d\end{matrix}")
st.latex(r"\begin{pmatrix} a&b \\ c&d \end{pmatrix}")
st.latex(r"\begin{bmatrix} a&b \\ c&d \end{bmatrix}")
st.latex(r"\begin{vmatrix} a&b \\ c&d \end{vmatrix}")
st.latex(r"\begin{Bmatrix} a&b \\ c&d \end{Bmatrix}")

st.write("---")
# image
st.image("image.jpg")
# caption
st.caption("Somebody once told me the world is gonna roll me")

# json function
json={"a":"1,2,3", "b":"4,5,6"}
st.json(json)

# code function
code=   """
print("Hello World")
def funct():
    return 0
"""
st.code(code)
st.code(code, language="python")

