import streamlit as st

x = st.number_input("masukkan angka")
sx = st.selecbox("satuan", ("C","F","K","R"), key='sx')
st.write("Anda memasukkan", x,' ',sx)
sy = st.selecbox("Dikonversi ke", ("C","F","K","R"), key='sy')
y = 0
if (sx == 'C'):
 if(sy == 'C'):
  y = x
 elif(sy == 'F'):
  y = x*9/5+32
 elif(sy == 'K'):
  y = x+273,15 
 elif(sy == 'R'):
  y = x*4/5 
y = 0
elif (sx == 'F'):
 if(sy == 'F'):
  y = x
 elif(sy == 'C'):
  y = (x-32)*5/9
 elif(sy == 'R'):
  y = 4/9*(x-32) 
 elif(sy == 'K'):
  y = (x+459,67)*5/9
y = 0
elif (sx == 'R'):
 if(sy == 'R'):
  y = x
 elif(sy == 'C'):
  y = x*5/4
 elif(sy == 'F'):
  y = 9/4*x+32 
 elif(sy == 'K'):
  y = 273,15+(x*5/4)
y = 0
elif (sx == 'K'):
 if(sy == 'K'):
  y = x
 elif(sy == 'C'):
  y = x-273,15
 elif(sy == 'F'):
  y = 9/5*x-459,67
 elif(sy == 'R'):
  y = (273,15-x)*4/5
st.write(x,' ',sx, '= ',y, sy)
