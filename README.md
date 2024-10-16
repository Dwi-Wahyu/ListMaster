<h1 align="center">ListMaster</h1> <p align="center"> <b>Solusi Sederhana untuk Manipulasi List di Python</b> </p>

### Apa fungsi library ini ?

**ListMaster** adalah library Python yang dirancang untuk memudahkan berbagai operasi pada list, termasuk sorting, modifikasi, penggabungan, dan manipulasi data lainnya. Dengan berbagai algoritma sorting klasik serta alat bantu lainnya, ListMaster membantu Anda mengelola data berbasis list secara efisien.

### Instalasi 
Instalasi ListMaster sangat sederhana dan dapat dilakukan dengan perintah berikut :
```
pip install ListMaster
```

### Fitur Utama
- Sorting dengan berbagai algoritma (bubble sort, selection sort, dll.)
- Search untuk mencari elemen atau subset list
- Statistik dasar seperti rata-rata, median dan modus
- Filter data berdasarkan kondisi tertentu
- Modifikasi elemen list secara mudah
- Mengelola elemen unik dan menemukan elemen duplikat.

## 1. Modul `list_sorting`

Modul ini berisi berbagai algoritma pengurutan yang dapat digunakan untuk mengurutkan data dalam bentuk array atau list. Algoritma yang disertakan antara lain: **Bubble Sort**, **Selection Sort**, **Insertion Sort** dan **Tim Sort** yang merupakan sorting bawaan Python. Setiap algoritma mendukung pengurutan secara ascending (menaik) maupun descending (menurun).

### Daftar Algoritma

1. **Bubble Sort**: 
   - Mengurutkan dengan membandingkan elemen bersebelahan dan menukarnya jika diperlukan. Proses diulangi sampai semua elemen terurut.

2. **Selection Sort**: 
   - Menemukan elemen terkecil atau terbesar di bagian tidak terurut dan menukarnya dengan elemen di posisi yang sesuai.

3. **Insertion Sort**: 
   - Mengurutkan dengan cara memasukkan elemen dari bagian tidak terurut ke bagian yang sudah terurut pada posisi yang tepat.

4. **Tim Sort**: 
   - Sorting bawaan Python yang merupakan kombinasi dari Merge Sort dan Insertion Sort, dioptimalkan untuk performa.

### Penggunaan

Setiap fungsi pengurutan menerima dua parameter:

- **arr**: List yang akan diurutkan.
- **reverse** (opsional): Boolean yang menentukan urutan hasil pengurutan. Jika `True`, list akan diurutkan secara menurun (descending). Jika `False`, list akan diurutkan secara menaik (ascending). Nilai default adalah `False`.

#### Contoh Penggunaan

```python
from ListMaster import bubble_sort, selection_sort, insertion_sort, tim_sort

arr = [64, 25, 12, 22, 11]

# Bubble Sort (ascending)
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]

# Tim Sort (ascending)
sorted_arr = tim_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]
```

Modul ini dirancang untuk memberikan kemudahan dalam mengurutkan data dengan berbagai metode yang efisien. Silakan gunakan sesuai kebutuhan Anda!

## 2. Modul `list_search`

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

#### Contoh dengan Angka

```python
from ListMaster import is_sorted, linear_search, binary_search
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
from ListMaster import is_sorted, linear_search, binary_search
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
from ListMaster import is_sorted, linear_search, binary_search 
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

## 3. Modul `list_statistic`

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
```python
from ListMaster import rata_rata
data = [1, 2, 3, 4]
result = rata_rata(data) # Output: 2.5
```

#### 2. median(target_list)

*Deskripsi*: 
Menghitung median dari elemen numerik dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen numerik (int atau float).

*Pengembalian*:
- float: Nilai median dari elemen dalam list.

*Contoh*:
```python
from ListMaster import median
data = [1, 2, 3, 4]
result = median(data) # Output: 2.5
```

#### 3. min_max(target_list)

*Deskripsi*: 
Mengembalikan nilai minimum dan maksimum dari elemen numerik dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen numerik (int atau float).

*Pengembalian*:
- tuple: Tuple yang berisi nilai minimum dan maksimum.

*Contoh*:
```python
from ListMaster import min_max
data = [1, 2, 3, 4]
result = min_max(data) # Output: (1, 4)
```

#### 4. modus(target_list)

*Deskripsi*: 
Menghitung modus dari elemen dalam list.

*Parameter*:
- target_list (list): List yang berisi elemen (int, float, atau tipe data lainnya).

*Pengembalian*:
- list atau string: Daftar modus jika ada lebih dari satu, atau pesan jika semua elemen muncul dengan frekuensi yang sama.

*Contoh*:
```python
from ListMaster import modus
data = [1, 2, 2, 3]
result = modus(data) # Output: [2]
```

### Penggunaan

Untuk menggunakan modul ini, cukup impor modul dalam skrip Python Anda dan panggil fungsi yang diperlukan.

```python
from ListMaster import rata_rata, median, min_max, modus

data = [1, 2, 2, 3, 4, 4, 4, 5]

print("Rata-rata:", rata_rata(data))
print("Median:", median(data))
print("Min dan Max:", min_max(data))
print("Modus:", modus(data))
```

### Catatan

- Pastikan bahwa list yang digunakan untuk fungsi ini hanya berisi elemen numerik (int atau float).
- Modul ini akan menghasilkan exception jika list tidak memenuhi syarat.

## 4. Modul `list_filter`

#### 1. filter_genap(list_angka)

*Deskripsi*: 
Memfilter angka genap dari list.

*Parameter*:
- list_angka (list): List yang berisi angka (int atau float).

*Pengembalian*:
- list: List yang hanya berisi angka genap.

*Contoh*:
```python
from ListMaster import filter_genap
angka = [1, 2, 3, 4, 5, 6]
result = filter_genap(angka) 
# Output: [2, 4, 6]
```

---

#### 2. filter_lebih_dari(list_angka, nilai)

*Deskripsi*: 
Memfilter angka yang lebih besar dari nilai tertentu.

*Parameter*:
- list_angka (list): List yang berisi angka (int atau float).
- nilai (int/float): Nilai batas untuk filter.

*Pengembalian*:
- list: List yang berisi angka yang lebih besar dari nilai.

*Contoh*:
```python
from ListMaster import filter_lebih_dari
angka = [1, 2, 3, 4, 5, 6]
result = filter_lebih_dari(angka, 3)
# Output: [4, 5, 6]
```
---

#### 3. filter_habis_dibagi(list_angka, pembagi)

*Deskripsi*: 
Memfilter angka yang habis dibagi oleh pembagi tertentu.

*Parameter*:
- list_angka (list): List yang berisi angka (int atau float).
- pembagi (int/float): Angka yang digunakan sebagai pembagi.

*Pengembalian*:
- list: List yang berisi angka yang habis dibagi oleh pembagi.

*Contoh*:
```python
from ListMaster import filter_habis_dibagi
angka = [1, 2, 3, 4, 5, 6]
result = filter_habis_dibagi(angka, 2)
# Output: [2, 4, 6]
```

---

#### 4. filter_mengandung(list_string, substring)

*Deskripsi*: 
Memfilter string yang mengandung substring tertentu.

*Parameter*:
- list_string (list): List yang berisi string.
- substring (str): Substring yang dicari dalam string.

*Pengembalian*:
- list: List yang berisi string yang mengandung substring.

*Contoh*:
```python
from ListMaster import filter_mengandung
strings = ["apel", "jeruk", "anggur"]
result = filter_mengandung(strings, "an")
# Output: ["anggur"]
```

---

### Cara Menggunakan

Untuk menggunakan modul ini, Anda dapat mengimpor fungsi yang diperlukan dalam skrip Python Anda. Berikut adalah contoh penggunaan dari setiap fungsi:

python
from list_filter import filter_genap, filter_lebih_dari, filter_habis_dibagi, filter_mengandung

### Contoh penggunaan filter untuk angka
```python
from ListMaster import filter_genap, filter_lebih_dari, filter_habis_dibagi
angka = [1, 2, 3, 4, 5, 6]
print("Angka Genap:", filter_genap(angka))
print("Angka lebih dari 3:", filter_lebih_dari(angka, 3))
print("Angka yang habis dibagi 2:", filter_habis_dibagi(angka, 2))
```

### Contoh penggunaan filter untuk string
```python
from ListMaster import filter_mengandung
strings = ["apel", "jeruk", "anggur"]
print("String yang mengandung 'an':", filter_mengandung(strings, "an"))
```

## 5. Modul `list_modification`
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
```python
from ListMaster import gabungkan_list
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
```python
from ListMaster import gabungkan_tanpa_duplikat
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
```python
from ListMaster import gabungkan_list_unik
list1 = [1, 2, 3, 3]
list2 = [4, 5, 6, 4]
gabungan = gabungkan_list_unik(list1, list2)
print(gabungan)  # Output: [1, 2, 3, 4, 5, 6]
```

## 6. Modul `list_unique`
Modul ini menyediakan beberapa fungsi untuk memanipulasi list di Python, termasuk mengambil elemen unik, menghitung jumlah elemen unik, mengurutkan elemen unik, dan menemukan elemen yang duplikat.

###  Fungsi

### 1. unique_elements(input_list)
Mengembalikan list hanya dengan elemen-elemen unik (tanpa duplikat).

- *Argumen*:  
  - input_list (list): List yang berisi elemen-elemen.
  
- *Mengembalikan*:  
  - List elemen unik.
  
- *Catatan*:  
  - Jika input tidak valid (misalnya, elemen tidak bisa di-hash), akan mengembalikan list kosong dan mencetak pesan kesalahan.
    
- *Contoh Penggunaan*:
  ```python
  from ListMaster import unique_elements
  data = [1, 2, 2, 3, 4, 4, 5]
  result = unique_elements(data)
  print(result)  # Output: [1, 2, 3, 4, 5]
  ```

### 2. sum_unique(input_list)
Mengembalikan jumlah dari semua elemen unik dalam list.

- *Argumen*:  
  - input_list (list): List yang berisi elemen-elemen.
  
- *Mengembalikan*:  
  - Jumlah dari elemen-elemen unik (int/float).
  
- *Catatan*:  
  - Jika input tidak valid (misalnya, elemen tidak bisa dijumlahkan), akan mengembalikan 0 dan mencetak pesan kesalahan.

- *Contoh Penggunaan*:
  ```python
  from ListMaster import sum_unique
  data = [1, 2, 2, 3, 4, 4, 5]
  result = sum_unique(data)
  print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)
  ```

### 3. unique_and_sort(input_list)
Mengembalikan elemen unik yang sudah diurutkan secara ascending.

- *Argumen*:  
  - input_list (list): List yang berisi elemen-elemen.
  
- *Mengembalikan*:  
  - List elemen unik yang diurutkan.
  
- *Catatan*:  
  - Jika input tidak valid (misalnya, elemen tidak bisa diurutkan), akan mengembalikan list kosong dan mencetak pesan kesalahan.
    
- *Contoh Penggunaan*:
  ```python
  from ListMaster import unique_and_sort
  data = [4, 2, 5, 1, 3, 2, 5]
  result = unique_and_sort(data)
  print(result)  # Output: [1, 2, 3, 4, 5]
  ```

### 4. get_duplicates(input_list)
Mengembalikan elemen-elemen yang duplikat dalam list (tidak unik).

- *Argumen*:  
  - input_list (list): List yang berisi elemen-elemen.
  
- *Mengembalikan*:  
  - List elemen-elemen yang duplikat.
  
- *Catatan*:  
  - Jika input tidak valid (misalnya, elemen tidak bisa di-hash), akan mengembalikan list kosong dan mencetak pesan kesalahan.

- *Contoh Penggunaan*:
  ```python
  from ListMaster import get_duplicates
  data = [1, 2, 2, 3, 4, 4, 5]
  result = get_duplicates(data)
  print(result)  # Output: [2, 4]
  ```

### Penggunaan
Untuk menggunakan modul ini, cukup impor modul list_unique.py dalam skrip Python Anda dan panggil fungsi yang diperlukan.

```python
from ListMaster import unique_elements, sum_unique, unique_and_sort, get_duplicates

data = [1, 2, 2, 3, 4, 4, 5]

print("Elemen Unik:", unique_elements(data))               # Output: [1, 2, 3, 4, 5]
print("Jumlah Elemen Unik:", sum_unique(data))            # Output: 15
print("Elemen Unik Terurut:", unique_and_sort(data))      # Output: [1, 2, 3, 4, 5]
print("Elemen Duplikat:", get_duplicates(data))           # Output: [2, 4]
```

## Author
<a href="https://github.com/Dwi-Wahyu/ListMaster/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Dwi-Wahyu/ListMaster" />
</a>
