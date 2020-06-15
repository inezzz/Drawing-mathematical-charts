from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import numpy as np
from sympy import *
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

class GraphUI:
    def __init__(self, master):
        '''Initialization object and function call'''
        self.master = master
        color = '#ffffcc'
        master.title("Rysownik wykresów")
        master.geometry('902x650+100+100')
        master.configure(background=color)
        style.use("ggplot")
        self.label_to_entry_a_function()
        self.field_to_entry_a_function()
        self.set_xlim()
        self.set_ylim()
        self.set_name_title()
        self.set_label_for_plot()
        self.set_legend()
        self.button_wykres()
        #ALL BOTTON
        self.button_left_bracket()
        self.button_right_bracket()
        self.button_e()
        self.button_ln()
        self.button_sin()
        self.button_cos()
        self.button_tan()
        self.button_pow()
        self.button_arcsin()
        self.button_arccos()
        self.button_arctan()
        self.button_to_quit()

#---------WPISANIE FUNKCJI
    def label_to_entry_a_function(self):
        '''Set an information in label about entering function in empty place'''
        label_to_inform_about_writing_a_graph=Label(self.master, text="Podaj funkcję:", bg='#ffffcc')
        label_to_inform_about_writing_a_graph.config(font=("Verdana", 17))
        label_to_inform_about_writing_a_graph.place(x=10, y=5)
        label_to_fx=Label(self.master, text="f(x) = ", bg="#ffffcc")
        label_to_fx.config(font=("Verdana", 15))
        label_to_fx.place(x=5, y=40)


    def field_to_entry_a_function(self):
        '''Entry field to entering a function'''
        self.field_to_entry_function=Entry(self.master, font = "Verdena 13", width=30, justify='center')
        self.field_to_entry_function.place(x=75, y=47)

#----------------PODANIE ZAKRESÓW
    def set_xlim(self):
        '''Information about setting range x'''
        label_to_xlim=Label(self.master, text="Zakres x:", bg="#ffffcc")
        label_to_xlim.config(font=("Verdana", 10))
        label_to_xlim.place(x=10, y=85)
        label_from=Label(self.master, text="od", bg="#ffffcc")
        label_from.place(x=10, y=110)
        self.field_from_entry_xlim=Entry(self.master, font = "Verdena 10", width=5, justify='center')
        self.field_from_entry_xlim.place(x=30, y=110)
        label_to=Label(self.master, text="do", bg="#ffffcc")
        label_to.place(x=80, y=110)
        self.field_to_entry_xlim=Entry(self.master, font = "Verdena 10", width=5, justify='center')
        self.field_to_entry_xlim.place(x=100, y=110)

    def set_ylim(self):
        '''Information about setting range x'''
        label_to_ylim=Label(self.master, text="Zakres y:", bg="#ffffcc")
        label_to_ylim.config(font=("Verdana", 10))
        label_to_ylim.place(x=10, y=140)
        label_from=Label(self.master, text="od", bg="#ffffcc")
        label_from.place(x=10, y=165)
        self.field_from_entry_ylim=Entry(self.master, font = "Verdena 10", width=5, justify='center')
        self.field_from_entry_ylim.place(x=30, y=165)
        label_to=Label(self.master, text="do", bg="#ffffcc")
        label_to.place(x=80, y=165)
        self.field_to_entry_ylim=Entry(self.master, font = "Verdena 10", width=5, justify='center')
        self.field_to_entry_ylim.place(x=100, y=165)

# ----------TYTUŁ ORAZ ETYKIETY

    def set_name_title(self):
        '''Setting title for function'''
        label_to_title=Label(self.master, text="Tytuł wykresu:", bg="#ffffcc")
        label_to_title.config(font=("Verdana", 10))
        label_to_title.place(x=10, y=270)
        self.field_entry_title=Entry(self.master, font = "Verdena 10", width=18, justify='center')
        self.field_entry_title.place(x=10, y=295)

    def set_label_for_plot(self):
        '''Setting xlabel adn ylabel for plot'''
        label_to_label = Label(self.master, text="Etykiety:", bg="#ffffcc")
        label_to_label.config(font=("Verdana", 10))
        label_to_label.place(x=10, y=330)
        label_to_x = Label(self.master, text="oś x: ", bg="#ffffcc")
        label_to_x.config(font=("Verdana", 10))
        label_to_x.place(x=10, y=355)
        label_to_y = Label(self.master, text="oś y: ", bg="#ffffcc")
        label_to_y.config(font=("Verdana", 10))
        label_to_y.place(x=10, y=380)
        self.field_entry_xlabel_label = Entry(self.master, font="Verdena 10", width=12, justify='center')
        self.field_entry_xlabel_label.place(x=50, y=355)
        self.field_entry_ylabel_label = Entry(self.master, font="Verdena 10", width=12, justify='center')
        self.field_entry_ylabel_label.place(x=50, y=380)

#-------------LEGENDA

    def set_legend(self):
        '''Setting the chart legend based on the selection in radiobutton'''
        label_to_legend=Label(self.master, text="Czy ustawić legendę?", bg="#ffffcc")
        label_to_legend.config(font=("Verdana", 10))
        label_to_legend.place(x=10, y=210)
        self.var = IntVar()
        yes=Radiobutton(self.master, text="tak", variable=self.var, value=1, bg="#ffff80", width=5, indicatoron = 0)
        yes.config(font=("Verdana", 10))
        yes.place(x=10, y=232)
        no = Radiobutton(self.master, text="nie", variable=self.var, value=2, bg="#ffff80", width=5, indicatoron = 0)
        no.config(font=("Verdana", 10))
        no.place(x=60, y=232)


#------------------PRZYCISKI
    def set_text(self, text):
        '''Set text into an entry field'''
        self.field_to_entry_function.insert(INSERT, text) #INSTERT jest uzyty do wpisywania tekstu na samym koncu

    def button_left_bracket(self):
        '''Set "("'''
        button=Button(self.master, text='(', width=3, height=1, command=lambda:self.set_text("("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=290, y=0)

    def button_right_bracket(self):
        '''Set ")"'''
        button=Button(self.master, text=')', width=3, height=1, command=lambda:self.set_text(")"))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=330, y=0)

    def button_e(self):
        '''Set "e"'''
        button=Button(self.master, text='e', width=3, height=1, command=lambda:self.set_text("exp("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=370, y=0)

    def button_ln(self):
        '''Set "ln"'''
        button=Button(self.master, text='ln()', width=3, height=1, command=lambda:self.set_text("ln("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=410, y=0)

    def button_sin(self):
        '''Set "sin"'''
        button=Button(self.master, text='sin()', width=4, height=1, command=lambda:self.set_text("sin("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=450, y=0)

    def button_cos(self):
        '''Set "cos"'''
        button=Button(self.master, text='cos()', width=4, height=1, command=lambda:self.set_text("cos("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=500, y=0)

    def button_tan(self):
        '''Set "tan"'''
        button=Button(self.master, text='tan()', width=4, height=1, command=lambda:self.set_text("tan("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=550, y=0)

    def button_pow(self):
        '''Set "pow"'''
        button=Button(self.master, text='^', width=3, height=1, command=lambda:self.set_text("**"))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=600, y=0)

    def button_arcsin(self):
        '''Set "arcsin"'''
        button=Button(self.master, text='arcsin()', width=7, height=1, command=lambda:self.set_text("asin("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=380, y=32)

    def button_arccos(self):
        '''Set "arccos"'''
        button=Button(self.master, text='arccos()', width=7, height=1, command=lambda:self.set_text("acos("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=460, y=32)

    def button_arctan(self):
        '''Set "arctan"'''
        button=Button(self.master, text='arctan()', width=7, height=1, command=lambda:self.set_text("atan("))
        button.config(font=("Verdana", 12), bg="#ffff80")
        button.place(x=540, y=32)

    def button_wykres(self):
        '''Set button to start plot'''
        button = Button(self.master, text='Pokaż wykres', width=12, height=2, command=lambda:self.wykres())
        button.config(font=("Verdana", 12), bg="#ffff66")
        button.place(x=10, y=430)

    def quit(self):
        '''Destroying window and exit'''
        self.master.destroy()

    def button_to_quit(self):
        '''Set button to end of program'''
        button=Button(self.master, text='Zakończ', width=28, height=1, command=self.quit)
        button.config(font=("Verdena", 12), bg='#ff9966')
        button.place(x=640, y=0)

#-----------------WYKRES
    def wykres(self):
        '''Based on the information provided in each method above, create a plot'''
        from_xlim=int(self.field_from_entry_xlim.get())
        to_xlim=int(self.field_to_entry_xlim.get())
        from_ylim=int(self.field_from_entry_ylim.get())
        to_ylim=int(self.field_to_entry_ylim.get())
        title=self.field_entry_title.get()
        xlabel=self.field_entry_xlabel_label.get()
        ylabel=self.field_entry_ylabel_label.get()
        var_legend=self.var.get()

        function_string=self.field_to_entry_function.get()
        tab_func_string=function_string.split(';')
        tab_func=[]
        for i in range(len(tab_func_string)):
            func=parse_expr(tab_func_string[i], evaluate=0)
            func = lambdify(x, func, "numpy")
            tab_func.append(func)

        f=Figure(figsize=(7,5), facecolor="#ffffcc")
        a=f.add_subplot(111)
        a.set_xlim(from_xlim,to_xlim)
        a.set_ylim(from_ylim, to_ylim)
        a.set_title(title, fontsize=18)
        a.set_xlabel(xlabel, fontsize=14)
        a.set_ylabel(ylabel, fontsize=14)
        xs=np.linspace(from_xlim, to_xlim, 600)

        for i in range(len(tab_func)):
            fx=tab_func[i](xs)
            if tab_func_string[i] == 'tan(x)':
                fx[:-1][np.diff(fx) < 0] = np.nan
            name_label=tab_func_string[i]
            a.plot(xs, fx, label=name_label)

        if var_legend == 1:
            a.legend()

        canvas = FigureCanvasTkAgg(f, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().place(x=170, y=90)

        toolbar=NavigationToolbar2Tk(canvas, self.master)
        toolbar.config(background="#ffffcc")
        toolbar.update()
