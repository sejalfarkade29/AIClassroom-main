import streamlit as st


def footer_home():

    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center; items-align:center">
                <p style="font-weight:bold; color:white;">&copy; 2026 AIClassroom | </p>
                <p style="font-weight:bold; color:white;">
                Connect:
                <a href="https://github.com/sejalfarkade29" target="_blank">GitHub</a>|
                <a href="https://www.linkedin.com/in/sejal-farkade-bb4911289" target="_blank">LinkedIn</a>|
                <a href="mailto:sejalfarkade205@gmail.com">Email</a>
                </P>
        </div>
                """,unsafe_allow_html=True)
    
def footer_dashboard():

    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center; items-align:center">
                <p style="font-weight:bold; color:black;">&copy; 2026 AIClassroom | </p>
                <p style="font-weight:bold; color:black;">
                Connect:
                <a href="https://github.com/sejalfarkade29" target="_blank">GitHub</a>|
                <a href="https://www.linkedin.com/in/sejal-farkade-bb4911289" target="_blank">LinkedIn</a>|
                <a href="mailto:sejalfarkade205@gmail.com">Email</a>
                </P>
        </div>
                """,unsafe_allow_html=True)