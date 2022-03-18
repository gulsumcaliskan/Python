"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir.

Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""

flatten_list = []

def flatten(l):
    for i in l:
        if type(i) == list:
            flatten(i)
        else:
            flatten_list.append(i)

flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(flatten_list)


"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon 
yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların 
elemanlarını da tersine döndürün. 

Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]

"""

list = [[1, 2], [3, 4], [5, 6, 7]]
 
a = list.reverse()

for l in list:
    l.reverse()

print(list)