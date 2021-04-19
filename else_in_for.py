# # else in for solo se ejecuta si el ciclo no se interrumpe
# # out = 0 1 2 3 4
for i in range(10):
    if i == 5:
        break
    else:
        print(i)
else:
    print("not break")
