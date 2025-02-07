section .data
    hello_message db 'Hello, World!',0   ; Null-terminated string

section .text
    global _start

_start:
    ; sys_write (syscall number 1)
    ; File descriptor 1 (stdout), message address, message length
    mov eax, 4          ; sys_write system call number
    mov ebx, 1          ; File descriptor 1 (stdout)
    mov ecx, hello_message ; Address of the string
    mov edx, 13         ; Length of the string
    int 0x80            ; Call kernel

    ; sys_exit (syscall number 1)
    mov eax, 1          ; sys_exit system call number
    xor ebx, ebx        ; Return code 0
    int 0x80            ; Call kernel

