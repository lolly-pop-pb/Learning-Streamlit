import streamlit as st
import pandas as pd
import time as ts
from datetime import time

# Convert to seconds
def converter(value):
    m,s,ms=value.split(":")
    t_s=int(m)*60+int(s)+int(ms)/1000
    return t_s

val=st.time_input("Set timer", value=time(0,0,0))
print(type(val))
if str(val)=="00:00:00":
    st.write("Please set timer")
else:
    sec=converter(str(val))
    print(sec)
    bar=st.progress(0)
    percentage=sec/100
    progress_status=st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1)+" %")
        ts.sleep(percentage)