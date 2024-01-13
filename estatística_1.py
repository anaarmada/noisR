from math import sqrt,erfc
from matplotlib import pyplot as plt


def read_txt_file(file_path):
    try:
        with open(file_path,'r') as file:
            data = file.read().replace('\n','')
            return data.strip()
    except FileNotFoundError:
        return "File not found"

def convert_to_string(data):
    lines = data.split('\n')
    binary_string = ''.join(lines)
    return binary_string

teste = list(read_txt_file("seq1.txt"))
teste.reverse()

"""def integers(lst,max):
    current_integer=0
    i=0
    new=[]
    while len(lst)>i:
        if lst[i]=='1' and current_integer+2**i<=max:
            current_integer=current_integer+2**i
            i+=1
        elif lst[i]=='0':
            i+=1
        elif current_integer+2**i>max:
            new.append(current_integer)
            for j in range(0,i):
                lst.pop(0)
            i=0
            current_integer=0
    new.append(current_integer)
    return new"""

def integers(lst,new):
    current=0
    if len(lst)>=6:
        for i in range(0,6):
            if lst[i]=='0':
                current+=1
            else:
                current+=2**i
        new.append(current)
        return integers(lst[6:-1],new)
    else:
        for i in range(len(lst)):
            if lst[i]=='0':
                current+=1
            else:
                current+=2**i
        new.append(current)
        return new

int_list=integers(teste,[])

def  plot_histogram(int_list):
    plt.hist(int_list,bins=max(int_list)-min(int_list)+1,align='left',edgecolor='black')
    plt.xlabel('Integers')
    plt.title('Histogram of Integers')
    plt.grid(True)
    plt.show()

plot_histogram(int_list)