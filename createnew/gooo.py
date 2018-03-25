import base64
"""base64编码
    对于给出的二进制数据(字节)，按顺序每3个字节划分为1组，同时每个字节为8bit，所以共3 x 8 =24bit, 将24bit 划分为4组，即每组6位
    那么每组就有2^6=64种可能性，编制一个base64编码表，每组的数值对应从编码表查询出的码。即每三个字符有4个码，
    遇到给出的字符串非3的倍数，直接尾部补\x00以及1个或2个==,表示补了多少字节
"""

def main():
    string = 'Glad,My Half'.encode('ascii') #编码为ascii 字节数据
    string2 = '黎明'.encode('utf-8') #中文用utf-8编码为 字节数据
    encrypt=base64.b64encode(string)
    print(encrypt)
    decrypt = base64.b64decode(encrypt)
    print(decrypt)
if __name__ == '__main__':
    main()
