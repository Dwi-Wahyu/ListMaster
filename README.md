<h1 align="center">ListMaster</h1>

### Apa fungsi library ini ?

ListMaster adalah library yang memungkinkan anda untuk menyortir, memodifikasi, menggabungkan dan masih banyak lagi

## 1. Modul `list_sorting`

Modul ini berisi berbagai algoritma pengurutan yang dapat digunakan untuk mengurutkan data dalam bentuk array atau list. Algoritma yang disertakan antara lain: **Bubble Sort**, **Selection Sort**, **Insertion Sort**, **Merge Sort**, **Quick Sort**, serta **Tim Sort** yang merupakan sorting bawaan Python. Setiap algoritma mendukung pengurutan secara ascending (menaik) maupun descending (menurun).

### Daftar Algoritma

1. **Bubble Sort**: 
   - Mengurutkan dengan membandingkan elemen bersebelahan dan menukarnya jika diperlukan. Proses diulangi sampai semua elemen terurut.

2. **Selection Sort**: 
   - Menemukan elemen terkecil atau terbesar di bagian tidak terurut dan menukarnya dengan elemen di posisi yang sesuai.

3. **Insertion Sort**: 
   - Mengurutkan dengan cara memasukkan elemen dari bagian tidak terurut ke bagian yang sudah terurut pada posisi yang tepat.

4. **Merge Sort**: 
   - Menggunakan pendekatan divide and conquer untuk membagi array, mengurutkan setiap bagian secara rekursif, lalu menggabungkannya kembali.

5. **Quick Sort**: 
   - Menggunakan pivot untuk mempartisi array menjadi dua bagian, dan mengurutkan secara rekursif pada kedua bagian.

6. **Tim Sort**: 
   - Sorting bawaan Python yang merupakan kombinasi dari Merge Sort dan Insertion Sort, dioptimalkan untuk performa.

### Penggunaan

Setiap fungsi pengurutan menerima dua parameter:

- **arr**: List yang akan diurutkan.
- **reverse** (opsional): Boolean yang menentukan urutan hasil pengurutan. Jika `True`, list akan diurutkan secara menurun (descending). Jika `False`, list akan diurutkan secara menaik (ascending). Nilai default adalah `False`.

#### Contoh Penggunaan

```python
from sorting_module import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, tim_sort

arr = [64, 25, 12, 22, 11]

# Bubble Sort (ascending)
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]

# Quick Sort (descending)
sorted_arr = quick_sort(arr, reverse=True)
print(sorted_arr)  # Output: [64, 25, 22, 12, 11]

# Tim Sort (ascending)
sorted_arr = tim_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]
```

Modul ini dirancang untuk memberikan kemudahan dalam mengurutkan data dengan berbagai metode yang efisien. Silakan gunakan sesuai kebutuhan Anda!

## Modul statistik_list.py

Modul ini menyediakan fungsi-fungsi untuk melakukan analisis statistik pada list, termasuk menghitung rata-rata, median, nilai minimum, nilai maksimum, dan modus. Modul ini dirancang untuk mempermudah pengguna dalam melakukan analisis data numerik.

### Fungsi-Fungsi

#### 1. rata_rata(target_list)

*Deskripsi*: 
Menghitung rata-rata dari elemen numerik dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen numerik (int atau float).

*Pengembalian*:
- float: Rata-rata dari elemen dalam list. Mengembalikan 0 jika list kosong.

*Contoh*:
python
data = [1, 2, 3, 4]
result = rata_rata(data)
# Output: 2.5


---

#### 2. median(target_list)

*Deskripsi*: 
Menghitung median dari elemen numerik dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen numerik (int atau float).

*Pengembalian*:
- float: Nilai median dari elemen dalam list.

*Contoh*:
python
data = [1, 2, 3, 4]
result = median(data)
# Output: 2.5


---

#### 3. min_max(target_list)

*Deskripsi*: 
Mengembalikan nilai minimum dan maksimum dari elemen numerik dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen numerik (int atau float).

*Pengembalian*:
- tuple: Tuple yang berisi nilai minimum dan maksimum.

*Contoh*:
python
data = [1, 2, 3, 4]
result = min_max(data)
# Output: (1, 4)


---

#### 4. modus(target_list)

*Deskripsi*: 
Menghitung modus dari elemen dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen (int, float, atau tipe data lainnya).

*Pengembalian*:
- list atau string: Daftar modus jika ada lebih dari satu, atau pesan jika semua elemen muncul dengan frekuensi yang sama.

*Contoh*:
python
data = [1, 2, 2, 3]
result = modus(data)
# Output: [2]


---

### Penggunaan

Untuk menggunakan modul ini, cukup impor modul dalam skrip Python Anda dan panggil fungsi yang diperlukan.

python
from statistik_list import *

data = [1, 2, 2, 3, 4, 4, 4, 5]

print("Rata-rata:", rata_rata(data))
print("Median:", median(data))
print("Min dan Max:", min_max(data))
print("Modus:", modus(data))

### Catatan

- Pastikan bahwa list yang digunakan untuk fungsi ini hanya berisi elemen numerik (int atau float).
- Modul ini akan menghasilkan exception jika list tidak memenuhi syarat.

## 5. modul `list_search`

Modul ini berisi implementasi Python dari berbagai algoritma pencarian, termasuk pencarian linear dan pencarian biner, serta fungsi utilitas untuk memeriksa apakah sebuah list diurutkan dalam urutan menaik.

### Fungsi

#### 1. `is_sorted(arr)`

Memeriksa apakah sebuah list diurutkan dalam urutan menaik.

- **Parameter:**
  - `arr`: Sebuah list elemen yang akan diperiksa.
  
- **Mengembalikan:**
  - `True` jika list diurutkan, `False` jika tidak.

#### 2. `linear_search(arr, target)`

Melakukan pencarian linear untuk menemukan semua kemunculan elemen target dalam sebuah list.

- **Parameter:**
  - `arr`: Sebuah list elemen yang akan dicari.
  - `target`: Elemen yang dicari.
  
- **Mengembalikan:**
  - Sebuah list indeks di mana target ditemukan, atau list kosong jika tidak ditemukan.

- **Mengangkat:**
  - `ValueError`: Jika argumen pertama bukan sebuah list.

#### 3. `binary_search(arr, target)`

Melakukan pencarian biner untuk menemukan semua kemunculan elemen target dalam sebuah list yang terurut.

- **Parameter:**
  - `arr`: Sebuah list yang sudah diurutkan untuk pencarian.
  - `target`: Elemen yang dicari.
  
- **Mengembalikan:**
  - Sebuah list indeks di mana target ditemukan, atau list kosong jika tidak ditemukan.

- **Mengangkat:**
  - `ValueError`: Jika argumen pertama bukan sebuah list atau jika list tidak diurutkan dalam urutan menaik.

### Penggunaan

Untuk menggunakan fungsi-fungsi ini, cukup impor ke dalam skrip Python Anda dan panggil dengan parameter yang sesuai. Pastikan bahwa list sudah diurutkan sebelum menggunakan fungsi `binary_search`.

### Contoh

#### Contoh dengan Angka

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

#### Contoh dengan String

```python
arr = ["apel", "jeruk", "jeruk", "mangga", "pisang"]
target = "jeruk"

# Periksa apakah list diurutkan
print(is_sorted(arr))  # Output: True

# Lakukan pencarian linear
print(linear_search(arr, target))  # Output: [1, 2]

# Lakukan pencarian biner
print(binary_search(arr, target))  # Output: [1, 2]
```

#### Contoh dengan Tuple

```python
arr = [(1, 'a'), (2, 'b'), (2, 'b'), (3, 'c')]
target = (2, 'b')

# Periksa apakah list diurutkan
print(is_sorted(arr))  # Output: True

# Lakukan pencarian linear
print(linear_search(arr, target))  # Output: [1, 2]

# Lakukan pencarian biner
print(binary_search(arr, target))  # Output: [1, 2]
```

#### Contoh dengan Boolean

```python
arr = [True, True, False, False, True]
target = True

# Periksa apakah list diurutkan
print(is_sorted(arr))  # Output: False

# Lakukan pencarian linear
print(linear_search(arr, target))  # Output: [0, 1, 4]

# Pencarian biner tidak dapat dilakukan karena list tidak terurut
```

## 1. Modul list_modification
Modul ini menyediakan tiga fungsi utama untuk menggabungkan beberapa list menjadi satu list. Fungsinya termasuk menggabungkan list dengan atau tanpa duplikasi, serta menjaga urutan elemen dalam penggabungan tanpa duplikat.

## Fitur
+ gabungkan_list: Menggabungkan sejumlah list menjadi satu list besar tanpa menghapus elemen duplikat.

+ gabungkan_tanpa_duplikat: Menggabungkan list tanpa elemen duplikat, tanpa mempertahankan urutan kemunculan.

+ gabungkan_list_unik: Menggabungkan list tanpa elemen duplikat, dengan mempertahankan urutan kemunculan pertama dari setiap elemen.

## Instalasi
Modul ini tidak memerlukan instalasi khusus. Cukup salin kode fungsi ke dalam proyek Python Anda.

## Fungsi
### 1. gabungkan_list(*lists)
Fungsi ini menggabungkan sejumlah list menjadi satu list besar. Semua elemen dari list yang diberikan akan dimasukkan ke dalam list hasil, tanpa menghapus duplikat.

### Parameter:
+ *lists: Satu atau lebih list yang ingin digabungkan

### Return:
+ Mengembalikan satu list besar yang berisi semua elemen dari list yang diberikan.

### Kesalahan yang Mungkin Terjadi:
+ Jika salah satu argumen bukan list, akan muncul TypeError.

### Contoh Penggunaan
``` py 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
gabungan = gabungkan_list(list1, list2)
print(gabungan)  # Output: [1, 2, 3, 4, 5, 6]

```
### 2. gabungkan_tanpa_duplikat(*lists)
Fungsi ini menggabungkan sejumlah list menjadi satu list besar tanpa menyertakan elemen yang duplikat. Pengurutan elemen mungkin berubah karena penggunaan set untuk menghapus duplikat.

### Parameter:
+ *lists: Satu atau lebih list yang ingin digabungkan.

+ Return:
Mengembalikan satu list besar tanpa elemen duplikat.

+ Kesalahan yang Mungkin Terjadi:
Jika salah satu argumen bukan list, akan muncul TypeError.

### Contoh Penggunaan:
```py
list1 = [1, 2, 3, 3]
list2 = [4, 5, 6, 4]
gabungan = gabungkan_tanpa_duplikat(list1, list2)
print(gabungan)  # Output: [1, 2, 3, 4, 5, 6]
```
### 3. gabungkan_list_unik(*lists)
Fungsi ini menggabungkan sejumlah list menjadi satu list besar tanpa elemen duplikat, sambil mempertahankan urutan kemunculan pertama dari setiap elemen. Tidak seperti gabungkan_tanpa_duplikat, fungsi ini tidak mengubah urutan elemen yang pertama kali muncul.

### Parameter:
*lists: Satu atau lebih list yang ingin digabungkan.

### Return:
Mengembalikan satu list besar yang berisi semua elemen tanpa elemen duplikat, mempertahankan urutan kemunculan pertama.

### Kesalahan yang Mungkin Terjadi:
Jika salah satu argumen bukan list, akan muncul TypeError.

### Contoh Penggunaan:
```py 
list1 = [1, 2, 3, 3]
list2 = [4, 5, 6, 4]
gabungan = gabungkan_list_unik(list1, list2)
print(gabungan)  # Output: [1, 2, 3, 4, 5, 6]
```
### Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan kode ini selama menyertakan atribusi yang sesuai.

