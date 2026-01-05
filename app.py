import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Input Data", layout="centered")

st.title("Form Input Data")

FILE_EXCEL = "data_inputan.xlsx"

# ==========================
# Load data dari Excel
# ==========================
if os.path.exists(FILE_EXCEL):
    df_data = pd.read_excel(FILE_EXCEL)
else:
    df_data = pd.DataFrame(columns=["NIK", "No KK", "Nama"])

# ==========================
# Form Input
# ==========================
st.subheader("Input Data")

nik = st.text_input("NIK")
kk = st.text_input("No KK")
nama = st.text_input("Nama")

if st.button("Simpan Data"):
    if not nik or not kk or not nama:
        st.error("⚠️ Semua field wajib diisi")
    elif nik in df_data["NIK"].astype(str).values:
        st.error("❌ NIK sudah terdaftar (data ganda)")
    else:
        data_baru = pd.DataFrame([{
            "NIK": nik,
            "No KK": kk,
            "Nama": nama
        }])

        df_data = pd.concat([df_data, data_baru], ignore_index=True)
        df_data.to_excel(FILE_EXCEL, index=False)

        st.success("✅ Data berhasil disimpan ke Excel")
        st.rerun()

# ==========================
# Tampilkan Data
# ==========================
st.subheader("Data Tersimpan")

if not df_data.empty:
    st.dataframe(df_data, use_container_width=True)

    with open(FILE_EXCEL, "rb") as f:
        st.download_button(
            "⬇️ Download Excel",
            f,
            file_name="data_inputan.xlsx"
        )
else:
    st.info("Belum ada data")
