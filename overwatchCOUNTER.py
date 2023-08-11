from tkinter import *

def c_DVA():
    global choice
    choice = 'DVA'

def c_Doomfist():
    global choice
    choice = 'Doomfist'

def c_Junker_Queen():
    global choice
    choice = "Junker Queen"

def c_Ramatra():
    global choice
    choice = 'Ramatra'

def c_Orisa():
    global choice
    choice = 'Orisa'

def c_reinhardt():
    global choice
    choice = 'Reinhardt'

def c_Roadhog():
    global choice
    choice = 'Roadhog'

def c_sigma():
    global choice
    choice = 'Sigma'

def c_winston():
    global choice
    choice = "Winston"

def c_hammond():
    global choice
    choice = 'Wrecking Ball'

def c_zarya():
    global choice
    choice = 'Zarya'

def c_ashe():
    global choice
    choice = 'Ashe'

def c_bastion():
    global choice
    choice = 'Bastion'

def c_mcree():
    global choice
    choice = 'Mcree'

def c_echo():
    global choice
    choice = 'Echo'

def c_genji():
    global choice
    choice = 'Genji'

def c_hanzo():
    global choice
    choice = 'Hanzo'

def c_junkrat():
    global choice
    choice = 'Junkrat'

def c_mei():
    global choice
    choice = 'Mei'

def c_pharah():
    global choice
    choice = 'Pharah'

def c_reaper():
    global choice
    choice = 'Reaper'

def c_sojourn():
    global choice
    choice = 'Sojourn'

def c_soldier():
    global choice
    choice = 'Soldier'

def c_sombra():
    global choice
    choice = 'Sombra'

def c_Symmetra():
    global choice
    choice = 'Symmetra'

def c_Torbjorn():
    global choice
    choice = 'Torbjorn'


def c_Tracer():
    global choice
    choice = 'Tracer'

def c_Widowmaker():
    global choice
    choice = 'Widow maker'

def c_Ana():
    global choice
    choice = 'Ana'

def c_Baptiste():
    global choice
    choice = 'Baptiste'

def c_Brigitte():
    global choice
    choice = 'Brigitte'

def c_Kiriko():
    global choice
    choice = 'Kiriko'

def c_Lifeweaver():
    global choice
    choice = 'Lifeweaver'

def c_Lucio():
    global choice
    choice = 'Lucio'

def c_Mercy():
    global choice
    choice = 'Mercy'

def c_Moira():
    global choice
    choice = 'Moira'

def c_Zenyatta():
    global choice
    choice = 'Zenyatta'

window = Tk()
window.configure(bg='black')

DVA = Button(text='DVA', fg='dark red', bg='black', font="Courier 22 bold")
DVA.configure(command=c_DVA)
DVA.grid(row=2, column=0)

Doom = Button(text='Doom Fist', fg='red', bg='black', font="Courier 22 bold")
Doom.configure(command=c_Doomfist)
Doom.grid(row=2, column=1)

Junk = Button(text='Junker Queen', fg='orange', bg='black', font="Courier 22 bold")
Junk.configure(command=c_Junker_Queen)
Junk.grid(row=2, column=2)

Orisa = Button(text='Orisa', fg='yellow', bg='black', font="Courier 22 bold")
Orisa.configure(command=c_Orisa)
Orisa.grid(row=2, column=3)

Ram = Button(text='Ramattra', fg='light yellow', bg='black', font="Courier 22 bold")
Ram.configure(command=c_Ramatra)
Ram.grid(row=2, column=4)

Rein = Button(text='Reinhardt', fg='light green', bg='black', font="Courier 22 bold")
Rein.configure(command=c_reinhardt)
Rein.grid(row=2, column=5)

Hog = Button(text='Road Hog', fg='green', bg='black', font="Courier 22 bold")
Hog.configure(command=c_Roadhog)
Hog.grid(row=2, column=6)

sigma = Button(text='Sigma', fg='blue', bg='black', font="Courier 22 bold")
sigma.configure(command=c_sigma)
sigma.grid(row=3, column=0)

Win = Button(text='Winston', fg='light blue', bg='black', font="Courier 22 bold")
Win.configure(command=c_winston)
Win.grid(row=3, column=1)

Ball = Button(text='Wrecking ball', fg='magenta', bg='black', font="Courier 22 bold")
Ball.configure(command=c_hammond)
Ball.grid(row=3, column=2)

Zarya = Button(text='Zarya', fg='purple', bg='black', font="Courier 22 bold")
Zarya.configure(command=c_zarya)
Zarya.grid(row=3, column=3)

Ashe = Button(text='Ashe', fg='dark red', bg='black', font="Courier 22 bold")
Ashe.configure(command=c_ashe)
Ashe.grid(row=3, column=4)

bas = Button(text='Bastion', fg='red', bg='black', font="Courier 22 bold")
bas.configure(command=c_bastion)
bas.grid(row=3, column=5)

Mc = Button(text='Mcree', fg='yellow', bg='black', font="Courier 22 bold")
Mc.configure(command=c_mcree)
Mc.grid(row=3, column=6)

echo = Button(text='Echo', fg='light yellow', bg='black', font="Courier 22 bold")
echo.configure(command=c_echo)
echo.grid(row=4, column=0)

Genji = Button(text='Genji', fg='light green', bg='black', font="Courier 22 bold")
Genji.configure(command=c_genji)
Genji.grid(row=4, column=1)

hanzo = Button(text='Hanzo', fg='green', bg='black', font="Courier 22 bold")
hanzo.configure(command=c_hanzo)
hanzo.grid(row=4, column=2)

Junkrat = Button(text='Junkrat', fg='blue', bg='black', font="Courier 22 bold")
Junkrat.configure(command=c_junkrat)
Junkrat.grid(row=4, column=3)

Mei = Button(text='Mei', fg='light blue', bg='black', font="Courier 22 bold")
Mei.configure(command= c_mei)
Mei.grid(row=4, column=4)

Pharah = Button(text='Pharah', fg='magenta', bg='black', font="Courier 22 bold")
Pharah.configure(command=c_pharah)
Pharah.grid(row=4, column=5)

rea = Button(text='Reaper', fg='purple', bg='black', font="Courier 22 bold")
rea.configure(command=c_reaper)
rea.grid(row=4, column=6)

Sojourn = Button(text='Sojourn', fg='dark red', bg='black', font="Courier 22 bold")
Sojourn.configure(command=c_sojourn)
Sojourn.grid(row=5, column=0)

soldier = Button(text='Soldier 76', fg='red', bg='black', font="Courier 22 bold")
soldier.configure(command=c_soldier)
soldier.grid(row=5, column=1)

sombra = Button(text='Sombra', fg='orange', bg='black', font="Courier 22 bold")
sombra.configure(command=c_sombra)
sombra.grid(row=5, column=2)

sym = Button(text='Symmetra', fg='light yellow', bg='black', font="Courier 22 bold")
sym.configure(command=c_Symmetra)
sym.grid(row=5, column=3)

tor = Button(text='Torbjorn', fg='yellow', bg='black', font="Courier 22 bold")
tor.configure(command=c_Torbjorn)
tor.grid(row=5, column=4)

tra = Button(text='Tracer', fg='light green', bg='black', font="Courier 22 bold")
tra.configure(command=c_Tracer)
tra.grid(row=5, column=5)

wid = Button(text='Widow', fg='green', bg='black', font="Courier 22 bold")
wid.configure(command=c_Widowmaker)
wid.grid(row=5, column=6)

ana = Button(text='Ana', fg='light blue', bg='black', font="Courier 22 bold")
ana.configure(command=c_Ana)
ana.grid(row=6, column=0)

bap = Button(text='Baptist', fg='blue', bg='black', font="Courier 22 bold")
bap.configure(command=c_Baptiste)
bap.grid(row=6, column=1)

bri = Button(text='Brigitte', fg='magenta', bg='black', font="Courier 22 bold")
bri.configure(command=c_Brigitte)
bri.grid(row=6, column=2)

kir = Button(text='Kiriko', fg='Purple', bg='black', font="Courier 22 bold")
kir.configure(command=c_Kiriko)
kir.grid(row=6, column=3)

weaver = Button(text='Life W', fg='dark red', bg='black', font="Courier 22 bold")
weaver.configure(command=c_Lifeweaver)
weaver.grid(row=6, column=4)

luc = Button(text='Lucio', fg='red', bg='black', font="Courier 22 bold")
luc.configure(command=c_Lucio)
luc.grid(row=6, column=5)

mer = Button(text='Mercy', fg='orange', bg='black', font="Courier 22 bold")
mer.configure(command=c_Mercy)
mer.grid(row=6, column=6)

moi = Button(text='Moira', fg='yellow', bg='black', font="Courier 22 bold")
moi.configure(command=c_Moira)
moi.grid(row=7, column=3)

zen = Button(text='Zenyatta', fg='light yellow', bg='black', font="Courier 22 bold")
zen.configure(command=c_Zenyatta)
zen.grid(row=7, column=4)

def start_push():
    new_window = Toplevel()
    new_window.configure(bg='black')

    new_label = Label(new_window, text='Play These Heros:', font="Courier 22 bold", fg='Red', bg='black')
    new_label.grid(row=0)

    global choice

    if choice == 'Ashe':
        display = Label(new_window, text='Doomfist, Echo, Genji, Reaper, Roadhog, Soldier: 76, Sombra, Tracer', fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Bastion':
        display = Label(new_window, text='Ana, Genji, Junkrat, Pharah, Roadhog, Sombra, Tracer, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Mcree':
        display = Label(new_window, text='Ana, Ashe, Bastion, Genji, Hanzo, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Echo':
        display = Label(new_window, text='Ana, Ashe, Baptiste, Cassidy, D.Va, Junker Queen, Moira, Reaper, Soldier: 76, Widowmaker, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Genji':
        display = Label(new_window, text='Brigitte, Mei, Moira, Symmetra, Winston, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Hanzo':
        display = Label(new_window, text='D.Va, Genji, Lucio, Moira, Pharah, Sombra, Tracer, Wrecking Ball',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Junkrat':
        display = Label(new_window, text='Ashe, D.va, Cassidy, Echo, Genji, Lucio, Pharah, Reaper, Roadhog, Soldier: 76, Sombra, Tracer, Wrecking Ball',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Mei':
        display = Label(new_window, text='Echo, Pharah, Reaper, Sombra, Tracer',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Pharah':
        display = Label(new_window, text='Ana, Ashe, Baptiste, Cassidy, D.va, Soldier: 76, Sombra, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Reaper':
        display = Label(new_window, text='Ana, Ashe, Echo, Junkrat, Pharah, Ramattra, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Sojourn':
        display = Label(new_window, text='D.Va, Lucio, Orisa, Reaper, Tracer, Sigma, Sombra, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Soldier':
        display = Label(new_window, text='Ana, Cassidy, D.va, Junkrat, Reaper, Roadhog, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Sombra':
        display = Label(new_window, text='Ana, Brigitte, Junkrat, Mei, Moira, Pharah, Winston, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Symmetra':
        display = Label(new_window, text='Echo, Junkrat, Pharah, Reaper, Sombra, Tracer, Winston',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Torbjorn':
        display = Label(new_window, text='Ana, Bastion, Junkrat, Pharah, Sombra, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Tracer':
        display = Label(new_window, text='Ana, Junkrat, Pharah, Sombra, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Widow maker':
        display = Label(new_window, text='D.va, Genji, Sombra, Tracer, Winston',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'DVA':
        display = Label(new_window, text='Brigitte, Doomfist, Moira, Reaper, Roadhog, Sigma, Symmetra, Winston, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Doomfist':
        display = Label(new_window, text='Brigitte, Doomfist, Moira, Reaper, Roadhog, Sigma, Symmetra, Winston, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'DVA':
        display = Label(new_window, text='Brigitte, Doomfist, Moira, Reaper, Roadhog, Sigma, Symmetra, Winston, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Junker Queen':
        display = Label(new_window, text='Ana, Ashe, Baptiste, Cassidy, Pharah, Soldier: 76, Widowmaker, Zenyatta',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Orisa':
        display = Label(new_window, text='Ana, Ashe, Baptiste, D.Va, Echo, Hanzo, Kiriko, Pharah, Reaper, Sojourn, Sombra, Soldier: 76, Widowmaker, Zenyatta',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Ramatra':
        display = Label(new_window, text='Ana, Bastion, D.Va, Kiriko, Orisa, Roadhog, Symmetra, Tracer, Zenyatta',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Reinhardt':
        display = Label(new_window, text='	Ana, Brigitte, Junkrat, Mei, Pharah, Reaper, Sombra, Tracer',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Roadhog':
        display = Label(new_window, text='Ana, Genji, Echo, Junkrat, Pharah, Reaper, Sombra, Tracer, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Sigma':
        display = Label(new_window, text='Genji, Lucio, Moira, Sombra, Symmetra, Tracer, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Winston':
        display = Label(new_window, text='Ana, Brigitte, Mei, Roadhog',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Wrecking Ball':
        display = Label(new_window, text='Ana, Brigitte, Mei, Roadhog, Torbjorn',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Zarya':
        display = Label(new_window, text='Ashe, Bastion, D.Va, Echo, Pharah, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Ana':
        display = Label(new_window, text='Echo, Genji, Lucio, Moira, Pharah, Sombra, Tracer',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Baptiste':
        display = Label(new_window, text='Ana, Echo, Genji, Hanzo, Lucio, Pharah, Reaper, Roadhog, Sombra, Tracer',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Brigette':
        display = Label(new_window, text='Cassidy, Bastion, D.Va, Echo, Genji, Junkrat, Moira, Pharah, Sombra, Tracer, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Kiriko':
        display = Label(new_window, text='Ana, Ashe, Baptiste, Cassidy, Doomfist, Genji, Moira, Reaper, Sojourn, Tracer, Widowmaker, Wrecking Ball',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Lucio':
        display = Label(new_window, text='Ashe, Cassidy, Moira, Soldier: 76, Symmetra, Torbjorn, Winston, Zarya',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Mercy':
        display = Label(new_window, text='Ana, Ashe, Baptiste, Cassidy, Genji, Moira, Reaper, Roadhog, Soldier: 76, Winston, Wrecking Ball',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Moira':
        display = Label(new_window, text='Ana, Ashe, Echo, Genji, Pharah, Reaper, Sojourn, Sombra, Soldier: 76, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Zenyatta':
        display = Label(new_window, text='D.Va, Echo, Genji, Pharah, Reaper, Sigma, Tracer, Widowmaker',
                        fg='yellow', bg='black')
        display.grid(row=1)

    if choice == 'Lifeweaver':
        display = Label(new_window, text='D.Va, Sigma, Reinhardt',
                        fg='yellow', bg='black')
        display.grid(row=1)


start = Button(window, text='                        -- Overwatch Counters --                           ', font="Courier 22 bold", fg='black', bg='red')
start.grid(row=0, column=0, columnspan=10)
start.configure(command=start_push)

window.mainloop()