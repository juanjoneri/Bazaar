    .file       "hello.c"
    .option      nopic
    .section    .rodata
    .align       3
.LC0:
    .string     "Hello world!"
    .text
    .align      2
    .globl      main
    .type       main, @function
main:
    add         sp,sp,-16
    sd          ra,8(sp)
    sd          s0,0(sp)
    add         s0,sp,16
    lui         a5,%hi(.LC0)
    add         a0,a5,%lo(.LC0)
    call        puts
    li          a5,0
    mv          a0,a5
    ld          ra,8(sp)
    ld          s0,0(sp)
    add         sp,sp,16
    jr          ra
    .size       main, .-main
    .ident      "GCC: (GNU) 6.1.0"
