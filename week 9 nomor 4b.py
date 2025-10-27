import numpy as np

nilai = np.array([
    [85, 80, 90],
    [72, 82, 88],
    [92, 90, 94],
    [70, 68, 72],
    [88, 85, 84],
    [60, 75, 70],
    [95, 92, 98],
    [74, 70, 76],
    [81, 85, 83],
    [69, 72, 77],
    [78, 88, 92],
    [76, 80, 79],
    [84, 86, 79],
    [79, 82, 85],
    [67, 70, 68],
    [91, 94, 93],
    [73, 78, 75],
    [87, 84, 89],
    [65, 80, 89],
    [93, 90, 95],
    [77, 80, 78],
    [82, 84, 78],
    [89, 85, 90],
    [71, 74, 76],
])

rata2 = np.mean(nilai)
tertinggi = np.max(nilai)
terendah = np.min(nilai)

print("\nRata-rata keseluruhan nilai:", rata2)
print("Nilai tertinggi:", tertinggi)
print("Nilai terendah:", terendah)