class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Antrian kosong"

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    while True:
        print("\nMenu:")
        print("1. Tambah pesanan ke antrian (Enqueue)")
        print("2. Hapus pesanan dari antrian (Dequeue)")
        print("3. Keluar")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            pesanan = input("Masukkan nama pesanan: ")
            q.enqueue(pesanan)
            print(f"Pesanan '{pesanan}' telah ditambahkan ke antrian.")

        elif pilihan == "2":
            dihapus = q.dequeue()
            if dihapus != "Antrian kosong":
                print(f"Pesanan '{dihapus}' telah dihapus dari antrian.")
            else:
                print(dihapus)

        elif pilihan == "3":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

        print(f"Antrian saat ini: {q.items}")
