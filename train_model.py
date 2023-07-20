
from tqdm import tqdm
import pickle 

def __main__():
    with open('txt_inp/compiled.mg','r') as file:
        dict_out = {}
        file_arr = file.read().strip().split(' ')
        size_arr = len(file_arr)-1
        dict_aux = {}
        prog_bar = tqdm(total=size_arr,desc='Analizing file')

        for word in file_arr:
            dict_aux[word] = dict_aux.get(word,0)+1
            prog_bar.update(1)
        
        prog_bar.close()
        
        total_words = len(dict_aux.keys())
        stats_progs = tqdm(total=total_words,desc="Training..")

        for idx in range(size_arr):
            lv1_word = file_arr[idx]
            tmp_dict = {}
            
            if dict_out.get(lv1_word,None) == None:
                for idy in range(size_arr):
                    lv2_word = file_arr[idy]
                    lv3_word = file_arr[idy+1] if idy+1 <= size_arr else None

                    if lv2_word == lv1_word and lv3_word != None:
                        tmp_dict[lv3_word] = tmp_dict.get(lv3_word,0)+1

                dict_out[lv1_word] = dict_out.get(lv1_word,tmp_dict)
                stats_progs.update(1)
        stats_progs.close()
        
        with open('txt_out/treined.dic','wb') as outfile:
            pickle.dump(dict_out,outfile)

        print('Ok, all right \n')
        
        return True

__main__()
