import tkinter
import requests
import urllib
import sys

root = tkinter.Tk()
root.title(u"Fuwasaba archive")
root.geometry("400x300") # Windowサイズ


Static1 = tkinter.Label(text=u'過去シーズン構成ダウンロード')
Static1.pack()

# β3
def b3download(event):
    url='https://u.q-mc.xyz/SlrXLh'
    filename='β3.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖β3期ファイル')
Static1.place(y=50)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-1>",b3download)
Button.place(x=125, y=50)


# β5
def b5download(event):
    url='https://u.q-mc.xyz/27BLeG'
    filename='β5.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖β5期ファイル')
Static1.place(y=100)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-2>",b5download)
Button.place(x=125, y=100)



# β6
def b6download(event):
    url='https://u.q-mc.xyz/9iPcZH'
    filename='β6.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖β6期ファイル')
Static1.place(y=150)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-3>",b6download)
Button.place(x=125, y=150)



# s1
def s1download(event):
    url='https://u.q-mc.xyz/8cD5MB'
    filename='s1.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖新1期ファイル')
Static1.place(y=200)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-4>",s1download)
Button.place(x=125, y=200)



root.mainloop()
