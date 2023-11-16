import math
import os
from datetime import datetime

output = ''

ip = ''
Mask = ''
subMask = ''

def imprimir(str):
    global output
    output += str + '\n'
    print(str)

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

def maskDec(mask):
    return mask.count('1')

def points(str):
    ret = ''
    n = str.count('.')
    if n == 0:
        segmentos = [str[i:i+8] for i in range(0, len(str), 8)]
        ret = '.'.join(segmentos)
    else:
        ret = str.replace('.', '')
    return ret

def sumBin(b1, b2):
    ret = ''
    acarreo = 0
    
    for bit1, bit2 in zip(reversed(b1), reversed(b2)):
        suma_bits = int(bit1) + int(bit2) + acarreo
        resultado_bit = suma_bits % 2
        acarreo = suma_bits // 2
        # Agregar el bit al principio del resultado
        ret = str(resultado_bit) + ret
    
    if acarreo == 1:
        return -1
    else:
        return ret

def sumAt(b, n):
    sumando = '0'*(n-1) + '1' + '0'*(32-n)
    return sumBin(points(b), sumando)

def invrsMask(n):
    ret = '0'*n + '1'*(32-n)
    return ret
    
def getBroad(b, n):
    mascara = invrsMask(n)
    sumando = sumBin(points(b), mascara)
    return sumando

def getPrimera(b):
    return str(sumAt(b, 32))
    
def dobleIP(b):
    return '{:^35} \t-{:^35}'.format(b, read_ip2(b))

def subNet():
    global ip, Mask
    
    IPb = read_ip10(ip)
    MaskBin = mascarar(int(Mask))
        
    imprimir('{:<30}{}/{}'.format('\nIP red:', dobleIP(IPb),Mask))
    imprimir('{:<30}{}'.format('Mascara red:', dobleIP(MaskBin)))
    
    getIPs(IPb, MaskBin)
    
    newIP = sumAt(IPb, maskDec(MaskBin))
    ip = read_ip2(points(newIP))
    Mask = input('\nMascara de subred: ')
        
def getIPs(ip, mask):
    broad = points(getBroad(ip, maskDec(mask)))
    imprimir('{:<30}{}'.format('\tIP Broadcast:', dobleIP(broad)))
    
    primera = points(getPrimera(ip))
    imprimir('{:<30}{}'.format('\tPrimera IP:', dobleIP(primera)))
    
    ultima = broad[:-1] + '0'
    imprimir('{:<30}{}'.format('\tUltima IP:', dobleIP(ultima)))

def calcSubMasks(nSubRedes):
    ret = []
    for i in range(len(nSubRedes)):
        nDisp = nSubRedes[i]+2
        ret.append(32-math.ceil(math.log2(nDisp)))
    return ret
        

def readTxt():
    global ip, Mask
    try:
        nSubRedes = []
        with open('input.txt', "r") as archivo:
            content = archivo.read().split('\n')
            for i in range(len(content)):
                if i == 0:
                    if content[i].count('/') == 1:
                        line = content[i].split('/')
                        ip = line[0]
                        Mask = line[1]
                    else:
                        print('Error en la primera linea del archivo')
                        exit()
                else:
                    nSubRedes.append(content[i])
            nSubRedes = list(map(int,nSubRedes))
            nSubRedes.sort(reverse=True)
            imprimir('IP inicial: ' + ip)
            imprimir('Mascara: ' + Mask)
            imprimir('Numero de subredes: ' + str(len(nSubRedes)))
            nDisp = sum([i+2 for i in nSubRedes])
            imprimir('Numero de dispositivos totales: ' + str(nDisp))
            if(nDisp > 2**(32-int(Mask))):
                imprimir('Error, demasiados dispositivos para esta mascara')
                exit()
            else:
                subMasks = calcSubMasks(nSubRedes)
                for mask in subMasks:
                    IPb = read_ip10(ip)
                    MaskBin = mascarar(int(mask))
                        
                    imprimir('{:<30}{}/{}'.format('\nIP red:', dobleIP(IPb), mask))
                    imprimir('{:<30}{}'.format('Mascara red:', dobleIP(MaskBin)))
                    
                    getIPs(IPb, MaskBin)
                    
                    newIP = sumAt(IPb, maskDec(MaskBin))
                    ip = read_ip2(points(newIP))
    except FileNotFoundError:
        imprimir('No se encontro el archivo')
        with open('input.txt', "w") as archivo:
            archivo.write('')
        exit()
    
if __name__ == "__main__":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        leerTxt = input('Leer de archivo? (y/n): ')
        if leerTxt == 'y':
            readTxt()
        else:
            if ip == '':
                ip = input('IP inicial: ')
            if Mask == '':
                Mask = input('Mascara primera subred: ')
                IPred = read_ip10(ip)
                mascaraRed = mascarar(int(Mask))
                while True:
                    subNet()
    except KeyboardInterrupt:
        imprimir('\nStopped by user')
    
    fecha_hora_actual = datetime.now()
    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d_%H.%M.%S")
    with open('salida_'+cadena_fecha_hora+'.txt', "w") as archivo:
        archivo.write(output)