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
    url='https://cdn.discordapp.com/attachments/1226705659022676049/1226708224762318938/3.zip?ex=6625c00f&is=66134b0f&hm=de343276afd5541eb60f9895f8338d8e16363eac29699fb35babb92c2b86e402&'
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
    url='https://cdn.discordapp.com/attachments/1226705659022676049/1226708226792488960/5.zip?ex=6625c010&is=66134b10&hm=ccd5551aa8ab3cfde8aece590cf827ec583a611fec743e61822cc284156087db&'
    filename='β5.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖β5期ファイル')
Static1.place(y=100)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-1>",b5download)
Button.place(x=125, y=100)



# β6
def b6download(event):
    url='https://cdn.discordapp.com/attachments/1226705659022676049/1226708297260990557/6.zip?ex=6625c021&is=66134b21&hm=61ae36332778283be8e39d2f0abfde084e8c2fb8c087cd2de1b63ee91afb3701&'
    filename='β6.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖β6期ファイル')
Static1.place(y=150)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-1>",b6download)
Button.place(x=125, y=150)



# s1
def s1download(event):
    url='https://cdn.discordapp.com/attachments/1226705659022676049/1226705733115052105/1.zip?ex=6625bdbd&is=661348bd&hm=6861d521e80b13b5fcd33cf4d3559af171c2793d6c5990ae6199ea23b2fd8db7&'
    filename='s1.zip'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

Static1 = tkinter.Label(text=u'ふわ鯖新1期ファイル')
Static1.place(y=200)

Button = tkinter.Button(text=u'download', width=20)
Button.bind("<Button-1>",s1download)
Button.place(x=125, y=200)



root.mainloop()
