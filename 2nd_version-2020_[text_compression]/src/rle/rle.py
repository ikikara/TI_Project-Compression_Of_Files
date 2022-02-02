import sys

class rle:
    def __init__(self, preview=1, extension="txt"):
        self.preview = preview
        self.extension = "."+extension


    def compress(self, name):
        with open(name, 'rb') as file:
            text = bytearray(file.read())

        BIN = bytearray('', 'utf-8')
        i = 0

        while i < len(text) :
            count = 1
            char = text[i]

            while i < len(text) - 1:
                if text[i] == text[i + 1]:
                    i += 1
                    count = count + 1
                else:
                    break

            i += 1
            BIN += bytes([count]) + bytes([char])

        splitted = name.split(".")
        toremove = splitted[len(splitted)-1]
        towrite = 'rle/compressed/compressed_'+name[0:len(name)-len(toremove)-1]+".bin"
        
        with open(towrite, "wb") as encodedFile:
            encodedFile.write(BIN)

        if self.preview==1:
            print("\nPREVIEW OF COMPRESSION:")
            for i in range(0, len(BIN), 2):
                print(BIN[i], end="") 
                print(chr(BIN[i+1]), end="") 
            print("\n")


    def decompress(self, name):
        with open(name, 'rb') as encodedFile:
            dic = encodedFile.read()

        text = ""

        for i in range(0, len(dic), 2):
            text+=dic[i]*chr(dic[i+1])

        splitted = name.split("_")
        toremove = splitted[0]
        towrite = 'rle/decompressed/decompressed_'+name[len(toremove)+1:len(name)-4]+self.extension

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
            rle(preview).compress(sys.argv[3])
            

        elif(sys.argv[1]=="-decompress"):
            if len(sys.argv)==5:  
                rle(preview, sys.argv[4]).decompress(sys.argv[3])
            else:
                print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file> <extension-of-file>\n")
                print("Program closing..\n")

    else:
        print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file>\n")
        print("Program closing..\n")