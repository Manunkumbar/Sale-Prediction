from tkinter import *
import pickle

class LRwindow:
    def __init__(self,win):
        f = open("sales_model.sav","rb")
        self.model = pickle.load(f)
        f.close()

        self.lbl1=Label(win, text='TV')
        self.lbl2=Label(win, text='Radio')
        self.lbl3=Label(win, text='News Paper')
        self.lbl4=Label(win, text='Sales')


        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()


        self.lbl1.place(x=100, y=50)
        self.t1.place(x=300, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=300, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=300, y=150)

        self.b1=Button(win, text='Predict', command=self.predict)

        self.b1.place(x = 200,y = 200)

        self.lbl4.place(x=100, y=250)
        self.t4.place(x=300, y=250)

    def predict(self):
        TV          = float(self.t1.get())
        radio       = float(self.t2.get())
        news_paper  = float(self.t3.get())

        result = self.model.predict([[TV,radio,news_paper]])
        result = result[0]
        self.t4.insert(END,float(result))
