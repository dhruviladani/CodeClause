from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
        songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
        songs_list.grid(columnspan=9)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Add = Button(window, text = 'Add Song', width = 10, font = ('Times', 10), command = self.addsongs)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=55,y=60);Add.place(x=165,y=60)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def addsongs(self): 
        temp_song=filedialog.askopenfilenames(initialdir="MusicPlayer/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()

app= MusicPlayer(root)
root.mainloop()

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)
root.mainloop()
#add many songs to the playlist of python mp3 player

