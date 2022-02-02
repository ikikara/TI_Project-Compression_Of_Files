# TI_Project-Huffman Encoding

- [x] Finished

## Index:
- [Description](#description)
- [To run this project](#to-run-this-project)
- [Notes important to read](#notes-important-to-read)

## Description:
Algorithm of compression. This Algorithm use Huffman Encoding and RLE.

## To run this project:
[WARNING] Python 3.9(or higher) and the libraries refered must be installed <br>
For compression:<br>
```shellscript
[your-disk]:[name-path]> python huffman.py <window-size> <buffer-size> -compress on/off <name-of-file>
```
*NOTE: The file 'huffman_aux.bin' is generated which stores the character frequencies*

For decompression:<br>
```shellscript
[your-disk]:[name-path]> python huffman.py <window-size> <buffer-size> -decompress on/off <name-of-file> <extension>
```
*NOTE: It is necessary to have the file 'huffman_aux.bin' in the same directory as huffman.py*

## Notes important to read
- It is necessary to have the files to be compressed/decompressed in the same folder as the huffman.py file 
- The -compress and -decompress flags are used to distinguish whether to compress or decompress.
- If you run the program with:<br>
     + on -> the compression or decompression will be displayed in the terminal<br>
     + off -> nothing will be displayed
- The < extension> will define the type of file that will be retrieved when decompressing
- The compressed files will go to the following directory:<br>
     + huffman/compressed
- The unzipped files will go to the following directory:<br>
     + huffman/decompress 
- Although the on/off part appears, running the compression command will never show any "print" in the terminal 
