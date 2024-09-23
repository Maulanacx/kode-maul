import streamlit as st

x = st.number_input("masukkan angka")
sx = st.text_input("satuan", "C")
st.write("Anda memasukkan", x,' ',sx)
sy = st.text_input("Dikonversi ke", "C")
y = 0
if (sx == 'C'):
 if(sy == 'C'):
  y = x
 elif(sy == 'F'):
  y = x*9/5+32
 y = 0
if (sx == 'C'):
 if(sy == 'C'):
  y = x
 elif(sy == 'K'):
  y = x+273,15
st.write(x,' ',sx, '= ',y, sy)
