import streamlit as st
import pandas as pd

st.write("My First Streamlit App")
data = {
    "sales" : [30,40,50,20,10,40]
}

df = pd.DataFrame(data)
st.line_chart(df)