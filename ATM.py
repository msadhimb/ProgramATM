from getpass import getpass
temp = [0]
adhim = [0]
ilham = [0]
daffa = [0]
akbar = [0]
paksyaifur = [0]
akses = {'Muhamad Salman Adhim Baqy' : adhim, 
    'Ilham Maulana Putra' : ilham, 
    'Daffa Radhitya Pratama Wina Putra' : daffa, 
    'Akbar Priyo Santosa' : akbar, 
    'Muhammad Syaifur Rohman' : paksyaifur
}
print("\n")
print("\t Selamat Datang \n")
print("Karena tidak ada kartu yang bisa dibaca maka")
print("Masukkan nama lengkap anda \n" )
nama = input("Masukkan nama lengkap anda (ex. Salman Adhim) = ")

def password():
    if nama in akses:
        ATM(getpass("Masukkan 6 digit pin anda : "))
        ATM.program()
        ATM.option()
    else:
        print("Nama anda belum terdaftar didatabase kami.")
        print("\n")


class ATM():

    def __init__(self, pin):
        self.pin = pin

    def program():
        print("\n")
        print("Selamat Datang")
        print("Selamat bertransaksi")
        print("1. 100.000 ")
        print("2. 200.000")
        print("3. 300.000")
        print("4. 500.000")
        print("5. Ambil Uang anda")
        print("6. Transfer")
        print("7. Cek Saldo")
        print("8. Setor Tunai")
        print("9. Keluar")
        
    def option():   
        input1 = int(input("Masukkan pilihan anda (Hanya nomernya) : "))
        if input1 == 1:
            for x in temp:
                if x > 100000:
                    x -= 100000
                    temp.append(x)
                    del(temp[0])
                    akses[nama].append(x)
                    z = akses.get(nama)
                    del(z[0])
                    print("\n")
                    print(f"\tSisa saldo anda adalah {x} \n")
                else:
                    print("\n")
                    print("\tSaldo anda tidak mencukupi.")
                    print("===========================")
                    print("\tSilahkan melakukan setor tunai.")
                    print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba. \n")
            ATM.lanjutan()
        if input1 == 2:
            for x in temp:
                if x > 200000:
                    x -= 200000
                    temp.append(x)
                    del(temp[0])
                    akses[nama].append(x)
                    z = akses.get(nama)
                    del(z[0])
                    print("\n")
                    print(f"\tSisa saldo anda adalah {x} \n")
                else:
                    print("\n")
                    print("\tSaldo anda tidak mencukupi.")
                    print("===========================")
                    print("\tSilahkan melakukan setor tunai.")
                    print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba. \n")
            ATM.lanjutan()
        if input1 == 3:
            for x in temp:
                if x > 300000:
                    x -= 300000
                    temp.append(x)
                    del(temp[0])
                    akses[nama].append(x)
                    z = akses.get(nama)
                    del(z[0])
                    print("\n")
                    print(f"\tSisa saldo anda adalah {x} \n")
                else:
                    print("\n")
                    print("\tSaldo anda tidak mencukupi.")
                    print("===========================")
                    print("\tSilahkan melakukan setor tunai.")
                    print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba. \n")
            ATM.lanjutan()
        if input1 == 4:
            for x in temp:
                if x > 500000:
                    x -= 500000
                    temp.append(x)
                    del(temp[0])
                    akses[nama].append(x)
                    z = akses.get(nama)
                    del(z[0])
                    print("\n")
                    print(f"\tSisa saldo anda adalah {x} \n")
                else:
                    print("\n")
                    print("\tSaldo anda tidak mencukupi.")
                    print("===========================")
                    print("\tSilahkan melakukan setor tunai.")
                    print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba. \n")
            ATM.lanjutan()

        if input1 == 5:
            print('\n')
            input4 = int(input('Tulis jumlah uang yang ingin anda ambil : '))
            for x in temp:
                if x > input4:
                    x -= input4
                    temp.append(x)
                    del(temp[0])
                    akses[nama].append(x)
                    z = akses.get(nama)
                    del(z[0])
                    print(f"\tSisa saldo anda adalah {x} \n")
                else:
                    print("\n")
                    print("\tSaldo anda tidak mencukupi.")
                    print("===========================")
                    print("\tSilahkan melakukan setor tunai.")
                    print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba. \n")
            ATM.lanjutan()

        if input1 == 6:
            print("\n")
            input2 = input("Masukkan nama pengguna yang ingin anda transfer : ")
            if input2 in akses:
                input3 = int(input("Masukkan jumlah yang ingin anda transfer : "))
                for x in akses[nama]:
                    if x > input3:
                        x -= input3
                        temp.append(x)
                        del(temp[0])
                        akses[nama].append(x)
                        z = akses.get(nama)
                        del(z[0])
                        print("\n")
                        print("\tSisa saldo anda adalah : ", x)
                    else:
                        print("\n")
                        print("\tSaldo anda tidak mencukupi.")
                        print("===========================")
                        print("\tSilahkan melakukan setor tunai.")
                        print("\tATM kami mengharuskan untuk saldo atm minimal 50.000 untuk riba. \n")
            else:
                print("\n")
                print("\tNama pengguna tidak terdaftar di database kami.")
            ATM.lanjutan()
        if input1 == 7:
            for i in temp:
                akses[nama].append(i)
                z = akses.get(nama)
                del(z[0])
                for x in akses[nama]:
                    print("\n")
                    print(f"\tSaldo anda saat ini adalah {x} \n")
            ATM.lanjutan()

        if input1 == 8:
            ATM.setor()
                    
        if input1 == 9:
            ATM.lanjutan()

    def setor():
        print('\n')
        input4 = int(input("Masukkan jumlah yang ingin anda setorkan : "))
        temp.append(input4)
        del(temp[0])
        for i in temp:
            akses[nama].append(i)
            z = akses.get(nama)
            del(z[0])
            print("Jumlah saldo anda saat ini adalah ", i)
        ATM.lanjutan()

    def lanjutan():
        print("\nAnda sudah selesai bertransaksi ?")
        print("1. Ya")
        print("2. Tidak")
        input5 = int(input())
        if input5 == 2:
            while nama in akses:
                ATM.program()
                ATM.option()
                break
        elif input5 == 1:
            print('\n')
            print("\tSelamat Tinggal")
            print('\n')
        else:
            print("\n")
            print("\tInput yang anda masukkan salah. Selamat Tinggal")
            print('\n')


password()
