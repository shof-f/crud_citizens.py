# CURD_citizens
🏡 Aplikasi Data Warga (CRUD)
📋 Deskripsi
Ini adalah aplikasi Python berbasis terminal yang digunakan untuk mengelola data warga, seperti nama, NIK, tempat lahir, tanggal lahir, no HP, email, agama, dan status pernikahan.
Aplikasi ini memungkinkan kamu untuk:
    Menambahkan data warga (Create),
    Melihat semua data warga (Read),
    Mengedit data warga tertentu (Update),
    Menghapus data warga tertentu (Delete),
    Semua data disimpan dalam bentuk list of dictionary (array of object) selama program berjalan.

🧠 Fitur Utama
1. Tambah Data Warga
  Pengguna diminta mengisi semua kolom (dengan validasi input):
    Nama: hanya huruf, 
    NIK: harus 16 digit angka, 
    Tempat Lahir: hanya huruf, 
    Tanggal Lahir: format DDMMYYYY, divalidasi tanggal valid, 
    No HP: format 08xxxxxx atau +628xxxxx, 
    Email: validasi email umum, 
    Agama: hanya pilihan umum (Islam, Kristen, dll.), 
    Status: hanya "Lajang", "Nikah", "Cerai".

2. Lihat Data Warga:
    Menampilkan semua data dalam bentuk tabel menggunakan tabulate.

3. Edit Data Warga:
    Cari warga berdasarkan NIK, 
    Edit kolom tertentu berdasarkan menu 1–8, 
    Data diperbarui secara langsung di memori.

4. Hapus Data Warga:
    Cari berdasarkan NIK,
    Konfirmasi sebelum menghapus,
    Data dihapus dari list.

5. Menu Utama:
    Looping terus sampai user memilih keluar (exit),
    Navigasi menggunakan input angka.
