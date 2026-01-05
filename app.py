import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Form Input Data Penduduk")

if "data" not in st.session_state:
    st.session_state.data = {}

data = st.session_state.data

nik = st.text_input("NIK")
kk = st.text_input("No KK")
nama = st.text_input("Nama")

if st.button("Simpan Data"):
    if not nik or not kk or not nama:
        st.warning("Semua field wajib diisi")
    elif nik in data:
        st.error("NIK sudah terdaftar")
    else:
        data[nik] = {"No KK": kk, "Nama": nama}
        st.success("Data tersimpan")

if st.button("Tampilkan Data"):
    if data:
        df = pd.DataFrame.from_dict(data, orient="index")
        st.dataframe(df)
    else:
        st.info("Belum ada data")

if st.button("Download Excel"):
    if data:
        df = pd.DataFrame.from_dict(data, orient="index")
        buffer = BytesIO()
        df.to_excel(buffer)
        buffer.seek(0)
        st.download_button(
            "Download",
            buffer,
            "data_penduduk.xlsx"
        )
    else:
        st.warning("Data kosong")
