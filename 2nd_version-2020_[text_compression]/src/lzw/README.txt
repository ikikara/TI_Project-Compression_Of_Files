Método de compressão LZW (versão com dicionário inicial de 128 entradas)
Para a sua utilização é necessário criar 1 pasta (lzw) com 2 pastas lá dentro (compressed e decompressed).
Ainda para assegurar o seu funcionamento é necessário ter os ficheiros a comprimir/descomprimir na mesma pasta do ficheiro lzw.py e correr o seguinte código no terminal:

Para compressão:
    python lzw.py <tamanho-janela> <tamanho-buffer> <-compress> <on/off> <name-of-file>

Para descompressão:
    python lzw.py <tamanho-janela> <tamanho-buffer> <-decompress> <on/off> <name-of-file> <extensão>


As flags -compress e -decompress servem para distinguir se vai fazer uma compressão ou descompressão.
Se correr o programa com:
    on -> será apresentado, no terminal, a compressão ou descompressão
    off -> não será nada apresentado
A extensão definirá o tipo de ficheiro que irá ser obtido aquando da descompressão

Os ficheiros comprimidos irão para a seguinte diretoria:
    lzw/compressed

Os ficheiros descomprimidos irão para a seguinte diretoria:
    lzw/decompress


NOTAS FINAIS:
-> O método 'decompress' foi baseado/retirado de: https://rosettacode.org/wiki/LZW_compression#Python