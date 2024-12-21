import streamlit as st

st.set_page_config(page_title="CGPA Calculator", page_icon=":book:", layout="wide")
st.title("CGPA Calculator")
sgpa = [0.0]*8

col1, col2 = st.columns([4, 1])

with col1:
    col11, col12 = st.columns(2)
    with col11:
        st.markdown("## First Year")
        sgpa[0] = st.slider("Semester 1", 0.0, 10.0, 9.0, 0.01)
        sgpa[1] = st.slider("Semester 2", 0.0, 10.0, 9.0, 0.01)

        st.markdown("## Third Year")
        sgpa[4] = st.slider("Semester 5", 0.0, 10.0, 9.0, 0.01)
        sgpa[5] = st.slider("Semester 6", 0.0, 10.0, 9.0, 0.01)

    with col12:
        st.markdown("## Second Year")
        sgpa[2] = st.slider("Semester 3", 0.0, 10.0, 9.0, 0.01)
        sgpa[3] = st.slider("Semester 4", 0.0, 10.0, 9.0, 0.01)

        st.markdown("## Fourth Year")
        sgpa[6] = st.slider("Semester 7", 0.0, 10.0, 9.0, 0.01)
        sgpa[7] = st.slider("Semester 8", 0.0, 10.0, 9.0, 0.01)
        
with col2:
    cgpa = 0.0
    weights = [0.05, 0.05, 0.1, 0.1, 0.175, 0.175, 0.175, 0.175]
    
    for i in range(8):
        cgpa += sgpa[i]*weights[i]
        
    st.write("## Your CGPA is: ", round(cgpa, 2))