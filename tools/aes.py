import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AESCipher:
    """
    AES加密、解密工具类
    """

    def __init__(self, key):
        self.key = key
        # 这里直接用key充当iv
        self.iv = key

    def encrypt(self, raw):
        """
        加密方法
        :param raw: 需要加密的密文 str
        :return: base64编码的密文 str
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(self.__pad(raw).encode())).decode()

    def decrypt(self, enc):
        """
        解密方法
        :param enc: base64编码的密文 str
        :return: 解密后的明文 str
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.__unpad(cipher.decrypt(base64.b64decode(enc)).decode())

    def __pad(self, text):
        # 填充方法，加密内容必须为16字节的倍数
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        # 截取填充的字符
        pad = ord(text[-1])
        return text[:-pad]


cipher = AESCipher(b"get_random_bytes")

if __name__ == '__main__':
    # 随机生成16位aes密钥
    cipher = AESCipher(b'get_random_bytes')
    text = "43052499803100722"
    t = text[2:-4]
    print(text[0:2],text[-4:])
    encrypt = cipher.encrypt(t)
    print('加密后:\n%s' % text[0:2]+encrypt+text[-4:])
    decrypt = cipher.decrypt(encrypt)
    print('解密后:\n%s' % decrypt)
