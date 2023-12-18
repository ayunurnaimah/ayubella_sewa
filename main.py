import streamlit as st

with st.form("my_form"):

   st.title("Booking Motor Wisata Semarang")
   slider_val = st.slider("Estimasi Jarak")
   checkbox_val = st.checkbox("Setuju")
   my_number = st.slider('Jumlah Motor ', 1, 10)
   my_color = st.selectbox('Merk Motor', ['Beat','Aerox','Vario','N-Max','PCX','KLX'])
   

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val, "slider", my_number , "color", my_color)

st.write("@AyuBella_sewaMotor")