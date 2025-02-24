import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from PIL import Image
import numpy as np
import time
import os
import plotly.express as px
import plotly.graph_objects as go
from ydata_profiling import ProfileReport  #type: ignore
from streamlit_pandas_profiling import st_profile_report #type: ignore
from annotated_text import annotated_text #type: ignore
import base64 


# Loading Image using PIL
web_icon = Image.open('dashboard/image/Gojo Chibi.jpg') # Adding Image to web app
st.set_page_config(page_title="Air Quality Dashboard", layout="wide", initial_sidebar_state="auto", page_icon = web_icon)

# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)


# Dialog Input Nama
@st.dialog("Selamat Datang! 🎉")
def get_name():
    st.write("Silakan masukkan nama Anda untuk melanjutkan:")
    name = st.text_input("Nama Anda", key="user_name_input")
    
    if st.button("Masuk"):
        if name:
            st.session_state.user_name = name  # Simpan nama ke session_state
            st.rerun()
        else:
            st.warning("Silakan isi nama terlebih dahulu!")

# Periksa apakah pengguna sudah memasukkan nama sebelumnya
if "user_name" not in st.session_state:
    get_name()
else:
    # Tampilkan toast sambutan
    st.toast(f"Selamat datang, {st.session_state.user_name}! 🎉")
    time.sleep(0.5)
    st.toast("Semoga harimu menyenangkan! ☀️")
    time.sleep(0.5)
    st.toast("Ayo jelajahi dashboard ini!", icon="🚀")


# ======================================== Sidebar Configuration ========================================

with st.sidebar:
    # Gunakan f-string agar nilai user_name dari session_state bisa ditampilkan dengan benar
    if "user_name" in st.session_state: # Jika sudah ada nama, tampilkan nama
        st.markdown(f"""<h1 style='text-align: center; color: black;'>🙏 <strong>WELCOME</strong> 🙏<br><i>{st.session_state.user_name}</i>👋</h1>""", unsafe_allow_html=True)
    else: # Jika belum ada nama, tampilkan "Guest"
        st.markdown("""<h1 style='text-align: center; color: black;'>🙏 <strong>WELCOME</strong> 🙏<br><i>Guest</i>👋</h1>""", unsafe_allow_html=True)  # Jika belum ada nama, tampilkan "Guest"

    st.sidebar.image("https://i.pinimg.com/originals/fc/71/63/fc71635c7f1b09ed30413f59bb749582.gif", use_container_width=True)

    # Sidebar with two columns
    col1, col2 = st.columns(2)

    # Column 1: Social Media Badges
    with col1:
        # Instagram Badge (shields.io)
        st.markdown("[![Instagram Badge](https://img.shields.io/badge/Instagram-8a3ab9?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/rendika__07/?hl=en)")
        
        # GitHub Badge (shields.io)
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/Rendika7)")

    with col2:

        # WhatsApp Badge (shields.io)
        st.markdown("[![WhatsApp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6281334814045)")
        
        # LinkedIn Badge (shields.io)
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/rendika-nurhartanto-s-882431218/)")

        
    # Deskripsi Data yang Digunakan ========================================
    st.markdown("""
    <div style="text-align: center;">
        🚀 <strong>Information</strong> 🚀
        <hr style="border: 1px solid #ddd; width: 50%; margin: 10px auto;">
        <p><strong>Data</strong> yang digunakan telah <strong>melewati</strong> tahap <strong>processing</strong> ⚙️ terlebih dahulu untuk memastikan <strong>kualitasnya</strong> ✨ dan siap untuk <strong>dianalisis</strong>. 🌟</p>
    </div>
    """, unsafe_allow_html=True)

    # Menampilkan tombol switch untuk menghidupkan/mematikan musik latar belakang ========================================
    play_music = st.toggle("🎵 Background Music")

    # Jika switch diaktifkan, jalankan musik dari file lokal dengan HTML (autoplay & loop)
    if play_music:
        music_file = "dashboard/audio/Background-lofi-by-pixabay.mp3"  # Ganti dengan file lokal kamu

        # Konversi file audio ke base64
        with open(music_file, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode()

        # Gunakan HTML untuk autoplay dan loop
        audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# ======================================== Sidebar Configuration ========================================

# Menampilkan banner gambar sebagai hero image  ========================================
st.image('dashboard/image/Dashboard Analysis for E-Commerce Public Dataset.png', use_container_width=True)

# Membuat DataFrame untuk menampilkan tabel
data_diri = pd.DataFrame({
    "Nama": ["[Rendika Nurhartanto Suharto](https://www.linkedin.com/in/rendika-nurhartanto-s-882431218/)"],
    "Email": ["rendikarendi96@gmail.com"],
    "ID Dicoding": ["[RENDIKA NURHARTANTO SUHARTO](https://www.dicoding.com/users/rendika7/academies)"]
})
# Menampilkan tabel  ========================================
st.table(data_diri)

# -------------------------------------- Load Data !!! -------------------------------------- #

# Folder path
dataPath = "dashboard/main_data.csv"

@st.cache_data
def load_data():
    # Load data
    df = pd.read_csv(dataPath) # csv
    return df

# Will only run once if already cached  ========================================
df = load_data()

# -------------------------------------- Start Dashboard Here !!! -------------------------------------- #

# CSS untuk memposisikan tabs di tengah
st.markdown("""
    <style>
        div[data-baseweb="tab-list"] {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Membuat Tabs untuk membagi tampilan menjadi beberapa section
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 EDA Overview", "📑 Pandas Profiling", "📖 Explanatory Insights", "📊 RFM Analysis", "🔍 Manual Clustering Analysis"])


# -------------------------------------- Tab 1: Exploratory Data Analysis (EDA) -------------------------------------- #
with tab1:

    # Menambahkan custom CSS untuk menata judul agar berada di tengah dengan background
    st.markdown("""
        <style>
            .section-title {
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                padding: 20px;
                background-color: #E36A64;
                color: white;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Menampilkan judul dengan CSS custom
    st.markdown('<div class="section-title">📊 EXPLORATORY DATA ANALYSIS</div>', unsafe_allow_html=True)

    # -------------------------------------- Exploratory Data Analysis (EDA) -------------------------------------- #

    # Membuat dua kolom untuk menampilkan informasi
    col1, col2 = st.columns([2, 3])  # Kolom pertama lebih kecil (2) dan kolom kedua lebih besar (3)

    # Kolom Kiri: Informasi Data dan Metric
    with col1:
        # Sample DataFrame 5 baris acak ========================================
        st.write("### 1. Sample DataFrame")
        
        st.dataframe(df.sample(5))  # DataFrame sample tanpa random state agar berubah-ubah
        
        # Jumlah Baris dan Kolom ========================================
        st.write("### 2. Jumlah Baris dan Kolom")
        # Membuat dua kolom dalam kolom kiri
        metric_col1, metric_col2 = st.columns(2)  # Dua kolom untuk metric
        # Jumlah Baris dan Kolom secara berdampingan
        with metric_col1:
            st.metric("Jumlah Baris", df.shape[0], border=True)
        with metric_col2:
            st.metric("Jumlah Kolom", df.shape[1], border=True)

        # Jenis Kolom (Kategorikal vs Numerikal) ========================================
        st.write("### 3. Jenis Feature (Kolom)")
        numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()
        categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
        # Membuat dua kolom dalam kolom kiri
        metric_col1, metric_col2 = st.columns(2)  # Dua kolom untuk metric
        with metric_col1:
            st.metric("Feature Numerikal", len(numerical_columns), border=True)
        with metric_col2:
            st.metric("Feature Kategorikal", len(categorical_columns), border=True)
        
        # Rentang Waktu Pada Dataset ========================================
        st.write("### 4. Rentang Waktu Pada Dataset")
        # Start Date dan End Date berdasarkan 'order_approved_at'
        start_date = pd.to_datetime(df['order_approved_at'].min())  # Pastikan ini menjadi Timestamp
        end_date = pd.to_datetime(df['order_approved_at'].max())  # Pastikan ini menjadi Timestamp
        # Dua kolom untuk metric
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("Start Date", start_date.strftime('%Y-%m-%d'), border=True)
        with metric_col2:
            st.metric("End Date", end_date.strftime('%Y-%m-%d'), border=True)

        # Menampilkan jumlah nilai unik untuk kolom kategorikal dalam DataFrame
        st.write("### 5. Jumlah Nilai Unik Setiap Kolom Kategorikal")
        # Mengambil kolom kategorikal
        categorical_columns = df.select_dtypes(include=['object']).columns
        # Menghitung jumlah nilai unik per kolom kategorikal
        unique_values = {col: df[col].nunique() for col in categorical_columns}
        # Membuat DataFrame untuk menampilkan hasil
        unique_values_df = pd.DataFrame(list(unique_values.items()), columns=["Kolom", "Jumlah Nilai Unik"])
        # Menampilkan DataFrame dengan kemampuan scroll
        st.dataframe(unique_values_df)

    # Kolom Kanan: Exploratory Data Analysis (EDA)
    with col2:
        # Statistik Deskriptif Kolom Numerikal
        st.write("### 6. Statistik Deskriptif")
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        descriptive_stats = df[numeric_columns].describe()
        st.write(descriptive_stats)

        # Visualisasi Distribusi Data untuk Kolom Numerik
        st.write("### 7. Visualisasi Distribusi Data")
        plt.figure(figsize=(12, 8))
        df[numeric_columns].hist(bins=20, figsize=(12, 8), edgecolor='black', color='lightcoral')
        plt.suptitle('Distribusi Data Kolom Numerik (2023)', fontsize=15)
        plt.tight_layout()
        st.pyplot(plt)

        # Korelasi Tinggi (Misalnya lebih dari 0.3)
        st.write("### 8. Heatmap Feature Correlation")
        corr_matrix = df[numeric_columns].corr()
        high_corr = corr_matrix[(corr_matrix > 0.3) & (corr_matrix != 1.0)]  # Menghindari korelasi dengan dirinya sendiri (1.0)
        high_corr = high_corr.dropna(how='all', axis=1)  # Menghapus kolom yang tidak memiliki korelasi tinggi
        high_corr = high_corr.dropna(how='all', axis=0)  # Menghapus baris yang tidak memiliki korelasi tinggi

        # Menampilkan Heatmap Korelasi Tinggi menggunakan Plotly Express
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=high_corr.values,
            x=high_corr.columns,
            y=high_corr.index,
            colorscale='Reds' # 'Viridis', 'Cividis', 'Blues', 'Reds', 'Greens', 'Oranges', 'YlOrRd', 'YlGnBu', 'YlOrBr'
        ))
        fig_heatmap.update_layout(
            title={
                'text': 'Showing High Correlation Between Features (> 0.3)',
                'x': 0.5,  # Center the title
                'xanchor': 'center',  # Ensure the title is centered
            },
            xaxis_title='Kolom',
            yaxis_title='Kolom',
            template='plotly_dark'
        )
        st.plotly_chart(fig_heatmap)

# -------------------------------------- Tab 2: Pandas Profiling -------------------------------------- #
with tab2:
    # Menampilkan judul halaman
    st.markdown('<h2 style="text-align: center; font-size: 40px; font-weight: bold; background-color: #E36A64; color: white; padding: 20px; border-radius: 8px;">📝 PANDAS PROFILING REPORT</h2>', unsafe_allow_html=True)

    # Menambahkan deskripsi halaman
    st.markdown("""
        <p style="text-align: center; font-size: 18px; margin-bottom: 20px; color: #333;">
            Laporan Pandas Profiling ini memberikan gambaran lengkap tentang dataset yang Anda miliki. 
            Dengan sekali klik, Anda bisa melihat analisis statistik yang mencakup distribusi data, 
            hubungan antar fitur, nilai hilang, dan banyak lagi. Gunakan laporan ini untuk mendapatkan wawasan mendalam yang membantu Anda memahami kualitas dan pola dalam data Anda.
        </p>
    """, unsafe_allow_html=True)

    # Membuat layout kolom untuk tombol
    col1, col2, col3 = st.columns([1.8, 1.3, 1.8])  # Kolom tengah lebih lebar

    with col2:
        # Membuat tombol dan menempatkannya di tengah kolom
        button_clicked = st.button("Generate Pandas Profiling Report")

    if button_clicked:
        with st.spinner("🔄 Generating report... Please wait..."):
            # Membuat laporan profiling dari dataset
            pr = ProfileReport(df, explorative=True)
            # Menampilkan laporan di Streamlit tanpa menggunakan kolom
            st_profile_report(pr)


            
# -------------------------------------- Tab 3: Explanatory Insights -------------------------------------- #
with tab3:
    
        # Extra Styling for the page
    st.markdown("""
        <style>
            h3 {
                color: #4CAF50;
            }
            p {
                font-size: 16px;
                line-height: 1.6;
            }
            i {
                color: #FF6347;
            }
            .section-title {
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                padding: 20px;
                background-color: #E36A64;
                color: white;
                border-radius: 8px;
            }
            .description {
                font-size: 18px;
                text-align: center;
                margin-bottom: 20px;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)
    
        # Menampilkan judul dengan CSS custom
    st.markdown('<div class="section-title">📖 EXPLANATORY INSIGHTS</div>', unsafe_allow_html=True)

    # Menambahkan deskripsi halaman
    st.markdown("""
        <div class="description">
            Dalam bagian ini, akan menyajikan analisis dan menjawab pertanyaan-pertanyaan bisnis mendalam tentang temuan-temuan utama yang telah diperoleh dari eksplorasi data. Penjelasan ini bertujuan untuk memberikan wawasan yang lebih jelas dan mudah dipahami mengenai tren, pola, dan hubungan yang ada dalam data, serta implikasi yang dapat ditarik dari hasil analisis tersebut.
        </div>
    """, unsafe_allow_html=True)

    # Create two columns for side-by-side layout
    col1, col2 = st.columns(2)
    
    # Left Column: Customer Satisfaction Analysis Based on Product Categories (2017)
    with col1:
        # Title
        st.title("[1] Bagaimana perbandingan tingkat kepuasan pelanggan berdasarkan rating review dengan kategori produk pada tahun 2017?")

        # Adding some description and styling with HTML
        st.markdown("""
            <h3 style="color:#4CAF50;">Analysis of Customer Satisfaction by Product Category in 2017</h3>
            <p>This analysis compares the average review ratings and distribution of ratings across different product categories for the year 2017. 
            The goal is to identify the most and least satisfying product categories based on customer feedback.</p>
            <p><b>Visualizations:</b> The first graph shows the top and bottom 5 categories based on the average rating. The second graph shows the distribution of reviews for these categories.</p>
        """, unsafe_allow_html=True)

        # Filter Data for 2017
        df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])
        df_2017 = df[df['order_approved_at'].dt.year == 2017]

        # Calculate Average Review per Category
        avg_review_by_category = df_2017.groupby('product_category_name')['review_score'].mean().reset_index()
        avg_review_by_category = avg_review_by_category.sort_values(by='review_score', ascending=False)

        # Top and Bottom 5 Categories
        top_k = 5
        bottom_k = 5
        top_k_categories = avg_review_by_category.head(top_k)
        bottom_k_categories = avg_review_by_category.tail(bottom_k)

        # Visualization 1: Barplot for Top 5 and Bottom 5 Categories
        st.subheader("Visualisasi 1: Top 5 and Bottom 5 Categories Based on Average Rating (2017)")

        fig, axes = plt.subplots(1, 2, figsize=(18, 8))

        # Top Categories Barplot
        ax1 = axes[0]
        sns.barplot(x='review_score', y='product_category_name', data=top_k_categories, palette='viridis', ax=ax1)

        # Add labels to the bars
        for p in ax1.patches:
            ax1.annotate(f'{p.get_width():.2f}', 
                        (p.get_width(), p.get_y() + p.get_height() / 2), 
                        ha='left', va='center', fontsize=12)

        ax1.set_title(f'Top {top_k} Categories Based on Average Review Rating (2017)', fontsize=15)
        ax1.set_xlabel('Average Review Rating')
        ax1.set_ylabel('Product Category')

        # Bottom Categories Barplot
        ax2 = axes[1]
        sns.barplot(x='review_score', y='product_category_name', data=bottom_k_categories, palette='coolwarm', ax=ax2)

        # Add labels to the bars
        for p in ax2.patches:
            ax2.annotate(f'{p.get_width():.2f}', 
                        (p.get_width(), p.get_y() + p.get_height() / 2), 
                        ha='left', va='center', fontsize=12)

        ax2.set_title(f'Bottom {bottom_k} Categories Based on Average Review Rating (2017)', fontsize=15)
        ax2.set_xlabel('Average Review Rating')
        ax2.set_ylabel('Product Category')

        plt.tight_layout()
        st.pyplot(fig)

        # Visualization 2: Boxplot for Distribution of Ratings
        st.subheader("Visualisasi 2: Boxplot Distribution of Review Ratings by Product Category (2017)")

        # Get top 10 and bottom 10 categories based on average review score
        top_k = 10
        bottom_k = 10

        # Filter Data
        top_k_categories = avg_review_by_category.head(top_k)['product_category_name'].tolist()
        bottom_k_categories = avg_review_by_category.tail(bottom_k)['product_category_name'].tolist()

        filtered_df = df_2017[df_2017['product_category_name'].isin(top_k_categories + bottom_k_categories)]

        fig, ax = plt.subplots(figsize=(14, 15))  # Membuat objek fig dan ax
        sns.boxplot(x='review_score', y='product_category_name', data=filtered_df, palette='Set2', ax=ax)
        ax.set_title('Distribusi Rating Review Berdasarkan Kategori Produk (Top 5 dan Bottom 5) - 2017', fontsize=15)
        ax.set_xlabel('Rating Review')
        ax.set_ylabel('Kategori Produk')
        plt.tight_layout()
        st.pyplot(fig)  # Menyertakan fig di sini


        # Adding Insights with HTML Styling
        st.markdown("""
            <h3 style="color:#FF6347;">Insights</h3>
            <p><b>Top 5 Categories:</b> Categories like <i>fashion_roupa_infanto_juvenil</i> and <i>artes_e_artesanato</i> each received an average rating of 5.00, 
            indicating exceptional customer satisfaction and consistent positive feedback. </p>
            <p><b>Bottom 5 Categories:</b> On the other hand, categories like <i>fraldas_higiene</i> had a significantly lower average rating of 1.00, 
            signaling extreme customer dissatisfaction. This suggests an urgent need for improvement in product quality and customer service.</p>
            <p>The <b>Boxplot Distribution</b> further reveals that the top categories have a tightly clustered rating around 5.00, indicating uniform customer satisfaction. 
            However, the bottom categories exhibit a much wider distribution, with some extreme ratings (outliers), especially in <i>fraldas_higiene</i>, where there are numerous 1-star ratings.</p>
        """, unsafe_allow_html=True)

    # Right Column: Faktor yang Mempengaruhi Waktu Pengiriman dan Kepuasan Pelanggan (2017)
    with col2:

        # Title
        st.title("[2] Apa saja faktor yang mempengaruhi waktu pengiriman produk, dan bagaimana pengaruhnya terhadap kepuasan pelanggan pada periode 2017?")

        # Adding some description and styling with HTML
        st.markdown("""
            <h3 style="color:#4CAF50;">Analisis Waktu Pengiriman dan Kepuasan Pelanggan pada Tahun 2017</h3>
            <p>Analisis ini menggali faktor-faktor yang mempengaruhi waktu pengiriman produk dan bagaimana pengaruhnya terhadap kepuasan pelanggan. 
            Fokus utama adalah pada hubungan antara waktu pengiriman dan rating review serta kategori produk dengan waktu pengiriman terbaik dan terburuk.</p>
            <p><b>Visualisasi:</b> Visualisasi pertama menunjukkan hubungan antara waktu pengiriman dan rating review. Visualisasi kedua membandingkan waktu pengiriman rata-rata berdasarkan kategori produk.</p>
        """, unsafe_allow_html=True)

        # Filter Data for 2017
        df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])
        df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
        df_2017 = df[df['order_approved_at'].dt.year == 2017]

        # Calculate shipping time in days
        df_2017['shipping_time'] = (df_2017['order_delivered_customer_date'] - df_2017['order_approved_at']).dt.days

        # Visualization 1: Scatter Plot for Shipping Time vs Rating Review
        st.subheader("Visualisasi 1: Scatter Plot Waktu Pengiriman vs Rating Review (2017)")

        fig, ax = plt.subplots(figsize=(10, 6))  # Membuat objek fig dan ax
        sns.scatterplot(x='shipping_time', y='review_score', data=df_2017, alpha=0.6, ax=ax)
        ax.set_title('Waktu Pengiriman vs Rating Review (2017)', fontsize=15)
        ax.set_xlabel('Waktu Pengiriman (Hari)')
        ax.set_ylabel('Rating Review')
        ax.grid(True)
        plt.tight_layout()
        st.pyplot(fig)  # Menyertakan fig di sini

        # Visualization 2: Top 5 and Bottom 5 Product Categories Based on Average Shipping Time
        avg_shipping_time_by_category = df_2017.groupby('product_category_name')['shipping_time'].mean().reset_index()
        avg_shipping_time_by_category = avg_shipping_time_by_category.sort_values(by='shipping_time', ascending=False)

        top_k = 5
        bottom_k = 5
        top_k_shipping_time = avg_shipping_time_by_category.head(top_k)
        bottom_k_shipping_time = avg_shipping_time_by_category.tail(bottom_k)

        st.subheader("Visualisasi 2: Top 5 dan Bottom 5 Kategori Produk Berdasarkan Rata-rata Waktu Pengiriman (2017)")

        fig, axes = plt.subplots(1, 2, figsize=(18, 8))  # Membuat objek fig dan axes

        # Plot untuk Top k Kategori
        ax1 = axes[0]
        sns.barplot(x='shipping_time', y='product_category_name', data=top_k_shipping_time, palette='coolwarm', ax=ax1)

        # Menambahkan label pada setiap bar di plot top
        for p in ax1.patches:
            ax1.annotate(f'{p.get_width():.2f}', 
                        (p.get_width(), p.get_y() + p.get_height() / 2), 
                        ha='left', va='center', fontsize=12)

        ax1.set_title(f'Top {top_k} Kategori Berdasarkan Rata-rata Waktu Pengiriman', fontsize=15)
        ax1.set_xlabel('Rata-rata Waktu Pengiriman (Hari)')
        ax1.set_ylabel('Kategori Produk')

        # Plot untuk Bottom k Kategori
        ax2 = axes[1]
        sns.barplot(x='shipping_time', y='product_category_name', data=bottom_k_shipping_time, palette='coolwarm', ax=ax2)

        # Menambahkan label pada setiap bar di plot bottom
        for p in ax2.patches:
            ax2.annotate(f'{p.get_width():.2f}', 
                        (p.get_width(), p.get_y() + p.get_height() / 2), 
                        ha='left', va='center', fontsize=12)

        ax2.set_title(f'Bottom {top_k} Kategori Berdasarkan Rata-rata Waktu Pengiriman', fontsize=15)
        ax2.set_xlabel('Rata-rata Waktu Pengiriman (Hari)')
        ax2.set_ylabel('Kategori Produk')

        plt.tight_layout()
        st.pyplot(fig)  # Menyertakan fig di sini

        # Adding Insights with HTML Styling
        st.markdown("""
            <h3 style="color:#FF6347;">Insights</h3>
            <p><b>Insight dari Visualisasi 1:</b> Pada <i>scatter plot</i> yang menunjukkan hubungan antara <i>waktu pengiriman</i> dan <i>rating review</i> tahun 2017, 
            dapat terlihat bahwa sebagian besar ulasan dengan rating tinggi (4.0 - 5.0) cenderung memiliki waktu pengiriman yang singkat (0-50 hari). 
            Namun, ada juga ulasan dengan rating rendah (1.0 - 2.0) yang terjadi pada waktu pengiriman yang lebih lama, menunjukkan bahwa pengiriman yang lebih lambat dapat mempengaruhi ketidakpuasan pelanggan.</p>
            
            <p><b>Insight dari Visualisasi 2:</b> Pada <i>Top 5 kategori produk</i> dengan rata-rata waktu pengiriman tercepat, kategori <i>moveis_escritorio</i> mencatatkan 
            rata-rata waktu pengiriman 17.65 hari, yang menunjukkan pengiriman yang relatif cepat dibandingkan kategori lainnya. 
            Di sisi lain, pada <i>Bottom 5 kategori produk</i>, kategori seperti <i>cds_dvds_musicais</i> dan <i>portateis_casa_forno_e_cafe</i> memiliki rata-rata waktu pengiriman lebih lama sekitar 8-9 hari, 
            yang menunjukkan adanya masalah pada efisiensi logistik.</p>
            
            <p>Data ini menunjukkan bahwa pengiriman yang lebih cepat dapat berkontribusi pada kepuasan pelanggan yang lebih tinggi, sementara pengiriman yang lebih lama dapat menyebabkan ketidakpuasan yang signifikan.</p>
        """, unsafe_allow_html=True)

        # Extra Styling for the page
        st.markdown("""
            <style>
                h3 {
                    color: #4CAF50;
                }
                p {
                    font-size: 16px;
                    line-height: 1.6;
                }
                i {
                    color: #FF6347;
                }
            </style>
        """, unsafe_allow_html=True)


# -------------------------------------- Tab 4: RFM Analysis -------------------------------------- #
with tab4:
            # Menampilkan judul dengan CSS custom
    st.markdown('<div class="section-title">📊 RFM Analysis</div>', unsafe_allow_html=True)

    # Menambahkan deskripsi halaman
    st.markdown("""
        <div class="description">
            Bagian ini akan berisi analisis RFM untuk segmentasi pelanggan berdasarkan Recency, Frequency, dan Monetary.
        </div>
    """, unsafe_allow_html=True)


    # Pastikan order_purchase_timestamp dikonversi ke datetime
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    # Hitung Recency, Frequency, dan Monetary
    current_date = df['order_purchase_timestamp'].max()  # Tanggal transaksi terakhir dalam dataset

    # 1. Recency - selisih hari antara transaksi terakhir dan transaksi masing-masing pelanggan
    df['recency'] = (current_date - df['order_purchase_timestamp']).dt.days

    # 2. Frequency - jumlah transaksi per customer_id
    frequency = df.groupby('customer_id')['order_id'].count().reset_index()
    frequency.columns = ['customer_id', 'frequency']

    # 3. Monetary - total pengeluaran per customer_id
    df['total_spent'] = df['price'] + df['freight_value']
    monetary = df.groupby('customer_id')['total_spent'].sum().reset_index()
    monetary.columns = ['customer_id', 'monetary']

    # Gabungkan semua hasilnya ke dalam satu dataframe
    rfm = frequency.merge(monetary, on='customer_id')
    rfm = rfm.merge(df[['customer_id', 'recency']].drop_duplicates(), on='customer_id')

    # Membuat dua kolom
    col1, col2 = st.columns(2)

    # Menampilkan Top 10 Frequency menggunakan Plotly Express
    top_10_frequency = rfm.nlargest(10, 'frequency')

    fig1 = px.bar(top_10_frequency, x='customer_id', y='frequency', 
                labels={'customer_id': 'Customer ID', 'frequency': 'Frequency'},
                title='Top 10 Frequency Transaksi')

    col1.plotly_chart(fig1, use_container_width=True)

    # Menampilkan Top 5 Monetary dan Bottom 5 Monetary menggunakan Plotly Express
    top_10_monetary = rfm.nlargest(5, 'monetary')
    bottom_10_monetary = rfm.nsmallest(5, 'monetary')

    # Top 5 Monetary
    fig2 = px.bar(top_10_monetary, x='monetary', y='customer_id', 
                orientation='h', 
                labels={'monetary': 'Monetary (IDR)', 'customer_id': 'Customer ID'},
                title='Top 5 Monetary Pengeluaran')

    col2.plotly_chart(fig2, use_container_width=True)

    # Bottom 5 Monetary
    fig3 = px.bar(bottom_10_monetary, x='monetary', y='customer_id', 
                orientation='h', 
                labels={'monetary': 'Monetary (IDR)', 'customer_id': 'Customer ID'},
                title='Bottom 5 Monetary Pengeluaran')

    col2.plotly_chart(fig3, use_container_width=True)

    # Recency Distribution menggunakan Plotly Express
    fig4 = px.histogram(rfm, x='recency', nbins=10, 
                        labels={'recency': 'Hari Sejak Transaksi Terakhir'},
                        title='Distribusi Recency')

    col1.plotly_chart(fig4, use_container_width=True)

    # Rekomendasi Bisnis
    st.markdown("""
    **Beberapa rekomendasi bisnis yang bisa dilakukan antara lain:**

    1. **Strategi Loyalitas untuk Pelanggan dengan Frekuensi Tinggi**  
    - Berikan **program loyalitas atau VIP membership** kepada pelanggan dengan frekuensi transaksi tinggi untuk mempertahankan mereka.
    - **Personalisasi promosi** dengan memberikan diskon atau voucher eksklusif untuk pembelian selanjutnya.

    2. **Strategi Upselling dan Cross-selling untuk Pelanggan dengan Pengeluaran Tinggi**  
    - Pelanggan yang memiliki pengeluaran besar cenderung memiliki daya beli tinggi, sehingga bisa ditargetkan dengan **produk premium atau bundling eksklusif**.
    - Gunakan **strategi pemasaran berbasis rekomendasi** agar mereka tertarik membeli produk lain yang sesuai dengan histori pembeliannya.

    3. **Strategi Retensi untuk Pelanggan yang Mulai Tidak Aktif**  
    - Untuk pelanggan yang belum bertransaksi dalam **lebih dari 300 hari**, kirimkan **email re-engagement**, seperti penawaran spesial, diskon eksklusif, atau rekomendasi produk baru.
    - Berikan **insentif cashback atau poin reward** agar mereka kembali melakukan transaksi.

    4. **Strategi Konversi untuk Pelanggan dengan Pengeluaran Rendah**  
    - Pelanggan dengan pengeluaran rendah mungkin masih dalam tahap eksplorasi, sehingga bisa diberikan **promo produk pertama** atau **gratis ongkir** agar mereka lebih tertarik melakukan pembelian lebih besar.
    - Berikan edukasi mengenai produk dengan **konten interaktif, demo, atau review pengguna** untuk meningkatkan kepercayaan mereka dalam melakukan transaksi lebih besar.
    """)
    
    
with tab5:
    # Menghitung percentile untuk total_spent dan recency
    percentiles_total_spent = df['total_spent'].quantile([0.25, 0.50, 0.75])
    percentiles_recency = df['recency'].quantile([0.25, 0.50, 0.75])

    # Mendapatkan nilai percentiles untuk total_spent dan recency
    Q1_total_spent = percentiles_total_spent[0.25]
    Q2_total_spent = percentiles_total_spent[0.50]
    Q3_total_spent = percentiles_total_spent[0.75]

    Q1_recency = percentiles_recency[0.25]
    Q2_recency = percentiles_recency[0.50]
    Q3_recency = percentiles_recency[0.75]

    # Fungsi untuk binning berdasarkan percentile pada total_spent
    def total_spent_percentile_grouping(row):
        if row['total_spent'] <= Q1_total_spent:
            return 'Rendah Pengeluaran'
        elif Q1_total_spent < row['total_spent'] <= Q3_total_spent:
            return 'Pengeluaran Menengah'
        else:
            return 'Tinggi Pengeluaran'

    # Fungsi untuk binning berdasarkan percentile pada recency
    def recency_percentile_grouping(row):
        if row['recency'] <= Q1_recency:
            return 'Pelanggan Baru'
        elif Q1_recency < row['recency'] <= Q3_recency:
            return 'Pelanggan Rutin'
        else:
            return 'Pelanggan Tidak Aktif'

    # Fungsi untuk binning review_score
    def review_score_grouping(row):
        if row['review_score'] == 5:
            return 'Puas'
        elif row['review_score'] in [4, 3]:
            return 'Cukup Puas/Biasa'
        else:
            return 'Tidak Puas'

    # Terapkan fungsi binning ke dalam kolom baru
    df['total_spent_percentile_group'] = df.apply(total_spent_percentile_grouping, axis=1)
    df['recency_percentile_group'] = df.apply(recency_percentile_grouping, axis=1)
    df['review_score_group'] = df.apply(review_score_grouping, axis=1)

    # Fungsi untuk menampilkan label di setiap bar
    def plot_bar_with_labels(ax, data, title, xlabel, ylabel, rotate_labels=False):
        sns.countplot(x=data, ax=ax, palette="Set2")
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        # Menambahkan label di setiap bar
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        fontsize=12, color='black', fontweight='bold', 
                        xytext=(0, 9), textcoords='offset points')
            
                # Memutar label di sumbu x
        if rotate_labels:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha='center')

    # Menyiapkan data untuk value_counts
    total_spent_groups = df['total_spent_percentile_group'].value_counts()
    recency_groups = df['recency_percentile_group'].value_counts()
    review_score_groups = df['review_score_group'].value_counts()

    # Streamlit Layout
    st.title('Clustering - With Manual Grouping/Binning')

    # Membuat subplot dengan 3 bar chart (1x3)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Plot untuk 'total_spent_percentile_group'
    plot_bar_with_labels(axes[0], df['total_spent_percentile_group'], 
                        'Distribusi Pengeluaran', 'Pengeluaran', 'Jumlah Pelanggan', rotate_labels=True)

    plot_bar_with_labels(axes[1], df['recency_percentile_group'], 
                            'Distribusi Recency', 'Recency (Hari)', 'Jumlah Pelanggan')
    
    # Plot untuk 'review_score_group'
    plot_bar_with_labels(axes[2], df['review_score_group'], 
                        'Distribusi Skor Ulasan', 'Skor Ulasan', 'Jumlah Pelanggan')

    # Layout Adjustments
    plt.tight_layout()
    st.pyplot(fig)
    
# Plot untuk 'recency_percentile_group'
col1, col2, col3 = st.columns([1, 1, 1])  # Membagi kolom menjadi 3

with col1:
    st.markdown("""
    **Distribusi Pengeluaran**:

    Mayoritas pelanggan berada dalam kategori pengeluaran menengah (56.600 pelanggan), menunjukkan bahwa sebagian besar pelanggan tidak berbelanja dalam jumlah kecil atau sangat besar.  
    Segmen pelanggan dengan pengeluaran rendah (28.300 pelanggan) dan tinggi (28.293 pelanggan) relatif seimbang, yang menunjukkan adanya dua kelompok pelanggan yang mungkin membutuhkan pendekatan strategi yang berbeda.
    """)

with col2:
    st.markdown("""
    **Distribusi Recency (Kapan Terakhir Bertransaksi)**:

    Pelanggan rutin (56.586 pelanggan) mendominasi, yang menunjukkan bahwa mayoritas pelanggan masih aktif melakukan transaksi dalam periode waktu yang relatif dekat.  
    Namun, terdapat sekitar 28.065 pelanggan yang tergolong tidak aktif, yang berpotensi mengalami churn dan perlu ditargetkan untuk re-engagement.
    """)

with col3:
    st.markdown("""
    **Distribusi Skor Ulasan**:

    Mayoritas pelanggan (65.145 pelanggan) memberikan rating "puas" (5 bintang), menunjukkan bahwa layanan atau produk secara keseluruhan mendapatkan ulasan positif.  
    Namun, 16.704 pelanggan merasa tidak puas, yang merupakan jumlah signifikan dan perlu dianalisis lebih lanjut untuk mengetahui penyebab utama ketidakpuasan mereka.
    """)
