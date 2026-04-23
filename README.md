# Tutorial: Thresholding

Aplikasi web berbasis Streamlit untuk melakukan thresholding pada gambar medis dengan berbagai metode.

## Daftar Isi
- [Prasyarat](#prasyarat)
- [Instalasi](#instalasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Cara Penggunaan](#cara-penggunaan)
- [Metode Thresholding](#metode-thresholding)

---

## Prasyarat

Sebelum memulai, pastikan Anda telah menginstall:
- Python 3.7 atau versi lebih tinggi
- pip (package installer untuk Python)

---

## Instalasi

### 1. Clone Repository (Opsional)
Jika Anda mengambil dari GitHub:
```bash
git clone https://github.com/Fauzan-Aldi/Thresholding.git
cd Thresholding
```

### 2. Install Dependencies
Jalankan perintah berikut untuk menginstall semua library yang dibutuhkan:

```bash
pip install streamlit scikit-image plotly
```

Atau jika menggunakan requirements.txt:
```bash
pip install -r requirements.txt
```

**Library yang dibutuhkan:**
| Library | Fungsi |
|---------|--------|
| streamlit | Framework web untuk aplikasi |
| scikit-image | Pemrosesan gambar dan thresholding |
| plotly | Visualisasi histogram interaktif |

---

## Menjalankan Aplikasi

### 1. Pastikan File Gambar Tersedia
Untuk mencoba aplikasi, siapkan file gambar grayscale (contoh: `Lungs.jpg` atau `writing.png` yang sudah tersedia di folder).

### 2. Jalankan Streamlit
```bash
streamlit run app.py
```

Atau dengan Python:
```bash
python -m streamlit run app.py
```

### 3. Buka di Browser
Setelah menjalankan perintah di atas, aplikasi akan otomatis terbuka di browser default Anda dengan alamat:
- **Local URL:** `http://localhost:8501`

---

## Cara Penggunaan

### Langkah 1: Unggah Gambar
1. Klik tombol **"Unggah file gambar"**
2. Pilih file gambar grayscale dari komputer Anda
3. Aplikasi akan otomatis memuat dan menampilkan gambar

### Langkah 2: Pilih Metode Thresholding
Dari dropdown **"Pilih metode thresholding yang diinginkan"**, pilih salah satu:
- **Manual Thresholding** - Tentukan nilai threshold secara manual
- **Local Thresholding** - Threshold adaptif berbasis wilayah
- **Global Thresholding** - Threshold otomatis untuk seluruh gambar

### Langkah 3: Sesuaikan Parameter
Setiap metode memiliki parameter yang dapat disesuaikan:
- **Manual**: Geser slider untuk menentukan nilai threshold
- **Local**: Pilih metode adaptif (Gaussian, Mean, dll)
- **Global**: Pilih algoritma otomatis (Otsu, Triangle, dll)

### Langkah 4: Lihat Hasil
- Histogram gambar akan ditampilkan
- Gambar hasil thresholding akan muncul
- Bandingkan gambar asli dengan hasil

---

## Metode Thresholding

### 1. Manual Thresholding
Memungkinkan Anda menentukan nilai threshold sendiri menggunakan slider.
- **Kelebihan**: Kontrol penuh atas hasil
- **Kegunaan**: Eksperimen dan penyesuaian manual

### 2. Local Thresholding (Adaptive Thresholding)
Menerapkan threshold berbeda untuk setiap wilayah gambar berdasarkan karakteristik lokal.
- **Metode**: Gaussian, Mean, Median
- **Block Size**: Ukuran wilayah lokal
- **Offset**: Penyesuaian nilai threshold
- **Kegunaan**: Gambar dengan pencahayaan tidak merata

### 3. Global Thresholding
Menggunakan satu nilai threshold untuk seluruh gambar dengan algoritma otomatis.
- **Algoritma**:
  - **Otsu**: Meminimalkan varians intra-kelas
  - **Triangle**: Berbasis geometri
  - **Minimum**: Berbasis histogram multimodal
  - **IsoData**: Iteratif thresholding
- **Kegunaan**: Gambar dengan kontras baik dan pencahayaan merata

---

## Troubleshooting

### Error: "No module named 'skimage'"
**Solusi**: Install scikit-image
```bash
pip install scikit-image
```

### Error: "No module named 'streamlit'"
**Solusi**: Install streamlit
```bash
pip install streamlit
```

### Gambar tidak terbaca
**Solusi**: Pastikan:
- File gambar ada di folder yang sama dengan `app.py`
- Format gambar didukung (JPG, PNG, TIFF)
- Gambar dalam mode grayscale

---

## Struktur File
```
Thresholding/
├── app.py                  # Aplikasi utama Streamlit
├── global_thresholding.py  # Modul thresholding global
├── local_thresholding.py   # Modul thresholding lokal
├── manual_thresholding.py  # Modul thresholding manual
├── requirements.txt        # Daftar dependencies
├── Lungs.jpg              # Contoh gambar
├── writing.png            # Contoh gambar
└── tutorial.md            # File tutorial ini
```

---

## Tips
- Gunakan gambar grayscale untuk hasil terbaik
- Cobalah semua metode untuk melihat mana yang paling cocok untuk gambar Anda
- Sesuaikan parameter pada Local Thresholding untuk gambar kompleks
- Screenshot hasil thresholding untuk dokumentasi

---

## Kontak
Jika ada pertanyaan atau masalah, silakan buat issue di repository GitHub.
