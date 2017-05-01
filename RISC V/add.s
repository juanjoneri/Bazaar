	.file	"add.c"
	.option nopic
	.section	.rodata
	.align	3
.LC0:
	.string	"Enter two integers: "
	.align	3
.LC1:
	.string	"%d %d"
	.align	3
.LC2:
	.string	"%d + %d = %d"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	add	sp,sp,-32
	sd	ra,24(sp)
	sd	s0,16(sp)
	add	s0,sp,32
	lui	a5,%hi(.LC0)
	add	a0,a5,%lo(.LC0)
	call	printf
	add	a4,s0,-28
	add	a5,s0,-24
	mv	a2,a4
	mv	a1,a5
	lui	a5,%hi(.LC1)
	add	a0,a5,%lo(.LC1)
	call	scanf
	lw	a4,-24(s0)
	lw	a5,-28(s0)
	addw	a5,a4,a5
	sw	a5,-20(s0)
	lw	a5,-24(s0)
	lw	a4,-28(s0)
	lw	a3,-20(s0)
	mv	a2,a4
	mv	a1,a5
	lui	a5,%hi(.LC2)
	add	a0,a5,%lo(.LC2)
	call	printf
	li	a5,0
	mv	a0,a5
	ld	ra,24(sp)
	ld	s0,16(sp)
	add	sp,sp,32
	jr	ra
	.size	main, .-main
	.ident	"GCC: (GNU) 6.1.0"
