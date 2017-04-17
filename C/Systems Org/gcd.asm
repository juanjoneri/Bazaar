; Recursive implementation of
;
;   uint64_t gcd(uint64_t x, uint64_t y) {
;     return (y == 0) ? x : gcd(y, x mod y);
;   }
;
; On entry, x in rdi and y in rsi. Return value in rax, as per convention.

        global  _gcd
        section .text
_gcd:
        cmp     rsi, 0                  ; y == 0?
        jne     L1                      ; if not, go do work
        mov     rax, rdi                ; otherwise, just return x
        ret
L1:
        mov     rax, rdi
        xor     rdx, rdx                ; rdx:rax <- x
        div     rsi                     ; rdx <- remainder
        mov     rdi, rsi                ; y
        mov     rsi, rdx                ; x % y
        call    _gcd                    ; gcd(y, x % y)
        ret
