import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Penduduk", layout="centered")

st.title("🧾 Form Input Data Penduduk")

# ===============================
# Penyimpanan data (Session)
# ===============================
if "data_penduduk" not in st.session_state:
    st.session_state.data_penduduk = {}

data_penduduk = st.session_state.data_penduduk

# ===============================
# Input Form
# ===============================
nik = st.text_input("NIK")
kk = st.text_input("No KK")
nama = st.text_input("Nama")

col1, col2, col3 = st.columns(3)

# ===============================
# Simpan Data
# ===============================
with col1:
    if st.button("💾 Simpan Data"):
        if not nik or not kk or not nama:
            st.warning("⚠️ Semua field wajib diisi!")
        elif nik in data_penduduk:
            st.error("❌ NIK sudah terdaftar!")
        else:
            data_penduduk[nik] = {
                "No KK": kk,
                "Nama": nama
            }
            st.success("✅ Data berhasil disimpan")

# ===============================
# Tampilkan Data
# ===============================
with col2:
    tampil = st.button("📊 Tampilkan Data")

if tampil:
    if not data_penduduk:
        st.info("📭 Belum ada data")
    else:
        df = pd.DataFrame.from_dict(data_penduduk, orient="index")
        df.index.name = "NIK"
        st.dataframe(df, use_container_width=True)

        st.subheader("🗑️ Hapus Data")
        for nik_key in list(data_penduduk.keys()):
            if st.button(f"Hapus {nik_key}"):
                del data_penduduk[nik_key]
                st.experimental_rerun()

# ===============================
# Download Excel
# ===============================
with col3:
    if st.button("⬇️ Download Excel"):
        if not data_penduduk:
            st.error("❌ Tidak ada data")
        else:
            df = pd.DataFrame.from_dict(data_penduduk, orient="index")
            df.index.name = "NIK"
            st.download_button(
                label="📥 Download Excel",
                data=df.to_excel(index=True),
                file_name="data_penduduk.xlsx"
            )
# Input_Data
