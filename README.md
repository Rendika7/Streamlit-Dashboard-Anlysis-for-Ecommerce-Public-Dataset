# 📊 Proyek Analisis Data & Dashboard Interaktif

## 📌 Deskripsi
Repositori ini berisi proyek analisis data yang mencakup **Eksplorasi Data (EDA), Analisis RFM (Recency, Frequency, Monetary), serta Visualisasi Data** dalam bentuk **dashboard interaktif** menggunakan **Streamlit**. Data yang digunakan telah melewati tahap preprocessing untuk memastikan kualitasnya sebelum dianalisis.

## 🛠️ Teknologi yang Digunakan
- **Python** (Pandas, Matplotlib, Seaborn, Plotly, NumPy)
- **Streamlit** (Dashboard interaktif)
- **Jupyter Notebook** (Eksplorasi dan analisis data)
- **ydata_profiling** (Pandas Profiling untuk analisis cepat)

## 📂 Struktur Repository
```
📦 Nama Repository
 ┣ 📂 dashboard                    # Folder untuk file dashboard interaktif
 ┃ ┣ 📜 dashboard.py               # Kode utama untuk dashboard interaktif
 ┃ ┣ 📂 .streamlit                 # Konfigurasi untuk Streamlit
 ┃ ┣ 📂 audio                      # Folder untuk file musik latar (opsional)
 ┃ ┣ 📜 main_data.csv              # Data yang digunakan untuk dashboard streamlit
 ┃ ┗ 📂 image                      # Folder untuk gambar visualisasi
 ┣ 📂 data                         # Folder untuk dataset yang digunakan (E-Commerce Public Dataset)
 ┃ ┣ 📜 customers_dataset.csv       # Data pelanggan
 ┃ ┣ 📜 geolocation_dataset.csv     # Data lokasi pelanggan
 ┃ ┣ 📜 order_items_dataset.csv     # Data item pesanan
 ┃ ┣ 📜 order_payments_dataset.csv  # Data pembayaran
 ┃ ┣ 📜 order_reviews_dataset.csv   # Data ulasan pelanggan
 ┃ ┣ 📜 orders_dataset.csv          # Data pesanan
 ┃ ┣ 📜 product_category_name_translation.csv  # Kategori produk
 ┃ ┣ 📜 products_dataset.csv        # Data produk
 ┃ ┗ 📜 sellers_dataset.csv         # Data penjual
 ┣ 📜 notebook.ipynb     # Notebook Jupyter untuk analisis data
 ┣ 📜 README.md                      # Dokumentasi proyek
 ┣ 📜 How to use.txt                  # Panduan penggunaan
 ┣ 📜 url.txt                          # Link referensi terkait proyek
 ┗ 📜 main_data.csv                    # Dataset utama yang telah dibersihkan
```

## 🔍 Fitur Utama
### 1️⃣ **Exploratory Data Analysis (EDA)**
- Menampilkan **statistik deskriptif** dari dataset.
- Visualisasi distribusi data dengan **histogram dan heatmap korelasi**.
- Identifikasi tren dan pola utama dalam data.

### 2️⃣ **Analisis RFM untuk Segmentasi Pelanggan**
- **Recency**: Mengukur waktu sejak transaksi terakhir pelanggan.
- **Frequency**: Menghitung jumlah transaksi yang dilakukan pelanggan.
- **Monetary**: Menentukan total pengeluaran pelanggan.
- Klasifikasi pelanggan berdasarkan nilai RFM.

### 3️⃣ **Dashboard Interaktif dengan Streamlit**
- Menyajikan data dalam bentuk **grafik dinamis** menggunakan **Plotly & Seaborn**.
- **Sidebar navigasi** untuk eksplorasi yang lebih mudah.
- **Pandas Profiling** untuk analisis data secara otomatis.

## 🚀 Cara Menjalankan Proyek
### **1. Clone Repository**
```sh
git clone https://github.com/username/repository-name.git
cd repository-name
```

### **2. Make Virtual Environment With Conda**
Pastikan Anda membuat Virtual Environment baru untuk menghindari conflict:
```sh
conda create --name streamlit-venv python=3.9
conda activate streamlit-venv
```

### **3. Install Dependencies**
Pastikan Anda memiliki **Python 3.9+** dan jalankan perintah berikut:
```sh
pip install -r requirements.txt
```

### **4. Jalankan Dashboard**
```sh
streamlit run dashboard/dashboard.py
```

## 📌 Contoh Visualisasi
### 📊 **Analisis RFM**
![Distribusi RFM](dashboard/image/rfm_analysis.png)

### 📈 **Dashboard Interaktif**
![Dashboard](dashboard/image/dashboard_preview.png)

## 🤝 Kontribusi
Jika Anda ingin berkontribusi, silakan buat **pull request** atau buka **issue** untuk diskusi lebih lanjut.

## 📧 Kontak
- **Nama**: Rendika Nurhartanto Suharto
- **LinkedIn**: [Profil Saya](https://www.linkedin.com/in/rendika-nurhartanto-s-882431218/)
- **GitHub**: [Rendika7](https://github.com/Rendika7)
- **Email**: rendikarendi96@gmail.com

---
✍ **Dibuat dengan ❤️ oleh Rendika Nurhartanto Suharto**