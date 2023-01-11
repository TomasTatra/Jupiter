#! /usr/bin/env python
import os
import subprocess

print('Start');
stream = os.popen('ps -u  mustar| grep "python" | grep -o "^ *[0-9]*"')
default = stream.read();
default = default.split();
default2=[];
for i in default:
	 default2.append(int(i));
default = default2;
print(default2);


def movenexttowall():
    stoptask()
    comand1 = subprocess.Popen(['python' , '/home/mustar/catkin_ws/src/tomas_showcase/src/Moving_next_wall.py'])
    stream = os.popen('ps -u  mustar| grep "python" | grep -o "^ *[0-9]*"')
    movenexttowall = stream.read()
    print(movenexttowall);

def forward():
    stoptask()
    comand1 = subprocess.Popen(['python' , '/home/mustar/catkin_ws/src/tomas_showcase/src/forward.py'])
    stream = os.popen('ps -u  mustar| grep "python" | grep -o "^ *[0-9]*"')
    movenexttowall = stream.read()
    print(movenexttowall);

def rotate(x):
    stoptask()
    comand1 = subprocess.Popen(['python' , '/home/mustar/catkin_ws/src/tomas_showcase/src/rotate_'+ x +'.py'])
    stream = os.popen('ps -u  mustar| grep "python" | grep -o "^ *[0-9]*"')
    movenexttowall = stream.read()
    print(movenexttowall);

def stoptask():
    stream = os.popen('ps -u  mustar| grep "python" | grep -o "^ *[0-9]*"')
    stoped = stream.read()
    stoped = stoped.split();
    for i in stoped:
	if (int(i) not in default):
		print(i);
		os.system('kill -TERM ' + i);
    #Moving_next_wall.GoToWall();

import Tkinter as tk
import tkFont;

root = tk.Tk()
root.geometry("2000x1000")

helv30 = tkFont.Font(family="Helvetica",size=32,weight="bold")
helv20 = tkFont.Font(family="Helvetica",size=30,weight="bold")
helv10 = tkFont.Font(family="Helvetica",size=20,weight="bold")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="QUIT", fg="white", bg="#8b0000",
                   command=quit, font=helv30, height = 2, borderwidth=6);
button.grid(sticky="news",row = 0 , column =3, columnspan=2);

wall= tk.Button(frame, text="go if is possible",font=helv10,
                   command =movenexttowall,bg='#add8e6', borderwidth=6) 
wall.grid(sticky="news",row = 5 , column =3, columnspan = 2);

dopredu= tk.Button(frame, text="forward",font=helv20,
                   command =forward, width =40, bg='#add8e6', borderwidth=6) 
dopredu.grid(sticky="news",row = 1 , column =3,rowspan = 3, columnspan=2);

right= tk.Button(frame, text="right",font=helv20,
                   command =lambda: rotate('l'), bg='#add8e6', borderwidth=6) 
right.grid(sticky="news",row = 4 , column =4);

left= tk.Button(frame, text="left",font=helv20,
                   command =lambda: rotate('r'),bg='#add8e6', borderwidth=6) 
left.grid(sticky="news",row = 4 , column =3);

button2 = tk.Button(frame, text="STOP", font=helv30, fg="white",
                   command=stoptask, bg="#8b0000", borderwidth=6)
button2.grid(sticky="news", row = 6 , column =3, columnspan = 2,rowspan = 7);
root.mainloop()



