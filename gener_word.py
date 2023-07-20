
import pickle
import random
import sys

def __main__(init_word,randomic):
    dict_file = open('txt_out/treined.dic','rb')
    word_dict = pickle.load(dict_file)
    words = word_dict.get(init_word,None)

    if words != None:
        if randomic:
            return random.choice([x for x in words.keys()])

        pword_str = ' '
        pword_int =  -1
        wword_int =  sum(words.values())

        for key,val in words.items():
            if len(key) > 0:
                probability = (val/wword_int)
                if probability >= pword_int:
                    pword_int = probability
                    pword_str = key
        return pword_str

    return ''


def __start():
   
    if len(sys.argv) <= 3:
        print(f'Usage: \033[31m {sys.argv[0]} \033[32m word \033[33m text-len \033[0m random (s/n) \n')
        return False

    word = sys.argv[1]
    limt = sys.argv[2]
    rand = False if sys.argv[3].lower() == 'n' else True

    outp = []

    for x in range(int(limt)):
        word = __main__(word,rand)
        outp.append(word)

    print(f'{sys.argv[1]} ', ' '.join(str(x) for x in outp ))
    return True


__start()
