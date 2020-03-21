import youtube_dl
import tkinter as tk
opts={'outtmpl':'./videos/%(title)s.%(ext)s',}

def ytdl(x):
    with youtube_dl.YoutubeDL(opts)as y:
      t=y.download([x])

box=tk.Tk()
box.title("YT_downloader")
box.geometry('300x70')


url=tk.Entry(box)
url.pack(padx=5,pady=5)

def ytl():
    v=url.get()
    url.delete(0,'end')
    if len(v)!=0:
        ytdl(v)
    else:
        print('Not Done!')




down=tk.Button(box,text='Download',command=ytl)
down.pack(padx=5,pady=5)


box.mainloop()




import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("tkinterVid28.py", base=base, icon="clienticon.ico")]

cx_Freeze.setup(
    name = "SeaofBTC-Client",
    options = {"build_exe": {"packages":["tkinter","matplotlib"], "include_files":["clienticon.ico"]}},
    version = "0.01",
    description = "Sea of BTC trading application",
    executables = executables
    )
