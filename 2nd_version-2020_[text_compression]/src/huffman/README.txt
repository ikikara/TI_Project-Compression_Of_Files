Método de compressão Huffman
Para a sua utilização é necessário criar 1 pasta (huffman) com 2 pastas lá dentro (compressed e decompressed) e instalar a biblioteca dahuffman:
    - pip install dahuffman
Ainda para assegurar o seu funcionamento é necessário ter os ficheiros a comprimir/descomprimir na mesma pasta do ficheiro huffman.py e correr o seguinte código no terminal:

Para compressão:
    python <-compress> <on/off> <name-of-file>
    NOTA: É gerado o ficheiro 'huffman_aux.bin' que guarda as frequências dos caracteres

Para descompressão:
    python <-decompress> <on/off> <name-of-file> <extensão>
    NOTA: É necessário ter o ficheiro 'huffman_aux.bin' na mesma diretoria do huffman.py


As flags -compress e -decompress servem para distinguir se vai fazer uma compressão ou descompressão.
Se correr o programa com:
    on -> será apresentado, no terminal, a compressão ou descompressão
    off -> não será nada apresentado
A extensão definirá o tipo de ficheiro que irá ser obtido aquando da descompressão

Os ficheiros comprimidos irão para a seguinte diretoria:
    huffman/compressed

Os ficheiros descomprimidos irão para a seguinte diretoria:
    huffman/decompress


NOTAS FINAIS:
-> Apesar de aparecer a parte <on/off>, ao correr o comando da compressão nunca será apresentado qualquer "print" no terminal