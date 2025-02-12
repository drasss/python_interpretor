import streamlit as st
st.set_page_config(layout="wide")

st.text("col1 et col2 sont les noms des deux colonnes")
col1,col2=st.columns([1,1])
 
value_base="""import numpy as np
import matplotlib.pyplot as plt
 
ranging=st.slider("range",0.,100.,(0.,100.))
 
n=st.slider("n",1,50)
X=np.arange(ranging[0],ranging[1],0.1)
 
 
u=0*X
signe=1
for i in range(1,n+1):
 u+=signe*X**i/i
 signe*=-1
Y=u
Z=np.log(1+X)
 
 
fig, ax = plt.subplots()
 
ax.plot(X,Y)
ax.plot(X,Z)
 
col2.pyplot(fig)
 
 
"""
def f(aaaaaaaaaaaaaaaaaaaaaa):
    return exec(aaaaaaaaaaaaaaaaaaaaaa.replace("print","col2.text"))
aaaaaaaaaaaaaaaaaaaaaa=col1.text_area("code",height=500,value=value_base)
 
f(aaaaaaaaaaaaaaaaaaaaaa)
