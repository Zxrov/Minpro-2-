print("=====================================================")
print("========= Selamat Datang Posyandu Masyarakat ========")
print("=====================================================")

Login = {
    'admin': {
        'password': 'masyarakatsehat',
        'role': 'admin'
    },
    'user': {
        'password': 'posyandumasyarakat',
        'role': 'user'
    }
}

data_anak = []          
data_lansia = []

def tambah_data_anak():
    print("-- Input Data Anak --")
    nama   = input("Masukkan Nama Anak: ")
    usia   = int(input("Masukkan Usia Anak (tahun): "))
    berat  = float(input("Masukkan Berat Badan Anak (kg): "))
    tinggi = float(input("Masukkan Tinggi Badan Anak (cm): "))
    gol_darah = input("Masukkan Golongan Darah Anak: ")
    
    anak = {
        'Nama': nama,
        'Usia': usia,
        'Berat Badan': berat,
        'Tinggi Badan': tinggi,
        'Golongan Darah': gol_darah  
    }
    
    data_anak.append(anak)
    print("Data Anak berhasil ditambahkan")
    print(f"{nama} telah mendapatkan asupan gizi berupa biskuit sehat dan susu.")

def tambah_data_lansia():
    print("-- Input Data Lansia --")
    nama   = input("Masukkan Nama Anak: ")
    usia   = int(input("Masukkan Usia Lansia (tahun): "))
    berat  = float(input("Masukkan Berat Badan Lansia (kg): "))
    tinggi = float(input("Masukkan Tinggi Badan Lansia (cm): "))
    gol_darah = input("Masukkan Golongan Darah Lansia: ")
    
    anak = {
        'Nama': nama,
        'Usia': usia,
        'Berat Badan': berat,
        'Tinggi Badan': tinggi,
        'Golongan Darah': gol_darah
    }
    
    data_lansia.append(anak)
    print("Data Lansia berhasil ditambahkan!")
    print(f"{nama} telah mendapatkan asupan gizi berupa susu kalsium dan biskuit sehat.")


from prettytable import PrettyTable
def tampilkan_data_anak():
    if not data_anak:
        print("Belum ada data anak yang dimasukkan.")
    else:
        table = PrettyTable()
        
        table.field_names = ["No", "Nama", "Usia (tahun)", "Berat Badan (kg)", "Tinggi Badan (cm)", "Golongan Darah"]
        
        for i, anak in enumerate(data_anak, 1):
            table.add_row([i, anak["Nama"], anak["Usia"], anak["Berat Badan"], anak["Tinggi Badan"], anak["Golongan Darah"]])

        print(table)

tampilkan_data_anak()

from prettytable import PrettyTable

def tampilkan_data_lansia():
    if not data_lansia:
        print("Belum ada data lansia yang dimasukkan.")
    else:
        table = PrettyTable()
        
        table.field_names = ["No", "Nama", "Usia (tahun)", "Berat Badan (kg)", "Tinggi Badan (cm)", "Golongan Darah"]

        for i, lansia in enumerate(data_lansia, 1):
            table.add_row([i, lansia["Nama"], lansia["Usia"], lansia["Berat Badan"], lansia["Tinggi Badan"], lansia["Golongan Darah"]])

        print(table)

tampilkan_data_lansia()

def menu():
    while True:
        print("=== Posyandu Masyarakat ===")
        print("1. Tambah Data Anak")
        print("2. Tambah Data Lansia")
        print("3. Tampilkan Data Anak")
        print("4. Tampilkan Data Lansia")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_data_anak()
        elif pilihan == '2':
            tambah_data_lansia()
        elif pilihan == '3':
            tampilkan_data_anak()
        elif pilihan == '4':
            tampilkan_data_lansia()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi Posyandu Masyarakat!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

def edit_data_anak():
    tampilkan_data_anak()
    if data_anak:
        index = int(input("Masukkan nomor data yang ingin diedit: ")) - 1
        if 0 <= index < len(data_anak):
            print("-- Edit Data Anak --")
            nama = input("Masukkan Nama Anak: ")
            usia = int(input("Masukkan Usia Anak (tahun): "))
            berat = float(input("Masukkan Berat Badan Anak (kg): "))
            tinggi = float(input("Masukkan Tinggi Badan Anak (cm): "))
            gol_darah = input("Masukkan Golongan Darah Anak: ")
            
            # Update data anak
            data_anak[index] = {
                'Nama': nama,
                'Usia': usia,
                'Berat Badan': berat,
                'Tinggi Badan': tinggi,
                'Golongan Darah': gol_darah
            }
            print("Data Anak berhasil diedit!")
        else:
            print("Nomor tidak valid.")
    

def edit_data_lansia():
    tampilkan_data_lansia()
    if data_lansia:
        index = int(input("Masukkan nomor data yang ingin diedit: ")) - 1
        if 0 <= index < len(data_lansia):
            print("-- Edit Data Lansia --")
            nama = input("Masukkan Nama Lansia: ")
            usia = int(input("Masukkan Usia Lansia (tahun): "))
            berat = float(input("Masukkan Berat Badan Lansia (kg): "))
            tinggi = float(input("Masukkan Tinggi Badan Lansia (cm): "))
            gol_darah = input("Masukkan Golongan Darah Lansia: ")
            
            # Update data lansia
            data_lansia[index] = {
                'Nama': nama,
                'Usia': usia,
                'Berat Badan': berat,
                'Tinggi Badan': tinggi,
                'Golongan Darah': gol_darah
            }
            print("Data Lansia berhasil diedit!")
        else:
            print("Nomor tidak valid.")

def hapus_data_anak():
    tampilkan_data_anak()
    if data_anak:
        index = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
        if 0 <= index < len(data_anak):
            del data_anak[index]
            print("Data Anak berhasil dihapus!")
        else:
            print("Nomor tidak valid.")

def hapus_data_lansia():
    tampilkan_data_lansia()
    if data_lansia:
        index = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
        if 0 <= index < len(data_lansia):
            del data_lansia[index]
            print("Data Lansia berhasil dihapus!")
        else:
            print("Nomor tidak valid.")


def login():
    print("=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in Login and Login[username]['password'] == password:
        print(f"Login berhasil sebagai {Login[username]['role']}.")
        return Login[username]['role']
    else:
        print("Login gagal. Username atau password salah.")
        return None

def logout():
    print("Logout berhasil.")
    return None

def menu_admin():
    while True:
        print("=== Menu Admin ===")
        print("1. Tampilkan Data Anak")
        print("2. Tampilkan Data Lansia")
        print("3. Edit Data Anak")
        print("4. Edit Data Lansia")
        print("5. Hapus Data Anak")
        print("6. Hapus Data Lansia")
        print("7. Logout")
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == '1':
            tampilkan_data_anak()
        elif pilihan == '2':
            tampilkan_data_lansia()
        elif pilihan == '3':
            edit_data_anak()
        elif pilihan == '4':
            edit_data_lansia()
        elif pilihan == '5':
            hapus_data_anak()
        elif pilihan == '6':
            hapus_data_lansia()
        elif pilihan == '7':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

def menu_user():
    while True:
        print("=== Menu User ===")
        print("1. Tambah Data Anak")
        print("2. Tambah Data Lansia")
        print("3. Tampilkan Data Anak")
        print("4. Tampilkan Data Lansia")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_data_anak()
        elif pilihan == '2':
            tambah_data_lansia()
        elif pilihan == '3':
            tampilkan_data_anak()
        elif pilihan == '4':
            tampilkan_data_lansia()
        elif pilihan == '5':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


def main():
    while True:
        role = login()
        if role == 'admin':
            menu_admin()
        elif role == 'user':
            menu_user()
        else:
            print("Silakan coba lagi.")

main()
