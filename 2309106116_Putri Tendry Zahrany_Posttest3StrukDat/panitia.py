
class Panitia:
    def __init__(self, nama, jabatan, umur):
        self.nama = nama         # Nama panitia
        self.jabatan = jabatan   # Jabatan panitia
        self.umur = umur         # Umur panitia
        self.next = None         # Pointer ke anggota panitia berikutnya


class DaftarKepanitiaan:
    def __init__(self):
        self.head = None  # Inisialisasi head sebagai None
    
    # Fungsi untuk menambahkan anggota baru di akhir linked list
    def tambah_panitia(self, nama, jabatan, umur):
        anggota_baru = Panitia(nama, jabatan, umur)
        if self.head is None:
            self.head = anggota_baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = anggota_baru
    
    # Fungsi untuk menampilkan semua anggota dalam linked list
    def tampilkan_daftar(self):
        if self.head is None:
            print("Daftar kepanitiaan kosong.")
        else:
            temp = self.head
            while temp:
                print(f"Nama: {temp.nama}, Jabatan: {temp.jabatan}, Umur: {temp.umur}")
                temp = temp.next
    
    # Fungsi untuk menghapus panitia berdasarkan nama
    def hapus_panitia(self, nama):
        if self.head is None:
            print("Daftar kosong, tidak bisa menghapus.")
            return
        if self.head.nama == nama:
            self.head = self.head.next
            print(f"{nama} telah dihapus dari daftar.")
            return
        
        temp = self.head
        while temp.next and temp.next.nama != nama:
            temp = temp.next
        
        if temp.next is None:
            print(f"{nama} tidak ditemukan dalam daftar.")
        else:
            temp.next = temp.next.next
            print(f"{nama} telah dihapus dari daftar.")

# Main program
daftar_panitia = DaftarKepanitiaan()

# Menambahkan data panitia
daftar_panitia.tambah_panitia("Putri", "Ketua", 21)
daftar_panitia.tambah_panitia("Tendry", "Wakil Ketua", 20)
daftar_panitia.tambah_panitia("Zahrany", "Sekretaris", 22)

# Menampilkan daftar panitia
print("Daftar Kepanitiaan:")
daftar_panitia.tampilkan_daftar()

# Menghapus panitia
daftar_panitia.hapus_panitia("Tendry")

# Menampilkan daftar panitia setelah penghapusan
print("\nDaftar Kepanitiaan setelah penghapusan:")
daftar_panitia.tampilkan_daftar()
