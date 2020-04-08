from covid import *

while True:
    A = Analysis()
    A.Gender()
    A.Resident_j()
    A.Prefecture_j()
    A.Age()

    a = input("閉じる/ 0を入力: ")
    if a == '0':
        break
    else:
        continue
