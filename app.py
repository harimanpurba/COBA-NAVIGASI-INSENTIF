import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Navigasi Insentif", layout="wide")
st.title("📊 Dashboard Navigasi Insentif")

# Tombol Upload File Excel
uploaded_file = st.file_uploader("Unggah File Excel Anda (Kapasitas > 153 MB)", type=["xlsx", "xlsb"])

if uploaded_file is not None:
    with st.spinner("Sedang membaca file Excel berukuran besar, mohon tunggu..."):
        # Membaca file Excel
        df = pd.read_excel(uploaded_file)
    
    st.success(f"Berhasil dimuat! Total baris data: {len(df):,}")
    
    # Menampilkan pratinjau 100 baris pertama agar browser tidak berat
    st.subheader("Pratinjau Data (100 Baris Pertama)")
    st.dataframe(df.head(100))
    
    # Ringkasan Statistik Otomatis
    st.subheader("Ringkasan Angka")
    st.write(df.describe())
