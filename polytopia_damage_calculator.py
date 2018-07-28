from tkinter import *


class PolytopiaCalculatorApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.ar1_label_text = StringVar()
        self.ar2_label_text = StringVar()
        self.error_label_text = StringVar()

        self.ah_label = Label(text="Attacker's current health:")
        self.ah_label.pack()
        self.ah_entry = Entry(self)
        self.ah_entry.pack()

        self.amh_label = Label(text="Attacker's maximum health:")
        self.amh_label.pack()
        self.amh_entry = Entry(self)
        self.amh_entry.pack()

        self.aa_label = Label(text="Attack value of attacker:")
        self.aa_label.pack()
        self.aa_entry = Entry(self)
        self.aa_entry.pack()

        self.ad_label = Label(text="Defense value of attacker:")
        self.ad_label.pack()
        self.ad_entry = Entry(self)
        self.ad_entry.pack()

        self.dh_label = Label(text="Defender's current health:")
        self.dh_label.pack()
        self.dh_entry = Entry(self)
        self.dh_entry.pack()

        self.dmh_label = Label(text="Defender's maximum health:")
        self.dmh_label.pack()
        self.dmh_entry = Entry(self)
        self.dmh_entry.pack()

        self.ad_label = Label(text="Defense value of defender:")
        self.ad_label.pack()
        self.dd_entry = Entry(self)
        self.dd_entry.pack()

        self.confirm_button = Button(text='Run', command=self.confirmation)
        self.confirm_button.pack()

        self.ar1_label = Label(textvariable=self.ar1_label_text)
        self.ar2_label = Label(textvariable=self.ar2_label_text)

        self.error_label = Label(textvariable=self.error_label_text)

    def confirmation(self):
        try:
            ah = float(self.ah_entry.get())
            amh = float(self.amh_entry.get())
            aa = float(self.aa_entry.get())
            ad = float(self.ad_entry.get())
            dd = float(self.dd_entry.get())
            dh = float(self.dh_entry.get())
            dmh = float(self.dmh_entry.get())

            af1 = aa * (ah / amh)
            df1 = dd * (dh / dmh) #* 4
            td1 = af1 + df1
            ar1 = round((af1 / td1) * aa * 4.5000001)

            af2 = dd * (dh / dmh) #* 4
            df2 = ad * (ah / amh)
            td2 = af2 + df2
            ar2 = round((af2 / td2) * dd * 4.5000001)

            self.ar1_label_text.set(f'Defender alive: {dh - ar1 > 0}. Defender\'s current health: {dh - ar1}')
            self.ar2_label_text.set(f'Attacker alive: {ah - ar2 > 0}. Attacker\'s current health: {ah - ar2}')
            self.ar1_label.pack()
            self.ar2_label.pack()
            self.error_label_text.set("")
            self.error_label.pack()

        except Exception as e:
            self.error_label_text.set(f'Error: {e}')
            self.error_label.pack()


app = PolytopiaCalculatorApp()
app.mainloop()
