import streamlit as st
import pandas as pd
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
# interactive widgets
# CHECKBOXES
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
