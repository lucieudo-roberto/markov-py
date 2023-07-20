
import re
import os

def __main__():
    file_list = os.popen('ls txt_inp/ | egrep .txt$').read().strip().split('\n')

    for file_nm in file_list:
        file_name = re.sub(r'.txt$','',file_nm)

        file_in = open(f'txt_inp/{file_name}.txt','r+')
        file_ot = open(f'txt_inp/{file_name}.txx','w')

        buff = file_in.read().lower().replace('\n','')
        file_ot.write(re.sub(r"[^a-z0-9áéíóúâêîôûàèìòùãõç]",' ',buff))

    os.popen('rm -rf txt_inp/*.txt')
    return True


__main__()

