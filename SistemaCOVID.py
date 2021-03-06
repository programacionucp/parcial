#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    May 27, 2020 04:29:12 PM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import SistemaCOVID_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    SistemaCOVID_support.set_Tk_var()
    top = Toplevel1 (root)
    SistemaCOVID_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    SistemaCOVID_support.set_Tk_var()
    top = Toplevel1 (w)
    SistemaCOVID_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("803x445+348+91")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.398, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.012, rely=0.056, relheight=0.887, relwidth=0.23)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.blb01 = tk.Label(self.Frame2)
        self.blb01.place(relx=0.281, rely=0.064, height=21, width=67)
        self.blb01.configure(activebackground="#f9f9f9")
        self.blb01.configure(activeforeground="black")
        self.blb01.configure(background="#d9d9d9")
        self.blb01.configure(disabledforeground="#a3a3a3")
        self.blb01.configure(font="-family {Arial} -size 10")
        self.blb01.configure(foreground="#000000")
        self.blb01.configure(highlightbackground="#d9d9d9")
        self.blb01.configure(highlightcolor="black")
        self.blb01.configure(text='''Argentina''')

        self.lbl01_1 = tk.Label(self.Frame2)
        self.lbl01_1.place(relx=0.054, rely=0.261, height=21, width=77)
        self.lbl01_1.configure(activebackground="#f9f9f9")
        self.lbl01_1.configure(activeforeground="black")
        self.lbl01_1.configure(background="#d9d9d9")
        self.lbl01_1.configure(disabledforeground="#a3a3a3")
        self.lbl01_1.configure(foreground="#000000")
        self.lbl01_1.configure(highlightbackground="#d9d9d9")
        self.lbl01_1.configure(highlightcolor="black")
        self.lbl01_1.configure(text='''Confirmados''')

        self.lbl01_2 = tk.Label(self.Frame2)
        self.lbl01_2.place(relx=0.054, rely=0.643, height=21, width=77)
        self.lbl01_2.configure(activebackground="#f9f9f9")
        self.lbl01_2.configure(activeforeground="black")
        self.lbl01_2.configure(background="#d9d9d9")
        self.lbl01_2.configure(disabledforeground="#a3a3a3")
        self.lbl01_2.configure(foreground="#000000")
        self.lbl01_2.configure(highlightbackground="#d9d9d9")
        self.lbl01_2.configure(highlightcolor="black")
        self.lbl01_2.configure(text='''Recuperados''')

        self.lbl01_3 = tk.Label(self.Frame2)
        self.lbl01_3.place(relx=0.168, rely=0.452, height=21, width=56)
        self.lbl01_3.configure(activebackground="#f9f9f9")
        self.lbl01_3.configure(activeforeground="black")
        self.lbl01_3.configure(background="#d9d9d9")
        self.lbl01_3.configure(disabledforeground="#a3a3a3")
        self.lbl01_3.configure(foreground="#000000")
        self.lbl01_3.configure(highlightbackground="#d9d9d9")
        self.lbl01_3.configure(highlightcolor="black")
        self.lbl01_3.configure(text='''Fallecidos''')

        self.lbl01_conf = tk.Label(self.Frame2)
        self.lbl01_conf.place(relx=0.508, rely=0.261, height=21, width=77)
        self.lbl01_conf.configure(activebackground="#f9f9f9")
        self.lbl01_conf.configure(activeforeground="black")
        self.lbl01_conf.configure(background="#d9d9d9")
        self.lbl01_conf.configure(disabledforeground="#a3a3a3")
        self.lbl01_conf.configure(foreground="#000000")
        self.lbl01_conf.configure(highlightbackground="#d9d9d9")
        self.lbl01_conf.configure(highlightcolor="black")
        self.lbl01_conf.configure(relief="ridge")
        self.lbl01_conf.configure(textvariable=SistemaCOVID_support.lbl_conf)

        self.lbl01_recup = tk.Label(self.Frame2)
        self.lbl01_recup.place(relx=0.508, rely=0.643, height=21, width=77)
        self.lbl01_recup.configure(activebackground="#f9f9f9")
        self.lbl01_recup.configure(activeforeground="black")
        self.lbl01_recup.configure(background="#d9d9d9")
        self.lbl01_recup.configure(disabledforeground="#a3a3a3")
        self.lbl01_recup.configure(foreground="#000000")
        self.lbl01_recup.configure(highlightbackground="#d9d9d9")
        self.lbl01_recup.configure(highlightcolor="black")
        self.lbl01_recup.configure(relief="ridge")
        self.lbl01_recup.configure(text='''''')
        self.lbl01_recup.configure(textvariable=SistemaCOVID_support.lbl01_recup)

        self.lbl01_fall = tk.Label(self.Frame2)
        self.lbl01_fall.place(relx=0.508, rely=0.452, height=21, width=77)
        self.lbl01_fall.configure(activebackground="#f9f9f9")
        self.lbl01_fall.configure(activeforeground="black")
        self.lbl01_fall.configure(background="#d9d9d9")
        self.lbl01_fall.configure(disabledforeground="#a3a3a3")
        self.lbl01_fall.configure(foreground="#000000")
        self.lbl01_fall.configure(highlightbackground="#d9d9d9")
        self.lbl01_fall.configure(highlightcolor="black")
        self.lbl01_fall.configure(relief="ridge")
        self.lbl01_fall.configure(text='''''')
        self.lbl01_fall.configure(textvariable=SistemaCOVID_support.lbl01_fall)

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.244, rely=0.056, relheight=0.887
                , relwidth=0.243)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Frame2_2 = tk.Frame(self.Frame3)
        self.Frame2_2.place(relx=1.477, rely=0.427, relheight=1.0, relwidth=1.0)
        self.Frame2_2.configure(relief='groove')
        self.Frame2_2.configure(borderwidth="2")
        self.Frame2_2.configure(relief="groove")
        self.Frame2_2.configure(background="#d9d9d9")
        self.Frame2_2.configure(highlightbackground="#d9d9d9")
        self.Frame2_2.configure(highlightcolor="black")

        self.blb02 = tk.Label(self.Frame3)
        self.blb02.place(relx=0.318, rely=0.064, height=21, width=67)
        self.blb02.configure(activebackground="#f9f9f9")
        self.blb02.configure(activeforeground="black")
        self.blb02.configure(background="#d9d9d9")
        self.blb02.configure(disabledforeground="#a3a3a3")
        self.blb02.configure(font="-family {Arial} -size 10")
        self.blb02.configure(foreground="#000000")
        self.blb02.configure(highlightbackground="#d9d9d9")
        self.blb02.configure(highlightcolor="black")
        self.blb02.configure(text='''Paraguay''')

        self.lbl02_1 = tk.Label(self.Frame3)
        self.lbl02_1.place(relx=0.108, rely=0.261, height=21, width=77)
        self.lbl02_1.configure(activebackground="#f9f9f9")
        self.lbl02_1.configure(activeforeground="black")
        self.lbl02_1.configure(background="#d9d9d9")
        self.lbl02_1.configure(disabledforeground="#a3a3a3")
        self.lbl02_1.configure(foreground="#000000")
        self.lbl02_1.configure(highlightbackground="#d9d9d9")
        self.lbl02_1.configure(highlightcolor="black")
        self.lbl02_1.configure(text='''Confirmados''')

        self.lbl02_2 = tk.Label(self.Frame3)
        self.lbl02_2.place(relx=0.215, rely=0.452, height=21, width=56)
        self.lbl02_2.configure(activebackground="#f9f9f9")
        self.lbl02_2.configure(activeforeground="black")
        self.lbl02_2.configure(background="#d9d9d9")
        self.lbl02_2.configure(disabledforeground="#a3a3a3")
        self.lbl02_2.configure(foreground="#000000")
        self.lbl02_2.configure(highlightbackground="#d9d9d9")
        self.lbl02_2.configure(highlightcolor="black")
        self.lbl02_2.configure(text='''Fallecidos''')

        self.lbl02_3 = tk.Label(self.Frame3)
        self.lbl02_3.place(relx=0.108, rely=0.643, height=21, width=77)
        self.lbl02_3.configure(activebackground="#f9f9f9")
        self.lbl02_3.configure(activeforeground="black")
        self.lbl02_3.configure(background="#d9d9d9")
        self.lbl02_3.configure(disabledforeground="#a3a3a3")
        self.lbl02_3.configure(foreground="#000000")
        self.lbl02_3.configure(highlightbackground="#d9d9d9")
        self.lbl02_3.configure(highlightcolor="black")
        self.lbl02_3.configure(text='''Recuperados''')

        self.lbl02_conf = tk.Label(self.Frame3)
        self.lbl02_conf.place(relx=0.533, rely=0.261, height=21, width=77)
        self.lbl02_conf.configure(activebackground="#f9f9f9")
        self.lbl02_conf.configure(activeforeground="black")
        self.lbl02_conf.configure(background="#d9d9d9")
        self.lbl02_conf.configure(disabledforeground="#a3a3a3")
        self.lbl02_conf.configure(foreground="#000000")
        self.lbl02_conf.configure(highlightbackground="#d9d9d9")
        self.lbl02_conf.configure(highlightcolor="black")
        self.lbl02_conf.configure(relief="ridge")
        self.lbl02_conf.configure(text='''''')
        self.lbl02_conf.configure(textvariable=SistemaCOVID_support.lbl02_conf)

        self.lbl02_fall = tk.Label(self.Frame3)
        self.lbl02_fall.place(relx=0.533, rely=0.452, height=21, width=77)
        self.lbl02_fall.configure(activebackground="#f9f9f9")
        self.lbl02_fall.configure(activeforeground="black")
        self.lbl02_fall.configure(background="#d9d9d9")
        self.lbl02_fall.configure(disabledforeground="#a3a3a3")
        self.lbl02_fall.configure(foreground="#000000")
        self.lbl02_fall.configure(highlightbackground="#d9d9d9")
        self.lbl02_fall.configure(highlightcolor="black")
        self.lbl02_fall.configure(relief="ridge")
        self.lbl02_fall.configure(text='''''')
        self.lbl02_fall.configure(textvariable=SistemaCOVID_support.lbl02_fall)

        self.lbl02_recup = tk.Label(self.Frame3)
        self.lbl02_recup.place(relx=0.533, rely=0.643, height=21, width=77)
        self.lbl02_recup.configure(activebackground="#f9f9f9")
        self.lbl02_recup.configure(activeforeground="black")
        self.lbl02_recup.configure(background="#d9d9d9")
        self.lbl02_recup.configure(disabledforeground="#a3a3a3")
        self.lbl02_recup.configure(foreground="#000000")
        self.lbl02_recup.configure(highlightbackground="#d9d9d9")
        self.lbl02_recup.configure(highlightcolor="black")
        self.lbl02_recup.configure(relief="ridge")
        self.lbl02_recup.configure(text='''''')
        self.lbl02_recup.configure(textvariable=SistemaCOVID_support.lbl02_recup)

        self.Frame4 = tk.Frame(self.Frame1)
        self.Frame4.place(relx=0.489, rely=0.056, relheight=0.887
                , relwidth=0.244)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Frame2_3 = tk.Frame(self.Frame4)
        self.Frame2_3.place(relx=1.474, rely=0.427, relheight=1.0, relwidth=1.0)
        self.Frame2_3.configure(relief='groove')
        self.Frame2_3.configure(borderwidth="2")
        self.Frame2_3.configure(relief="groove")
        self.Frame2_3.configure(background="#d9d9d9")
        self.Frame2_3.configure(highlightbackground="#d9d9d9")
        self.Frame2_3.configure(highlightcolor="black")

        self.blb03 = tk.Label(self.Frame4)
        self.blb03.place(relx=0.316, rely=0.064, height=21, width=67)
        self.blb03.configure(activebackground="#f9f9f9")
        self.blb03.configure(activeforeground="black")
        self.blb03.configure(background="#d9d9d9")
        self.blb03.configure(disabledforeground="#a3a3a3")
        self.blb03.configure(font="-family {Arial} -size 10")
        self.blb03.configure(foreground="#000000")
        self.blb03.configure(highlightbackground="#d9d9d9")
        self.blb03.configure(highlightcolor="black")
        self.blb03.configure(text='''Uruguay''')

        self.lbl03_1 = tk.Label(self.Frame4)
        self.lbl03_1.place(relx=0.107, rely=0.261, height=21, width=77)
        self.lbl03_1.configure(activebackground="#f9f9f9")
        self.lbl03_1.configure(activeforeground="black")
        self.lbl03_1.configure(background="#d9d9d9")
        self.lbl03_1.configure(disabledforeground="#a3a3a3")
        self.lbl03_1.configure(foreground="#000000")
        self.lbl03_1.configure(highlightbackground="#d9d9d9")
        self.lbl03_1.configure(highlightcolor="black")
        self.lbl03_1.configure(text='''Confirmados''')

        self.lbl03_2 = tk.Label(self.Frame4)
        self.lbl03_2.place(relx=0.107, rely=0.452, height=21, width=56)
        self.lbl03_2.configure(activebackground="#f9f9f9")
        self.lbl03_2.configure(activeforeground="black")
        self.lbl03_2.configure(background="#d9d9d9")
        self.lbl03_2.configure(disabledforeground="#a3a3a3")
        self.lbl03_2.configure(foreground="#000000")
        self.lbl03_2.configure(highlightbackground="#d9d9d9")
        self.lbl03_2.configure(highlightcolor="black")
        self.lbl03_2.configure(text='''Fallecidos''')

        self.lbl03_3 = tk.Label(self.Frame4)
        self.lbl03_3.place(relx=0.051, rely=0.643, height=21, width=78)
        self.lbl03_3.configure(activebackground="#f9f9f9")
        self.lbl03_3.configure(activeforeground="black")
        self.lbl03_3.configure(background="#d9d9d9")
        self.lbl03_3.configure(disabledforeground="#a3a3a3")
        self.lbl03_3.configure(foreground="#000000")
        self.lbl03_3.configure(highlightbackground="#d9d9d9")
        self.lbl03_3.configure(highlightcolor="black")
        self.lbl03_3.configure(text='''Recuperados''')

        self.lbl03_conf = tk.Label(self.Frame4)
        self.lbl03_conf.place(relx=0.531, rely=0.261, height=21, width=77)
        self.lbl03_conf.configure(activebackground="#f9f9f9")
        self.lbl03_conf.configure(activeforeground="black")
        self.lbl03_conf.configure(background="#d9d9d9")
        self.lbl03_conf.configure(disabledforeground="#a3a3a3")
        self.lbl03_conf.configure(foreground="#000000")
        self.lbl03_conf.configure(highlightbackground="#d9d9d9")
        self.lbl03_conf.configure(highlightcolor="black")
        self.lbl03_conf.configure(relief="ridge")
        self.lbl03_conf.configure(text='''''')
        self.lbl03_conf.configure(textvariable=SistemaCOVID_support.lbl03_conf)

        self.lbl03_fall = tk.Label(self.Frame4)
        self.lbl03_fall.place(relx=0.531, rely=0.452, height=21, width=77)
        self.lbl03_fall.configure(activebackground="#f9f9f9")
        self.lbl03_fall.configure(activeforeground="black")
        self.lbl03_fall.configure(background="#d9d9d9")
        self.lbl03_fall.configure(disabledforeground="#a3a3a3")
        self.lbl03_fall.configure(foreground="#000000")
        self.lbl03_fall.configure(highlightbackground="#d9d9d9")
        self.lbl03_fall.configure(highlightcolor="black")
        self.lbl03_fall.configure(relief="ridge")
        self.lbl03_fall.configure(text='''''')
        self.lbl03_fall.configure(textvariable=SistemaCOVID_support.lbl03_fall)

        self.lbl03_recup = tk.Label(self.Frame4)
        self.lbl03_recup.place(relx=0.531, rely=0.643, height=21, width=77)
        self.lbl03_recup.configure(activebackground="#f9f9f9")
        self.lbl03_recup.configure(activeforeground="black")
        self.lbl03_recup.configure(background="#d9d9d9")
        self.lbl03_recup.configure(disabledforeground="#a3a3a3")
        self.lbl03_recup.configure(foreground="#000000")
        self.lbl03_recup.configure(highlightbackground="#d9d9d9")
        self.lbl03_recup.configure(highlightcolor="black")
        self.lbl03_recup.configure(relief="ridge")
        self.lbl03_recup.configure(text='''''')
        self.lbl03_recup.configure(textvariable=SistemaCOVID_support.lbl03_recup)

        self.Frame4_4 = tk.Frame(self.Frame1)
        self.Frame4_4.place(relx=0.735, rely=0.056, relheight=0.887
                , relwidth=0.243)
        self.Frame4_4.configure(relief='groove')
        self.Frame4_4.configure(borderwidth="2")
        self.Frame4_4.configure(relief="groove")
        self.Frame4_4.configure(background="#d9d9d9")
        self.Frame4_4.configure(highlightbackground="#d9d9d9")
        self.Frame4_4.configure(highlightcolor="black")

        self.Frame2_4 = tk.Frame(self.Frame4_4)
        self.Frame2_4.place(relx=1.477, rely=0.427, relheight=1.0, relwidth=1.0)
        self.Frame2_4.configure(relief='groove')
        self.Frame2_4.configure(borderwidth="2")
        self.Frame2_4.configure(relief="groove")
        self.Frame2_4.configure(background="#d9d9d9")
        self.Frame2_4.configure(highlightbackground="#d9d9d9")
        self.Frame2_4.configure(highlightcolor="black")

        self.blb04 = tk.Label(self.Frame4_4)
        self.blb04.place(relx=0.318, rely=0.064, height=21, width=67)
        self.blb04.configure(activebackground="#f9f9f9")
        self.blb04.configure(activeforeground="black")
        self.blb04.configure(background="#d9d9d9")
        self.blb04.configure(disabledforeground="#a3a3a3")
        self.blb04.configure(font="-family {Arial} -size 10")
        self.blb04.configure(foreground="#000000")
        self.blb04.configure(highlightbackground="#d9d9d9")
        self.blb04.configure(highlightcolor="black")
        self.blb04.configure(text='''Brasil''')

        self.lbl04_1 = tk.Label(self.Frame4_4)
        self.lbl04_1.place(relx=0.108, rely=0.261, height=21, width=77)
        self.lbl04_1.configure(activebackground="#f9f9f9")
        self.lbl04_1.configure(activeforeground="black")
        self.lbl04_1.configure(background="#d9d9d9")
        self.lbl04_1.configure(disabledforeground="#a3a3a3")
        self.lbl04_1.configure(foreground="#000000")
        self.lbl04_1.configure(highlightbackground="#d9d9d9")
        self.lbl04_1.configure(highlightcolor="black")
        self.lbl04_1.configure(text='''Confirmados''')

        self.lbl04_2 = tk.Label(self.Frame4_4)
        self.lbl04_2.place(relx=0.215, rely=0.452, height=21, width=56)
        self.lbl04_2.configure(activebackground="#f9f9f9")
        self.lbl04_2.configure(activeforeground="black")
        self.lbl04_2.configure(background="#d9d9d9")
        self.lbl04_2.configure(disabledforeground="#a3a3a3")
        self.lbl04_2.configure(foreground="#000000")
        self.lbl04_2.configure(highlightbackground="#d9d9d9")
        self.lbl04_2.configure(highlightcolor="black")
        self.lbl04_2.configure(text='''Fallecidos''')

        self.lbl04_3 = tk.Label(self.Frame4_4)
        self.lbl04_3.place(relx=0.108, rely=0.643, height=21, width=77)
        self.lbl04_3.configure(activebackground="#f9f9f9")
        self.lbl04_3.configure(activeforeground="black")
        self.lbl04_3.configure(background="#d9d9d9")
        self.lbl04_3.configure(disabledforeground="#a3a3a3")
        self.lbl04_3.configure(foreground="#000000")
        self.lbl04_3.configure(highlightbackground="#d9d9d9")
        self.lbl04_3.configure(highlightcolor="black")
        self.lbl04_3.configure(text='''Recuperados''')

        self.lbl04_conf = tk.Label(self.Frame4_4)
        self.lbl04_conf.place(relx=0.533, rely=0.261, height=21, width=77)
        self.lbl04_conf.configure(activebackground="#f9f9f9")
        self.lbl04_conf.configure(activeforeground="black")
        self.lbl04_conf.configure(background="#d9d9d9")
        self.lbl04_conf.configure(disabledforeground="#a3a3a3")
        self.lbl04_conf.configure(foreground="#000000")
        self.lbl04_conf.configure(highlightbackground="#d9d9d9")
        self.lbl04_conf.configure(highlightcolor="black")
        self.lbl04_conf.configure(relief="ridge")
        self.lbl04_conf.configure(text='''''')
        self.lbl04_conf.configure(textvariable=SistemaCOVID_support.lbl04_conf)

        self.lbl04_fall = tk.Label(self.Frame4_4)
        self.lbl04_fall.place(relx=0.533, rely=0.452, height=21, width=77)
        self.lbl04_fall.configure(activebackground="#f9f9f9")
        self.lbl04_fall.configure(activeforeground="black")
        self.lbl04_fall.configure(background="#d9d9d9")
        self.lbl04_fall.configure(disabledforeground="#a3a3a3")
        self.lbl04_fall.configure(foreground="#000000")
        self.lbl04_fall.configure(highlightbackground="#d9d9d9")
        self.lbl04_fall.configure(highlightcolor="black")
        self.lbl04_fall.configure(relief="ridge")
        self.lbl04_fall.configure(text='''''')
        self.lbl04_fall.configure(textvariable=SistemaCOVID_support.lbl04_fall)

        self.lbl04_recup = tk.Label(self.Frame4_4)
        self.lbl04_recup.place(relx=0.533, rely=0.643, height=21, width=77)
        self.lbl04_recup.configure(activebackground="#f9f9f9")
        self.lbl04_recup.configure(activeforeground="black")
        self.lbl04_recup.configure(background="#d9d9d9")
        self.lbl04_recup.configure(disabledforeground="#a3a3a3")
        self.lbl04_recup.configure(foreground="#000000")
        self.lbl04_recup.configure(highlightbackground="#d9d9d9")
        self.lbl04_recup.configure(highlightcolor="black")
        self.lbl04_recup.configure(relief="ridge")
        self.lbl04_recup.configure(text='''''')
        self.lbl04_recup.configure(textvariable=SistemaCOVID_support.lbl04_recup)

        self.Frame5 = tk.Frame(top)
        self.Frame5.place(relx=0.012, rely=0.427, relheight=0.272
                , relwidth=0.979)
        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#d9d9d9")
        self.Frame5.configure(highlightbackground="#d9d9d9")
        self.Frame5.configure(highlightcolor="black")

        self.blb05 = tk.Label(self.Frame5)
        self.blb05.place(relx=0.076, rely=0.438, height=23, width=167)
        self.blb05.configure(activebackground="#f9f9f9")
        self.blb05.configure(activeforeground="black")
        self.blb05.configure(background="#d9d9d9")
        self.blb05.configure(disabledforeground="#a3a3a3")
        self.blb05.configure(font="-family {Arial} -size 10")
        self.blb05.configure(foreground="#000000")
        self.blb05.configure(highlightbackground="#d9d9d9")
        self.blb05.configure(highlightcolor="black")
        self.blb05.configure(text='''Pais con Mas Recuperados''')

        self.blb05_1 = tk.Label(self.Frame5)
        self.blb05_1.place(relx=0.688, rely=0.264, height=23, width=26)
        self.blb05_1.configure(activebackground="#f9f9f9")
        self.blb05_1.configure(activeforeground="black")
        self.blb05_1.configure(background="#d9d9d9")
        self.blb05_1.configure(disabledforeground="#a3a3a3")
        self.blb05_1.configure(font="-family {Arial} -size 10")
        self.blb05_1.configure(foreground="#000000")
        self.blb05_1.configure(highlightbackground="#d9d9d9")
        self.blb05_1.configure(highlightcolor="black")
        self.blb05_1.configure(text='''Pais''')

        self.blb05_3 = tk.Label(self.Frame5)
        self.blb05_3.place(relx=0.65, rely=0.521, height=23, width=67)
        self.blb05_3.configure(activebackground="#f9f9f9")
        self.blb05_3.configure(activeforeground="black")
        self.blb05_3.configure(background="#d9d9d9")
        self.blb05_3.configure(disabledforeground="#a3a3a3")
        self.blb05_3.configure(font="-family {Arial} -size 10")
        self.blb05_3.configure(foreground="#000000")
        self.blb05_3.configure(highlightbackground="#d9d9d9")
        self.blb05_3.configure(highlightcolor="black")
        self.blb05_3.configure(text='''Cantidad''')

        self.lbl_pais = tk.Label(self.Frame5)
        self.lbl_pais.place(relx=0.739, rely=0.264, height=22, width=154)
        self.lbl_pais.configure(activebackground="#f9f9f9")
        self.lbl_pais.configure(activeforeground="black")
        self.lbl_pais.configure(background="#d9d9d9")
        self.lbl_pais.configure(disabledforeground="#a3a3a3")
        self.lbl_pais.configure(foreground="#000000")
        self.lbl_pais.configure(highlightbackground="#d9d9d9")
        self.lbl_pais.configure(highlightcolor="black")
        self.lbl_pais.configure(relief="ridge")
        self.lbl_pais.configure(textvariable=SistemaCOVID_support.lbl_pais)

        self.lbl_cant = tk.Label(self.Frame5)
        self.lbl_cant.place(relx=0.739, rely=0.521, height=22, width=154)
        self.lbl_cant.configure(activebackground="#f9f9f9")
        self.lbl_cant.configure(activeforeground="black")
        self.lbl_cant.configure(background="#d9d9d9")
        self.lbl_cant.configure(disabledforeground="#a3a3a3")
        self.lbl_cant.configure(foreground="#000000")
        self.lbl_cant.configure(highlightbackground="#d9d9d9")
        self.lbl_cant.configure(highlightcolor="black")
        self.lbl_cant.configure(relief="ridge")
        self.lbl_cant.configure(textvariable=SistemaCOVID_support.lbl_cant)

        self.btn_Buscar_Pais = ttk.Button(self.Frame5)
        self.btn_Buscar_Pais.place(relx=0.331, rely=0.331, height=35, width=206)
        self.btn_Buscar_Pais.configure(command=SistemaCOVID_support.Buscar_Pais)
        self.btn_Buscar_Pais.configure(takefocus="")
        self.btn_Buscar_Pais.configure(text='''Buscar País''')

        self.Frame5_5 = tk.Frame(top)
        self.Frame5_5.place(relx=0.012, rely=0.719, relheight=0.249
                , relwidth=0.979)
        self.Frame5_5.configure(relief='groove')
        self.Frame5_5.configure(borderwidth="2")
        self.Frame5_5.configure(relief="groove")
        self.Frame5_5.configure(background="#d9d9d9")
        self.Frame5_5.configure(highlightbackground="#d9d9d9")
        self.Frame5_5.configure(highlightcolor="black")

        self.blb08_1 = tk.Label(self.Frame5_5)
        self.blb08_1.place(relx=0.051, rely=0.18, height=21, width=27)
        self.blb08_1.configure(activebackground="#f9f9f9")
        self.blb08_1.configure(activeforeground="black")
        self.blb08_1.configure(background="#d9d9d9")
        self.blb08_1.configure(disabledforeground="#a3a3a3")
        self.blb08_1.configure(font="-family {Arial} -size 10")
        self.blb08_1.configure(foreground="#000000")
        self.blb08_1.configure(highlightbackground="#d9d9d9")
        self.blb08_1.configure(highlightcolor="black")
        self.blb08_1.configure(text='''Pais''')

        self.btn_Buscar = ttk.Button(self.Frame5_5)
        self.btn_Buscar.place(relx=0.344, rely=0.27, height=35, width=206)
        self.btn_Buscar.configure(command=SistemaCOVID_support.Buscar)
        self.btn_Buscar.configure(takefocus="")
        self.btn_Buscar.configure(text='''Buscar''')

        self.entry_pais = tk.Entry(self.Frame5_5)
        self.entry_pais.place(relx=0.102, rely=0.18,height=20, relwidth=0.183)
        self.entry_pais.configure(background="white")
        self.entry_pais.configure(disabledforeground="#a3a3a3")
        self.entry_pais.configure(font="TkFixedFont")
        self.entry_pais.configure(foreground="#000000")
        self.entry_pais.configure(insertbackground="black")
        self.entry_pais.configure(textvariable=SistemaCOVID_support.entry_pais)

        self.blb08_2 = tk.Label(self.Frame5_5)
        self.blb08_2.place(relx=0.051, rely=0.45, height=21, width=27)
        self.blb08_2.configure(activebackground="#f9f9f9")
        self.blb08_2.configure(activeforeground="black")
        self.blb08_2.configure(background="#d9d9d9")
        self.blb08_2.configure(disabledforeground="#a3a3a3")
        self.blb08_2.configure(font="-family {Arial} -size 10")
        self.blb08_2.configure(foreground="#000000")
        self.blb08_2.configure(highlightbackground="#d9d9d9")
        self.blb08_2.configure(highlightcolor="black")
        self.blb08_2.configure(text='''Dia''')

        self.lbl04_2 = tk.Label(self.Frame5_5)
        self.lbl04_2.place(relx=0.662, rely=0.09, height=21, width=77)
        self.lbl04_2.configure(activebackground="#f9f9f9")
        self.lbl04_2.configure(activeforeground="black")
        self.lbl04_2.configure(background="#d9d9d9")
        self.lbl04_2.configure(disabledforeground="#a3a3a3")
        self.lbl04_2.configure(foreground="#000000")
        self.lbl04_2.configure(highlightbackground="#d9d9d9")
        self.lbl04_2.configure(highlightcolor="black")
        self.lbl04_2.configure(text='''Confirmados''')

        self.lbl04_3 = tk.Label(self.Frame5_5)
        self.lbl04_3.place(relx=0.687, rely=0.36, height=21, width=56)
        self.lbl04_3.configure(activebackground="#f9f9f9")
        self.lbl04_3.configure(activeforeground="black")
        self.lbl04_3.configure(background="#d9d9d9")
        self.lbl04_3.configure(disabledforeground="#a3a3a3")
        self.lbl04_3.configure(foreground="#000000")
        self.lbl04_3.configure(highlightbackground="#d9d9d9")
        self.lbl04_3.configure(highlightcolor="black")
        self.lbl04_3.configure(text='''Fallecidos''')

        self.lbl04_4 = tk.Label(self.Frame5_5)
        self.lbl04_4.place(relx=0.662, rely=0.631, height=21, width=77)
        self.lbl04_4.configure(activebackground="#f9f9f9")
        self.lbl04_4.configure(activeforeground="black")
        self.lbl04_4.configure(background="#d9d9d9")
        self.lbl04_4.configure(disabledforeground="#a3a3a3")
        self.lbl04_4.configure(foreground="#000000")
        self.lbl04_4.configure(highlightbackground="#d9d9d9")
        self.lbl04_4.configure(highlightcolor="black")
        self.lbl04_4.configure(text='''Recuperados''')

        self.lbl_cantConf = tk.Label(self.Frame5_5)
        self.lbl_cantConf.place(relx=0.776, rely=0.09, height=22, width=154)
        self.lbl_cantConf.configure(activebackground="#f9f9f9")
        self.lbl_cantConf.configure(activeforeground="black")
        self.lbl_cantConf.configure(background="#d9d9d9")
        self.lbl_cantConf.configure(disabledforeground="#a3a3a3")
        self.lbl_cantConf.configure(foreground="#000000")
        self.lbl_cantConf.configure(highlightbackground="#d9d9d9")
        self.lbl_cantConf.configure(highlightcolor="black")
        self.lbl_cantConf.configure(relief="ridge")
        self.lbl_cantConf.configure(textvariable=SistemaCOVID_support.lbl_cantConf)

        self.lbl_cantFall = tk.Label(self.Frame5_5)
        self.lbl_cantFall.place(relx=0.776, rely=0.36, height=22, width=154)
        self.lbl_cantFall.configure(activebackground="#f9f9f9")
        self.lbl_cantFall.configure(activeforeground="black")
        self.lbl_cantFall.configure(background="#d9d9d9")
        self.lbl_cantFall.configure(disabledforeground="#a3a3a3")
        self.lbl_cantFall.configure(foreground="#000000")
        self.lbl_cantFall.configure(highlightbackground="#d9d9d9")
        self.lbl_cantFall.configure(highlightcolor="black")
        self.lbl_cantFall.configure(relief="ridge")
        self.lbl_cantFall.configure(textvariable=SistemaCOVID_support.lbl_cantFall)

        self.lbl_cantRecup = tk.Label(self.Frame5_5)
        self.lbl_cantRecup.place(relx=0.776, rely=0.631, height=22, width=154)
        self.lbl_cantRecup.configure(activebackground="#f9f9f9")
        self.lbl_cantRecup.configure(activeforeground="black")
        self.lbl_cantRecup.configure(background="#d9d9d9")
        self.lbl_cantRecup.configure(disabledforeground="#a3a3a3")
        self.lbl_cantRecup.configure(foreground="#000000")
        self.lbl_cantRecup.configure(highlightbackground="#d9d9d9")
        self.lbl_cantRecup.configure(highlightcolor="black")
        self.lbl_cantRecup.configure(relief="ridge")
        self.lbl_cantRecup.configure(textvariable=SistemaCOVID_support.lbl_cantRecup)

        self.entry_dia = tk.Entry(self.Frame5_5)
        self.entry_dia.place(relx=0.102, rely=0.45,height=20, relwidth=0.183)
        self.entry_dia.configure(background="white")
        self.entry_dia.configure(disabledforeground="#a3a3a3")
        self.entry_dia.configure(font="TkFixedFont")
        self.entry_dia.configure(foreground="#000000")
        self.entry_dia.configure(highlightbackground="#d9d9d9")
        self.entry_dia.configure(highlightcolor="black")
        self.entry_dia.configure(insertbackground="black")
        self.entry_dia.configure(selectbackground="#c4c4c4")
        self.entry_dia.configure(selectforeground="black")
        self.entry_dia.configure(textvariable=SistemaCOVID_support.entry_dia)

if __name__ == '__main__':
    vp_start_gui()





