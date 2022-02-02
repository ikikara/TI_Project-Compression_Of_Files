
import sys
import time
import dahuffman
import pickle

class huffman_rle:
    def __init__(self, preview=1, extension="txt"):
        self.preview = preview
        self.extension = "."+extension


    def compress(name):
        with open(name, 'rb') as file:
            text = bytearray(file.read())
        
        codec = dahuffman.HuffmanCodec.from_data(text)
        BIN = codec.encode(text)

        BIN = bytearray(BIN)

        BIN2 = bytearray('', 'utf-8')
        i = 0

        while i < len(BIN) :
            count = 1
            char = BIN[i]

            while i < len(BIN) - 1:
                if BIN[i] == BIN[i + 1]:
                    i += 1
                    count = count + 1
                else:
                    break

            i += 1
            BIN2 += bytes([count]) + bytes([char])

        splitted = name.split(".")
        toremove = splitted[len(splitted)-1]
        towrite = 'huffman+rle/compressed/compressed_'+name[0:len(name)-len(toremove)-1]+".bin"
        
        with open('huffman+rle/compressed/huffman_aux.bin', 'wb') as freq:
            pickle.dump(codec, freq)

        with open(towrite, "wb") as encodedFile:
            encodedFile.write(BIN2)




    def decompress(self, name):
        with open('huffman_aux.bin', 'rb') as freq:
            codec = pickle.load(freq)

        with open(name, 'rb') as encodedFile:
            dic = encodedFile.read()

        text = bytearray('', 'utf-8')


        for i in range(0, len(dic), 2):
            for j in range(dic[i]):
                text+=bytes([int(dic[i+1])])

        text = codec.decode(bytearray(text))

        text2 = ''
        for char in text:
            text2 += chr(char)

        splitted = name.split("_")
        toremove = splitted[0]
        towrite = 'huffman+rle/decompressed/decompressed_'+name[len(toremove)+1:len(name)-4]+self.extension

        with open(towrite, "w") as decodedFile:
            decodedFile.write(text2)

        if self.preview==1:
            print("\nPREVIEW OF DECOMPRESSION:")
            print(text)
            print()



if __name__ == "__main__":
    if(len(sys.argv)>=4):
        if sys.argv[2]=="on":
            preview = 1
        elif sys.argv[2]=="off":
            preview = 0
        else:
            print("\n2nd argument must be on or off\nProgram closing..\n")
            exit(1)

        if(sys.argv[1]=="-compress"):
            start_time = time.time()
            huffman_rle.compress(sys.argv[3])
            print("--- %s seconds ---" % (time.time() - start_time))

        elif(sys.argv[1]=="-decompress"):
            if len(sys.argv)==5:
                start_time = time.time()
                huffman_rle(preview, sys.argv[4]).decompress(sys.argv[3])
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file> <extension-of-file>\n")
                print("Program closing..\n")

    else:
        print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file>\n")
        print("Program closing..\n")
