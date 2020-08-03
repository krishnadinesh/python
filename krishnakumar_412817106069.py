import math,random
def otp():
    dig="1234567890"
    o=" "
    for i in range(4):
        o+=dig[math.floor(random.random()*10)]
    return o
if __name__ == "__main__":
    print(otp())
