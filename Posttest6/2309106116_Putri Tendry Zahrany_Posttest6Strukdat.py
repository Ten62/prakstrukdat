def fibonacci_search(daftar, target_umur):
    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1 

    temp = daftar.head
    n = 0
    while temp:
        n += 1
        temp = temp.next

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1
    temp = daftar.head
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        current = get_node_at_index(daftar, i)

        if current.umur < target_umur:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif current.umur > target_umur:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i 
    return -1 

def get_node_at_index(daftar, index):
    current = daftar.head
    for i in range(index):
        if current is None:
            return None
        current = current.next
    return current

import math

def jump_search(daftar, target_umur):
    n = get_list_size(daftar)
    step = math.sqrt(n)
    prev = 0
    current = daftar.head

    while current and current.umur < target_umur:
        prev = int(min(prev + step, n))
        current = get_node_at_index(daftar, prev)
        if current is None:
            return -1

    
    for i in range(int(prev - step), prev):
        current = get_node_at_index(daftar, i)
        if current.umur == target_umur:
            return i
    return -1

def get_list_size(daftar):
    temp = daftar.head
    count = 0
    while temp:
        count += 1
        temp = temp.next
    return count

def boyer_moore_search(haystack, needle):
    m = len(needle)
    n = len(haystack)
    if m == 0:
        return 0

   
    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(needle[i])] = i

    s = 0  
    while s <= n - m:
        j = m - 1
        while j >= 0 and needle[j] == haystack[s + j]:
            j -= 1
        if j < 0:
            return s 
        else:
            s += max(1, j - bad_char[ord(haystack[s + j])])
    return -1

def cari_nama_boyer_moore(daftar, target_nama):
    temp = daftar.head
    index = 0
    while temp:
        if boyer_moore_search(temp.nama, target_nama) != -1:
            return index
        temp = temp.next
        index += 1
    return -1

target_umur = 21
index = fibonacci_search(daftar_panitia, target_umur)
if index != -1:
    print(f"Panitia dengan umur {target_umur} ditemukan di indeks {index}")
else:
    print(f"Panitia dengan umur {target_umur} tidak ditemukan")

target_umur = 22
index = jump_search(daftar_panitia, target_umur)
if index != -1:
    print(f"Panitia dengan umur {target_umur} ditemukan di indeks {index}")
else:
    print(f"Panitia dengan umur {target_umur} tidak ditemukan")

target_nama = "Putri"
index = cari_nama_boyer_moore(daftar_panitia, target_nama)
if index != -1:
    print(f"Panitia dengan nama {target_nama} ditemukan di indeks {index}")
else:
    print(f"Panitia dengan nama {target_nama} tidak ditemukan")
