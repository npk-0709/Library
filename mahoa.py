import base64


class CLASS_:
    def __init__(self, string: str):
        self.string = string

    def __base(self, __type: str):
        if __type == "enc":
            return base64.b64encode(self.hex_e.encode("utf-8")).decode("utf-8")
        elif __type == "dec":
            self.base = base64.b64decode(self.string.encode("utf-8")).decode("utf-8")

    def encode(self):
        self.__kytu_so_enc()  # mã hóa kí tự thành số
        self.__so_hex_enc()  # mã hóa từ số sang hexa
        return self.__base("enc")  # mã hóa  hexa thành base64

    def __so_hex_enc(self):
        arr = []
        __list = self.so # lấy giá trị line 36
        for i in __list: 
            if i == ord(" "): #kiểm tra nếu bằng khoảng cách thì thêm khoảng cách vào list
                arr.append(" ") 
            else: 
                arr.append(hex(i)) #chuyển kí tự số thành mã hexa
        self.hex_e = "|".join(arr)

    def __kytu_so_enc(self): #func Chuyển Ký tự Thành Số 

        __str = self.string # lấy giá trị của line 6
        output = []
        for character in __str:
            number = ord(character)  # mã hóa kí tự số thành số
            output.append(number) # thêm kí tự vừa chuyển đổi vào list
        self.so = output

    def decode(self):
        self.__base("dec")  # giải chuỗi base64 -> hexa
        return "".join(self.__so_hex_dec())  # giải hexa -> return Kí Tự ????


    def __so_hex_dec(self): #func chuyển số thành mã hexa
        __hex = self.base # lấy giá trị line 12
        arr = []
        for s in __hex.split("|"):
            char = bytes.fromhex(s.split("0x")[1]).decode("utf-8") # giải hexa thành kí tự ????  - 
            arr.append(char)
        return arr


#đáng lẽ phải giải ra kí tự số vì ở trên mã hóa từ số => hexa  mà ở đây từ hexa nó ra thẳng chuỗi luôn à

if __name__ == "__main__":
    string = "Python"
    str_encode = CLASS_(string).encode()
    print(str_encode)
    str_decode = CLASS_(str_encode).decode()
    print(str_decode)
