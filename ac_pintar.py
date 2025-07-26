import streamlit as st

st.title("Sistem Pendingin Udara Pintar")

# Input dari pengguna menggunakan tombol pilihan
is_hot = st.radio("Apakah suhu panas?", ("ya", "tidak"))
window_closed = st.radio("Apakah jendela tertutup?", ("ya", "tidak"))
someone_home = st.radio("Apakah ada orang di rumah?", ("ya", "tidak"))

# Logika pendingin udara
if is_hot == "ya" and window_closed == "ya" and someone_home == "ya":
    st.success("✅ Penyejuk Udara **NYALA**")
else:
    st.warning("❌ Penyejuk Udara **MATI**")
