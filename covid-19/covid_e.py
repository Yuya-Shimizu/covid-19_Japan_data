from covid import *

while True:
    A = Analysis()
    A.Gender("English")
    A.Resident_e()
    A.Prefecture_e()
    A.Age("English")

    a = input("\nInput '0' to close this: ")
    if a == '0':
        break
    else:
        print("#"*50+"\n\n")
        continue
