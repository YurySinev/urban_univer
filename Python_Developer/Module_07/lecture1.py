a = "hello"
print(a)
chars = []
for i in a:
    chars.append(ord(i)) # преобразование символов в числа

print(chars)

b = ''
for i in chars:
    b += chr(i)  # обратное преобразование

print(b)

for i in range(128):
    print(chr(i), end=' ')

print()
print()

for i in range(1000, 1200):
    print(chr(i), end=' ')

print()
print(hex(ord('h')))
bb = b'\x68'
print(bb)
print(type(bb))
print(bb.decode())

