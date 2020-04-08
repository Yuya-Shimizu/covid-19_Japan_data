import pandas as pd
import requests
import io


def pre():
    #Excelファイルを読み込む
    url = 'https://dl.dropboxusercontent.com/s/6mztoeb6xf78g5w/COVID-19.csv'
    res = requests.get(url).content
    df = pd.read_csv(io.StringIO(res.decode('utf-8')), header=0, index_col=False)

    df2 = pd.read_csv("COVID-19.csv", index_col=False)
    d = df2.loc[:,["都道府県","Prefecture"]]
    df2 = df.loc[:,:'Field10']    
    df2 = df2.rename(columns={'Field2':'都道府県', 'Field4':'Prefecture'})

    for i in range(47):
        df2.iloc[i,43] = d["都道府県"][i]
        df2.iloc[i,44] = d["Prefecture"][i]

    df2.to_csv("COVID-19.csv", index=False, encoding="utf-8-sig")

    
pre()
csv_data = pd.read_csv("COVID-19.csv")
gender_data = csv_data["Gender"]
prefecture_j = csv_data["都道府県"]
prefecture_e = csv_data["Prefecture"]
resident_e = csv_data["Residential Pref"]
resident_j = csv_data["居住都道府県"]
Age_data = csv_data["年代"]

class Analysis():

    def Gender(self, lang):
        M=0
        F=0
        U=0
        for G in gender_data:
            if G == "Male":
                M += 1
            elif G == "Female":
                F += 1
            else:
                U += 1 

        ratio_M = M/len(gender_data)*100
        ratio_F = F/len(gender_data)*100
        ratio_U = U/len(gender_data)*100

        ratio_W = ratio_M + ratio_F + ratio_U

        if lang == 'Japanese':
            text = "感染者(性別割合)\n男性: %.3f％\t\t女性: %.3f％\t\t性別不明: %.3f％\t\t合計: %.3f％" %(ratio_M,ratio_F,ratio_U,ratio_W)
        elif lang == 'English':
            text = "the Infected(gender)\nMale: %.3f％\t\tFemale: %.3f％\t\tUnkown: %.3f％\t\tTotal: %.3f％" %(ratio_M,ratio_F,ratio_U,ratio_W)
        print(text)
        #return text
        #print("感染者(性別割合)\n\n男性: "+str(ratio_M)+"\t女性: "+str(ratio_F)+"\t性別不明: "+str(ratio_U)+"\t合計: "+str(ratio_W))


    def Resident_e(self):
        self.J = []
        Ov = []
        Ja=0
        Un=0
        Fo=0
        for R in resident_e:
            T = 0
            for P in prefecture_e[0:47]:
                if R == P:
                    self.J.append(R)
                    Ja += 1
                    T = 1
            if T == 0:     
                if R == "Unknown":
                    Un += 1
                else:
                    Ov.append(R)
                    Fo += 1

        ratio_Ja = Ja/len(resident_e)*100
        ratio_Un = Un/len(resident_e)*100
        ratio_Fo = Fo/len(resident_e)*100

        ratio_W_ = ratio_Ja + ratio_Un + ratio_Fo

        text = "\n\nthe Infected(Resident)\nJapan: %.3f％\t\tOther countries: %.3f％\t\tUnkown: %.3f％\t\tTotal: %.3f％\n\n"%(ratio_Ja, ratio_Un, ratio_Fo, ratio_W_)
        print(text)
        #return text

    def Prefecture_e(self):
        Pre = pd.DataFrame(self.J)


        for p in prefecture_e[0:47]:
            exec("t_%s = %d" %(p, 0))

        for P in Pre[0]:
            for p in prefecture_e[0:47]:
                if P == p:
                    exec("t_%s += %d" %(p, 1))
                else:
                    exec("t_%s += %d" %(p, 0))
                
        for p in prefecture_e[0:47]:
                #exec("num = t_%s" %(p))
                num = eval("t_%s" %(p))
                ratio = num/len(self.J)*100
                caution = "#"*int(ratio)
                if int(ratio)==0:
                    print("%s: %.3f ％   \t\t%d people" %(p, ratio, num))
                else:
                    print("%s: %.3f ％   \t\t%d people\t\t%s  %s (%d％)" %(p, ratio, num, caution, p, int(ratio)))


    def Resident_j(self):
        self.J_ = []
        Ov = []
        Ja=0
        Un=0
        Fo=0
        for R in resident_j:
            T = 0
            for P in prefecture_j[0:47]:
                if R == P:
                    self.J_.append(R)
                    Ja += 1
                    T = 1
            if T == 0:     
                if R == "不明":
                    Un += 1
                else:
                    Ov.append(R)
                    Fo += 1

        ratio_Ja = Ja/len(resident_j)*100
        ratio_Un = Un/len(resident_j)*100
        ratio_Fo = Fo/len(resident_j)*100

        ratio_W_ = ratio_Ja + ratio_Un + ratio_Fo

        text = "\n\n感染者(居住地割合)\n日本: %.3f％\t\t海外: %.3f％\t\t居住地不明: %.3f％\t\t合計: %.3f％\n\n"%(ratio_Ja, ratio_Un, ratio_Fo, ratio_W_)
        print(text)
        #return text

    def Prefecture_j(self):
        Pre = pd.DataFrame(self.J_)


        for p in prefecture_j[0:47]:
            exec("t_%s = %d" %(p, 0))

        for P in Pre[0]:
            for p in prefecture_j[0:47]:
                if P == p:
                    exec("t_%s += %d" %(p, 1))
                else:
                    exec("t_%s += %d" %(p, 0))
                
        for p in prefecture_j[0:47]:
                #exec("num = t_%s" %(p))
                num = eval("t_%s" %(p))
                ratio = num/len(self.J_)*100
                caution = "#"*int(ratio)
                if int(ratio)==0:
                    print("%s: %.3f ％   \t\t%d 人" %(p, ratio, num))
                else:
                    print("%s: %.3f ％   \t\t%d 人\t\t%s  %s (%d％)" %(p, ratio, num, caution, p, int(ratio)))



    def Age(self, lang):
        for i in range(1,6):
            exec("age_%d = %d" %(10*i, 0))
        age_under_10 = 0
        age_over_60 = 0
        unknown = 0
        Age = pd.DataFrame(Age_data)
        
        for a in Age["年代"]:
            if a == "0-10":
                age_under_10 += 1
            elif a == "不明":
                unknown += 1
            elif int(a) < 20:
                exec("age_%d += %d" %(10, 1))
            elif int(a) < 30:
                exec("age_%d += %d" %(20, 1))
            elif int(a) < 40:
                exec("age_%d += %d" %(30, 1))
            elif int(a) < 50:
                exec("age_%d += %d" %(40, 1))
            elif int(a) < 60:
                exec("age_%d += %d" %(50, 1))
            else:
                age_over_60 += 1

        S = age_under_10 + age_over_60 + unknown

        if lang == "Japanese":
            print("\n10歳未満: %d人" %(age_under_10))
            for i in range(1,6):
                age = eval("age_%d" %(10*i))
                S += age
                print("\n%d代: %d 人" %(10*i, age))
            print("\n60歳以上: %d 人" %(age_over_60))
            print("\n不明: %d 人" %(unknown))
            print("\n合計: %d 人" %(S))

        elif lang == "English":
            print("\nunder 10 years old: %dpeople" %(age_under_10))
            for i in range(1,6):
                age = eval("age_%d" %(10*i))
                S += age
                print("\n%ds: %d people" %(10*i, age))
            print("\nover 60 years old: %d people" %(age_over_60))
            print("\nunkown: %d people" %(unknown))
            print("\nTotal: %d people" %(S))

        
if __name__ == '__main__':
    while True:
        A = Analysis()
        #print(A.Gender())
        #print(A.Resident_e())

        while True:
            o = input("日本語表示/ 0を入力\t英語表示/ 1を入力\n入力: ")
            if o == '0':
                A.Gender("Japanese")                
                A.Resident_j()
                A.Prefecture_j()
                A.Age("Japanese")
                break
            elif o == '1':
                A.Gender("English")
                A.Resident_e()
                A.Prefecture_e()
                A.Age("English")
                break


        a = input("閉じる/ 0を入力: ")
        if a == '0':
            break
        else:
            continue
