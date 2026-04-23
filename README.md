# Thresholding Medical Images

Aplikasi web berbasis Streamlit untuk melakukan **thresholding** pada gambar medis dengan berbagai metode (Manual, Local, dan Global Thresholding).

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Overview

Aplikasi ini memungkinkan pengguna untuk:
- Mengunggah gambar medis (grayscale)
- Menerapkan thresholding dengan 3 metode berbeda
- Melihat histogram gambar secara interaktif
- Menyesuaikan parameter thresholding
- Membandingkan hasil thresholding dengan gambar asli

---

## Instalasi & Penggunaan

### Prasyarat
- Python 3.7 atau lebih tinggi
- pip (Python package installer)

### 1. Install Dependencies

```bash
pip install streamlit scikit-image plotly
```

### 2. Clone Repository (Opsional)

```bash
git clone https://github.com/Fauzan-Aldi/Thresholding.git
cd Thresholding
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada alamat `http://localhost:8501`

---

## Cara Penggunaan

### 1. Unggah Gambar
- Klik tombol **"Unggah file gambar"**
- Pilih file gambar (JPG, PNG, TIFF) dari komputer

### 2. Pilih Metode Thresholding
Dari dropdown pilih salah satu metode:
- **Manual Thresholding** - Atur nilai threshold secara manual
- **Local Thresholding** - Threshold adaptif berbasis wilayah
- **Global Thresholding** - Threshold otomatis dengan algoritma

### 3. Sesuaikan Parameter
- **Manual**: Geser slider untuk nilai threshold (0-255)
- **Local**: Pilih metode (Gaussian/Mean/Median) dan ukuran blok
- **Global**: Pilih algoritma (Otsu, Triangle, Minimum, IsoData)

### 4. Lihat Hasil
- Histogram gambar ditampilkan secara interaktif
- Gambar asli dan hasil thresholding ditampilkan berdampingan

---

## Fitur Thresholding

| Metode | Deskripsi | Kegunaan |
|--------|-----------|----------|
| **Manual** | Tentukan threshold sendiri dengan slider | Eksperimen, kontrol penuh |
| **Local (Adaptive)** | Threshold berbeda per wilayah | Gambar dengan pencahayaan tidak merata |
| **Global (Otsu, dll)** | Satu threshold untuk seluruh gambar | Gambar dengan kontras baik |

---

## Struktur Project

```
Thresholding/
├── app.py                  # Aplikasi utama Streamlit
├── global_thresholding.py  # Modul Global Thresholding
├── local_thresholding.py   # Modul Local/Adaptive Thresholding
├── manual_thresholding.py  # Modul Manual Thresholding
├── requirements.txt        # Dependencies
├── tutorial.md            # Tutorial lengkap
├── Lungs.jpg             # Contoh gambar
└── writing.png           # Contoh gambar
```

---

## Troubleshooting

### Module Not Found Error
```bash
# Install dependencies yang kurang
pip install streamlit scikit-image plotly
```

### Gambar Tidak Terbaca
- Pastikan file gambar ada di folder yang sama dengan `app.py`
- Gunakan format: JPG, PNG, atau TIFF
- Gambar sebaiknya dalam mode grayscale

---

## Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| streamlit | latest | Web framework |
| scikit-image | latest | Image processing |
| plotly | latest | Interactive visualization |

---

## Tutorial Lengkap

Untuk tutorial lengkap dengan penjelasan detail, lihat file [tutorial.md](tutorial.md).

---

## Screenshot

Aplikasi memiliki tampilan dengan:
- Background gradasi biru-putih
- Judul "Thresholding Medical Images" berwarna putih
- Interface bersih tanpa menu tambahan

---

## Lisensi

MIT License - Lihat file [LICENSE.txt](LICENSE.txt) untuk detail.

## Kontak

- GitHub: https://github.com/Fauzan-Aldi/Thresholding
- Author asli: Omar Alkousa (omar.ok1998@gmail.com)
