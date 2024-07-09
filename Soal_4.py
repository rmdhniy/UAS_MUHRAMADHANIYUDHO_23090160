class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

mangga_harum_manis = Mangga("Harum Manis", "Hijau", "Manis", "Vitamin C")

print(mangga_harum_manis.nama)      
print(mangga_harum_manis.warna)     
print(mangga_harum_manis.rasa)       
print(mangga_harum_manis.vitamin)    

mangga_harum_manis.setNama("Arumanis")
mangga_harum_manis.setWarna("Kuning")
mangga_harum_manis.setRasa("Manis Asam")
mangga_harum_manis.setVitamin("Vitamin A")

print(mangga_harum_manis.information())  
