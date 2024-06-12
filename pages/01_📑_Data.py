import streamlit as st
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title = 'Data Page',
    page_icon = '🗃',
    layout = 'wide'
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.title('Telco Customer Churn Data 🗃')

@st.cache_data
def load_data0():
    data0 = pd.read_csv('Data/telco_churn_sql.csv')
    return data0

@st.cache_data
def load_data():
    data = pd.read_csv('Data/telco_churn_git.csv')
    return data

@st.cache_data
def load_concat_data():
    concat_df = pd.read_csv('Data/df_churn.csv')
    return concat_df

# Function to get all columns from a specific table
def get_all_column():
    data0 = pd.read_csv("Data/telco_churn_sql.csv")
    data = pd.read_csv('Data/telco_churn_git.csv')
    concat_df = pd.read_csv('Data/df_churn.csv')
    st.session_state['data0'], st.session_state['data'], st.session_state['concat_df'] = data0, data, concat_df

# Initialize the dataframe in session state if not already there
if 'data0' not in st.session_state and 'data' not in st.session_state and 'concat_df' not in st.session_state:
    get_all_column()

st.subheader('Telco churn data Category')
# Dropdown select box
selection = st.selectbox('Select..', options=['All columns', 'Numerical Columns', 'Categorical Columns'], on_change=get_all_column)

# Filter the DataFrame based on the selection
if selection == 'Numerical Columns':
    data0_to_display = st.session_state['data0'].select_dtypes(include=['number'])
    data_to_display = st.session_state['data'].select_dtypes(include=['number'])
    concat_df_to_display = st.session_state['concat_df'].select_dtypes(include=['number'])
elif selection == 'Categorical Columns':
    data0_to_display = st.session_state['data0'].select_dtypes(include=['object', 'category'])
    data_to_display = st.session_state['data'].select_dtypes(include=(['object', 'category']))
    concat_df_to_display = st.session_state['concat_df'].select_dtypes(include=(['object', 'category']))
else:
    data0_to_display = st.session_state['data0']
    data_to_display = st.session_state['data']
    concat_df_to_display = st.session_state['concat_df']

# Display the DataFrame
if st.checkbox('Show data from SQL'):
    st.subheader(f'**{selection}**')
    st.write(data0_to_display)

if st.checkbox('Show data from GitHub'):    
    st.subheader('Telco churn data from GitHub')
    st.subheader(f'**{selection}**')
    st.write(data_to_display)

if st.checkbox('Show cleaned and merged data'):
    st.subheader('Cleaned and merged Telco churn data')
    st.subheader(f'**{selection}**')
    st.write(concat_df_to_display)

# Dataset Overview Section
st.markdown("## Dataset Overview")
st.markdown("""
This application provides access to three datasets related to Telco Customer Churn:

- **SQL Dataset**: Data loaded from a SQL database.
- **GitHub Dataset**: Data loaded from a GitHub repository.
- **Cleaned and Merged Dataset**: A preprocessed and merged version of the datasets.
""")

# Data Statistics
st.markdown("## Data Statistics")
if st.checkbox('Show data statistics from SQL'):
    st.write(data0_to_display.describe())

if st.checkbox('Show data statistics from GitHub'):
    st.write(data_to_display.describe())

if st.checkbox('Show data statistics from Cleaned and Merged'):
    st.write(concat_df_to_display.describe())

# Data Visualization
st.markdown("## Data Visualization")

if st.checkbox('Show data visualization for SQL'):
    st.subheader('Numerical Columns')
    for col in data0_to_display.select_dtypes(include=['number']).columns:
        st.write(f"### {col}")
        fig, ax = plt.subplots()
        sns.histplot(data0_to_display[col], kde=True, ax=ax)
        st.pyplot(fig)

if st.checkbox('Show data visualization for GitHub'):
    st.subheader('Numerical Columns')
    for col in data_to_display.select_dtypes(include=['number']).columns:
        st.write(f"### {col}")
        fig, ax = plt.subplots()
        sns.histplot(data_to_display[col], kde=True, ax=ax)
        st.pyplot(fig)

if st.checkbox('Show data visualization for Cleaned and Merged'):
    st.subheader('Numerical Columns')
    for col in concat_df_to_display.select_dtypes(include=['number']).columns:
        st.write(f"### {col}")
        fig, ax = plt.subplots()
        sns.histplot(concat_df_to_display[col], kde=True, ax=ax)
        st.pyplot(fig)

# Data Download Option
st.markdown("## Download Data")
if st.checkbox('Download data from SQL'):
    csv = data0_to_display.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download SQL Data as CSV",
        data=csv,
        file_name='telco_churn_sql.csv',
        mime='text/csv'
    )

if st.checkbox('Download data from GitHub'):
    csv = data_to_display.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download GitHub Data as CSV",
        data=csv,
        file_name='telco_churn_git.csv',
        mime='text/csv'
    )

if st.checkbox('Download cleaned and merged data'):
    csv = concat_df_to_display.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download Cleaned and Merged Data as CSV",
        data=csv,
        file_name='df_churn.csv',
        mime='text/csv'
    )

# Highlight Missing Values
st.markdown("## Missing Values")
if st.checkbox('Show missing values in SQL data'):
    st.write(data0_to_display.isnull().sum())

if st.checkbox('Show missing values in GitHub data'):
    st.write(data_to_display.isnull().sum())

if st.checkbox('Show missing values in cleaned and merged data'):
    st.write(concat_df_to_display.isnull().sum())
