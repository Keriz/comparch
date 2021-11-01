.text
    lui $s0, 0x1000 # data memory: 0x10000000
    lw $s1, ($s0)
    lw $s1, ($s0)
    
    addiu $v0, $0, 10
    syscall