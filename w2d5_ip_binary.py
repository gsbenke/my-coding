# IP Binary Converter

ip = str(input("Type ip4 number: "))
print('.'.join([bin(int(x)+256)[3:] for x in ip.split(".")]))