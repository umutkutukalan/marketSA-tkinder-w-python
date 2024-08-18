class urunEkle:
    def __init__(self, root, focus, onFocusIn, onFocusOut, listele):
        import tkinter as tk

        self.urun_listesi = []

        # Texts Ekle
        self.textUrun = tk.Text(root, height=2, width=25, font=("Arial", 16), bg='white', fg='black')
        self.textUrun.grid(row=0, column=1, pady=5, sticky="n")
        self.textFiyat = tk.Text(root, height=2, width=25, font=("Arial", 16), bg='white', fg='black')
        self.textFiyat.grid(row=1, column=1, pady=5, sticky="n")

        # Input Validation
        self.textUrun.bind("<KeyRelease>", self.validate_urun)
        self.textFiyat.bind("<KeyRelease>", self.validate_fiyat)

        # Texts Listele
        self.labelUrunList = tk.Label(root, height=15, width=30, font=("Arial", 16), bg='white', fg='black', anchor="nw", justify='left')
        self.labelUrunList.grid(row=0, column=0, rowspan=10, padx=10, pady=5, sticky="nw")

        self.texts = [self.textUrun, self.textFiyat]
        self.focus = focus
        self.texts[0].insert("1.0", focus[0])
        self.texts[1].insert("1.0", focus[1])
        self.texts[0].bind("<FocusIn>", onFocusIn)
        self.texts[0].bind("<FocusOut>", onFocusOut)
        self.texts[1].bind("<FocusIn>", onFocusIn)
        self.texts[1].bind("<FocusOut>", onFocusOut)

        # Buttons
        self.btnEkle = tk.Button(root, height=2, width=5, text="Ekle", font=("Arial", 16),bg='blue', command=listele)
        self.btnEkle.grid(row=3, column=1, pady=10, sticky="nw")

    def validate_urun(self, event):
        content = self.textUrun.get("1.0", "end-1c")
        if not content.isalpha():  # Sadece harflerden oluşmalı
            self.textUrun.delete("1.0", "end")
            self.textUrun.insert("1.0", ''.join(filter(str.isalpha, content)))

    def validate_fiyat(self, event):
        content = self.textFiyat.get("1.0", "end-1c")
        if not content.isdigit():  # Sadece rakamlardan oluşmalı
            self.textFiyat.delete("1.0", "end")
            self.textFiyat.insert("1.0", ''.join(filter(str.isdigit, content)))

