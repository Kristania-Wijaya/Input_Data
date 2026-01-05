import streamlit as st
import pandas as pd

st.set_page_config(page_title="Input Data", layout="centered")

st.title("Form Input Data")

# ==========================
# Inisialisasi session_state
# ==========================
if "data" not in st.session_state:
    st.session_state.data = []

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
    else:
        # Ambil semua NIK yang sudah ada
        nik_terdaftar = [d["NIK"] for d in st.session_state.data]

        if nik in nik_terdaftar:
            st.error("❌ NIK sudah terdaftar (data ganda tidak diperbolehkan)")
        else:
            st.session_state.data.append({
                "NIK": nik,
                "No KK": kk,
                "Nama": nama
            })
            st.success("✅ Data berhasil disimpan")

# ==========================
# Tampilkan Data
# ==========================
st.subheader("Data Tersimpan")

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Belum ada data")
