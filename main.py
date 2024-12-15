import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

# Параметры
n_base64 = "0hlNqd4ffKgOwrerzUNQM3MllBID63F3LZPwBuj15BvdqCpvtn2+EkI5wCB3a4WPyx37r/TftEYwtqiy9Qylz+cfOWO+k8ApzByxiaHBIfiiuduPwlOMm3JSSC5JjFTn8l7Dn4hc9nHv9M/3TEaOhKMu5jt5w6ICN8rXRuzWl7E="
e_base64 = "AQAB"



# Подписи для проверки
signatures = [
    "fa0w8VSf7sFKbiXDSUX13XR7po905sUsOnHDEwCULg99xbkTDjB+PPicbTMOIOK2MUG4YJ4hR/Wo8Nb7MaYLL+CO6/HgKPsoqshNdXRCc3iH0WVRsTT35kvNW0urTzoW7pC2ATU6Z/ajM30m84bw5JNepiRju40yWVjVVWYiy9c=",
    "fMPNCGxiWn7z/Kix9NpdUVv+V4yzaHKNLerQq0/G46cxhe05FagmZCsAkYlcWYiV92b0rZpPELknlPsXP/0cSANN+db4TTqT0GrqLY/4X7TIEqHeiwrgqtvW9VWZzjcKP/sINu6hlyRuROhAAkDwblZa0IsU+N6tPcaTbkLWu/o=",
    "C1/eh2MFjVGlJXDq/S9cr+7lYag8xslI26EzqrPMg/4sKjOn+CfDb3JN6vkd5EafZbNnwyh2r8Yrxe35XEk4qIXSGTaoRSLKY8NtcWhQKR01d5OlKEpOB8ro1kn4zsz5k0U2Oq7xfiEsV9YMugiFmNMbZkNhSryzCNsuVNUlKBc=",
    "GfaR6vrV+O0w3rbYQ3FpUHkB+zCVkxjgpWGbpMAUYQ2E0y4uE2eroj0UjrufaEMkxqoUCQ6zo/qoEfbNpdAqtHWAk/pG4ErUfCpLbvfk6eMQkczPYhYxrP+au67IBIe+koOg5JWvYq2mQP9XxtyzGbgF4jChkJEite0jVSNo2gc=",
    "jGECSYKTt+eEomnbAZ0n0BrFYg+kTBSm3LJK7YPLt3dr6GlDILCEN3+fhUZMrJee2i5mDG+2UdrdZ16obMBnDkTooq3gd/ZZPCwvlh04Vi2iZHI9BwemwWDrgivKg6ZGbyXnWMwG/TX9A7B3iM9bDK1/O0mb4pi9x3my1gOQKJ0="
]

# Декодирование n и e
n = int.from_bytes(base64.b64decode(n_base64), byteorder='big')
e = int.from_bytes(base64.b64decode(e_base64), byteorder='big')

# Создание открытого ключа RSA
public_key = RSA.construct((n, e))

# Проверка каждой подписи
for signature_base64 in signatures:
    signature = base64.b64decode(signature_base64)

    # Хеширование файла logo.png
    with open('logo.png', 'rb') as f:
        file_data = f.read()
        hash_value = SHA256.new(file_data)

    # Верификация подписи
    try:
        pkcs1_15.new(public_key).verify(hash_value, signature)
        print(f"Подпись {signature_base64} верна.")
    except (ValueError, TypeError):
        print(f"Подпись {signature_base64} не верна.")