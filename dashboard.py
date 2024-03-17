import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style
sns.set(style='darkgrid')

# Load data
hours_df = pd.read_csv("hour_clean.csv")

# Convert 'date' column to datetime and extract 'month' and 'year'
hours_df['date'] = pd.to_datetime(hours_df['date'])
hours_df['month'] = hours_df['date'].dt.month
hours_df['year'] = hours_df['date'].dt.year

# Function to create line chart for bike usage trend
def line_chart(df, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[x_col].astype(str) + '-' + df['month'].astype(str), df[y_col], marker='o', color='blue')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True)
    st.pyplot(fig)

# Function to create bar chart for seasonal pattern
def bar_chart(data, title, x_label, y_label):
    st.header(title)
    st.bar_chart(data)
    st.write(x_label)  
    st.write(y_label)  

# Sidebar for selecting options
st.sidebar.header("Pilih Opsi:")
selected_year = st.sidebar.selectbox('Pilih Tahun:', hours_df['year'].unique())

# Function to filter data based on year
def filter_data_by_year(df, year):
    return df[df['year'] == year]

# Function to create line chart for bike usage trend
def line_chart(df, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[x_col], df[y_col], marker='o', color='blue')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True)
    st.pyplot(fig)

# Function to create bar chart for seasonal pattern
def bar_chart(data, title, x_label, y_label):
    st.header(title)
    st.bar_chart(data)
    st.write(x_label)  
    st.write(y_label)  

# Sidebar for selecting options
st.sidebar.header("Pilih Opsi:")
selected_year = st.sidebar.selectbox('Pilih Tahun:', hours_df['year'].unique())

# Filter data based on selected year
filtered_data = filter_data_by_year(hours_df, selected_year)

# Tambahkan bagian kode Anda di sini
st.header("Tren penggunaan sepeda")

# Line chart for bike usage trend
line_chart(filtered_data, 'month', 'count', f'Tren Penggunaan Sepeda Tahun {selected_year}', 'Bulan', 'Jumlah Sepeda')

# Bar chart for seasonal pattern
seasonal_pattern = filtered_data.groupby('season')['count'].mean()
seasonal_pattern.index = ['Spring', 'Summer', 'Fall', 'Winter']
bar_chart(seasonal_pattern, 'Pola Musiman dalam Penggunaan Sepeda', 'Musim', 'Jumlah Rata-rata Sepeda')

# Display data table
st.header("Tabel Data")
st.write(filtered_data)

# Display heatmap for hourly usage
st.header("Peta Panas Penggunaan Sepeda per Jam")
hourly_usage = filtered_data.pivot_table(values='count', index='season', columns='hour', aggfunc='mean')
fig, ax = plt.subplots()
sns.heatmap(hourly_usage, cmap='YlGnBu', ax=ax)
plt.xlabel('Jam')
plt.ylabel('Musim')
plt.title('Penggunaan Sepeda per Jam berdasarkan Musim')
st.pyplot(fig)
