# Kelompok 16
# Dilia Fadilah Mutmainah
# Muhammad Rafiqi Masrur
# Nabila Luthfia Arifin

from timeit import default_timer

# Floor and Ceiling in a Sorted Array (Bruteforce)

startTime = default_timer()

# Fungsi untuk mendapatkan index floor dari x pada arr[0...n-1]

def cariFloor(arr, n, x):
    # Jika x lebih kecil dari elemen pertama, maka floor tidak ditemukan
    if (x < arr[0]):
        return -1

    # Jika x lebih besar atau sama dengan element terakhir, maka return element terakhir
    if (x >= arr[n-1]):
        return n

    # Mencari element pertama yang lebih besar dari x satu per satu
    i = 0
    while i < n-1:
        if arr[i] == x:
            return i

        # Jika arr[i] lebih besar dari x, return i - 1
        
        if (arr[i] > x):
            return i - 1
            
        i = i + 1

# Fungsi untuk mendapatkan index ceiling dari x pada arr[0...n-1]
def cariCeiling(arr, n, x):
    # Jika x lebih kecil atau sama dengan element pertama, return element pertama
    if x <= arr[0]:
        return 0
 
    # Jika tidak, cari nilai ceiling satu per satu
    i = 0
    while i <= n-1:
        if arr[i] == x:
            return i
 
        # jika x berada diantara arr[i] dan arr[i+1], return i+1
        if arr[i] < x and arr[i+1] >= x:
            return i+1

        i = i + 1
         
    # Jika x lebih besar dari element terakhir, maka ceiling tidak ditemukan
    return -1

endTime = default_timer()

arr = list(map(int, input("Masukkan element array, dipisah spasi, dari kecil ke besar : ").split()))
n = len(arr)
x = int(input("Masukkan nilai x : "))

indexFloor = cariFloor(arr, n-1, x)
indexCeiling = cariCeiling(arr, n-1, x)

if (indexFloor == -1):
    print("Floor dari", x, "tidak ada pada array")
else:
    print("Floor dari", x, "adalah", arr[indexFloor])

if (indexCeiling == -1):
    print("Ceiling dari", x, "tidak ada pada array")
else:
    print("Ceiling dari", x, "adalah", arr[indexCeiling])

print("Running Time :", (endTime - startTime), "second")