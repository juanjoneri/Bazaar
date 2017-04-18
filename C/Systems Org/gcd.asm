        global  _gcd
        section .text
_gcd:
        cmp     rsi, 0
        jne     L1
        mov     rax, rdi
        ret
L1:
        mov     rax, rdi
        xor     rdx, rdx
        div     rsi
        mov     rdi, rsi
        mov     rsi, rdx
        call    _gcd
        ret
