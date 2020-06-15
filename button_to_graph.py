from tkinter import *

class Button:
    def __init__(self, master, field_to_entry_function):
        self.master=master
        self.button_left_bracket(field_to_entry_function)
        self.button_right_bracket(field_to_entry_function)
        self.button_e(field_to_entry_function)
        self.button_ln(field_to_entry_function)
        self.button_add(field_to_entry_function)
        self.button_minus(field_to_entry_function)
        self.button_multi(field_to_entry_function)
        self.button_div(field_to_entry_function)

    def set_text(self, text, field_to_entry_function):
        '''Set text into an entry field'''
        field_to_entry_function.insert(INSERT, text) #INSTERT jest uzyty do wpisywania tekstu na samym koncu

    def button_left_bracket(self, field_to_entry_function):
        '''Set "("'''
        button=Button(self.master, text='(', width=3, height=1, command=lambda:self.set_text("(", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=290, y=0)

    def button_right_bracket(self, field_to_entry_function):
        '''Set ")"'''
        button=Button(self.master, text=')', width=3, height=1, command=lambda:self.set_text(")", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=330, y=0)

    def button_e(self, field_to_entry_function):
        '''Set "e"'''
        button=Button(self.master, text='e', width=3, height=1, command=lambda:self.set_text("e", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=370, y=0)

    def button_ln(self, field_to_entry_function):
        '''Set "ln"'''
        button=Button(self.master, text='ln', width=3, height=1, command=lambda:self.set_text("ln", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=410, y=0)

    def button_add(self, field_to_entry_function):
        '''Set "+"'''
        button=Button(self.master, text='+', width=3, height=1, command=lambda:self.set_text("+", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=290, y=32)

    def button_minus(self, field_to_entry_function):
        '''Set "-"'''
        button=Button(self.master, text='-', width=3, height=1, command=lambda:self.set_text("-", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=330, y=32)

    def button_multi(self, field_to_entry_function):
        '''Set "*"'''
        button=Button(self.master, text='*', width=3, height=1, command=lambda:self.set_text("*", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=370, y=32)

    def button_div(self, field_to_entry_function):
        '''Set "/"'''
        button=Button(self.master, text='/', width=3, height=1, command=lambda:self.set_text("/", field_to_entry_function))
        button.config(font=("Verdana", 12), bg="#5ed45e")
        button.place(x=410, y=32)