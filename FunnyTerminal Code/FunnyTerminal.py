import math
import time
import threading
import os
import logging
Key = input('boot:')
if Key == 'quash':
    exit()
else:
    pass
funny = 0x512c00
print('Booting...')
def disk():
        f = 0x7c00
        for i in range(funny):
                f = f + 0x1
                h = hex(f)
        print(h)
        logging.basicConfig(filename=os.path.join(os.getcwd(),'run.log'),level=logging.DEBUG)
        logging.debug('run')
disk()
print('')
print('       ################################')
print('       #  >>>                         #')
print('       #     >>>                      #')
print('       #  >>>   ____                  #')
print('       #                              #')
print('       #                              #')
print('       #                              #')
print('       ################################')
print('')
print('FunnyTerminal 2022.')
print('Copyright <c> Li Yangshuo.')
print('')
class Cheese:
    def OS_ONE():
        pyos = '<funny>'
        mk = '>'
        ef = 'File: '
        eef = '*: '
        kt = input(pyos)
        if kt == 'ps':
            os.system('tasklist')
        if kt == ('delps'):
            ps = input('taskkill /im XXX: ')
            os.system(ps)
        if kt == 'wrdir':
            tk = input('File: ')
            wr = input('> ')
            kt0 = open(tk,'w+')
            kt0.write(wr)
        if kt[0:5] == 'mkdir':
            so = input(mk)
            os.mkdir(so)
        if kt == '':
            Cheese.OS_ONE()
        if kt == 'reboot':
            print('Rebooting...')
            for i in range (255):
                Cheese.OS_ONE()
        if kt == 'dir':
            ls = os.listdir()
            print(ls)
        if kt == kt:
            print(Cheese())
        if kt == 'egg':
            while True:
                print(8192**8192)
        if kt == 'rename':
            r = input(ef)
            n = input(eef)
            os.rename(r,n)
        if kt == 'exit':
                exit()
        if kt == 'square':
                    tt = input('square root: ')
                    yy = int(tt)
                    pp = math.sqrt(yy)
                    print(pp)
        if kt == 'main':
            print('Main Model...')
            def target(sleep):
                time.sleep(sleep)
                print('Main:',threading.current_thread().name,'sleep:',sleep)
            if __name__=='__main__':
                t1 = threading.Thread(name='t1',target=target,args=(1,))
                t2 = threading.Thread(name='t1',target=target,args=(2,))
                t3 = threading.Thread(name='t1',target=target,args=(3,))
                t4 = threading.Thread(name='t1',target=target,args=(4,))
                t5 = threading.Thread(name='t1',target=target,args=(5,))
                t6 = threading.Thread(name='t1',target=target,args=(6,))
                t7 = threading.Thread(name='t1',target=target,args=(7,))
                t8 = threading.Thread(name='t1',target=target,args=(8,))
                t1.start()
                t2.start()
                t3.start()
                t4.start()
                t5.start()
                t6.start()
                t7.start()
                t8.start()
        if kt == ('B5C835E9-E1B6-6A50-E8BB-7F632355451A'):
            ct = open('Copyright.txt','w+')
            ct.write('LiYangshuo show Copyright----Key:B5C835E9-E1B6-6A50-E8BB-7F632355451A')
            print('原作者:李阳硕')
            print('您已经获得原作者的同意,可以进行任何有关版权操作,但在操作时必须标注原作者姓名,已在本程序所在文件夹内创建证件')
        if kt == 'ntoff':
            os.system('shutdown -s -t 0')
        if kt == 'version':
            print('FunnyTerminal 2022 on windows.')
while True:
    Cheese.OS_ONE()