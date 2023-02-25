password = "123456"
num = 3
key = input("請輸入您的密碼：")

while num > 0:
    if key == password:
        print("登入成功!")
        break   
    else:
        num -= 1
        if num == 0:
            break    
        print(f"密碼錯誤! 還有{num}次機會")
        key = input("請輸入您的密碼：")
 



    
    
    