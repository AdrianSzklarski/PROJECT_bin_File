import numpy as np


class Convert:
    def __init__(self):
        self.linkTXT = r'/home/adrian/Pulpit/GitHub/BIN/txt/data.txt'
        self.link = r'/home/adrian/Pulpit/GitHub/BIN/bin/data.bin'
        self.link1 = r'/home/adrian/Pulpit/Marek/Droga/Test27092023/APM/LOGS/00000001.BIN'

        # self.get_txt_to_bin()
        self.get_read_binary()

    def get_txt_to_bin(self):
        '''Convert txt to bin file
        Method used if you have a txt file'''
        with open(self.linkTXT, 'r') as f:
            string = f.read()
            string = string.split()

            stringtab = []
            for x in range(0, len(string)):
                stringtab.append([string[x]])

            with open(self.link, 'w') as fbin:
                for i in stringtab:
                    for j in i:
                        p = j + '\n'
                        for k in p:
                            binstring = format(ord(k), 'b').encode()
                            decstring = format(ord(k)).encode()
                            resume = str(binstring)
                            fbin.write(resume + '\n')

    def get_read_binary(self):
        # Opening the binary file in binary mode as rb(read binary)
        with open(self.link, mode='rb') as f:
            data = str(f.read())
            clear_data = data.replace('"', '').replace(data[0], '')


        tab = []
        clear_tab = []
        indices = []
        [tab.append(i) for i in clear_data]
        [clear_tab.append(tab[j]) for j in range(0, len(tab), 1) if tab[j] != "n" and tab[j] != "\\"]
        del clear_tab[0]
        del clear_tab[-1]
        [indices.append(i) for i in range(len(clear_tab)) if clear_tab[i] == "'"]

        # print(clear_tab)
        # print(indices)

        step = len(clear_tab[:indices[0]])
        next_step = step+1
        slice = indices[1::2]
        numbers = []
        n = []

        for k in range(0, len(indices)):
            if k <= step-1:
                first = clear_tab[k]
                n.append(first)
                a = ''.join(n)
            elif k > next_step and slice:
                self.div = []
                self.number = []
                for d in range(0, len(slice)-1):
                    di = slice[d+1] - slice[d] - 2
                    self.div.append(di)

        for k in self.div:
            for e in (range(1, k+1, 1)):
                numbers.append(e)

        print(numbers)
        print(slice)

        repeated_indexes = []
        pos = 0
        for item in numbers:
            if item == 1:
                index = numbers.index(item, pos)
                repeated_indexes.append(index)
            pos += 1

        print(len(numbers))
        print(repeated_indexes)

        for el in repeated_indexes[1:]:
            scope = numbers[:el]
            if el > repeated_indexes[0]:
                pass

        # continued: cleaning arrays, adding values....


if __name__ == '__main__':
    app = Convert()
    print(app)
