set_A = {20,30,40,50,60}
set_B = {25,30,35,40,45}
set_C = {30,40,50,70,80,}
set_D = {40,50,60,90,100}

cara1 = set_A.intersection(set_C, set_D)
print("Irisan A, C, D:", cara1)

cara2 = set_A.union(set_B).difference(set_D)
print("Gabungan A dan B dikurangi D:", cara2)

cara3 = set_B.symmetric_difference(set_C)
print("Selisih simetris B dan C:", cara3)

cara4 = set_A.union(set_B).intersection(set_C.union(set_D))
print("Irisan (A U B) dengan (C U D):", cara4)