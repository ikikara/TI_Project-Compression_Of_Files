import sys
import pickle
from io import StringIO

class lzw:
    def __init__(self, preview=1, extension="txt"):
        self.preview = preview
        self.extension = "."+extension


    def compress(self, name):
        with open(name, 'rb') as file:
            text = bytearray(file.read())

        size = 128
        init = {chr(i): i for i in range(size)}

        string = ""
        encoded = []

        for i in text:
            char = chr(i)
            if string + char in init:
                string += char
            else:
                encoded += [init[string]]
                init[string + char] = size
                string = char
                size += 1

        encoded += [init[string]]

        splitted = name.split(".")
        toremove = splitted[len(splitted)-1]
        towrite = 'lzw/compressed/compressed_'+name[0:len(name)-len(toremove)-1]+".bin"

        with open(towrite, "wb") as encodedFile:
            pickle.dump(encoded, encodedFile)

        if self.preview==1:
            print("\nPREVIEW OF COMPRESSION:")
            print(encoded)
            print("\n")


    def decompress(self, name):
        with open(name, 'rb') as encodedFile:
            dic = pickle.load(encodedFile)

        dict_size = 128
        init = {i: chr(i) for i in range(dict_size)}

        text = StringIO()
        w = chr(dic.pop(0))
        text.write(w)
        for k in dic:
            if k in init:
                entry = init[k]
            elif k == dict_size:
                entry = w + w[0]
            text.write(entry)

            init[dict_size] = w + entry[0]
            dict_size += 1

            w = entry

        text = text.getvalue()


        splitted = name.split("_")
        toremove = splitted[0]
        towrite = 'lzw/decompressed/decompressed_'+name[len(toremove)+1:len(name)-4]+self.extension

        with open(towrite, "w") as decodedFile:
            decodedFile.write(text)

        if self.preview==1:
            print("\nPREVIEW OF DECOMPRESSION:")
            print(text)
            print()

    '''def decompress(self, name):
        dic_size = 128
        init = {i: chr(i) for i in range(dic_size)}

        text = ""
        decoded = []
        for char in dic:
            if char < 128:
                decoded.append(init[char])
                if string + init[char] in init.values():
                    string = string + init[char]
                else:
                    init[dic_size] = string + init[char]
                    dic_size += 1
                    string = init[char]
            else:
                print(init[char])
                for i in range(len(init[char])):
                    decoded.append(init[char][i])

        toprint = ''
        for i in decoded:
            toprint +=i

        print(toprint)'''



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
            lzw(preview).compress(sys.argv[3])

        elif(sys.argv[1]=="-decompress"):
            if len(sys.argv)==5:  
                lzw(preview, sys.argv[4]).decompress(sys.argv[3])
            else:
                print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file> <extension-of-file>\n")
                print("Program closing..\n")

    else:
        print("\nNumber of arguments invalid\nTo use this program write the correct parameters:\n\t <-compress/-decompress> <on/off> <name-of-file>\n")
        print("Program closing..\n")
