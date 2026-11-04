name = "anna"   # change this to any name

s = sum(1337 + ord(c) for c in name)
a = (s * 30) & 0xFFFFFFFF
serial = ((a - (a ^ 0x37)) * 8) & 0xFFFFFFFF
if serial >= 2**31:
    serial -= 2**32
print("name:", name)
print("sum:", s)
print("serial:", serial)