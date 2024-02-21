# Capstone Project 1

Case Study: Data Nilai Siswa

## Fitur 1 (Lihat Data)
Fungsi data_siswa(), ketika dijalankan akan menampilkan sub menu pada data_siswa() dan meminta user untuk menginput angka
Ketika sub menu 1 dijalankan, maka akan menampilkan seluruh data siswa dari variabel siswa
Ketika sub menu 2 dijalankan, maka akan mengembalikan user ke menu utama

## Fitur 2 (Pencarian Data Siswa)
Fungsi cari_siswa(), ketika dijalankan akan menampilkan sub menu pada cari_siswa() dan meminta user untuk menginput angka
Ketika sub menu 1 dijalankan, maka akan meminta user untuk menginput nama siswa
Jika nama siswa ditemukan, maka akan menampilkan data siswa tersebut
Jika nama siswa tidak ditemukan, maka akan menampilkan informasi bahwa data tidak ada, dan kembali ke sub menu
Ketika sub menu 2 dijalankan, maka akan mengembalikan user ke menu utama

## Fitur 3 (Tambah Data Siswa)
Fungsi tambah_data(), ketika dijalankan akan menampilkan sub menu pada tambah_data() dan meminta user untuk menginput angka
Ketika sub menu 1 dijalankan, maka akan meminta user untuk menginput nama, kelas, dan nilai siswa
Jika data siswa ditemukan, maka akan menampilkan informasi bahwa data siswa sudah ada
Jika data siswa tidak ditemukan, maka akan menampilkan konfirmasi untuk menambah data siswa tersebut ke variabel siswa
Kemudian akan ada konfirmasi untuk menyimpan data dan setelah itu kembali ke sub menu
Ketika sub menu 2 dijalankan, maka akan mengembalikan user ke menu utama

## Fitur 4: (Ubah Data Siswa)
Fungsi ubah_data(), ketika dijalankan akan menampilkan sub menu pada ubah_siswa() dan meminta user untuk menginput angka
Ketika sub menu 1 dijalankan, maka akan meminta user untuk menginput nama siswa
Jika data siswa ditemukan, maka akan menampilkan informasi bahwa data siswa ada dan meminta konfirmasi untuk mengubah data
Jika menjawab ya, akan meminta user untuk menginput data-data yang akan diubah (nama, kelas, dan nilai)
Kemudian akan meminta konfirmasi lagi untuk menyimpan data, jika 'ya' data akan tersimpan, jika 'tidak' maka data tidak tersimpan
Jika data siswa tidak ditemukan, maka akan menampilkan informasi bahwa data tidak ada, dan kembali ke sub menu
Ketika sub menu 2 dijalankan, maka akan mengembalikan user ke menu utama

## Fitur 5 (Hapus Data Siswa)
Fungsi hapus_data() ketika dijalankan akan menampilkan sub menu pada hapus_data() dan meminta user untuk menginput angka
Ketika sub menu 1 dijalankan, maka akan meminta meminta user untuk memasukkan nama siswa yang ingin dihapus datanya
Jika data siswa ditemukan, akan ada konfirmasi untuk menghapus data siswa tersebut
Jika memilih 'ya' akan ada informasi bahwa data telah dihapus dan kembali ke sub menu
Jika 'tidak' akan ada informasi bahwa data tidak dihapus dan kembali ke sub menu
Ketika sub menu 2 dijalankan, maka akan mengembalikan user ke menu utama

## Fitur 6 (Menu Utama)
Fungsi menu_utama() adalah untuk menjalankan program dan menampilkan menu utama
Kemudian akan meminta user untuk menginput angka
Memanggil fungsi yang sesuai berdasarkan input angka dari user
Program akan keluar jika user menginput angka 6

## Fitur Tambahan (Mengubah Warna Teks)
Fungsi print_warna() ketika dijalankan akan mengubah warna teks sesuai kode warna yang kita inginkan
Informasi dari gist github
