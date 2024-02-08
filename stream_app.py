import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.title("IRIS FLOWER DASHBOARD")

st.sidebar.header("Description")
st.sidebar.write("The Iris flower data set or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.")


col1,col2 = st.columns(2)
col1.write("pie chart of species")
col2.write("bar chart of species")
df  = pd.read_csv("Iris.csv")
with col1:
    class_data=df['class'].value_counts()
    fig,ax = plt.subplots()
    ax.pie(class_data,labels=['setosa','versicolor','virginice'])
    st.pyplot(fig)
    









