# Kelompok 16
# Dilia Fadilah Mutmainah
# Muhammad Rafiqi Masrur
# Nabila Luthfia Arifin

from timeit import default_timer

# Floor and Ceiling in a Sorted Array (Divide and Conquer)

startTime = default_timer()

# Fungsi untuk mendapatkan index floor dari x pada arr[low...high]
def cariFloor(arr, low, high, x):
    # Jika x lebih kecil dari element pertama maka floor tidak ada
    if (x < arr[low]):
        return -1

    # Jika x lebih besar atau sama dengan element terakhir, maka return element terakhir
    if (x >= arr[high]):
        return high

    # Mencari titik tengah
    mid = int((low + high) // 2)

    # Jika titik tengah adalah floor, return titik tengah
    if (arr[mid] == x):
        return mid

    # Jika x berada diantara arr[mid-1] dan arr[mid], return mid-1
    if (mid > 0 and x >= arr[mid-1] and x < arr[mid]):
        return mid - 1

    # Jika x lebih kecil dari titik tengah, maka floor berada di bagian kiri
    if (x < arr[mid]):
        return cariFloor(arr, low, mid - 1, x)
    
    # Jika mid-1 bukan floor dan x lebih besar dari titik tengah, maka floor berada di bagian kanan
    else:
        return cariFloor(arr, mid + 1, high, x)

# Fungsi untuk mencari index ceiling dari x pada arr[low...high]
def cariCeiling(arr, low, high, x):

    # Jika x lebih besar dari element terakhir, maka ceiling tidak ada
    if (x > arr[high]):
        return -1

    # Jika x lebih kecil atau sama dengan element pertama, return element pertama
    if (x <= arr[low]):
        return low

    # Mencari titik tengah
    mid = int((low + high) // 2)

    # Jika x sama dengan titik tengah, return titik tengah
    if (arr[mid] == x):
        return mid

    # Jika x lebih besar dari titik tengah, maka ceiling berada di bagian kanan
    elif (arr[mid] < x):
        if mid + 1 <= high and x <= arr[mid+1]:
            return mid + 1
        else:
            return cariCeiling(arr, mid + 1, high, x)
    
    # Jika x lebih kecil dari titik tengah, maka ceiling berada di bagian kiri
    else:
        if mid - 1 >= low and x > arr[mid-1]:
            return mid
        else:
            return cariCeiling(arr, low, mid - 1, x)

endTime = default_timer()

arr = list(map(int, input("Masukkan element array, dipisah spasi, dari kecil ke besar : ").split()))
n = len(arr)
x = int(input("Masukkan nilai x : "))

indexFloor = cariFloor(arr, 0, n-1, x)
indexCeiling = cariCeiling(arr, 0, n-1, x)

if (indexFloor == -1):
    print("Floor dari", x, "tidak ada pada array")
else:
    print("Floor dari", x, "adalah", arr[indexFloor])

if (indexCeiling == -1):
    print("Ceiling dari", x, "tidak ada pada array")
else:
    print("Ceiling dari", x, "adalah", arr[indexCeiling])

print("Running Time :", (endTime - startTime), "second")