import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Judul Dashboard
st.title("Bike Sharing Data Analysis Dashboard")
st.write("""
Dashboard ini dirancang untuk menganalisis tren penyewaan sepeda berdasarkan waktu dan musim menggunakan Bike Sharing Dataset.
""")

# Path file lokal di Windows
# Ganti path file disesuaikan dengan lokasi file sebelum dashboard dijalankan
hourly_data_path = r'C:\LASKAR AI\Proyek1\Submission\data\hour.csv'
daily_data_path = r'C:\LASKAR AI\Proyek1\Submission\data\day.csv'

# Membaca dataset
hourly_df = pd.read_csv(hourly_data_path)
daily_df = pd.read_csv(daily_data_path)

# Menampilkan beberapa baris pertama dari data
print("Hourly Data:")
print(hourly_df.head())
print("")

print("\nDaily Data:")
print(daily_df.head())
print("")

# Proses datanya
# if hour_file and day_file:
# Load datasets
hourly_df = pd.read_csv(hourly_data_path)
daily_df = pd.read_csv(daily_data_path)

# Convert date columns to datetime
hourly_df['dteday'] = pd.to_datetime(hourly_df['dteday'])
daily_df['dteday'] = pd.to_datetime(daily_df['dteday'])

# Analisis Data
st.subheader("Preview Data")
st.write("**Data Hourly (Top 5 rows):**")
st.dataframe(hourly_df.head())
st.write("**Data Daily (Top 5 rows):**")
st.dataframe(daily_df.head())

# Statistik Deskriptif
st.subheader("Descriptive Statistics")
st.write("**Hourly Data:**")
st.write(hourly_df.describe())
st.write("**Daily Data:**")
st.write(daily_df.describe())

# Visualisasi 1: Rentals by Hour
st.subheader("Visualisasi 1: Average Bike Rentals by Hour of the Day")
hourly_trends = hourly_df.groupby('hr')['cnt'].mean()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=hourly_trends.index, y=hourly_trends.values, ax=ax1)
ax1.set_title('Average Bike Rentals by Hour')
ax1.set_xlabel('Hour of the Day')
ax1.set_ylabel('Average Rentals')
st.pyplot(fig1)


# Visualisasi 2: Rentals by Season
st.subheader("Visualisasi 2: Total Bike Rentals by Season")
rentals_by_season = hourly_df.groupby('season')['cnt'].sum()

# Define a dictionary to map season numbers to names
season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}

# Convert the index to season names
rentals_by_season.index = rentals_by_season.index.map(season_labels.get)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=rentals_by_season.index, y=rentals_by_season.values, ax=ax2, palette="viridis")
ax2.set_title('Total Rentals by Season')
ax2.set_xlabel('Season')
ax2.set_ylabel('Total Rentals')
st.pyplot(fig2)

# Analisis Lanjutan: RFM Analysis (Opsional)
st.subheader("Visualisasi 3: Advanced Analysis: RFM Segmentation")
reference_date = hourly_df['dteday'].max() + pd.Timedelta(days=1)

# RFM Metrics
rfm_df = hourly_df.groupby('casual').agg({
'dteday': lambda x: (reference_date - x.max()).days,  # Recency
'hr': 'count',  # Frequency
'cnt': 'sum'  # Monetary
 }).reset_index()

rfm_df.columns = ['User', 'Recency', 'Frequency', 'Monetary']
rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], 4, labels=[4, 3, 2, 1])
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'], 4, labels=[1, 2, 3, 4])
rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], 4, labels=[1, 2, 3, 4])
rfm_df['RFM_Segment'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)

st.write("**RFM Segmentation:**")
st.dataframe(rfm_df)

# Filter Rentang Tanggal
st.subheader("Fitur Interaktif: Filter Date Range")
date_range = st.date_input(
    "Pilih Rentang Tanggal",
    value=(hourly_df['dteday'].min(), hourly_df['dteday'].max()),
    key="date_range"
)

# Filter dataframe berdasarkan rentang tanggal
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_hourly_df = hourly_df[
        (hourly_df['dteday'] >= pd.to_datetime(start_date)) & 
        (hourly_df['dteday'] <= pd.to_datetime(end_date))
    ]
    st.write("**Data Hourly setelah filter:**")
    st.dataframe(filtered_hourly_df)

    # Visualisasi setelah filter
    st.subheader("Average Bike Rentals by Hour (Filtered)")
    hourly_trends_filtered = filtered_hourly_df.groupby('hr')['cnt'].mean()
    fig_filtered, ax_filtered = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=hourly_trends_filtered.index, y=hourly_trends_filtered.values, ax=ax_filtered)
    ax_filtered.set_title('Average Bike Rentals by Hour (Filtered)')
    ax_filtered.set_xlabel('Hour of the Day')
    ax_filtered.set_ylabel('Average Rentals')
    st.pyplot(fig_filtered)