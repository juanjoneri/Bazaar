	.file	"multiplication_table.c"
	.option nopic
	.section	.rodata
	.align	3
.LC0:
	.string	"Enter an integer: "
	.align	3
.LC1:
	.string	"%d"
	.align	3
.LC2:
	.string	"%d * %d = %d \n"
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
	add	a5,s0,-24
	mv	a1,a5
	lui	a5,%hi(.LC1)
	add	a0,a5,%lo(.LC1)
	call	scanf
	li	a5,1
	sw	a5,-20(s0)
	j	.L2
.L3:
	lw	a1,-24(s0)
	lw	a4,-24(s0)
	lw	a5,-20(s0)
	mulw	a5,a4,a5
	mv	a3,a5
	lw	a2,-20(s0)
	lui	a5,%hi(.LC2)
	add	a0,a5,%lo(.LC2)
	call	printf
	lw	a5,-20(s0)
	addw	a5,a5,1
	sw	a5,-20(s0)
.L2:
	lw	a4,-20(s0)
	li	a5,10
	ble	a4,a5,.L3
	li	a5,0
	mv	a0,a5
	ld	ra,24(sp)
	ld	s0,16(sp)
	add	sp,sp,32
	jr	ra
	.size	main, .-main
	.ident	"GCC: (GNU) 6.1.0"
