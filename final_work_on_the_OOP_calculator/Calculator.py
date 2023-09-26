from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    # Вывод результата
    
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Visitor Rus", 23, "bold"), bg="#808080", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        #Кнопки 
        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        # Отображение кнопок калькулятора
        
        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#C0C0C0",
                   font=("Visitor Rus", 20),
                   command=com).place(x=x, y=y,
                                      width=116,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

#Дизайн калькулятора
if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#808080"
    root.geometry("490x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()