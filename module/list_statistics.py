def rata_rata(target_list):
    """Menghitung rata-rata dari elemen numerik dalam list."""
    if not all(isinstance(i, (int, float)) for i in target_list):
        raise ValueError("List harus berisi angka.")
    return sum(target_list) / len(target_list) if target_list else 0

def median(target_list):
    """Menghitung median dari elemen numerik dalam list."""
    if not all(isinstance(i, (int, float)) for i in target_list):
        raise ValueError("List harus berisi angka.")
    sorted_list = sorted(target_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

def min_max(target_list):
    """Mengembalikan nilai minimum dan maksimum dari elemen numerik dalam list."""
    if not target_list:
        raise ValueError("List tidak boleh kosong.")
    if not all(isinstance(i, (int, float)) for i in target_list):
        raise ValueError("List harus berisi angka.")
    return min(target_list), max(target_list)

def modus(target_list):
    """Menghitung modus dari elemen dalam list."""
    if not target_list:
        raise ValueError("List tidak boleh kosong.")
    
    frekuensi = {}
    for elemen in target_list:
        frekuensi[elemen] = frekuensi.get(elemen, 0) + 1
        
    max_freq = max(frekuensi.values())
    modus_list = [k for k, v in frekuensi.items() if v == max_freq]
    
    return modus_list if len(modus_list) < len(frekuensi) else "Tidak ada modus (semua elemen muncul dengan frekuensi yang sama)."

