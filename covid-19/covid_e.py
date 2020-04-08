from covid import *

while True:
    A = Analysis()
    A.Gender()
    A.Resident_e()
    A.Prefecture_e()
    A.Age()

    a = input("閉じる/ 0を入力: ")
    if a == '0':
        break
    else:
        continue
