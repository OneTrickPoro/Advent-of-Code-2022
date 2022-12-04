import pyxel
from time import sleep
from string import ascii_letters

def import_data1():
    with open('advent2022/3/3.txt', 'r') as f:
        data = f.readlines()
    data_ez = [i.strip() for i in data]
    res = [[b[:len(b)//2],b[len(b)//2:]] for b in data_ez]
    return res

def val_obj(char):
    return ascii_letters.index(char)+1

data = import_data1()

class App():
    def __init__(self):
        pyxel.init(150,100,'Advent of Code 2022 - Day 3', fps=20)
        sleep(0.8)
        self.data = data
        self.count_word = 0
        self.count_letter = 0
        self.word_end = False
        self.lampeggia = False
        self.s = ''
        self.s1 = ''
        self.s2 = ''
        self.char = ''
        self.val = 0
        self.total = 0
        self.rect = False
        self.rect_done = False
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.count_word+1 == len(self.data):
            self.rect = True
            self.count_word = len(self.data)-1
        elif self.word_end:
            sleep(0.5)
            self.lampeggia = False
            self.s = ''
            self.s1 = ''
            self.s2 = ''
            self.count_letter = 0
            self.count_word += 1
            self.word_end = False
        elif self.lampeggia:
            self.char = list(set(self.data[self.count_word][0]) & set(self.data[self.count_word][1]))[0]
            for i in self.data[self.count_word][0]:
                if i == self.char:
                    self.s1 += str(self.char)
                else:
                    self.s1 += ' '
            for i in self.data[self.count_word][1]:
                if i == self.char:
                    self.s2 += str(self.char)
                else:
                   self.s2 += ' '
            if self.char in ascii_letters[0: len(ascii_letters)//2]:
                for i in ascii_letters[0: len(ascii_letters)//2]:
                    if i == self.char:
                        self.s += str(self.char)
                    else:
                        self.s += ' '
            if self.char in ascii_letters[len(ascii_letters)//2:]:
                for i in ascii_letters[len(ascii_letters)//2:]:
                    if i == self.char:
                        self.s += str(self.char)
                    else:
                        self.s += ' '
            self.val = val_obj(self.char)
            self.total += self.val
            self.word_end  = True
        elif self.count_letter == len(self.data[self.count_word][0]):
            self.lampeggia = True
        elif not self.word_end:
            self.count_letter += 1
        
    def draw(self):
        pyxel.cls(6)
        pyxel.text(20, 10,'Rucksacks number: ', 0)
        pyxel.text(110, 10, str(self.count_word+1), 8)
        pyxel.text(20, 65, ascii_letters[0: len(ascii_letters)//2], 0)
        pyxel.text(20, 75, ascii_letters[len(ascii_letters)//2:], 0)
        pyxel.text(50, 55, 'Value: ', 3)
        pyxel.text(50, 90, 'Total: ', 3)
        pyxel.text(90, 55, '+'+str(self.val), 8)
        pyxel.text(90, 90, str(self.total), 8)
        pyxel.text(20, 30, self.data[self.count_word][0][:self.count_letter], 0)
        pyxel.text(20, 40, self.data[self.count_word][1][:self.count_letter], 0)
        if self.lampeggia:
            pyxel.text(20, 30, self.data[self.count_word][0], 0)
            pyxel.text(20, 40, self.data[self.count_word][1], 0)
            pyxel.text(20, 30, self.s1, 8)
            pyxel.text(20, 40, self.s2, 8)
            if self.char in ascii_letters[0: len(ascii_letters)//2]:
                pyxel.text(20, 65, self.s, 8)
            if self.char in ascii_letters[len(ascii_letters)//2:]:
                pyxel.text(20, 75, self.s, 8)
        if self.rect_done:
            sleep(10)
            quit()
        if self.rect:
            pyxel.rectb(78, 88, 35 , 10 , 8)
            self.rect_done = True 
           
App()