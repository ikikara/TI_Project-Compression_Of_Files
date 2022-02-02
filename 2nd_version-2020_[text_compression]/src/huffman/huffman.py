
import sys
import dahuffman
import pickle

class huffman:
    def __init__(self, preview=1, extension="txt"):
        self.preview = preview
        self.extension = "."+extension


    def compress(name):
        with open(name, 'rb') as file:
            text = bytearray(file.read())
        
        codec = dahuffman.HuffmanCodec.from_data(text)
        BIN = codec.encode(text)

        splitted = name.split(".")
        toremove = splitted[len(splitted)-1]
        towrite = 'huffman/compressed/compressed_'+name[0:len(name)-len(toremove)-1]+".bin"
        
        with open('huffman/compressed/huffman_aux.bin', 'wb') as freq:
            pickle.dump(codec, freq)

        with open(towrite, "wb") as encodedFile:
            encodedFile.write(BIN)


    def decompress(self, name):
        with open('huffman_aux.bin', 'rb') as freq:
            codec = pickle.load(freq)

        with open(name, 'rb') as encodedFile:
            dic = encodedFile.read()
        
        text = ''
        for char in codec.decode(dic):
            text += chr(char)

        splitted = name.split("_")
        toremove = splitted[0]
        towrite = 'huffman/decompressed/decompressed_'+name[len(toremove)+1:len(name)-4]+self.extension

        with open(towrite, "w") as decodedFile:
            decodedFile.write(text)

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
            huffman.compress(sys.argv[3])

        elif(sys.argv[1]=="-decompress"):
            if len(sys.argv)==5:
                huffman(preview, sys.argv[4]).decompress(sys.argv[3])
            else:
                print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file> <extension-of-file>\n")
                print("Program closing..\n")

    else:
        print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file>\n")
        print("Program closing..\n")
