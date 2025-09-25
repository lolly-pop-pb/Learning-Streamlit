
import streamlit as st
# MARKDOWN
st.markdown("# MARKDOWN")
# HEADING: #=H1, ##=H2, ###=H3
st.markdown("# This is H1")
st.markdown("## This is H2")
st.markdown("### This is H3")
# horizontal line
st.markdown("---")
# BOLD: ** bold text **
st.markdown("**This is in bold**")
# ITALIC: * italic text *
st.markdown("*This is in italic*")
# blockquote: >
st.markdown("> Blockquote")
# link
st.markdown("[title](https://www.example.com)")

# ordered list
st.markdown("""
            1. Apples 
            2. Bananas 
            3. Oranges
            """)
# unordered list
st.markdown("""
            - Carrots 
            - Onions 
            - Cucumbers
            """)
# inline code
st.markdown('This is some inline code: `print("Hello World")`')

# table
st.markdown("""
|col1|col2|col3|col4|
|----|----|----|----|
|abcd|abcd|abcd|abcd|
|lmno|lmno|lmno|lmno|
            """)

# strikethrough
st.markdown("I am going to use ~~strikethrough~~")

# emoji
st.markdown("Hi hello namaskara! :pray:")