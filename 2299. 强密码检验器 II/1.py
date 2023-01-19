class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        special=set("!@#$%^&*()-+")
        Lower,Upper,Number,Special=False,False,False,False
        for i,ch in enumerate(password):
            if i !=0 and password[i-1] == password[i]:
                return False
            if ch.islower():
                Lower = True
            elif ch.isupper():
                Upper = True
            elif ch.isdigit():
                Number= True
            elif ch in special:
                Special=True
        return Lower and Upper and Number and Special
