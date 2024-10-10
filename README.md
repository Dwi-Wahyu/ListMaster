# ListMaster

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

