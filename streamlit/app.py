import streamlit as st
import dashboard
import stats
import login
import home

st.set_page_config(page_title="PollVue", layout="wide")


st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home","Login/Signup", "News","Statistics"])


if page == "Home":
    home.main()
elif page == "News":
    dashboard.main()
elif page=="Login/Signup":
    login.main()
elif page=="Statistics":
    stats.main();

 
