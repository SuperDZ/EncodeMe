from crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(plain_text: str, key: str) -> str:
    """
    AES加密函数
    
    Args:
        plain_text: 需要加密的明文字符串
        key: 16/24/32位的密钥字符串
        
    Returns:
        加密后的base64编码字符串
    """
    # 将密钥转换为bytes
    key_bytes = key.encode('utf-8')
    # 如果密钥长度不是16/24/32字节，进行填充或截断
    if len(key_bytes) not in [16, 24, 32]:
        key_bytes = key_bytes[:16].ljust(16, b'\0')
    
    # 创建AES加密器，使用ECB模式
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    
    # 对明文进行填充并加密
    plain_bytes = plain_text.encode('utf-8')
    padded_bytes = pad(plain_bytes, AES.block_size)
    cipher_bytes = cipher.encrypt(padded_bytes)
    
    # 将加密结果转为base64编码
    return base64.b64encode(cipher_bytes).decode('utf-8')

def aes_decrypt(cipher_text: str, key: str) -> str:
    """
    AES解密函数
    
    Args:
        cipher_text: base64编码的密文字符串
        key: 16/24/32位的密钥字符串
        
    Returns:
        解密后的明文字符串
    """
    # 将密钥转换为bytes
    key_bytes = key.encode('utf-8')
    # 如果密钥长度不是16/24/32字节，进行填充或截断
    if len(key_bytes) not in [16, 24, 32]:
        key_bytes = key_bytes[:16].ljust(16, b'\0')
    
    # 创建AES解密器，使用ECB模式
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    
    # 对base64编码的密文进行解码和解密
    cipher_bytes = base64.b64decode(cipher_text)
    padded_bytes = cipher.decrypt(cipher_bytes)
    
    # 去除填充并返回明文
    return unpad(padded_bytes, AES.block_size).decode('utf-8')
