        global   _power_of_difference
        extern   _pow
        section  .text

_power_of_difference:
        push     rbp
        subsd    xmm0, xmm1
        cvtsi2sd xmm1, edi
        call     _pow
        pop      rbp
        ret
