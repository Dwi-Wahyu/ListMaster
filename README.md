# ListMaster

### Apa fungsi library ini ?

ListMaster adalah library yang memungkinkan anda untuk menyortir, memodifikasi, menggabungkan dan masih banyak lagi

## 1. Modul list_sorting
Modul ini berisi berbagai algoritma pengurutan  yang dapat digunakan untuk mengurutkan data dalam bentuk array atau list. Algoritma yang disertakan antara lain: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, serta Tim Sort yang merupakan sorting bawaan Python. Setiap algoritma mendukung pengurutan secara ascending (menaik) maupun descending (menurun).

### Daftar Algoritma
+ Bubble Sort: Mengurutkan dengan membandingkan elemen bersebelahan dan menukarnya jika diperlukan. Proses diulangi sampai semua elemen terurut.

+ Selection Sort: Menemukan elemen terkecil atau terbesar di bagian tidak terurut dan menukarnya dengan elemen di posisi yang sesuai.

+ Insertion Sort: Mengurutkan dengan cara memasukkan elemen dari bagian tidak terurut ke bagian yang sudah terurut pada posisi yang tepat.

+ Merge Sort: Menggunakan pendekatan divide and conquer untuk membagi array, mengurutkan setiap bagian secara rekursif, lalu menggabungkannya kembali.

+ Quick Sort: Menggunakan pivot untuk mempartisi array menjadi dua bagian, dan mengurutkan secara rekursif pada kedua bagian.

+ Tim Sort: Sorting bawaan Python yang merupakan kombinasi dari Merge Sort dan Insertion Sort, dioptimalkan untuk performa.

### Penggunaan 
Setiap fungsi pengurutan menerima dua parameter:

1. arr: List yang akan diurutkan.

2. reverse (opsional): Boolean yang menentukan urutan hasil pengurutan. Jika True, list akan diurutkan secara menurun (descending). Jika False, list akan diurutkan secara menaik (ascending). Nilai default adalah False.

Contoh : 
```
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