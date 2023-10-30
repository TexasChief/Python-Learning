chars = " abcdefghijklmnopqrstuvwxyz1234567890"
chars_list = list(chars)
cipher = "x5jpht2viq6blu13of 7ndek9wazrgs08m4cy"
cipher_list = list(cipher)

key = input("Input Key: ")
msg = (str(input("Please enter message: ")))


def encrypt2():
    o = ""
    for i in msg:
        if i not in chars_list:
            print("Used invalid char, format")
            break
        k = chars_list.index(i)
        m = cipher[k]
        o += m
    print(":" + o + ":")


def decrypt2():
    o = ""
    for i in msg:
        if i not in chars_list:
            print("Used invalid char, format")
            break
        k = cipher_list.index(i)
        m = chars_list[k]
        o += m
    print(":" + o + ":")

if key == "Paratos":
    encrypt2()
elif key == "Psalms":
    decrypt2()
else:
    print('Something went wrong')