#!/usr/bin/env python
# -*- coding: utf-8 -*-

IP = input ('Введите ip адрес: ')
IP = IP.replace('.' , ' ').replace('/', ' ').split() #Избавляемся от символов вида . и /, с помощью сплит разделям октеты и маску на разные аргументы
a,b,c,d,e = IP
a,b,c,d,e = int(a), int(b), int(c), int(d), int(e)

Network = '''Network: 
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:08b} {1:08b} {2:08b} {3:08b} '''

x = '1' * e + '0' * (32 - e)  #Страница учебника 257


print(Network.format(a, b, c, d, e))
print("Mask:\n/{}".format(e))
print((int(x[0:8], 2)), (int(x[8:16], 2)), (int(x[16:24], 2)), (int(x[24::], 2)))
print((x[0:8]), (x[8:16]), (x[16:24]), (x[24::]))

