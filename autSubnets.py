import os

sig = True

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].zfill(8)
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return str(decimal)

def read_ip10(str):
    str = str.split('.')
    ip = []
    ret = ''
    for i in str:
        ip.append(decimal_to_binary(int(i)))
    for i in ip:
        ret += i + '.'
    return ret[:-1]

def read_ip2(str):
    str = str.split('.')
    ip = []
    retur = ''
    for i in str:
        ip.append(binary_to_decimal(i))
    for i in ip:
        retur += i + '.'
    return retur[:-1]

def mascarar(dec):
    ret = ''
    for i in range(32):
        if i < dec:
            ret += '1'
        else:
            ret += '0'
        if i % 8 == 7:
            ret += '.'
    return ret[:-1]

def invrsMask(str):
    return str.count('1')

def points(str):
    ret = ''
    n = str.count('.')
    if n == 0:
        segmentos = [str[i:i+8] for i in range(0, len(str), 8)]
        ret = '.'.join(segmentos)
    else:
        ret = str.replace('.', '')
    return ret

def sumAt(b, n):
    sumando = '0'*n + '1' + '0'*(31-n)
    
    ret = ''
    accarreo = 0
    
    for bit1, bit2 in zip(reversed(b), reversed(sumando)):
        suma_bits = int(bit1) + int(bit2) + acarreo
        resultado_bit = suma_bits % 2
        acarreo = suma_bits // 2

        # Agregar el bit al principio del resultado
        resultado = str(resultado_bit) + resultado
    
    if accarreo == 1:
        return -1
    else:
        return ret

def subNet(IPinicial, MaskInicial):
    binIP = bin(int(points(IPinicial),2))[2:]
    binMaskIni = bin(int(points(MaskInicial),2))[2:]
    
    mask = input('Mascara de subred: ')
    binMask = bin(int(points(mascarar(int(mask))),2))[2:]
    
    print(sumAt(binIP, invrsMask(MaskInicial)))
    
    
    
    
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    firstIP = '210.16.0.0'
    primeraMask = '21'
    if firstIP == '':
        firstIP = input('IP general: ')
    if primeraMask == '':
        primeraMask = input('Mascara general: ')
    try:
        while sig:
            firstIPb = read_ip10(firstIP)
            primeraMaskb = mascarar(int(primeraMask))
            subNet(firstIPb, primeraMaskb)
    except KeyboardInterrupt:
        print('Stopped by user')