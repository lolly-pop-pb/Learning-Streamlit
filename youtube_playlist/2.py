import streamlit as st
import pandas as pd
import time as ts

table=pd.DataFrame({"Col1":[1,2,3,4],"Col2":[5,6,7,8]})
st.metric(label="WindSpeed", value="120ms⁻¹" ,delta= "1.4ms⁻¹ ")
st.metric(label="WindSpeed", value="120ms⁻¹" ,delta= "-1.4ms⁻¹ ")

st.table(table)
st.dataframe(table)


# media
st.image("image.jpg")
st.image("image.jpg", caption="Shrek")
st.image("image.jpg", caption="Shrek", width=500)
st.audio("audio.mp3")
st.video("video.mp4")

st.write("---")

# INTERACTIVE WIDGETS
# # CHECKBOXES
st.write("CHECKBOXES")
st.checkbox("To do one")
st.checkbox("To do two")
st.checkbox("To do three")
st.checkbox("To do four")
state=st.checkbox("Check me")
if state:
    st.write("Aha! Got you!")
else:
    pass

st.checkbox("initially checked", value=True)
def change():
    print("Changed")
st.checkbox("CheckBox1", value=True, on_change=change)
def change2():
    print(st.session_state.checker)
st.checkbox("CheckBox2", value=True, on_change=change2, key="checker")

st.write("---")
# RADIO BUTTON
radio_btn=st.radio("Select country:", options=("India", "US", "Japan", "UK"))
print(radio_btn)

# BUTTON
def btn_click():
    print("Button Clicked")
btn=st.button("Click Me!", on_click=btn_click)

# SELECT BOX
select=st.selectbox("Favourite Sport", options= ("Badminton", "Tennis", "Cricket", "Chess"))
print(select)
multi_select=st.multiselect("Favourite Sport", options= ("Badminton", "Tennis", "Cricket", "Chess"))
print(multi_select)
st.write(multi_select)

# slider
s_val=st.slider("How's the energy today?")
print(s_val)
st.slider("Rate the weather", min_value=0, max_value=5)
st.slider("Another slider", min_value=10, max_value=20, value=17)

# text 
text1=st.text_input("Enter name")
print(text1)
text2=st.text_input("Enter Course title", max_chars=10)
print(text2)
text3=st.text_area("Enter course description")
print(text3)
# Date and time
text4=st.date_input("Enter registration date")
print(text4)
text5=st.time_input("Set timer")
print(text5)
# progress bar
bar=st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    ts.sleep(1)