import dahuffman

with open("D:\Pycharm\Codecs\egg.bmp"  , 'rb') as f:
    data = bytearray(f.read())

huff=dahuffman.HuffmanCodec.from_data(data).encode(data)

with open("D:\Pycharm\Codecs\eggHuf.dat"  , 'wb') as f:
    f.write(bytearray(huff))