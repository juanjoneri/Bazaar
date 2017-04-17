; Implementation of
;
;   double power_of_difference(double x, double y, int32_t b);
;
; Returns (x - y) ** b

        global   _power_of_difference
        extern   _pow
        section  .text

_power_of_difference:
        push     rbp                    ; for 16-byte stack alignment
        subsd    xmm0, xmm1             ; x - y
        cvtsi2sd xmm1, edi              ; b is now a double
        call     _pow                   ; result in xmm0
        pop      rbp
        ret
