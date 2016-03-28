#!/usr/bin/python
# -*- coding: utf-8 -*-

import chardet
import Tkinter
from Tkinter import Label
from Tkinter import Tk
from Tkinter import X
from tkFileDialog import askopenfilename
import os


def open_file():
    try:
        filename = askopenfilename()
        f = open(filename, 'r').read()
    except UnicodeDecodeError:
        print "can't open this file"
    else:
        try:
            encoding = chardet.detect(f)
            print encoding
        except UnicodeDecodeError:
            print('can\'t detect encoding')
        else:
            if encoding['encoding'] == 'ascii':
                print 'Encoding is: ascii'
            elif encoding['encoding'] == 'windows-1251':
                res.configure(text="Encoding is: windows-1251", fg="blue")
            elif encoding['encoding'] == 'utf-8':
                res.configure(text="Encoding is: utf-8", fg="blue")
            elif encoding['encoding'] == 'None':
                res.configure(text="Encoding is: None", fg="blue")
            else:
                res.configure(text='Encoding can\'t be detected', fg="blue")
                print 'Encoding can\'t be detected'


def convert_from_windows_1251():
    filename = askopenfilename()
    try:
        f = open(filename, 'r').read()
    except UnicodeDecodeError:
        print "it was not a windows-1251 unicode"
    else:
        try:
            unicode_text = f.decode('cp1251')
        except UnicodeDecodeError:
            print('unicode error, trying different encoding')
        else:
            abs_path = os.path.join(os.path.dirname(__file__), 'output_from_cp1251_to_utf8.txt')
            text_in_1251 = unicode_text.encode('utf-8')
            f = open(abs_path, 'w')
            f.write(text_in_1251)


def convert_from_utf8_to_windows_1251():
    filename = askopenfilename()
    try:
        f = open(filename, 'r').read()
    except UnicodeDecodeError:
        print "it was not a utf-8 unicode"
    else:
        try:
            unicode_text = f.decode('utf-8')
        except UnicodeDecodeError:
            print('unicode error, trying different encoding')
        else:
            abs_path = os.path.join(os.path.dirname(__file__), 'output_from_utf8_to_cp1251.txt')
            text_in_1251 = unicode_text.encode('cp1251')
            f = open(abs_path, 'w')
            f.write(text_in_1251)


root = Tk()
root.title('UTF-8 Converter')
root.geometry('250x250+500+300')
root.config(background="#FFFFFF")

button = Tkinter.Button(root, text="Check encoding", width=25, bg="#FFFFFF", command=open_file)
button.pack(fill=X, padx=10, pady=20)

res = Label(root, bg="#FFFFFF")
res.pack()

button1 = Tkinter.Button(root, text="Convert from windows-1251 to utf-8", width=25, bg="#FFFFFF",
                         command=convert_from_windows_1251)
button1.pack(fill=X, padx=10, pady=15)

button1 = Tkinter.Button(root, text="Convert from utf-8 to windows-1251", width=25, bg="#FFFFFF",
                         command=convert_from_utf8_to_windows_1251)
button1.pack(fill=X, padx=10, pady=15)

exit_button = Tkinter.Button(root, text='Quit', command=root.destroy, bg="#FFFFFF")
exit_button.pack(side='bottom')

root.mainloop()
