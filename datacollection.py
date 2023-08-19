import streamlit as st
import plotly.graph_objects as go

import calendar
from datetime import datetime

projects = ["Project Name", "PM", "Customer", "Project Source", "Service Type", "Billing Method", "GB", "Portfolio", "Rate", "Budget", "Business Cluster" ]
PM = ['Nguyen Duc Trung', "Bui Quoc Thai"]
pro_source = ["BGSV", "BGSW"]

allocation = ["NTID", "Project", "Technology"]
currency = 'USD'
page_title = "Dossier"
layout = 'centered'

st.set_page_config(page_title = page_title, layout = layout )
st.title(page_title)

years = [datetime.today().year,datetime.today().year+1]
months = list(calendar.month_name[1:])

st.header(f"Data Entry in {currency}")
with st.form('entry_form', clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select PM:", PM, key = 'PM')
    col2.selectbox("Select Project Source:",  pro_source, key = 'Project Source')

    "---"

    with st.expander("Project Name"):

        st.text_input(label = "Project Name")

    "---"
    submitted = st.form_submit_button("Save Data")
    

    if submitted:
        period = str(st.session_state['year']) + "_" + str(st.session_state['month'])
        

