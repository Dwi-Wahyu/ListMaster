## 2.Modul filter_list

#### 1. `filter_genap(list_angka)`

**Deskripsi**: 
Memfilter angka genap dari list.

**Parameter**:
- `list_angka` (list): List yang berisi angka (int atau float).

**Pengembalian**:
- list: List yang hanya berisi angka genap.

**Contoh**:
```python
angka = [1, 2, 3, 4, 5, 6]
result = filter_genap(angka)
# Output: [2, 4, 6]
```

---

#### 2. `filter_lebih_dari(list_angka, nilai)`

**Deskripsi**: 
Memfilter angka yang lebih besar dari nilai tertentu.

**Parameter**:
- `list_angka` (list): List yang berisi angka (int atau float).
- `nilai` (int/float): Nilai batas untuk filter.

**Pengembalian**:
- list: List yang berisi angka yang lebih besar dari nilai.

**Contoh**:
```python
angka = [1, 2, 3, 4, 5, 6]
result = filter_lebih_dari(angka, 3)
# Output: [4, 5, 6]
```

---

#### 3. `filter_habis_dibagi(list_angka, pembagi)`

**Deskripsi**: 
Memfilter angka yang habis dibagi oleh pembagi tertentu.

**Parameter**:
- `list_angka` (list): List yang berisi angka (int atau float).
- `pembagi` (int/float): Angka yang digunakan sebagai pembagi.

**Pengembalian**:
- list: List yang berisi angka yang habis dibagi oleh pembagi.

**Contoh**:
```python
angka = [1, 2, 3, 4, 5, 6]
result = filter_habis_dibagi(angka, 2)
# Output: [2, 4, 6]
```

---

#### 4. `filter_mengandung(list_string, substring)`

**Deskripsi**: 
Memfilter string yang mengandung substring tertentu.

**Parameter**:
- `list_string` (list): List yang berisi string.
- `substring` (str): Substring yang dicari dalam string.

**Pengembalian**:
- list: List yang berisi string yang mengandung substring.

**Contoh**:
```python
strings = ["apel", "jeruk", "anggur"]
result = filter_mengandung(strings, "an")
# Output: ["anggur"]
```

---

### Cara Menggunakan

Untuk menggunakan modul ini, Anda dapat mengimpor fungsi yang diperlukan dalam skrip Python Anda. Berikut adalah contoh penggunaan dari setiap fungsi:

```python
from list_filter import filter_genap, filter_lebih_dari, filter_habis_dibagi, filter_mengandung

# Contoh penggunaan filter untuk angka
angka = [1, 2, 3, 4, 5, 6]
print("Angka Genap:", filter_genap(angka))
print("Angka lebih dari 3:", filter_lebih_dari(angka, 3))
print("Angka yang habis dibagi 2:", filter_habis_dibagi(angka, 2))

# Contoh penggunaan filter untuk string
strings = ["apel", "jeruk", "anggur"]
print("String yang mengandung 'an':", filter_mengandung(strings, "an"))
```
