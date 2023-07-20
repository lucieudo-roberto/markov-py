
import os

def __main__():
    file_list = os.popen('ls txt_inp/ | egrep .txx$').read().strip().split('\n')
    file_vect = []

    if len(file_list) > 0:
        for file in file_list:
            with open(f'txt_inp/{file}','r') as file_data:
                file_vect.append(file_data.read().replace('\n',''))

        with open('txt_inp/compiled.mg','a') as file_out:
            file_out.write(str(file_vect).strip())

        print(f"Totoal files merged: {len(file_list)}")
        return True
    return False


__main__()
