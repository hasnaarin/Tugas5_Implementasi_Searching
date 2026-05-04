# Nama Program : Implementasi linear search dan binary search
# Nama Pembuat : Nisrina Dwi Hasna
# NIM : 301250001
# Tanggal Pembuatan : 04 Mei 2026
# Nama File : 301250001_Nisrina_Tugas5.py

def linear_search(arr, target):
    """
    Linear Search: memeriksa elemen satu per satu dari awal hingga akhir.
    Mengembalikan: (indeks, jumlah_langkah)
    """
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps


def binary_search(arr, target):
    """
    Binary Search: membagi interval pencarian menjadi dua secara berulang.
    Syarat: data harus dalam keadaan TERURUT (ascending).
    Mengembalikan: (indeks, jumlah_langkah)
    """
    steps = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, steps


def main():
    # 1. Persiapan Data (minimal 20 elemen)
    data_asli = [45, 12, 78, 3, 56, 89, 23, 67, 1, 90, 
                 34, 11, 76, 20, 5, 43, 88, 29, 60, 15]
    
    # Binary search mengharuskan data terurut
    data_terurut = sorted(data_asli)
    
    print("📦 DATA:")
    print(f"Data Asli   : {data_asli}")
    print(f"Data Terurut: {data_terurut}\n")

    # 2. Skenario Pencarian (target ditemukan & tidak ditemukan)
    targets = [56, 100]

    for target in targets:
        print(f"🔍 === MENCARI TARGET: {target} ===")
        
        # Linear Search pada data asli
        idx_lin, steps_lin = linear_search(data_asli, target)
        status_lin = f"Ditemukan di indeks {idx_lin}" if idx_lin != -1 else "Tidak ditemukan"
        print(f"Linear Search  -> {status_lin} | Langkah: {steps_lin}")

        # Binary Search pada data terurut
        idx_bin, steps_bin = binary_search(data_terurut, target)
        status_bin = f"Ditemukan di indeks {idx_bin} (array terurut)" if idx_bin != -1 else "Tidak ditemukan"
        print(f"Binary Search  -> {status_bin} | Langkah: {steps_bin}")
        
        print("-" * 45)

    # 3. Analisis Perbandingan
    print("\n📊 PERBANDINGAN & ANALISIS:")
    print("• Linear Search  : Kompleksitas O(n)")
    print("  - Langkah sebanding dengan posisi data atau ukuran array.")
    print("  - Cocok untuk data kecil atau tidak terurut.")
    print("• Binary Search  : Kompleksitas O(log₂ n)")
    print("  - Langkah jauh lebih sedikit karena pencarian dibagi dua tiap iterasi.")
    print("  - WAJIB data terurut terlebih dahulu (overhead sorting bisa mahal jika data sering berubah).")
    print(f"  - Untuk n=20, worst-case Binary Search ≈ {len(bin(len(data_terurut))) - 3} langkah vs Linear Search 20 langkah.")
    print("\n💡 Catatan: Indeks yang dikembalikan Binary Search merujuk pada posisi di array TERURUT, bukan array asli.")


if __name__ == "__main__":
    main()