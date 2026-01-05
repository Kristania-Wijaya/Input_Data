import streamlit as st

st.set_page_config(
    page_title="Input Data",
    layout="centered"
)

st.title("Aplikasi Input Data")
st.write("Aplikasi siap digunakan.")
st.subheader("Form Input Data")

nama = st.text_input("Nama Lengkap")
nik = st.text_input("NIK")

if st.button("Simpan"):
    st.success(f"Data {nama} dengan NIK {nik} berhasil disimpan (sementara).")
