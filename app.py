import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Input Data Penduduk", layout="centered")
st.title("Form Input Data Penduduk")

FILE_EXCEL = "data_penduduk.xlsx"

# ==========================
# Load / Init Excel
# ==========================
if os.path.exists(FILE_EXCEL):
    df_database = pd.read_excel(FILE_EXCEL, sheet_name="DATABASE")
else:
    df_database = pd.DataFrame(columns=["NIK", "No KK", "Nama"])
    with pd.ExcelWriter(FILE_EXCEL, engine="openpyxl") as writer:
        df_database.to_excel(writer, sheet_name="DATABASE", index=False)
        df_database.to_excel(writer, sheet_name="INPUT", index=False)

# ==========================
# FORM INPUT
# ==========================
st.subheader("Input Data")

nik = st.text_input("NIK")
kk = st.text_input("No KK")
nama = st.text_input("Nama")

if st.button("Simpan Data"):
    if not nik or not kk or not nama:
        st.error("⚠️ Semua field wajib diisi")
    elif nik in df_database["NIK"].astype(str).values:
        st.error("❌ NIK sudah terdaftar di DATABASE")
    else:
        data_baru = {
            "NIK": nik,
            "No KK": kk,
            "Nama": nama
        }

        df_database = pd.concat(
            [df_database, pd.DataFrame([data_baru])],
            ignore_index=True
        )

        # Simpan ke Excel (DATABASE + INPUT)
        with pd.ExcelWriter(FILE_EXCEL, engine="openpyxl", mode="w") as writer:
            df_database.to_excel(writer, sheet_name="DATABASE", index=False)
            pd.DataFrame([data_baru]).to_excel(writer, sheet_name="INPUT", index=False)

        st.success("✅ Data tersimpan ke DATABASE")
        st.rerun()

# ==========================
# TAMPILKAN DATABASE
# ==========================
st.subheader("Database Penduduk")

if not df_database.empty:
    st.dataframe(df_database, use_container_width=True)

    with open(FILE_EXCEL, "rb") as f:
        st.download_button(
            "⬇️ Download Excel",
            f,
            file_name="data_penduduk.xlsx"
        )
else:
    st.info("Database masih kosong")
