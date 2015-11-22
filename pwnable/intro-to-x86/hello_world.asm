; for use on mac syscalls are located @ 
; /usr/include/sys/syscalls.h
; nasm -f macho32 hello\ world.asm;
; ld -o hello hello\ world.o;
; ./hello hello world

BITS 32 ;use 32 bit code

section .text ;section declaration

global start

start:

;Write Prototype: 
;write(int fildes, const void *buf, size_t nbyte);
message_on_stack:
	push	dword 0xa
	push	dword '!'
	push	dword 'orld'
	push	dword 'o, W'
	push	dword 'Hell'
	push	esp

write_message:
	push	dword 17
	push	dword [esp+4]
	push	dword 1
	mov		eax, 4
	sub		esp, 4
	int		0x80
	
exit:
	xor 	ebx, ebx
	mov		eax, 1
	int		0x80

section .data

msg: db "Hello World!", 0xa
.len: equ $ - msg