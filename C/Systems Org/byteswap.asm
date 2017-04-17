; Implementation of
;
;   void byteswap(uint32_t *x);
;
; A pointer to an 32-bit integer is passed in and the bytes are swapped
; dirextly in memory.

        global  _byteswap
        section .text
_byteswap:
        mov     eax, [rdi]
        bswap   eax
        mov     [rdi], eax
        ret
