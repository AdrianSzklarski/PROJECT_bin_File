''' Convert *.*bin file
@AdrianSzklarski, 10.2023'''

import os

class Convert:

    def __init__(self):
        self.help_doc = """Program operation: - Adding a text file to the txt directory.
                        The program converts the contents to *.*bin and displays in the terminal - 
                        You can directly upload *.*bin file o display it in the terminal"""

        self.linkTXT = r'/home/adrian/Pulpit/GitHub/BIN/txt/data.txt'
        self.link = r'/home/adrian/Pulpit/GitHub/BIN/bin/data.bin'
        self.txt_dir = os.path.dirname(self.linkTXT)
        self.bin_dir = os.path.dirname(self.link)

        self.get_txt_to_bin()
        self.get_read_binary()

    def get_txt_to_bin(self):
        '''Convert txt to bin file
        Method used if you have a txt file'''
        with open(self.txt_dir + '/data.txt', 'r') as f:
            read_txt_file = f.read()
            read_txt_file = read_txt_file.split()

            text_in_the_table = []
            for x in range(0, len(read_txt_file)):
                text_in_the_table.append([read_txt_file[x]])

            with open(self.bin_dir + '/data.bin', 'w') as fbin:
                for iteration_txt in text_in_the_table:
                    for j in iteration_txt:
                        p = j + '\n'
                        for k in p:
                            binstring = format(ord(k), 'b').encode()  # bin
                            decstring = format(ord(k)).encode()  # hex
                            resume = str(binstring)
                            fbin.write(resume + '\n')

    def get_read_binary(self):
        '''Convert bin to text in the terminal'''

        # Opening the binary file in binary mode as rb(read binary)
        with open(self.bin_dir + '/data.bin', mode='rb') as f:
            data = str(f.read())
            clear_data = data.replace('"', '').replace(data[0], '')

        arrays = [[], [], []]

        # arrays[0]: array, arrays[1]: clear array, arrays[2]: indices

        #  Clearing a file of newline and quotation marks
        [arrays[0].append(i) for i in clear_data]
        [arrays[1].append(arrays[0][j]) for j in range(0, len(arrays[0]), 1)
        if arrays[0][j] != "n" and arrays[0][j] != "\\"]
        del arrays[1][0]
        del arrays[1][-1]
        [arrays[2].append(i) for i in range(len(arrays[1])) if arrays[1][i] == "'"]

        word = ''.join(arrays[1]).replace("''", "\n")
        text = "".join(chr(int(s, 2)) for s in word.split())

        return text

    def __str__(self):
        return f'Your text:\n {self.get_read_binary()}'


