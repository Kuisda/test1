num="23"
print(int(num)+2)

def JudgeTime(s1:str,s2:str)->bool:
            return int(s1[0:2])*60+int(s1[3:5])-int(s2[0:2])*60-int(s2[3:5])<=60
s1 = "09:00"
s2 = "11:00"

print(int(s1[0:2])*60+int(s1[3:5]))
print(int(s2[0:2])*60+int(s2[3:5]))
print(JudgeTime(s1,s2))