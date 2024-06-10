oper = ['add', 'and', 'or', 'xor', 'nor', 'sub', 'slt', 'sll', 'srl', 'sra', 'addi', 'andi', 'ori', 'xori', 'lui', 'beq', 'bne', 'lw', 'sw']
opcodes = ['000000', '000000', '000000', '000000', '000000', '000000', '000000', '000000', '000000', '000000', '001000', '001100', '001101', '001110', '001111', '000100', '000101', '100011', '101011']
funct = ['100000', '100100', '100101', '100110', '100111', '100010', '101010', '000000', '000010', '000011', '000000', '000000', '000000', '000000', '000000', '000000', '000000', '000000', '000000']

with open('codigo-entrada.txt', 'r') as input:
    entrada_ini = input.readlines()

li_ini = []

for linha in range(len(entrada_ini)):
    entrada = entrada_ini[linha]
    entrada = entrada.lower().split()
    li = []

    for i in range(0, 19):
        if (oper[i] == entrada[0]):
            li.append(opcodes[i])
            li.append(funct[i])
            break

    if (li[0] == '000000'):
        if(li[1] == '000000' or li[1] == '000010' or li[1] == '000011'):
            opcode = li[0]
            rd = entrada[1]
            rd = int(rd[1:])
            rd = str(f'{rd:05b}')
            rs = '00000'
            rt = entrada[2]
            rt = int(rt[1:])
            rt = str(f'{rt:05b}')
            sa = int(entrada[3])
            sa = str(f'{sa:05b}')
            fun = li[1]
            codigo = opcode+rs+rt+rd+sa+fun
            codigo = format(int(codigo, 2), '08X')
            li_ini.append(codigo)
            #print(codigo)
        else:
            opcode = li[0]
            rd = entrada[1]
            rd = int(rd[1:])
            rd = str(f'{rd:05b}')
            rs = entrada[2]
            rs = int(rs[1:])
            rs = str(f'{rs:05b}')
            rt = entrada[3]
            rt = int(rt[1:])
            rt = str(f'{rt:05b}')
            sa = '00000'
            fun = li[1]
            codigo = opcode+rs+rt+rd+sa+fun
            codigo = format(int(codigo, 2), '08X')
            li_ini.append(codigo)
            #print(codigo)
    elif (li[0] == '001111'):
        opcode = li[0]
        rt = entrada[1]
        rt = int(rt[1:])
        rt = str(f'{rt:05b}')
        rs = '00000'
        imm = entrada[2]
        if (imm[:2] == '0x'):
            if (int(imm[2:]) < 0):
                imm = int(imm[2:], 16)
                imm = str(f'{imm:016b}')
                imm = imm.replace('-', '0')
                posicao = imm.find('1')
                imm_pt1 = imm[:posicao]
                imm_pt1 = imm_pt1.replace('0', '1')
                imm_pt2 = imm[posicao:]
                imm = imm_pt1 + imm_pt2
            else:
                imm = int(imm[2:], 16)
                imm = str(f'{imm:016b}') 
        else:        
            if (int(entrada[2]) < 0):
                imm = int(entrada[2])
                imm = str(f'{imm:016b}')
                imm = imm.replace('-', '0')
                posicao = imm.find('1')
                imm_pt1 = imm[:posicao]
                imm_pt1 = imm_pt1.replace('0', '1')
                imm_pt2 = imm[posicao:]
                imm = imm_pt1 + imm_pt2
            else:
                imm = int(entrada[2])
                imm = str(f'{imm:016b}')
        codigo = opcode+rs+rt+imm
        codigo = format(int(codigo, 2), '08X')
        li_ini.append(codigo)
        #print(codigo)
    else:
        opcode = li[0]
        rt = entrada[1]
        rt = int(rt[1:])
        rt = str(f'{rt:05b}')
        rs = entrada[2]
        rs = int(rs[1:])
        rs = str(f'{rs:05b}')
        imm = entrada[3]
        if (imm[:2] == '0x'):
            if (int(imm[2:]) < 0):
                imm = int(imm[2:], 16)
                imm = str(f'{imm:016b}')
                imm = imm.replace('-', '0')
                posicao = imm.find('1')
                imm_pt1 = imm[:posicao]
                imm_pt1 = imm_pt1.replace('0', '1')
                imm_pt2 = imm[posicao:]
                imm = imm_pt1 + imm_pt2
            else:    
                imm = int(imm[2:], 16)
                imm = str(f'{imm:016b}')
        else:
            if (int(entrada[3]) < 0):
                imm = int(entrada[3])
                imm = str(f'{imm:016b}')
                imm = imm.replace('-', '0')
                posicao = imm.find('1')
                imm_pt1 = imm[:posicao]
                imm_pt1 = imm_pt1.replace('0', '1')
                imm_pt2 = imm[posicao:]
                imm = imm_pt1 + imm_pt2
            else:    
                imm = int(entrada[3])
                imm = str(f'{imm:016b}')
        codigo = opcode+rs+rt+imm
        codigo = format(int(codigo, 2), '08X')
        li_ini.append(codigo)
        #print(codigo)

print(li_ini)

with open('codigo-saida.txt', 'w') as output1:
    output1.write('v2.0 raw\n')

for a in range(len(li_ini)):
    with open('codigo-saida.txt', 'a') as output2:
        output2.write('{}\n'.format(li_ini[a]))


