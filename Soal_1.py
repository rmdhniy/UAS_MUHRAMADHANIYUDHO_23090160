def main():
    mahasiswa = []
    
    while True:
        nim = input("Masukan NIM: ")
        nama = input("Masukan Nama: ")
        mahasiswa.append({"NIM": nim, "Nama": nama})
        tambah_lagi = input("Ingin tambah lagi? (YA/TIDAK): ").strip().lower()
        
        if tambah_lagi != 'ya':
            break
    
    print("\nData Mahasiswa:")
    for mhs in mahasiswa:
        print(f"NIM: {mhs['NIM']}, Nama: {mhs['Nama']}")
    
    print("End")

if __name__ == "__main__":
    main()


