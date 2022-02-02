Método de compressão Run Length Encoding
Para a sua utilização é necessário criar 1 pasta (rle) com 2 pastas lá dentro (compressed e decompressed).
Ainda para assegurar o seu funcionamento é necessário ter os ficheiros a comprimir/descomprimir na mesma pasta do ficheiro rle.py e correr o seguinte código no terminal:

Para compressão:
    python rle.py <tamanho-janela> <tamanho-buffer> <-compress> <on/off> <name-of-file>

Para descompressão:
    python rle.py <tamanho-janela> <tamanho-buffer> <-decompress> <on/off> <name-of-file> <extensão>


As flags -compress e -decompress servem para distinguir se vai fazer uma compressão ou descompressão.
Se correr o programa com:
    on -> será apresentado, no terminal, a compressão ou descompressão
    off -> não será nada apresentado
A extensão definirá o tipo de ficheiro que irá ser obtido aquando da descompressão

Os ficheiros comprimidos irão para a seguinte diretoria:
    rle/compressed

Os ficheiros descomprimidos irão para a seguinte diretoria:
    rle/decompress


NOTAS FINAIS:
-> Devidos às limitações da funções utilizadas (bytes() e bytearray()) o programa pode originar erros se algum caracter se repetir mais do que 256 vezes.