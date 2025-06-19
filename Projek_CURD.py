from tabulate import tabulate
from datetime import datetime
import re

data_warga = [
    {
        'Nama'              : 'Santoso',
        'NIK'               : '3578123456789012',
        'Tempat Lahir'      : 'Surabaya',
        'Tanggal Lahir'     : '18-07-1987',
        'No Hp'             : '+6286754535213',
        'Email'             : 'santoso@example.com',
        'Agama'             : 'Islam',
        'Status'            : 'Menikah'
    }
]

# Input
# Nama
def nama_warga():
    while True :
        inp_nama = input("Masukan Nama: ").title().strip()
        if inp_nama.replace(' ','').isalpha():
            return inp_nama
        else:
            print("Hanya boleh Huruf!")
# NIK 
def nik_warga():
    while True:
        inp_nik = (input("Masukan NIK: ")).strip()
        if inp_nik.isdigit() and len(inp_nik) == 16:
         return inp_nik
        else:
            print("Hanya boleh angka dan berjumlah 16 karakter!")

# Tempat Lahir
def Tempat_Lahir():
    while True:
        inp_tempat_lahir = input("Masukan Tempat Lahir: ").title().strip()
        if inp_tempat_lahir.replace(" ", '').isalpha():
            return inp_tempat_lahir
        else:
            print("Hanya boleh huruf!")

# Tanggal Lahir
def Tanggal_Lahir():
    while True:
        inp_tanggal_lahir = input("Masukan Tanggal Lahir'DDMMYYYY' (Contoh: 05072001): ").strip()
        if inp_tanggal_lahir.isdigit() and len(inp_tanggal_lahir) == 8:
            tanggal_format = f'{inp_tanggal_lahir[:2]}-{inp_tanggal_lahir[2:4]}-{inp_tanggal_lahir[4:]}'
            try:
                tanggal = datetime.strptime(tanggal_format, "%d-%m-%Y")
                return tanggal.strftime("%d-%m-%Y")
            except ValueError:
                print("Tanggal tidak valid! ( misal : 32132001)")
        else:
            print("Format salah! Gunakan DDMMYYYY")

# No Hp
def no_hp():
    pola = r"^(?:\+62|0)(?:\d[\s-]?){8,12}\d$"
    while True:
        inp_no_hp = input("Masukan No Hp (Contoh: 080789467892): ").strip()
        if re.fullmatch(pola, inp_no_hp):
            return inp_no_hp
        else:
            print("Nomor HP tidak valid! Gunakan format 08xxxx atau +628xxxx")

# email
def email_warga():
    pola_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        inp_email = input("Masukan email: ").strip()
        if re.fullmatch(pola_email, inp_email):
            return inp_email
        else:
            print("Format Salah! (Contoh : nama@email.com)")

# Agama
def agama_warga():
    while True: 
        inp_agama = input("Masukan Agamanya: ").title().strip()
        if inp_agama in ("Islam", "Kristen", "Katholik", "Hindu", "Buddha", "Konghucu"):
            return inp_agama
        else:
            print("Hanya boleh Islam, kristen, Katholik, Hindu, Buddha, Konghucu!")

# Status
def status_warga():
    while True: 
        inp_status = input("Masukan Status (Lajang / Nikah / Cerai): ").title().strip()
        if inp_status in ("Lajang", "Nikah", "Cerai"):
            return inp_status
        else:
            print("Hanya boleh di isi Lajang/Nikah/Cerai")



# Tambah data
def tambah_data():
    warga = {
        'Nama'              : nama_warga(),
        'NIK'               : nik_warga(),
        'Tempat Lahir'      : Tempat_Lahir(),
        'Tanggal Lahir'     : Tanggal_Lahir(),
        'No Hp'             : no_hp(),
        'Email'             : email_warga(),
        'Agama'             : agama_warga(),
        'Status'            : status_warga()
    }
    data_warga.append(warga)
    print("Data berhasil ditambahkan!!!")

# Lihat Data Warga
def lihat_data():
    if len(data_warga) == 0:
        print("Tidak Ada data")
    else:
        print("\n==Data Warga==\n")
        print(tabulate(data_warga, headers='keys', tablefmt='grid'))

# Edit data
def edit_data():
    if len(data_warga) == 0:
        print("Belum ada data warga.")
        return
    
    # data warga di tampilkan
    print("\n====Data Warga=== ")
    print(tabulate(data_warga, headers= "keys", tablefmt= "grid"))
    

    target_nik = input("Masukan NIK warga yang akan diubah datanya: ").strip()

    for warga in data_warga:
        if warga["NIK"] == target_nik:
            print(f"\nData ditemukan untuk: {warga['Nama']}")
            while True:
                print("Pilih kolom yang ingin diedit:")
                print("1. Nama")
                print("2. NIK")
                print("3. Tempat Lahir")
                print("4. Tanggal Lahir")
                print("5. No Hp")
                print("6. Email")
                print("7. Agama")
                print("8. Status")
                print("9. selesai edit!")

                pilihan = input("Data mana yang mau diubah: ")
                if pilihan == "1":
                    warga["Nama"] = nama_warga()
                elif pilihan == "2":
                    warga["NIK"] = nik_warga()
                elif pilihan == "3":
                    warga["Tempat Lahir"] = Tempat_Lahir()
                elif pilihan == "4":
                    warga["Tanggal Lahir"] = Tanggal_Lahir()
                elif pilihan == "5":
                    warga["No Hp"] = no_hp()
                elif pilihan == "6":
                    warga["Email"] = email_warga()
                elif pilihan == "7":
                    warga["Agama"] = agama_warga()
                elif pilihan == "8":
                    warga["Status"] = status_warga()
                elif pilihan == "9":
                    print("Data Selesai diedit!")
                    # Data terbaru
                    print("\n=== Data Terbaru ===")
                    print(tabulate([warga], headers="keys", tablefmt="grid"))
                    return
                else:
                    print("pilihan tidak valid pilih 1-9")
    else:
        print("Data tidak ditemukan!")

# Hapus data
def hapus_data():
    if not data_warga:
        print("Tidak ada data")
        return
    print("\n===Data Warga===\n")
    print(tabulate(data_warga, headers="keys", tablefmt="grid"))
    #target untuk yang akan di hapus datanya pakai nik
    target_hapus = input("Masukan NIK data yang akan dihapus: ").strip()

    for i,warga in enumerate(data_warga):
        if warga["NIK"] == target_hapus:
            konfirmasi = input(f'Apakah Yakin ingin Menghapus data "{warga["Nama"]}"? (ya/tidak): ').strip().lower()
            if konfirmasi == "ya":
                del data_warga[i] # menghapus data
                print("Data telah di Hapus")
            else: 
                print("Penghapusan dibatalkan")
            return
    print("NIK tidak di temukan")

#Menu Utama
def menu_utama():
    while True:
        print("\n==Menu Data Warga==\n")
        print("1. Tambah Data warga")
        print("2. Lihat Data Warga")
        print("3. Ubah Data warga")
        print("4. Hapus Data warga")
        #print("5. Simpan ke csv")
        print("6. exit")

        pilihan_menu = input("Masukan Nomor Untuk menjalankan: ") 

        if pilihan_menu == "1":
            tambah_data()
        elif pilihan_menu == "2":
            lihat_data()
        elif pilihan_menu == "3":
            edit_data()
        elif pilihan_menu == "4":
            hapus_data()
        #elif pilihan_menu == "5":
        #    save_csv()
        elif pilihan_menu == "6":
            break

menu_utama ()
        
    


            










