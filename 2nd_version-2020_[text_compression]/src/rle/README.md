# TI_Project-Run Length Encoding

- [x] Finished

## Index:
- [Description](#description)
- [To run this project](#to-run-this-project)
- [Notes important to read](#notes-important-to-read)

## Description:
Algorithm of compression, RLE.

## To run this project:
[WARNING] Python 3.9(or higher) and the libraries refered must be installed <br>
For compression:<br>
```shellscript
[your-disk]:[name-path]> python rle.py <window-size> <buffer-size> -compress on/off <name-of-file>
```

For decompression:<br>
```shellscript
[your-disk]:[name-path]> python rle.py <window-size> <buffer-size> -decompress on/off <name-of-file> <extension>
```

## Notes important to read
- It is necessary to have the files to be compressed/decompressed in the same folder as the rle.py file 
- The -compress and -decompress flags are used to distinguish whether to compress or decompress.
- If you run the program with:<br>
     + on -> the compression or decompression will be displayed in the terminal<br>
     + off -> nothing will be displayed
- The < extension> will define the type of file that will be retrieved when decompressing
- The compressed files will go to the following directory:<br>
     + rle/compressed
- The unzipped files will go to the following directory:<br>
     + rle/decompress 
- Due to the limitations of the functions used (bytes() and bytearray()) the window size must be a number used between 0 and 256 (inclusive)
