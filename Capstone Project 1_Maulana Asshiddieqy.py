# Tampilan Menu
menu = '''
1. Data Nilai Siswa
2. Cari Data Siswa
3. Tambah Data Siswa
4. Ubah Data Siswa
5. Hapus Data Siswa
6. Keluar'''

# Data Siswa
siswa = [
    {
        'Nama' : 'Andi',
        'Kelas' : '1A',
        'Nilai' : '95'
    },
    {
        'Nama' : 'Budi',
        'Kelas' : '1B',
        'Nilai' : '80'
    },
    {
        'Nama' : 'Citra',
        'Kelas' : '1C',
        'Nilai' : '90'
    }]

# Fitur untuk Memberikan Warna pada Teks
def print_warna(variabel, kode_warna):
    print(f"\033[{kode_warna}m{variabel}\033[0m")

# Fitur Lihat Data
def data_siswa():
    while True:
        print("\nData Nilai Siswa SD Budi Pekerti")
        print("1. Tampilkan Data Nilai Siswa")
        print("2. Kembali ke Menu Utama")
        input1 = input("\nSilahkan masukkan angka: ")
        if input1 == '1':
            print(("-"*5),"Daftar Siswa",("-"*5))
            print("|Nama\t| Kelas\t| Nilai\t|")
            for i in siswa:
                print(f"|{i['Nama']}\t| {i['Kelas']}\t| {i['Nilai']}\t|")
        elif input1 == '2':
            menu_utama()
        else:
            print_warna("Invalid! Silahkan Coba Lagi1", "1;31")

# Fitur Pencarian Data
def cari_siswa():
    while True:
        print("\nPencarian Data Siswa")
        print("1. Pencarian Siswa")
        print("2. Kembali ke Menu Utama")
        input2 = input("\nSilahkan masukkan angka: ")
        if input2 == '1':
            cari = input("Masukkan nama siswa yang ingin dicari: ")
            for i in siswa:
                if i["Nama"].lower() == cari.lower():
                    print("\nHasil Pencarian:")
                    print("|Nama\t| Kelas\t| Nilai\t|")
                    print(f"|{i['Nama']}\t| {i['Kelas']}\t| {i['Nilai']}\t|")
                    break
                else:
                    print_warna("Data Siswa Tidak Ditemukan", "1;31")
                    break
        elif input2 == '2':
            menu_utama()
        else:
            print_warna("Invalid! Silahkan Coba Lagi1", "1;31")

# Fitur Tambah Data
def tambah_data():
    while True:
        print("\nTambah Data Siswa")
        print("1. Tambah Data")
        print("2. Kembali ke Menu Utama")
        input3 = input("\nSilahkan masukkan angka: ")
        if input3 == '1':
            nama = input("\nMasukkan Nama Siswa: ")
            kelas = input("Masukkan Kelas: ")
            nilai = input("Masukkan Nilai Siswa: ")
            for i in siswa:
                if i['Nama'] == nama.capitalize():
                    print("Data Siswa Sudah Ada")
                    break
                else:
                    simpan = input("\nApakah ingin menyimpan data? (y/n): ")
                    if simpan.lower() == 'y':
                        data_baru = {'Nama' : nama.capitalize(), 'Kelas' : kelas.upper(), 'Nilai' : nilai}
                        siswa.append(data_baru)
                        print_warna("Data Siswa Telah Tersimpan", "1;32")
                        break
                    else:
                        print_warna("Data Tidak Tersimpan", "1;33")
                        break
        elif input3 == '2':
            menu_utama()
        else:
            print_warna("Invalid! Silahkan Coba Lagi1", "1;31")

# Fitur Ubah Data
def ubah_data():
    while True:
        print("\nUbah Data Siswa")
        print("1. Ubah Data")
        print("2. Kembali ke Menu Utama")
        input4 = input("\nSilahkan masukkan angka: ")
        if input4 == '1':
            ubah = input("\nMasukkan nama siswa: ")
            for i in siswa:
                if i["Nama"].lower() == ubah.lower():
                    print("Data Ditemukan")
                    print("|Nama\t| Kelas\t| Nilai\t|")
                    print(f"|{i['Nama']}\t| {i['Kelas']}\t| {i['Nilai']}\t|")
                    while True:
                        tanya = input("\nApakah ingin mengubah data? (y/n): ")
                        if tanya.lower() == 'y':
                            nama_baru = input("Masukkan nama: ")
                            kelas_baru = input("Masukkan kelas: ")
                            nilai_baru = input("Masukkan nilai: ")
                            simpan_baru = input("\nApakah ingin menyimpan data? (y/n): ")
                            if simpan_baru.lower() == 'y':
                                if nama_baru:
                                    i["Nama"] = nama_baru
                                if kelas_baru:
                                    i["Kelas"] = kelas_baru
                                if nilai_baru:
                                    i["Nilai"] = nilai_baru
                                print_warna("Data berhasil disimpan", "1;32")
                                break
                            else:
                                print_warna("Data tidak berhasil disimpan", "1;33")
                                break
                        else:
                            print_warna("Data tidak berhasil diubah", "1;33")
                            break
                    break
                else:
                    print_warna("Data Siswa Tidak Ditemukan", "1;31")
                    break
        elif input4 == '2':
            menu_utama()
        else:
            print_warna("Invalid! Silahkan Coba Lagi1", "1;31")

# Fitur Hapus Data
def hapus_data():
    while True:
        print("\nHapus Data Siswa")
        print("1. Hapus Data")
        print("2. Kembali ke Menu Utama")
        input5 = input("\nSilahkan masukkan angka: ")
        if input5 == '1':
            hapus_siswa = input("\nMasukkan nama siswa yang ingin dihapus: ")
            for index, nama in enumerate(siswa):
                if nama["Nama"].lower() == hapus_siswa:
                    hapus = input("\Apakah ingin menghapus data siswa tersebut? (y/n): ")
                    if hapus.lower() == 'y':
                        del siswa[index]
                        print_warna("Data Siswa Telah Dihapus", "1;32")
                        break
                    else:
                        print_warna("Data Tidak Berhasil Dihapus", "1;33")
                else:
                    print_warna("Data Tidak Ditemukan", "1;31")
                    break
        elif input5 == '2':
            menu_utama()
        else:
            print_warna("Invalid! Silahkan Coba Lagi1", "1;31")

# Fitur Menu Utama
def menu_utama():
    while True:
        print("\nSelamat Datang di Database SD Budi Pekerti")
        print(menu)
        input = input("\nSilakan masukkan angka: ")
        if input == '1':
            data_siswa()
        elif input == '2':
            cari_siswa()
        elif input == '3':
            tambah_data()
        elif input == '4':
            ubah_data()
        elif input == '5':
            hapus_data()
        elif input == '6':
            print_warna("Terima Kasih Telah Mengakses Database Kami :)", "1")
            quit()
        else:
            print_warna("Invalid! Silahkan Coba Lagi", "1;31")


# Menjalankan Aplikasi
menu_utama()
