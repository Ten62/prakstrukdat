#include <iostream>
#include <string>

using namespace std;

// Struct untuk menyimpan data panitia
struct Panitia {
    string nama;
    string jabatan;
    string divisi; 
};

// Fungsi untuk menambahkan panitia 
int tambahPanitia(Panitia *panitia, int jumlah) {
    cout << "Masukkan nama panitia: ";
    cin.ignore(); // Membersihkan buffer input
    getline(cin, panitia[jumlah].nama);

    cout << "Masukkan jabatan panitia: ";
    getline(cin, panitia[jumlah].jabatan);
    
    cout << "Masukkan divisi panitia: ";
    getline(cin, panitia[jumlah].divisi);

    jumlah++;
    cout << "Panitia berhasil ditambahkan!\n\n";

    return jumlah; 
}

// Prosedur untuk menampilkan daftar panitia
void tampilkanPanitia(Panitia *panitia, int jumlah) {
    if (jumlah == 0) {
        cout << "Belum ada panitia yang terdaftar.\n";
        return;
    }

    cout << "Daftar Panitia:\n";
    for (int i = 0; i < jumlah; i++) {
        cout << i + 1 << ". Nama: " << panitia[i].nama 
             << ", Jabatan: " << panitia[i].jabatan 
             << ", Divisi: " << panitia[i].divisi << endl;
    }
    cout << endl;
}

// Prosedur untuk mengedit panitia berdasarkan index
void editPanitia(Panitia *panitia, int jumlah) {
    if (jumlah == 0) {
        cout << "Belum ada panitia yang terdaftar.\n";
        return;
    }

    int index;
    tampilkanPanitia(panitia, jumlah);
    cout << "Pilih nomor panitia yang ingin diedit: ";
    cin >> index;
    index--; 

    if (index >= 0 && index < jumlah) {
        cout << "Masukkan nama panitia baru: ";
        cin.ignore();
        getline(cin, panitia[index].nama);

        cout << "Masukkan jabatan panitia baru: ";
        getline(cin, panitia[index].jabatan);

        cout << "Masukkan divisi panitia baru: ";
        getline(cin, panitia[index].divisi);

        cout << "Panitia berhasil diubah!\n\n";
    } else {
        cout << "Indeks tidak valid!\n\n";
    }
}

// Fungsi untuk menghapus panitia berdasarkan index
int hapusPanitia(Panitia *panitia, int jumlah) {
    if (jumlah == 0) {
        cout << "Belum ada panitia yang terdaftar.\n";
        return jumlah;
    }

    int index;
    tampilkanPanitia(panitia, jumlah);
    cout << "Pilih nomor panitia yang ingin dihapus: ";
    cin >> index;
    index--; 

    if (index >= 0 && index < jumlah) {
        // Menggeser elemen array setelah elemen yang dihapus
        for (int i = index; i < jumlah - 1; i++) {
            panitia[i] = panitia[i + 1];
        }
        jumlah--; 

        cout << "Panitia berhasil dihapus!\n\n";
    } else {
        cout << "Indeks tidak valid!\n\n";
    }

    return jumlah; 
}

int main() {
    const int MAX_PANITIA = 100;
    Panitia panitia[MAX_PANITIA];
    int jumlahPanitia = 0;
    int pilihan;

    do {
        cout << "Menu CRUD Panitia:\n";
        cout << "1. Tambah Panitia\n";
        cout << "2. Tampilkan Panitia\n";
        cout << "3. Edit Panitia\n";
        cout << "4. Hapus Panitia\n";
        cout << "5. Keluar\n";
        cout << "Pilihan: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                jumlahPanitia = tambahPanitia(panitia, jumlahPanitia); 
                break;
            case 2:
                tampilkanPanitia(panitia, jumlahPanitia);
                break;
            case 3:
                editPanitia(panitia, jumlahPanitia);
                break;
            case 4:
                jumlahPanitia = hapusPanitia(panitia, jumlahPanitia); 
                break;
            case 5:
                cout << "Terima kasih!\n";
                break;
            default:
                cout << "Pilihan tidak valid!\n\n";
        }
    } while (pilihan != 5);

    return 0;
}
