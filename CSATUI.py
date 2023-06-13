import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from streamlit_option_menu import option_menu
import subprocess
import runpy
import time
case_level_met = pd.read_csv('Case_Level_Metrics_Pivot.csv')
csat_rr = pd.read_csv('CSAT_RR_Pivot.csv')
all_feedbacks = pd.read_csv('Merged_FB_File.csv')
cases_due = pd.read_csv('cases_due.csv')
astro_report = pd.read_csv('astro_combined.csv')
#astro_pivot = pd.pivot_table(astro, index =['owner'], values=['case_number'], columns=['status'], aggfunc= 'count', fill_value = 0)
st.set_page_config(layout="wide", page_icon=":bar_chart:", page_title="APIIS Quality Metrics Dashboard")
#Below is the structure of the containers within the Streamlit Page:
header = st.container()
sidebar = st.container()
case_level_data = st.container()
Response_rate_data = st.container()
NPS_data = st.container()
Individual_FB_data = st.container()
Program_level_FB_data = st.container()
Astro_Report_data = st.container()
def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
    df, enableRowGroup=True, enableValue=True, enablePivot=True
    )
    options.configure_side_bar()
    
    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )
    return selection
with header:
    st.title(":bar_chart: APIIS Quality Metrics Dashboard")
with st.sidebar:
    selected = option_menu( menu_title = "Navigation", options = ["Home","Individual Case Metrics",'CSAT Response Rate', 'Program Level Feedback Report', 'Individual Qualtrics Report'],icons =["house","bar-chart",':anchor:',':hash:', 'arrow-down-circle-fill'] , orientation='vertical', default_index= 0, menu_icon= 'cast')
if selected == "Home":
    with case_level_data:
        st.header("Individual Case Metrics")
        st.subheader('Please find below individual metrics at a status level:'); st.markdown("**Note**: The dashboard updates once in every 24 hours i.e. at 9AM everyday.")
        aggrid_interactive_table(case_level_met)
    with Response_rate_data:
        st.header('CSAT Response Rate')
        st.subheader('Please find below the feedback rate for each individual:')
        st.markdown('**Note:** The data for feedbacks refreshes every hour, if you wish you manually refresh, please *click the refresh button* below:')
        if st.button('Refresh the data'):
            subprocess.run(['python', 'C:/Users/komatiyk/Downloads/Qualtrics Weekly Files/csat.py'])
        aggrid_interactive_table(csat_rr)
    with Program_level_FB_data:
        st.header('Program Level Feedback Report')
        dropdown_col, download_button_col= st.columns(2)
        Program = dropdown_col.selectbox('Select your Region/Program from the dropdown below to filter the data:', options=['EU5', 'PAID', 'MENA', 'AU', 'SG', '3PX','Migration'])
        program_selection = astro_report.query('status_notes == @Program')
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv_program = convert_df(astro_report)
        st.download_button(
            label="Download your selected region Feedbacks data for completed cases",
            data=csv_program,
            file_name='Your Feedbacks.csv',
            mime='text/csv'
        )
        st.subheader("Filtered data will appear below 👇 ")
        st.dataframe(astro_report)
    with Individual_FB_data:
        st.header('Individual Qualtrics Report')
        dropdown_col, download_button_col= st.columns(2)
        # text_col.markdown('*Select your name from the drop down next*') 
        Specalist = dropdown_col.selectbox('Select your name from the dropdown below to filter the data:', options=['HARISH GANESAN', 'LAKSHMI PRATYUSHA VELAMAKANNI', 'FARAH BHAGAT','NIVEDITHA PARVATHA', 'PRAKASH JHA', 'PREMALATHA MADDIRALA','HIMANSHU DHAMI', 'YASHWANT KOMATI', 'DILIP CHAVALI','INDRA TATIKONDA', 'RAJARSHI CHATTERJEE', 'LIPSA MOHANTY','KEZIA IDIKKULA MUTHALALY'])
        FB_selection = all_feedbacks.query('SPOC == @Specalist')
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(FB_selection)
        st.download_button(
            label="Download all your Feedbacks data",
            data=csv,
            file_name='Your Feedbacks.csv',
            mime='text/csv'
        )
        st.subheader("Filtered data will appear below 👇 ")
        st.dataframe(FB_selection)
        cases_due_data = cases_due.query('owner== @Specalist')
        csv_cases_due = convert_df(cases_due_data)
        st.download_button(
            label="Download list of cases due Feedback",
            data=csv_cases_due,
            file_name='cases_due.csv',
            mime='text/csv'
        )  
if selected == "Individual Case Metrics":
    with case_level_data:
        st.header("Individual Case Metrics")
        st.subheader('Please find below individual metrics at a status level:'); st.markdown("**Note**: that the dashboard once in every 24 hours i.e. at 9AM everyday.")
        aggrid_interactive_table(case_level_met)    
if selected == 'CSAT Response Rate':
    with Response_rate_data:
        st.header('CSAT Response Rate')
        st.subheader('Please find below the feedback rate for each individual:')
        st.markdown('**Note:** The data for feedbacks refreshes every hour, if you wish you manually refresh, please *click the refresh button* below:')
        if st.button('Refresh the data'):
            subprocess.run(['python', 'C:/Users/komatiyk/Downloads/Qualtrics Weekly Files/csat.py'])
        aggrid_interactive_table(csat_rr)
if selected == 'Individual Qualtrics Report':
    with Individual_FB_data:
        st.header('Individual Qualtrics Report')
        dropdown_col, download_button_col = st.columns(2)
        # text_col.markdown('*Select your name from the drop down next*') 
        Specalist = dropdown_col.selectbox('Select your name from the dropdown below to filter the data:', options=['HARISH GANESAN', 'LAKSHMI PRATYUSHA VELAMAKANNI', 'FARAH BHAGAT','NIVEDITHA PARVATHA', 'PRAKASH JHA', 'PREMALATHA MADDIRALA','HIMANSHU DHAMI', 'YASHWANT KOMATI', 'DILIP CHAVALI','INDRA TATIKONDA', 'RAJARSHI CHATTERJEE', 'LIPSA MOHANTY','KEZIA IDIKKULA MUTHALALY'])
        FB_selection = all_feedbacks.query('SPOC == @Specalist')
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(FB_selection)
        st.download_button(
            label="Download all your Feedbacks data",
            data=csv,
            file_name='Your Feedbacks.csv',
            mime='text/csv'
        )
        st.subheader("Filtered data will appear below 👇 ")
        st.dataframe(FB_selection)
        cases_due_data = cases_due.query('owner== @Specalist')
        csv_cases_due = convert_df(cases_due_data)
        st.download_button(
            label="Download list of cases due Feedback",
            data=csv_cases_due,
            file_name='cases_due.csv',
            mime='text/csv'
        )
if selected == 'Program Level Feedback Report':
    with Program_level_FB_data:
        st.header('Program Level Feedback Report')
        dropdown_col, download_button_col= st.columns(2)
        Program = dropdown_col.selectbox('Select your Region/Program from the dropdown below to filter the data:', options=['EU5', 'PAID', 'MENA', 'AU', 'SG', '3PX','Migration'])
        program_selection = astro_report.query('status_notes == @Program')
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv_program = convert_df(astro_report)
        st.download_button(
            label="Download your selected region Feedbacks data for completed cases",
            data=csv_program,
            file_name='Your Feedbacks.csv',
            mime='text/csv'
        )
        st.subheader("Filtered data will appear below 👇 ")
        st.dataframe(astro_report)
