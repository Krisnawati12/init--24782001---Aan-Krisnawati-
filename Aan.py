"""
Nama File: Aan.py
Deskripsi: Program untuk menghitung rata-rata nilai mahasiswa.
Fitur utama:
- Menghitung rata-rata nilai dari daftar nilai yang diberikan.
- Menampilkan hasil rata-rata, nilai tertinggi, dan nilai terendah.
Penulis: Aan Krisnawati
Tanggal: 15 Maret 2025
"""


def hitung_rata2(daftar_nilai):
    """
    Menghitung rata-rata nilai dari daftar yang diberikan.

    Parameter:
    daftar_nilai (list): Daftar nilai mahasiswa (angka).

    Return:
    float: Rata-rata nilai dari daftar yang diberikan.

    Contoh penggunaan:
    >>> hitung_rata2([80, 90, 70])
    80.0
    """
    total = sum(daftar_nilai)
    return total / len(daftar_nilai)


def cetak_hasil(nama, daftar_nilai):
    """
    Mencetak hasil rata-rata, nilai tertinggi, dan nilai terendah.

    Parameter:
    nama (str): Nama mahasiswa.
    daftar_nilai (list): Daftar nilai mahasiswa.

    Return:
    None (hanya mencetak hasil ke layar).

    Contoh penggunaan:
    >>> cetak_hasil("Andi", [80, 75, 90])
    Mahasiswa: Andi, Rata-rata nilai: 81.67
    Nilai Terendah: 75 | Nilai Tertinggi: 90
    """
    hasil = hitung_rata2(daftar_nilai)
    print(f"Mahasiswa: {nama}, Rata-rata nilai: {round(hasil, 2)}")

    daftar_nilai.sort()
    print(f"Nilai Terendah: {daftar_nilai[0]}, "
          f"Nilai Tertinggi: {daftar_nilai[-1]}")


# Daftar nilai mahasiswa
nilai_siswa = [80, 75, 90, 85, 100, 60]

# Menampilkan hasil untuk mahasiswa bernama Andi
cetak_hasil("Andi", nilai_siswa)
