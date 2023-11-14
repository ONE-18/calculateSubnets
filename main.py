import os
import time

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

def Is_dec(str):
    str = str.split('.')
    if len(str[0]) == 3:
        return 10
    elif len(str[0]) == 8:
        return 2
    else:
        return 0

def normalize(str):
    num = str.split('.')
    for i in range(len(num)):
        num[i] = num[i].zfill(8)
    return '.'.join(num)

def tratar(file_path):
    os.system('cls' if os.name == 'nt' else 'clear')
    save = ''
    with open(file_path, 'r') as file:
        content = file.read().split('\n')
        lines = []
        for line in content:
            if line != '': lines.append(line)
        for line in lines:
            line = ''.join(line.split()).split('-')
            tipo = Is_dec(line[0])
            out = ''
            if tipo == 10:
                ip_trs = read_ip10(line[0])
                out = '{:>16}\t-\t {:<35}'.format(line[0], ip_trs)
            elif tipo == 2:
                line[0] = normalize(line[0])
                ip_trs = read_ip2(line[0])
                out = '{:<35} \t-\t{:>16}'.format(line[0], ip_trs)
            elif tipo == 0:
                print('Error 0')
            else:
                print('Error -1')
            
            if tipo > 0:
                save += out + '\n'
                print(out)
    save = save[:-1]
    write_file(file_path, save)

def watch_file(file_path):
    last_modified_time = os.path.getmtime(file_path)
    try:
        while True:
            time.sleep(1)
            current_modified_time = os.path.getmtime(file_path)
            tratar(file_path)
            if current_modified_time != last_modified_time:
                last_modified_time = current_modified_time
                tratar(file_path)
    except KeyboardInterrupt:
        print('Stopped watching the file')
        
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    file_path = 'file.txt'
    watch_file(file_path)