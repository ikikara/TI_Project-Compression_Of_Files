Método de compressão Lz77
Para a sua utilização é necessário criar 1 pasta (lz77) com 2 pastas lá dentro (compressed e decompressed).
Ainda para assegurar o seu funcionamento é necessário ter os ficheiros a comprimir/descomprimir na mesma pasta do ficheiro lz77.py e correr o seguinte código no terminal:

Para compressão:
    python lz77.py <tamanho-janela> <tamanho-buffer> <-compress> <on/off> <name-of-file>

Para descompressão:
    python lz77.py <tamanho-janela> <tamanho-buffer> <-decompress> <on/off> <name-of-file> <extensão>


As flags -compress e -decompress servem para distinguir se vai fazer uma compressão ou descompressão.
Se correr o programa com:
    on -> será apresentado, no terminal, a compressão ou descompressão
    off -> não será nada apresentado
A extensão definirá o tipo de ficheiro que irá ser obtido aquando da descompressão

Os ficheiros comprimidos irão para a seguinte diretoria:
    lz77/compressed

Os ficheiros descomprimidos irão para a seguinte diretoria:
    lz77/decompress


NOTAS FINAIS:
-> Devidos às limitações da funções utilizadas o tamanho da janela deverá ser um número utilizado entre 0 e 256 (inclusive)