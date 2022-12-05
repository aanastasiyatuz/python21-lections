import time
from jwt_handler import signJWT, decodeJWT, verify_jwt

user = {"id":1, "username":"nastya"}

"""получение токена"""
token = signJWT(user)
print(token) # {"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOnsiaWQiOjEsInVzZXJuYW1lIjoibmFzdHlhIn0sImV4cGlyeSI6MTY3MDIzOTMzNi4yMjM2Mjc2fQ.xbEmT-Af1Rk0ZmbEPfYujcIX9w9slaGzRVLE3JemYns"}

"""декодирование токена"""
decoded = decodeJWT(token['access'])
print(decoded) # {"id":1, "username":"nastya"}

"""проверка токена"""
print(verify_jwt(token["access"])) # True - токен еще не истек
time.sleep(10)
print(verify_jwt(token["access"])) # False - токен истек
