import deflate

#COMPRESSÃO
level = 6
with open("D:\Pycharm\Codecs\egg.bmp"  , 'rb') as f:
    data = bytearray(f.read())

dados = deflate.gzip_compress(data, level)

with open("D:\Pycharm\Codecs\eggDeflate.dat"  , 'wb') as f:
    f.write(bytearray(dados))


#DESCOMPRESSÃO
descomp = deflate.gzip_decompress(dados)

with open("D:\Pycharm\Codecs\eggDesc.bmp"  , 'wb') as f:
    f.write(bytearray(descomp))