import tkinter as tk
from urun_ekle import urunEkle
def onFocusIn(event):
    index = app.texts.index(event.widget)
    placeholder = app.focus[index]
    if event.widget.get("1.0", "end-1c").strip() == placeholder:
        event.widget.delete("1.0", "end")
def onFocusOut(event):
    index = app.texts.index(event.widget)
    placeholder = app.focus[index]
    if event.widget.get("1.0", "end-1c").strip() == "":
        event.widget.insert("1.0", placeholder)

def listele():
    urun = app.texts[0].get("1.0", "end-1c")
    fiyat = app.texts[1].get("1.0", "end-1c")
    if urun and fiyat:
        app.urun_listesi.append(f"{urun}: {fiyat} TL")
        app.labelUrunList.config(text="\n".join(app.urun_listesi))
        app.textUrun.delete("1.0", "end")
        app.textFiyat.delete("1.0", "end")

# ROOT
root = tk.Tk()
root.geometry("600x300")
root.title("marketSA")

focus=[
    "Ürün Adı:",
    "Ürün Fiyatı:"
]

app = urunEkle(root, focus, onFocusIn, onFocusOut, listele)



root.mainloop()

