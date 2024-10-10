# ListMaster

### Apa fungsi library ini ?

ListMaster adalah library yang memungkinkan anda untuk menyortir, memodifikasi, menggabungkan dan masih banyak lagi


# 5. modul `list_search`

Modul ini berisi implementasi Python dari berbagai algoritma pencarian, termasuk pencarian linear dan pencarian biner, serta fungsi utilitas untuk memeriksa apakah sebuah list diurutkan dalam urutan menaik.

## Fungsi

### 1. `is_sorted(arr)`

Memeriksa apakah sebuah list diurutkan dalam urutan menaik.

- **Parameter:**
  - `arr`: Sebuah list elemen yang akan diperiksa.
  
- **Mengembalikan:**
  - `True` jika list diurutkan, `False` jika tidak.

### 2. `linear_search(arr, target)`

Melakukan pencarian linear untuk menemukan semua kemunculan elemen target dalam sebuah list.

- **Parameter:**
  - `arr`: Sebuah list elemen yang akan dicari.
  - `target`: Elemen yang dicari.
  
- **Mengembalikan:**
  - Sebuah list indeks di mana target ditemukan, atau list kosong jika tidak ditemukan.

- **Mengangkat:**
  - `ValueError`: Jika argumen pertama bukan sebuah list.

### 3. `binary_search(arr, target)`

Melakukan pencarian biner untuk menemukan semua kemunculan elemen target dalam sebuah list yang terurut.

- **Parameter:**
  - `arr`: Sebuah list yang sudah diurutkan untuk pencarian.
  - `target`: Elemen yang dicari.
  
- **Mengembalikan:**
  - Sebuah list indeks di mana target ditemukan, atau list kosong jika tidak ditemukan.

- **Mengangkat:**
  - `ValueError`: Jika argumen pertama bukan sebuah list atau jika list tidak diurutkan dalam urutan menaik.

## Penggunaan

Untuk menggunakan fungsi-fungsi ini, cukup impor ke dalam skrip Python Anda dan panggil dengan parameter yang sesuai. Pastikan bahwa list sudah diurutkan sebelum menggunakan fungsi `binary_search`.

## Contoh

```python
arr = [1, 2, 2, 3, 4, 5]
target = 2

# Periksa apakah list diurutkan
print(is_sorted(arr))  # Output: True

# Lakukan pencarian linear
print(linear_search(arr, target))  # Output: [1, 2]

# Lakukan pencarian biner
print(binary_search(arr, target))  # Output: [1, 2]
```

