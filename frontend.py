from tkinter import Tk, W, E, BOTH, ttk, messagebox
import tkinter as tk
from tkinter.ttk import Frame, Button, Entry, Style, Label, Radiobutton
import plot, backend


import config


class PE2_Frame(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Нелинейные колебания")
        #Style().configure("TFrame", background="#333")
        self.pack(fill=BOTH, expand=True)

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(2, pad=5)
        self.rowconfigure(4, pad=5)

        self.plotF = plot.PlotFrame(self)
        self.bA = blockA(self)
        self.bB = blockB(self)
        self.bC = blockC(self)
        self.bD = blockD(self)
        self.common = common_frame(self)

        self.plotF.grid(row=0, column=0, rowspan=4)
        self.common.grid(row=0, column=1, columnspan=2)
        self.bA.grid(row=1, column=1)
        self.bB.grid(row=1, column=2)
        self.bC.grid(row=2, column=1)
        self.bD.grid(row=2, column=2)
        #self.bE.grid(row=3, column=1)

        #self.pack()


class blockA(Frame):
    def __init__(self, parent):
        self.master = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        #Style().configure("TFrame", background="#000")
        self.alpha = tk.StringVar()
        self.epsilon = tk.StringVar()

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(4, pad=3)

        # подпись
        self.tot_lbl = Label(self, text="Часть А", width=config.label_width_E1)
        self.tot_lbl.grid(row=0, column=0, columnspan=2)
        # поля для параметров
        self.al_lbl = Label(self, text="w0:", width=config.label_width_E1)
        self.al_lbl.grid(row=1, column=0)
        self.al_ent = Entry(self, textvariable=self.alpha)
        self.alpha.set(config.glob_A_w0)
        self.al_ent.grid(row=1, column=1)

        self.ep_lbl = Label(self, text="Epsilon:", width=config.label_width_E1)
        self.ep_lbl.grid(row=2, column=0)
        self.ep_ent = Entry(self, textvariable=self.epsilon)
        self.epsilon.set(config.glob_A_epsilon)
        self.ep_ent.grid(row=2, column=1)
        # кнопка для построения
        self.count_but = Button(self, text="Построить численное решение", command=self.compile)
        self.count_but.grid(row=3, column=0, columnspan=2)
        # шкала прогресса
        self.progress = ttk.Progressbar(self, orient="horizontal", maximum=config.full_number, mode="determinate")
        self.progress.grid(row=4, column=0, columnspan=2)

    def compile(self):
        config.curr_drawing = "A"

        try:
            self.master.common.unsafe_compile()
            config.glob_A_w0 = float(self.alpha.get())
            config.glob_A_epsilon = float(self.epsilon.get())
            self.master.plotF.plot(self.progress)
        except:
            messagebox.showinfo("Error", "Некорректный ввод")


class blockB(Frame):
    def __init__(self, parent):
        self.master = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):

        #Style().configure("TFrame", background="#333")
        self.alpha = tk.StringVar()
        self.epsilon = tk.StringVar()
        self.gamma = tk.StringVar()
        self.omega = tk.StringVar()
        self.f = tk.StringVar()
        self.check_var = tk.IntVar()

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(8, pad=3)

        # подпись
        self.tot_lbl = Label(self, text="Часть B", width=config.label_width_E1)
        self.tot_lbl.grid(row=0, column=0, columnspan=2)
        # поля для параметров
        self.al_lbl = Label(self, text="w0:", width=config.label_width_E1)
        #self.al_lbl.grid(row=1, column=0)
        self.al_ent = Entry(self, textvariable=self.alpha)
        self.alpha.set(config.glob_B_w0)
        #self.al_ent.grid(row=1, column=1)

        self.ep_lbl = Label(self, text="Epsilon:", width=config.label_width_E1)
        #self.ep_lbl.grid(row=2, column=0)
        self.ep_ent = Entry(self, textvariable=self.epsilon)
        self.epsilon.set(config.glob_B_epsilon)
        #self.ep_ent.grid(row=2, column=1)

        self.g_lbl = Label(self, text="Gamma:", width=config.label_width_E1)
        #self.g_lbl.grid(row=3, column=0)
        self.g_ent = Entry(self, textvariable=self.gamma)
        self.gamma.set(config.glob_B_gamma)
        #self.g_ent.grid(row=3, column=1)

        self.om_lbl = Label(self, text="Omega:", width=config.label_width_E1)
        self.om_lbl.grid(row=4, column=0)
        self.om_ent = Entry(self, textvariable=self.omega)
        self.omega.set(config.glob_B_omega)
        self.om_ent.grid(row=4, column=1)

        self.f_lbl = Label(self, text="f:", width=config.label_width_E1)
        self.f_lbl.grid(row=5, column=0)
        self.f_ent = Entry(self, textvariable=self.f)
        self.f.set(config.glob_B_f)
        self.f_ent.grid(row=5, column=1)
        # кнопка для построения
        self.count_but = Button(self, text="Построить численное решение", command=self.compile)
        self.count_but.grid(row=6, column=0, columnspan=2)
        # шкала прогресса
        self.progress = ttk.Progressbar(self, orient="horizontal", maximum=config.full_number, mode="determinate")
        self.progress.grid(row=7, column=0, columnspan=2)

        self.check_furie = ttk.Checkbutton(self, text='Преобразование Фурье', variable=self.check_var, onvalue=1, offvalue=0, command=self.check_box_furie)
        self.check_var.set(config.type_of_B)
        #self.check_furie.grid(row=8, column=0, columnspan=2)

    def compile(self):
        config.curr_drawing = "B"
        try:
            self.master.common.unsafe_compile()

            config.glob_B_w0 = float(self.alpha.get())
            config.glob_B_epsilon = float(self.epsilon.get())
            config.glob_B_gamma = float(self.gamma.get())
            config.glob_B_omega = float(self.omega.get())
            config.glob_B_f = float(self.f.get())

        except:
            messagebox.showinfo("Error", "Некорректный ввод")
        self.master.plotF.plot(self.progress)

    def check_box_furie(self):
        #print("fdsfdfd")
        config.type_of_B = self.check_var.get()
        if config.curr_drawing == "B":
            self.master.plotF.replot()


class blockC(Frame):
    def __init__(self, parent):
        self.master = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):

        #Style().configure("TFrame", background="#333")
        self.w0 = tk.StringVar()
        self.epsilon = tk.StringVar()
        self.omega = tk.StringVar()
        self.gamma = tk.StringVar()
        self.mu = tk.StringVar()

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(7, pad=3)

        # подпись
        self.tot_lbl = Label(self, text="Часть C", width=config.label_width_E1)
        self.tot_lbl.grid(row=0, column=0, columnspan=2)
        # поля для параметров
        self.w0_lbl = Label(self, text="w0:", width=config.label_width_E1)
        self.w0_lbl.grid(row=1, column=0)
        self.w0_ent = Entry(self, textvariable=self.w0)
        self.w0.set(config.glob_C_w0)
        self.w0_ent.grid(row=1, column=1)

        self.ep_lbl = Label(self, text="Epsilon:", width=config.label_width_E1)
        self.ep_lbl.grid(row=2, column=0)
        self.ep_ent = Entry(self, textvariable=self.epsilon)
        self.epsilon.set(config.glob_C_epsilon)
        self.ep_ent.grid(row=2, column=1)

        self.om_lbl = Label(self, text="Omega:", width=config.label_width_E1)
        self.om_lbl.grid(row=3, column=0)
        self.om_ent = Entry(self, textvariable=self.omega)
        self.omega.set(config.glob_C_omega)
        self.om_ent.grid(row=3, column=1)

        self.g_lbl = Label(self, text="Gamma:", width=config.label_width_E1)
        self.g_lbl.grid(row=4, column=0)
        self.g_ent = Entry(self, textvariable=self.gamma)
        self.gamma.set(config.glob_C_gamma)
        self.g_ent.grid(row=4, column=1)

        self.mu_lbl = Label(self, text="mu:", width=config.label_width_E1)
        self.mu_lbl.grid(row=5, column=0)
        self.mu_ent = Entry(self, textvariable=self.mu)
        self.mu.set(config.glob_C_mu)
        self.mu_ent.grid(row=5, column=1)
        # кнопка для построения
        self.count_but = Button(self, text="Построить численное решение", command=self.compile)
        self.count_but.grid(row=6, column=0, columnspan=2)
        # шкала прогресса
        self.progress = ttk.Progressbar(self, orient="horizontal", maximum=config.full_number, mode="determinate")
        self.progress.grid(row=7, column=0, columnspan=2)

    def compile(self):
        config.curr_drawing = "C"
        try:
            self.master.common.unsafe_compile()

            config.glob_C_w0 = float(self.w0.get())
            config.glob_C_epsilon = float(self.epsilon.get())
            config.glob_C_omega = float(self.omega.get())
            config.glob_C_gamma = float(self.gamma.get())
            config.glob_C_mu = float(self.mu.get())
            self.master.plotF.plot(self.progress)
        except:
            messagebox.showinfo("Error", "Некорректный ввод")


class blockD(Frame):
    def __init__(self, parent):
        self.master = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):

        #Style().configure("TFrame", background="white")
        self.w0 = tk.StringVar()
        self.gamma = tk.StringVar()
        self.f = tk.StringVar()

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(5, pad=3)

        # подпись
        self.tot_lbl = Label(self, text="Часть D", width=config.label_width_E1)
        self.tot_lbl.grid(row=0, column=0, columnspan=2)
        # поля для параметров
        self.w0_lbl = Label(self, text="w0:", width=config.label_width_E1)
        self.w0_lbl.grid(row=1, column=0)
        self.w0_ent = Entry(self, textvariable=self.w0)
        self.w0.set(config.glob_D_w0)
        self.w0_ent.grid(row=1, column=1)

        self.g_lbl = Label(self, text="Gamma:", width=config.label_width_E1)
        self.g_lbl.grid(row=2, column=0)
        self.g_ent = Entry(self, textvariable=self.gamma)
        self.gamma.set(config.glob_D_gamma)
        self.g_ent.grid(row=2, column=1)

        self.f_lbl = Label(self, text="f:", width=config.label_width_E1)
        self.f_lbl.grid(row=3, column=0)
        self.f_ent = Entry(self, textvariable=self.f)
        self.f.set(config.glob_D_f)
        self.f_ent.grid(row=3, column=1)
        # кнопка для построения
        self.count_but = Button(self, text="Построить численное решение", command=self.compile)
        self.count_but.grid(row=4, column=0, columnspan=2)
        # шкала прогресса
        self.progress = ttk.Progressbar(self, orient="horizontal", maximum=config.full_number, mode="determinate")
        self.progress.grid(row=5, column=0, columnspan=2)

    def compile(self):
        config.curr_drawing = "D"
        try:
            self.master.common.unsafe_compile()
            config.glob_D_w0 = float(self.w0.get())
            config.glob_D_gamma = float(self.gamma.get())
            config.glob_D_f = float(self.f.get())
            self.master.plotF.plot(self.progress)
        except:
            messagebox.showinfo("Error", "Некорректный ввод")


class common_frame(Frame):
    def __init__(self, parent):
        self.master = parent
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.delta_t = tk.StringVar()
        self.full_time = tk.StringVar()
        self.num_cont = tk.StringVar()
        self.x0 = tk.StringVar()
        self.v0 = tk.StringVar()

        self.columnconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        # подписи
        self.tot_lbl = Label(self, text="Общие параметры")
        self.tot_lbl.grid(row=0, column=0, columnspan=4)
        self.tot_lbl = Label(self, text="Параметры симуляции")
        self.tot_lbl.grid(row=1, column=0, columnspan=2)
        self.tot_lbl = Label(self, text="Начальные условия")
        self.tot_lbl.grid(row=1, column=2, columnspan=2)
        # поля для параметров
        self.dt_lbl = Label(self, text="Временной шаг:")
        self.dt_lbl.grid(row=2, column=0)
        self.dt_ent = Entry(self, textvariable=self.delta_t)
        self.delta_t.set(config.delta_t)
        self.dt_ent.grid(row=2, column=1)

        self.T_lbl = Label(self, text="Полное время:")
        self.T_lbl.grid(row=3, column=0)
        self.T_ent = Entry(self, textvariable=self.full_time)
        self.full_time.set(config.full_time)
        self.T_ent.grid(row=3, column=1)

        self.nc_lbl = Label(self, text="Точность симуляции:")
        #self.nc_lbl.grid(row=4, column=0)
        self.nc_ent = Entry(self, textvariable=self.num_cont)
        self.num_cont.set(config.num_cont)
        #self.nc_ent.grid(row=4, column=1)

        self.x0_lbl = Label(self, text="x_0:")
        self.x0_lbl.grid(row=2, column=2)
        self.x0_ent = Entry(self, textvariable=self.x0)
        self.x0.set(config.x0)
        self.x0_ent.grid(row=2, column=3)

        self.v0_lbl = Label(self, text="v_0:")
        self.v0_lbl.grid(row=3, column=2)
        self.v0_ent = Entry(self, textvariable=self.v0)
        self.v0.set(config.v0)
        self.v0_ent.grid(row=3, column=3)

    def unsafe_compile(self):
        config.delta_t = float(self.delta_t.get())
        config.full_time = float(self.full_time.get())
        config.num_cont = int(self.num_cont.get())
        config.x0 = float(self.x0.get())
        config.v0 = float(self.v0.get())