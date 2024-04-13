import tkinter
import threading
import requests

root = tkinter.Tk()
root.title(u"Fuwasaba archive")
root.geometry("400x300") # Windowサイズ


Static1 = tkinter.Label(text=u'過去シーズン構成ダウンロード')
Static1.pack()

def download_file(url, filename):
    urlData = requests.get(url).content
    with open(filename ,mode='wb') as f:
        f.write(urlData)

def b3download():
    url='https://u.q-mc.xyz/8cD5MB'
    filename='β3.zip'
    download_file(url, filename)

Static1 = tkinter.Label(text=u'ふわ鯖β3期ファイル')
Static1.place(y=50)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-1>", lambda event: threading.Thread(target=b3download).start())
Button.place(x=125, y=50)

def b5download():
    url='https://u.q-mc.xyz/27BLeG'
    filename='β5.zip'
    download_file(url, filename)

Static1 = tkinter.Label(text=u'ふわ鯖β5期ファイル')
Static1.place(y=100)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-2>", lambda event: threading.Thread(target=b5download).start())
Button.place(x=125, y=100)

def b6download():
    url='https://u.q-mc.xyz/9iPcZH'
    filename='β6.zip'
    download_file(url, filename)

Static1 = tkinter.Label(text=u'ふわ鯖β6期ファイル')
Static1.place(y=150)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-3>", lambda event: threading.Thread(target=b6download).start())
Button.place(x=125, y=150)

def s1download():
    url='https://u.q-mc.xyz/8cD5MB'
    filename='s1.zip'
    download_file(url, filename)

Static1 = tkinter.Label(text=u'ふわ鯖新1期ファイル')
Static1.place(y=200)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-4>", lambda event: threading.Thread(target=s1download).start())
Button.place(x=125, y=200)

root.mainloop()
