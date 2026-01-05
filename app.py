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
# Tampilkan Data & Hapus
# ==========================
st.subheader("Data Tersimpan")

if not df_data.empty:
    col1, col2 = st.columns([3, 1])

    with col1:
        st.dataframe(df_data, use_container_width=True)

    with col2:
        st.markdown("### Hapus Data")

        nik_hapus = st.selectbox(
            "Pilih NIK",
            df_data["NIK"].astype(str)
        )

        if st.button("🗑️ Hapus"):
            df_data = df_data[df_data["NIK"].astype(str) != nik_hapus]
            df_data.to_excel(FILE_EXCEL, index=False)

            st.success("Data berhasil dihapus")
            st.rerun()

    with open(FILE_EXCEL, "rb") as f:
        st.download_button(
            "⬇️ Download Excel",
            f,
            file_name="data_inputan.xlsx"
        )
else:
    st.info("Belum ada data")
