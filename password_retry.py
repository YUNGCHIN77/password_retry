password = "123456"
num = 2

while True :
    
    key = input("請輸入您的密碼：")

    if key != password :
        if num == 0 :
            break
        print(f"密碼錯誤! 還有{num}次機會")
        num -= 1
    else :
        print("登入成功!")
        break

    
    
    