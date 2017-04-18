        global  _byteswap
        section .text
_byteswap:
        mov     eax, [rdi]
        bswap   eax
        mov     [rdi], eax
        ret
