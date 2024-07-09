import pandas as pd

data = [
    ['Mahasiswa 1', 90, 80],
    ['Mahasiswa 2', 50, 60],
    ['Mahasiswa 3', 65, 70]
]

df = pd.DataFrame(data, columns=['Nama', 'Algoritma dan Struktur Data 2', 'Matematika Numerik'])
print(df)


#rata rata nilai untuk setiap matkul dan Mahasiswa
data = [
    ['Mahasiswa 1', 90, 80],
    ['Mahasiswa 2', 50, 60],
    ['Mahasiswa 3', 65, 70]
]

df = pd.DataFrame(data, columns=['Nama', 'Algoritma dan Struktur Data 2', 'Matematika Numerik'])

average_per_course = df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean()

df['Rata-rata'] = df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean(axis=1)

print("Rata-rata untuk setiap mata kuliah:")
print(average_per_course)
print("\nRata-rata untuk setiap mahasiswa:")
print(df[['Nama', 'Rata-rata']])

