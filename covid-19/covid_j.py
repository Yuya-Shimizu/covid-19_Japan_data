from covid import *

while True:
    A = Analysis()
    A.Gender("Japanese")
    A.Resident_j()
    A.Prefecture_j()
    A.Age("Japanese")

    a = input("閉じる/ 0を入力: ")
    if a == '0':
        break
    else:
        print("#"*50+"\n\n")
        continue
