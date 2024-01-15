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

def integers(lst,new):
    current=0
    if len(lst)>=6:
        curr_lst=lst[0:6]
        curr_lst.reverse()
        for i in range(0,6):
            if curr_lst[i]!='0':
                current+=2**i
        new.append(current)
        return integers(lst[6:-1],new)    
    return new

int_list=integers(teste,[])

def  plot_histogram(int_list):
    plt.hist(int_list,bins=max(int_list)-min(int_list)+1,align='left',edgecolor='black')
    plt.xlabel('Integers')
    plt.title('Histogram of Integers')
    plt.grid(True)
    plt.show()

plot_histogram(int_list)