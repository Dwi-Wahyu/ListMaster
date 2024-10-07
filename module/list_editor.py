# ModificationList.py

def add_to_list(target_list, element):
    """
    Menambahkan elemen ke dalam list.

    Args:
        target_list (list): List tempat elemen akan ditambahkan.
        element: Elemen yang akan ditambahkan ke list.
    """
    target_list.append(element)  


def remove_from_list(target_list, element):
    """
    Menghapus elemen dari list.

    Args:
        target_list (list): List tempat elemen akan dihapus.
        element: Elemen yang akan dihapus dari list.
    
    Raises:
        ValueError: Jika elemen tidak ditemukan dalam list.
    """
    try:
        target_list.remove(element) 
    except ValueError:
        raise ValueError(f"Elemen '{element}' tidak ditemukan dalam list.")


def add_to_list_if_not_exists(target_list, element):
    """
    Menambahkan elemen ke dalam list jika belum ada.

    Args:
        target_list (list): List tempat elemen akan ditambahkan.
        element: Elemen yang akan ditambahkan ke list.
    """
    if element not in target_list:
        target_list.append(element)  
    else:
        print(f"Elemen '{element}' sudah ada di dalam list.")


def remove_by_index(target_list, index):
    """
    Menghapus elemen dari list berdasarkan indeks tertentu.

    Args:
        target_list (list): List tempat elemen akan dihapus.
        index (int): Indeks dari elemen yang akan dihapus.
    
    Raises:
        IndexError: Jika indeks tidak valid.
    """
    try:
        del target_list[index] 
    except IndexError:
        raise IndexError(f"Indeks {index} tidak valid.")