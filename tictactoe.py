from os import system,remove
import time
import random
from pyfiglet import figlet_format 
import pygame
import threading
from rich import print as rprint
pygame.mixer.init()
m_sel = pygame.mixer.Sound('sounds/menu select.mp3')
bg_music = pygame.mixer.Sound('sounds/bg music.mp3')
m_deny = pygame.mixer.Sound('sounds/menu deny.mp3')
place_sfx = pygame.mixer.Sound('sounds/place sfx.mp3')
win_sfx = pygame.mixer.Sound('sounds/win SFX.mp3')
loss_sfx = pygame.mixer.Sound('sounds/loss sfx.mp3')
game_draw = pygame.mixer.Sound('sounds/game draw.mp3')
game_play = pygame.mixer.Sound('sounds/Play Music.mp3')
try:
    s1 = open("stats_sp.txt","r")
    stats = s1.readlines()[0]
    win,loss,draws = stats.split(",")
    win = int(win)
    loss = int(loss)
    draws = int(draws)
except Exception:
    win = 0
    loss = 0
    draws = 0
    s1 = open("stats_sp.txt","w")
    s1.write(str(win)+","+ str(loss)+","+ str(draws))
    s1.flush()
try:
    s2 = open("stats_mp.txt","r")
    stats2 = s2.readlines()[0]
    X_win,O_win,multi_draws = stats2.split(",")
    X_win = int(X_win)
    O_win = int(O_win)
    multi_draws = int(multi_draws)
except:
    X_win = 0
    O_win = 0
    multi_draws = 0
    s2 = open("stats_mp.txt","w")
    s2.write(str(X_win)+","+ str(O_win)+","+ str(multi_draws))
    s2.flush()
AItry = 1
tries = 1
firsttry = 1
label = 0
pos = []
AI_pos = []
ulb = 0
slb = 0
multi_tries = 1
firstmus = 1
def chance1():
    choice2 = [4,4,4,4,6,9]
    randchoice2 = random.choice(choice2)
    return randchoice2
def chance2():
    choice2 = [4,6,7,9,4,6,4,6]
    randchoice2 = random.choice(choice2)
    return randchoice2
def chance3():
    chance1 = [0,1]
    randchoice3 = random.choice(chance1)
    return randchoice3
def chance4():
    ptsign = [4,8]
    ptsign_one = random.choice(ptsign)
    return ptsign_one
def chance5():
    choicelast = [1,1,1,2]
    chclast = random.choice(choicelast)
    return chclast
def chance6():
    choicelast = [2,2,2,8]
    chclast = random.choice(choicelast)
    return chclast
def chance7():
    choicelast = [2,8]
    chclast = random.choice(choicelast)
    return chclast
def chance8():
    choicelast = [2,2,2,2,3]
    chclast = random.choice(choicelast)
    return chclast
def chance9():
    choice2 = [4,4,4,4,6,3]
    randchoice2 = random.choice(choice2)
    return randchoice2
def chance10():
    choice2 = [1,3,4,6,4,6,4,6]
    randchoice2 = random.choice(choice2)
    return randchoice2
def sounds(num,count = 0):
    global firstmus
    if num == 1:
        m_sel.set_volume(2)
        m_sel.play() 
    elif num == 2:
        if firstmus == 1:
            firstmus = 0
            game_play.fadeout(2000)
            bg_music.play(loops = -1,fade_ms = 2000)
            bg_music.set_volume(0.5)
    elif num == 3:
        m_deny.set_volume(2)
        m_deny.play()
    elif num == 4:
        place_sfx.set_volume(2)
        place_sfx.play()
    elif num == 5:
        win_sfx.set_volume(2)
        win_sfx.play()
    elif num == 6:
        loss_sfx.set_volume(2)
        loss_sfx.play()
    elif num == 7:
        game_draw.set_volume(2)
        game_draw.play()
    if count == 1:
        bg_music.fadeout(500)
        game_play.set_volume(0.05)
        game_play.play(loops = -1,fade_ms = 2000)
        firstmus = 1
class TicTacToe: 
    def __init__(self):
        t1 = threading.Thread(target=sounds, args=(2,))
        t1.start()
        while True:
            system("cls")
            print(figlet_format("       < TIC TAC TOE >",font = "standard"))
            rprint("[bold]\n1. Start The Game\n\n2. Stats\n\n3. Credits\n\n0. Exit\n\n")
            mmenu=input()
            if mmenu=="1":
                t1 = threading.Thread(target=sounds, args=(1,))
                t1.start()
                while True:
                    system("cls")
                    print(figlet_format("       < TIC TAC TOE >",font = "standard"))
                    rprint("[bold]\n1. Player VS AI\n\n2. Player VS Player \n\n\n0. Back\n\n")
                    mmenu2=input()
                    if mmenu2 == "1":
                        t1 = threading.Thread(target=sounds, args=(1,1))
                        t1.start()
                        self.TicTacToeLayout()
                    elif mmenu2 == "2":
                        t1 = threading.Thread(target=sounds, args=(1,1))
                        t1.start()
                        self.TicTacToePvP()
                    elif mmenu2 == "0":
                        t1 = threading.Thread(target=sounds, args=(1,))
                        t1.start()
                        break
                    else:
                        t1 = threading.Thread(target=sounds, args=(3,))
                        t1.start()
                        rprint("[red]You have entered the wrong output!")
                        time.sleep(2)
                        continue
            elif mmenu=="2":
                t1 = threading.Thread(target=sounds, args=(1,))
                t1.start()
                self.Stats()
            elif mmenu=="3":
                t1 = threading.Thread(target=sounds, args=(1,))
                t1.start()
                self.Credits()
            elif mmenu=="0":
                t1 = threading.Thread(target=sounds, args=(1,))
                t1.start()
                system("cls")
                print("Quitting!")
                bg_music.fadeout(1000)
                time.sleep(1)
                exit()
            else:
                t1 = threading.Thread(target=sounds, args=(3,))
                t1.start()
                rprint("[red]You have entered the wrong output!")
                time.sleep(2)
                continue
    def game_reset_and_file_update_sp(self):
        global tries , AItry , label , firsttry , ulb , slb , pos , AI_pos , s1
        tries = 1
        AItry = 1
        label = 0
        firsttry = 1
        ulb = 0
        slb = 0
        pos = []
        AI_pos = []
        s1.close()
        remove("stats_sp.txt")
        s1 = open("stats_sp.txt","w")
        s1.write(str(win) +","+ str(loss) +","+ str(draws))
        s1.flush()
    def game_reset_and_file_update_mp(self):
        global s2, X_win, O_win, multi_draws, multi_tries
        s2.close()
        remove("stats_mp.txt")
        s2 = open("stats_mp.txt","w")
        s2.write(str(X_win)+","+ str(O_win)+","+ str(multi_draws))
        s2.flush()
        multi_tries = 0
    def Stats(self):
        global win , loss , draws , X_win , O_win , multi_draws
        while True:
            system("cls")
            print(figlet_format("       < STATS >",font = "standard"))
            rprint("\n[bold black on white][big]Player VS AI Mode:-")
            rprint("[green]Wins:",win,"\n[red]Loss:",loss,"\n[yellow]Draw:",draws)
            rprint("\n[bold black on white][big]Player VS Player Mode:-")
            rprint("[green]Player[/green] [bright_blue]X[/bright_blue] [green]Wins:[/green]",X_win,"\n[green]Player[/green] [dark_orange]O[/dark_orange] [green]Wins:[/green]",O_win,"\n[yellow]Draw:",multi_draws)
            rprint("[bold]\n0. Go Back\n\n")
            mmenu=input()
            if mmenu=="0":
                t1 = threading.Thread(target=sounds, args=(1,))
                t1.start()
                self.__init__()
            else:
                t1 = threading.Thread(target=sounds, args=(3,))
                t1.start()
                rprint("[red]You have entered the wrong output!")
                time.sleep(2)
                continue
    def Credits(self):
        while True:
            system("cls")
            print(figlet_format("       < CREDITS >",font = "standard"))
            rprint("[bold]Made by:[/bold] [green]Shaheer Kashif")
            rprint("[bold]\n0. Go Back\n\n")
            mmenu=input()
            if mmenu=="0":
                t1 = threading.Thread(target=sounds, args=(1,))
                t1.start()
                self.__init__()
            else:
                t1 = threading.Thread(target=sounds, args=(3,))
                t1.start()
                rprint("[red]You have entered the wrong output!")
                time.sleep(2)
                continue
    def print_format(self,mode):
        global multi_tries,tries
        system("cls")
        if mode == 1:
            if tries > 1:
                if "X" in self.row1 or "X" in self.row2 or "X" in self.row3:
                    self.row1_temp = self.row1_temp.replace("X","[bright_blue]X[/bright_blue]")
                    self.row2_temp = self.row2_temp.replace("X","[bright_blue]X[/bright_blue]")
                    self.row3_temp = self.row3_temp.replace("X","[bright_blue]X[/bright_blue]")
                if "O" in self.row1 or "O" in self.row2 or "O" in self.row3:
                    self.row1_temp = self.row1_temp.replace("O","[dark_orange]O[/dark_orange]")
                    self.row2_temp = self.row2_temp.replace("O","[dark_orange]O[/dark_orange]")
                    self.row3_temp = self.row3_temp.replace("O","[dark_orange]O[/dark_orange]")
                rprint("[bold]"+self.row1_temp+"\n"+self.row2_temp+"\n"+self.row3_temp)
            else:
                rprint("[bold]"+self.row1+"\n"+self.row2+"\n"+self.row3)
        elif mode == 2:
            if multi_tries > 1:
                if "X" in self.row1 or "X" in self.row2 or "X" in self.row3:
                    self.row1_temp = self.row1_temp.replace("X","[bright_blue]X[/bright_blue]")
                    self.row2_temp = self.row2_temp.replace("X","[bright_blue]X[/bright_blue]")
                    self.row3_temp = self.row3_temp.replace("X","[bright_blue]X[/bright_blue]")
                if "O" in self.row1 or "O" in self.row2 or "O" in self.row3:
                    self.row1_temp = self.row1_temp.replace("O","[dark_orange]O[/dark_orange]")
                    self.row2_temp = self.row2_temp.replace("O","[dark_orange]O[/dark_orange]")
                    self.row3_temp = self.row3_temp.replace("O","[dark_orange]O[/dark_orange]")
                rprint("[bold]"+self.row1_temp+"\n"+self.row2_temp+"\n"+self.row3_temp)
            else:
                rprint("[bold]"+self.row1+"\n"+self.row2+"\n"+self.row3)
    def TicTacToePvP(self):
        switch = 0
        val_lis = [1,2,3,4,5,6,7,8,9]
        global X_win, O_win, multi_tries, multi_draws
        self.row1="1 | 2 | 3"
        self.row2="4 | 5 | 6"
        self.row3="7 | 8 | 9"
        self.row1_temp = self.row1
        self.row2_temp = self.row2
        self.row3_temp = self.row3
        while True:
            if ((self.row1 == "X | X | X" or self.row2 == "X | X | X" or self.row3 == "X | X | X") or (self.row1[0:3] == "X |" and self.row2[0:3]=="X |" and self.row3[0:3]=="X |") or (self.row1[4:7] == "X |" and self.row2[4:7]=="X |" and self.row3[4:7]=="X |") or (self.row1[8] == "X" and self.row2[8]=="X" and self.row3[8]=="X") or (self.row1[0:3] == "X |" and self.row2[4:7]=="X |" and self.row3[8]=="X") or (self.row1[8]=="X" and self.row2[4:7]=="X |" and self.row3[0:3] == "X |")) or ((self.row1 == "O | O | O" or self.row2 == "O | O | O" or self.row3 == "O | O | O") or (self.row1[0:3] == "O |" and self.row2[0:3]=="O |" and self.row3[0:3]=="O |") or (self.row1[4:7] == "O |" and self.row2[4:7]=="O |" and self.row3[4:7]=="O |") or (self.row1[8] == "O" and self.row2[8]=="O" and self.row3[8]=="O") or (self.row1[0:3] == "O |" and self.row2[4:7]=="O |" and self.row3[8]=="O") or (self.row1[8]=="O" and self.row2[4:7]=="O |" and self.row3[0:3] == "O |")) or multi_tries >= 10:
                self.print_format(2)
                if (self.row1 == "X | X | X" or self.row2 == "X | X | X" or self.row3 == "X | X | X") or (self.row1[0:3] == "X |" and self.row2[0:3]=="X |" and self.row3[0:3]=="X |") or (self.row1[4:7] == "X |" and self.row2[4:7]=="X |" and self.row3[4:7]=="X |") or (self.row1[8] == "X" and self.row2[8]=="X" and self.row3[8]=="X") or (self.row1[0:3] == "X |" and self.row2[4:7]=="X |" and self.row3[8]=="X") or (self.row1[8]=="X" and self.row2[4:7]=="X |" and self.row3[0:3] == "X |"):
                    X_win += 1
                    rprint("\n[green]Player [/green][bright_blue]X[/bright_blue][green] Wins!")
                    t1 = threading.Thread(target=sounds, args=(5,))
                    t1.start()
                elif (self.row1 == "O | O | O" or self.row2 == "O | O | O" or self.row3 == "O | O | O") or (self.row1[0:3] == "O |" and self.row2[0:3]=="O |" and self.row3[0:3]=="O |") or (self.row1[4:7] == "O |" and self.row2[4:7]=="O |" and self.row3[4:7]=="O |") or (self.row1[8] == "O" and self.row2[8]=="O" and self.row3[8]=="O") or (self.row1[0:3] == "O |" and self.row2[4:7]=="O |" and self.row3[8]=="O") or (self.row1[8]=="O" and self.row2[4:7]=="O |" and self.row3[0:3] == "O |"):
                    O_win += 1
                    rprint("\n[green]Player [/green][dark_orange]O[/dark_orange][green] Wins!")
                    t1 = threading.Thread(target=sounds, args=(5,))
                    t1.start()
                elif multi_tries >= 10:
                    multi_draws += 1
                    rprint("\n[yellow]It's a draw!")
                self.game_reset_and_file_update_mp()
                rprint("Would you like to continue? [yellow](Y/N): ",end = "")
                count=input()
                if count.upper()=="Y":
                    t1 = threading.Thread(target=sounds, args=(1,))
                    t1.start()
                    self.TicTacToePvP()
                elif count.upper()=="N":
                    t1 = threading.Thread(target=sounds, args=(1,))
                    t1.start()
                    self.__init__()
                else:
                    t1 = threading.Thread(target=sounds, args=(3,))
                    t1.start()
                    rprint("[red]That's not a Valid Input....\n")
                    time.sleep(2)
                    continue
            else:
                if switch == 0:
                    sign = "X"
                    format_sign = "[bright_blue]X[/bright_blue]"
                    switch = 1
                elif switch == 1:
                    sign = "O"
                    format_sign = "[dark_orange]O[/dark_orange]"
                    switch = 0
                while True:
                    self.print_format(2)
                    try:
                        rprint("\nPlayer "+format_sign+", Enter the input here: ",end = "")
                        self.num=input()
                        temp = self.num
                        self.num = int(self.num)
                        if self.num in val_lis:
                            if self.num >= 1 and self.num <= 3:
                                self.row1 = self.row1.replace(str(self.num),sign)
                                self.row1_temp = self.row1
                            elif self.num >= 4 and self.num <= 6:
                                self.row2 = self.row2.replace(str(self.num),sign)
                                self.row2_temp = self.row2
                            elif self.num >= 7 and self.num <= 9:
                                self.row3 = self.row3.replace(str(self.num),sign)
                                self.row3_temp = self.row3
                            val_lis.remove(self.num)
                            t1 = threading.Thread(target=sounds, args=(4,))
                            t1.start()
                            multi_tries += 1
                            print("Processing...")
                            time.sleep(0.5)
                            break
                        else:
                            t1 = threading.Thread(target=sounds, args=(3,))
                            t1.start()
                            rprint("[red]That's not a Valid Input....\n")
                            time.sleep(2)
                            continue
                    except ValueError:
                        if temp.upper() == "Q" or "QU" or "QUI" or "QUIT":
                            t1 = threading.Thread(target=sounds, args=(1,))
                            t1.start()
                            rprint("\nAre you sure you want to quit? [yellow](Y/N): ",end = "")
                            quit_input = input()
                            if quit_input.upper() == "Y":
                                t1 = threading.Thread(target=sounds, args=(1,))
                                t1.start()
                                self.__init__()
                            elif quit_input.upper() == "N":
                                t1 = threading.Thread(target=sounds, args=(1,))
                                t1.start()
                                continue
                            else:
                                t1 = threading.Thread(target=sounds, args=(3,))
                                t1.start()
                                rprint("That's the wrong input dummy...[red]Quitting Anyway.")
                                time.sleep(1.5)
                                self.__init__()
                        else:
                            t1 = threading.Thread(target=sounds, args=(3,))
                            t1.start()
                            rprint("[red]That's not a Valid Input....\n")
                            time.sleep(2)
                            continue
    def TicTacToeLayout(self):
        global tries , win , loss , draws , pos, AItry , label , firsttry , ch1, ch2 , ch3 , ch4 , ch5 , ch6 ,ch7 , ch8 , ch9, ch10 ,slb ,ulb, pos, AI_pos ,s1
        ch1 = chance1()
        ch2 = chance2()
        ch3 = chance3()
        ch4 = chance4()
        ch5 = chance5()
        ch6 = chance6()
        ch7 = chance7()
        ch8 = chance8()
        ch9 = chance9()
        ch10 = chance10()
        cond = 0
        self.row1="1 | 2 | 3"
        self.row2="4 | 5 | 6"
        self.row3="7 | 8 | 9"
        self.row1_temp = self.row1
        self.row2_temp = self.row2
        self.row3_temp = self.row3
        while True:
            self.print_format(1)
            if ((self.row1 == "O | O | O" or self.row2 == "O | O | O" or self.row3 == "O | O | O") or (self.row1[0:3] == "O |" and self.row2[0:3]=="O |" and self.row3[0:3]=="O |") or (self.row1[4:7] == "O |" and self.row2[4:7]=="O |" and self.row3[4:7]=="O |") or (self.row1[8] == "O" and self.row2[8]=="O" and self.row3[8]=="O") or (self.row1[0:3] == "O |" and self.row2[4:7]=="O |" and self.row3[8]=="O") or (self.row1[8]=="O" and self.row2[4:7]=="O |" and self.row3[0:3] == "O |")) or cond == 1 or cond == 2:
                if (self.row1 == "O | O | O" or self.row2 == "O | O | O" or self.row3 == "O | O | O") or (self.row1[0:3] == "O |" and self.row2[0:3]=="O |" and self.row3[0:3]=="O |") or (self.row1[4:7] == "O |" and self.row2[4:7]=="O |" and self.row3[4:7]=="O |") or (self.row1[8] == "O" and self.row2[8]=="O" and self.row3[8]=="O") or (self.row1[0:3] == "O |" and self.row2[4:7]=="O |" and self.row3[8]=="O") or (self.row1[8]=="O" and self.row2[4:7]=="O |" and self.row3[0:3] == "O |"):
                    t1 = threading.Thread(target=sounds, args=(6,))
                    t1.start()
                    loss += 1
                    rprint("\n[red]You Lost, The AI Won!")
                elif cond == 1:
                    t1 = threading.Thread(target=sounds, args=(5,))
                    t1.start()
                    win += 1
                    rprint("\n[green]You Won, The AI Lost!")
                elif cond == 2:
                    t1 = threading.Thread(target=sounds, args=(7,))
                    t1.start()
                    draws += 1
                    rprint("\n[yellow]It's a Draw! No one won...")
                self.game_reset_and_file_update_sp()
                rprint("Would you like to continue? [yellow](Y/N): ",end = "")
                count=input()
                if count.upper()=="Y":
                    t1 = threading.Thread(target=sounds, args=(1,))
                    t1.start()
                    self.TicTacToeLayout()
                elif count.upper()=="N":
                    t1 = threading.Thread(target=sounds, args=(1,))
                    t1.start()
                    self.__init__()
                else:
                    t1 = threading.Thread(target=sounds, args=(3,))
                    t1.start()
                    rprint("[red]That's not a Valid Input....\n")
                    time.sleep(2)
                    continue
            else:
                try:
                    self.num=input("\nEnter the input here: ")
                    temp = self.num
                    self.num = int(self.num)
                    if self.num >= 1 and self.num <= 9:
                        if self.num >= 1 and self.num <= 3:
                            pos = [self.row1.index(str(self.num)),1]
                            self.row1 = self.row1.replace(str(self.num),"X")
                            self.row1_temp = self.row1
                        elif self.num >= 4 and self.num <= 6:
                            pos = [self.row2.index(str(self.num)),2]
                            self.row2 = self.row2.replace(str(self.num),"X")
                            self.row2_temp = self.row2
                        elif self.num >= 7 and self.num <= 9:
                            pos = [self.row3.index(str(self.num)),3]
                            self.row3 = self.row3.replace(str(self.num),"X")
                            self.row3_temp = self.row3
                        t1 = threading.Thread(target=sounds, args=(4,))
                        t1.start()
                        if (self.row1 == "X | X | X" or self.row2 == "X | X | X" or self.row3 == "X | X | X") or (self.row1[0:3] == "X |" and self.row2[0:3]=="X |" and self.row3[0:3]=="X |") or (self.row1[4:7] == "X |" and self.row2[4:7]=="X |" and self.row3[4:7]=="X |") or (self.row1[8] == "X" and self.row2[8]=="X" and self.row3[8]=="X") or (self.row1[0:3] == "X |" and self.row2[4:7]=="X |" and self.row3[8]=="X") or (self.row1[8]=="X" and self.row2[4:7]=="X |" and self.row3[0:3] == "X |"):
                            cond = 1
                            continue
                        elif tries >= 9:
                            cond = 2
                            continue
                        else:
                            tries += 1
                            self.AIBot()
                            t1 = threading.Thread(target=sounds, args=(4,))
                            t1.start()
                            self.row1_temp = self.row1
                            self.row2_temp = self.row2
                            self.row3_temp = self.row3
                            continue        
                    else:
                        t1 = threading.Thread(target=sounds, args=(3,))
                        t1.start()
                        rprint("[red]That's not a Valid Number....\n")
                        time.sleep(2)
                        continue
                except ValueError:
                    if temp.upper() == "Q" or temp.upper() == "QU" or temp.upper() == "QUI" or temp.upper() == "QUIT":
                        rprint("\nAre you sure you want to quit? This will result in a loss.\n[yellow](Y/N): ",end = "")
                        quit_input = input()
                        if quit_input.upper() == "Y":
                            t1 = threading.Thread(target=sounds, args=(1,))
                            t1.start()
                            loss += 1
                            self.game_reset_and_file_update_sp()
                            self.__init__()
                        elif quit_input.upper() == "N":
                            t1 = threading.Thread(target=sounds, args=(1,))
                            t1.start()
                            continue
                        else:
                            t1 = threading.Thread(target=sounds, args=(3,))
                            t1.start()
                            rprint("That's the wrong input dummy...[red]Quitting Anyway.")
                            time.sleep(1.5)
                            loss += 1
                            self.game_reset_and_file_update_sp()
                            self.__init__()
                    else:
                        t1 = threading.Thread(target=sounds, args=(3,))
                        t1.start()
                        rprint("[red]That's not a Valid Input....\n")
                        time.sleep(2)
                        continue
    def AIBot(self):
        global AItry , tries , firsttry , label , AI_pos , ch1 , ch2 , ch3 , ch4 , ch5 , ch6 , ch7 , ch8 , slb , ulb , ch9 , ch10
        rprint("[yellow]AI[/yellow] is thinking.\r")
        time.sleep(1)
        if AItry == 1:
            if self.row2[4]!="X":
                self.row2 = self.row2.replace("5","O")
            else:
                ch = [1,2,3,4]
                randchoice=random.choice(ch)
                if randchoice==1:
                    self.row1=self.row1.replace("1","O")
                    AI_pos = [1,1]
                elif randchoice==2:
                    self.row1=self.row1.replace("3","O")
                    AI_pos = [3,1]
                elif randchoice==3:
                    self.row3=self.row3.replace("7","O")
                    AI_pos = [7,3]
                elif randchoice==4:
                    self.row3=self.row3.replace("9","O")
                    AI_pos = [9,3]
        elif AItry >= 2:
            if (self.row1[4] == "X" and self.row1[0] == "X") and (firsttry == 1 or label == 1):
                if firsttry == 1:
                    label = 1
                self.row1 = self.row1.replace("3","O")
                if self.row3[0] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("7","O")
                elif self.row3[0] == "X" and AItry >= 3:
                    if ch1 >= 4 and ch1 <= 6:
                        self.row2 = self.row2.replace(str(ch1),"O")
                        AI_pos = [ch1,2]
                    elif ch1 >= 7 and ch1 <= 9:
                        self.row3 = self.row3.replace(str(ch1),"O")
                        AI_pos = [ch1,3]
                    if AItry >= 4:
                        if AI_pos == [6,2] or AI_pos == [9,3]:
                            if self.row2[0] != "X":
                                self.row2 = self.row2.replace("4","O")
                        elif AI_pos == [4,2]:
                            if self.row2[8] != "X":
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
            elif (self.row1[8] == "X" and self.row1[0] == "X") and (firsttry == 1 or label == 2):
                if firsttry == 1:
                    label = 2
                self.row1=self.row1.replace("2","O")
                if self.row3[4] != "X" and AItry == 3:
                    self.row3=self.row3.replace("8","O")
                elif self.row3[4] == "X" and AItry >= 3:
                    if ch2 == 4 or ch2 == 6:
                        self.row2=self.row2.replace(str(ch2),"O")
                        AI_pos = [ch2,2]
                    elif ch2 == 7 or ch2 == 9:
                        self.row3=self.row3.replace(str(ch2),"O")
                        AI_pos = [ch2,3]
                    if AItry >= 4:
                        if AI_pos == [4,2]:
                            if self.row2[8] == "X":
                                self.row3 = self.row3.replace("9","O")
                            else:
                                self.row2 = self.row2.replace("6","O")
                        elif AI_pos == [6,2]:
                            if self.row2[0] == "X":
                                self.row3 = self.row3.replace("7","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
                        elif AI_pos == [7,3] or AI_pos == [9,3]:
                            if self.row2[0] == "X":
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
            elif (self.row3[8] == "X" and self.row1[0] == "X") and (firsttry == 1 or label == 3):
                if firsttry == 1:
                    label = 3
                if ch3 == 0:
                    self.row1 = self.row1.replace("3","O")
                    if self.row3[0] != "X" and AItry == 3:
                        self.row3=self.row3.replace("7","O")
                    elif self.row3[0] == "X" and AItry >= 3:
                        if ch4 == 4:
                            self.row2 = self.row2.replace("4","O")
                            AI_pos = [ch4,2]
                        elif ch4 == 8:
                            self.row3 = self.row3.replace("8","O")
                            AI_pos = [ch4,3]
                        if AItry >= 4:
                            if AI_pos == [4,2]:
                                if self.row2[8] != "X":
                                    self.row2 = self.row2.replace("6","O")
                                else:
                                    self.row3 = self.row3.replace("8","O")
                            elif AI_pos == [8,3]:
                                if self.row1[4] != "X":
                                    self.row1 = self.row1.replace("2","O")
                                else:
                                    self.row2 = self.row2.replace("4","O")                    
                elif ch3 == 1:
                    self.row2 = self.row2.replace("4","O")
                    if self.row2[8] != "X" and AItry == 3:
                        self.row2 = self.row2.replace("6","O")
                    elif self.row2[8] == "X" and AItry >= 3:
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if self.row3[0] == "X":
                                if ch5 == 1:
                                    self.row3 = self.row3.replace("8","O")
                                elif ch5 == 2:
                                    self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("7","O")
            elif (self.row1[0] == "X" and self.row2[0] == "X") and (firsttry == 1 or label == 4):
                if firsttry == 1:
                    label = 4
                self.row3 = self.row3.replace("7","O")
                if self.row1[8] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("3","O")
                elif self.row1[8] == "X" and AItry >= 3:
                    if ch6 == 2:
                        self.row1 = self.row1.replace(str(ch6),"O")
                        AI_pos = [ch6,1]
                    elif ch6 == 8:
                        self.row3 = self.row3.replace(str(ch6),"O")
                        AI_pos = [ch6,3]
                    if AItry >= 4:
                        if AI_pos == [2,1]:
                            if self.row3[4] == "X":
                                self.row3 = self.row3.replace("9","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                        elif AI_pos == [8,3]:
                            if self.row1[4] != "X":
                                self.row1 = self.row1.replace("2","O")
            elif (self.row1[0] == "X" and self.row3[0] == "X") and (firsttry == 1 or label == 5):
                if firsttry == 1:
                    label = 5
                self.row2 = self.row2.replace("4","O")
                if self.row2[8] != "X" and AItry == 3:
                    self.row2 = self.row2.replace("6","O")
                elif self.row2[8] == "X" and AItry >= 3:
                    if ch7 == 2:
                        self.row1 = self.row1.replace(str(ch7),"O")
                        AI_pos = [ch7,1]
                    elif ch7 == 8:
                        self.row3=self.row3.replace(str(ch7),"O")
                        AI_pos = [ch7,3]
                    if AItry >= 4:
                        if AI_pos == [2,1]:
                            if self.row3[4] == "X":
                                if ch6 == 8:
                                    self.row1 = self.row1.replace("3","O")
                                elif ch6 == 2:
                                    self.row3 = self.row3.replace("9","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                        elif AI_pos == [8,3]:
                            if self.row1[4] == "X":
                                if ch6 == 8:
                                    self.row3 = self.row3.replace("9","O")
                                elif ch6 == 2:
                                    self.row1 = self.row1.replace("3","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
            elif (self.row1[0] == "X" and self.row2[8] == "X") and (firsttry == 1 or label == 6):
                if firsttry == 1:
                    label = 6
                self.row1 = self.row1.replace("3","O")
                if self.row3[0] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("7","O")
                elif self.row3[0] == "X" and AItry >= 3:
                    self.row2 = self.row2.replace("4","O")
                    if AItry >= 4:
                        if pos == [4,3]:
                            if ch8 == 3:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                        elif pos == [8,3]:
                            if ch8 == 3:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                        else:
                            self.row3 = self.row3.replace("8","O")
            elif (self.row1[0] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 7):
                if firsttry == 1:
                    label = 7
                self.row3 = self.row3.replace("7","O")
                if self.row1[8] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("3","O")
                elif self.row1[8] == "X" and AItry >= 3:
                    self.row2 = self.row2.replace("6","O")
                    if AItry >= 4:
                        if self.row2[0] == "X":
                            self.row1 = self.row1.replace("2","O")
                        else:
                            self.row2 = self.row2.replace("4","O")
            elif (self.row1[0] == "X" and self.row2[4] == "X") and (firsttry == 1 or label == 8):
                if firsttry == 1:
                    label = 8
                if (AI_pos == [9,3] or AI_pos == [3,1]) and AItry >= 2:
                    if AI_pos == [9,3]:
                        self.row1 = self.row1.replace("3","O")
                    elif AI_pos == [3,1]:
                        self.row3 = self.row3.replace("9","O")
                    if self.row2[8] != "X" and AItry == 3:
                        self.row2 = self.row2.replace("6","O")
                    elif self.row2[8] == "X" and AItry >= 3:
                        self.row2 = self.row2.replace("4","O")
                        if AItry >= 4:
                            if self.row1[4] == "X":
                                if ch8 == 3:
                                    self.row3 = self.row3.replace("7","O")
                                else:
                                    self.row3 = self.row3.replace("8","O")
                            elif self.row3[4] == "X":
                                if ch8 == 3:
                                    self.row3 = self.row3.replace("7","O")
                                else:
                                    self.row1 = self.row1.replace("2","O")
                            else:
                                if ch3 == 0:
                                    self.row1 = self.row1.replace("2","O")
                                elif ch3 == 1:
                                    self.row3 = self.row3.replace("8","O")
                elif AI_pos == [7,3] and AItry >= 2:
                    self.row3 = self.row3.replace("9","O")
                    if self.row3[4] != "X" and AItry == 3:
                        self.row3 = self.row3.replace("8","O")
                    elif self.row3[4] == "X" and AItry >= 3:
                        self.row1 = self.row1.replace("2","O")
                        if AItry >= 4:
                            if pos == [0,2] or pos == [8,2]:
                                if pos == [0,2]:
                                    self.row2 = self.row2.replace("6","O")
                                elif pos == [8,2]:
                                    self.row2 = self.row2.replace("4","O")
                            else:
                                self.row2 = self.row2.replace("6","O")
            elif (self.row1[4] == "X" and self.row1[8] == "X") and (firsttry == 1 or label == 9):
                if firsttry == 1:
                    label = 9
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row2 = self.row2.replace("6","O")
                    if AItry >= 4:
                        if self.row2[0] != "X":
                            self.row2 = self.row2.replace("4","O")
                        else:
                            self.row3 = self.row3.replace("8","O")
            elif (self.row1[4] == "X" and self.row2[0] == "X") and (firsttry == 1 or label == 10):
                if firsttry == 1:
                    label = 10
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("3","O")
                    if AItry >= 4:
                        if self.row3[0] != "X":
                            self.row3 = self.row3.replace("7","O")
                        else:
                            if ch3 == 0:
                                self.row2 = self.row2.replace("6","O")
                            elif ch3 == 1:
                                self.row3 = self.row3.replace("8","O")
            elif (self.row1[4] == "X" and self.row2[4] == "X") and (firsttry == 1 or label == 11):
                if firsttry == 1:
                    label = 11
                self.row3 = self.row3.replace("8","O")
                if (AI_pos == [7,3] or AI_pos == [9,3]) and AItry >= 3:
                    if AI_pos == [7,3]:
                        if self.row3[8] != "X":
                            self.row3 = self.row3.replace("9","O")
                        elif self.row3[8] == "X":
                            self.row1 = self.row1.replace("1","O")
                            if AItry >= 4:
                                if self.row2[0] != "X":
                                    self.row2 = self.row2.replace("4","O")
                                else:
                                    if ch8 == 2:
                                        self.row2 = self.row2.replace("6","O")
                                    elif ch8 == 3:
                                        self.row1 = self.row1.replace("3","O")
                    elif AI_pos == [9,3]:
                        if self.row3[0] != "X":
                            self.row3 = self.row3.replace("7","O")
                        elif self.row3[0] == "X":
                            self.row1 = self.row1.replace("3","O")   
                            if AItry >= 4:
                                if self.row2[8] != "X":
                                    self.row2 = self.row2.replace("6","O") 
                                else:
                                    if ch8 == 2:
                                        self.row2 = self.row2.replace("4","O")
                                    elif ch8 == 3:
                                        self.row1 = self.row1.replace("1","O")
                elif (AI_pos == [1,1] or AI_pos == [3,1]) and AItry >= 3:
                        if AI_pos == [1,1]:
                            if (pos == [8,1] and AItry == 3) or slb == 111:
                                slb = 111
                                self.row3 = self.row3.replace("7","O")
                                if AItry >= 4:
                                    if pos == [8,3]:
                                        self.row2 = self.row2.replace("4","O")
                                    else:
                                        self.row3 = self.row3.replace("9","O")
                            elif ((pos == [0,2] or pos == [8,2]) and AItry == 3) or slb == 112:
                                slb = 112
                                if self.row2[0] == "X":
                                    self.row2 = self.row2.replace("6","O")
                                    if AItry >= 4:
                                        if pos == [8,3] or pos == [0,3]:
                                            self.row1 = self.row1.replace("3","O")
                                        else:
                                            self.row3 = self.row3.replace("7","O")
                                elif self.row2[8] == "X":
                                    self.row2 = self.row2.replace("4","O")
                                    if AItry >= 4:
                                        if pos == [0,3]:
                                            self.row1 = self.row1.replace("3","O")
                                        else:
                                            self.row3 = self.row3.replace("7","O")
                            elif (pos == [8,3] and AItry == 3) or slb == 113:
                                slb = 113
                                self.row3 = self.row3.replace("7","O")
                                if AItry >= 4:
                                    if pos != [0,2]:
                                        self.row2 = self.row2.replace("4","O")
                                    else:
                                        if ch8 == 2:
                                            self.row2 = self.row2.replace("6","O")
                                        elif ch8 == 3:
                                            self.row1 = self.row1.replace("3","O")
                            elif (pos == [0,3] and AItry == 3) or slb == 114:
                                slb = 114
                                self.row1 = self.row1.replace("3","O")
                                if AItry >= 4:
                                    if pos == [0,2] or pos == [8,3]:
                                        self.row2 = self.row2.replace("6","O")
                                    else:
                                        self.row2 = self.row2.replace("4","O")
                        elif AI_pos == [3,1]:
                            if (pos == [0,1] and AItry == 3) or slb == 115:
                                slb = 115
                                self.row3 = self.row3.replace("9","O")
                                if AItry >= 4:
                                    if pos == [0,3]:
                                        self.row2 = self.row2.replace("6","O")
                                    else:
                                        self.row3 = self.row3.replace("7","O")
                            elif ((pos == [0,2] or pos == [8,2]) and AItry == 3) or slb == 116:
                                slb = 116
                                if self.row2[0] == "X":
                                    self.row2 = self.row2.replace("6","O")
                                    if AItry >= 4:
                                        if pos == [0,1] or pos == [0,3]:
                                            self.row3 = self.row3.replace("9","O")
                                        else:
                                            self.row1 = self.row1.replace("1","O")
                                elif self.row2[8] == "X":
                                    self.row2 = self.row2.replace("4","O")
                                    if AItry >= 4:
                                        if pos == [8,3]:
                                            self.row1 = self.row1.replace("1","O")
                                        else:
                                            self.row3 = self.row3.replace("9","O")
                            elif (pos == [0,3] and AItry == 3) or slb == 117:
                                slb = 117
                                self.row3 = self.row3.replace("9","O")
                                if AItry >= 4:
                                    if pos != [8,2]:
                                        self.row2 = self.row2.replace("6","O")
                                    else:
                                        if ch8 == 2:
                                            self.row2 = self.row2.replace("4","O")
                                        elif ch8 == 3:
                                            self.row1 = self.row1.replace("1","O")
                            elif (pos == [8,3] and AItry == 3) or slb == 118:
                                slb = 118
                                self.row1 = self.row1.replace("1","O")
                                if AItry >= 4:
                                    if pos == [8,2] or pos == [0,3]:
                                        self.row2 = self.row2.replace("4","O")
                                    else:
                                        self.row2 = self.row2.replace("6","O")
            elif (self.row1[4] == "X" and self.row2[8] == "X") and (firsttry == 1 or label == 12):
                if firsttry == 1:
                    label = 12
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("3","O")
                    if AItry >= 4:
                        if self.row3[0] != "X":
                            self.row3 = self.row3.replace("7","O")
                        else:
                            self.row3 = self.row3.replace("8","O")
            elif (self.row1[4] == "X" and self.row3[0] == "X") and (firsttry == 1 or label == 13):
                if firsttry == 1:
                    label = 13
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row3 = self.row3.replace("8","O")
                    if AItry >= 4:
                        if pos == [0,2] or pos == [8,1]:
                            self.row2 = self.row2.replace("6","O")
                        elif pos == [8,2]:
                            self.row1 = self.row1.replace("3","O")
            elif (self.row1[4] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 14):
                if firsttry == 1:
                    label = 14
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row3 = self.row3.replace("7","O")
                    if AItry >= 4:
                        if pos == [8,1]:
                            self.row2 = self.row2.replace("4","O")
                        elif pos == [0,2]:
                            self.row1 = self.row1.replace("3","O")
                        else:
                            if ch3 == 0:
                                self.row2 = self.row2.replace("4","O")
                            elif ch3 == 1:
                                self.row1 = self.row1.replace("3","O")
            elif (self.row1[4] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 15):
                if firsttry == 1:
                    label = 15
                self.row1 = self.row1.replace("3","O")
                if self.row3[0] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("7","O")
                elif self.row3[0] == "X" and AItry >= 3:
                    self.row3 = self.row3.replace("8","O")
                    if AItry >= 4:
                        if pos == [0,2] or pos == [8,2]:
                            self.row1 = self.row1.replace("1","O")
                        elif pos == [0,1]:
                            self.row2 = self.row2.replace("4","O")
            elif (self.row1[8] == "X" and self.row2[0] == "X") and (firsttry == 1 or label == 16):
                if firsttry == 1:
                    label = 16
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row2 = self.row2.replace("6","O")
                    if AItry >= 4:
                        if pos == [0,3] or pos == [4,3]:
                            if ch1 == 9:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                if pos == [0,3]:
                                    self.row3 = self.row3.replace("8","O")
                                elif pos == [4,3]:
                                    self.row3 = self.row3.replace("7","O")
                        else:
                            self.row3 = self.row3.replace("8","O")
            elif (self.row1[8] == "X" and self.row2[4] == "X") and (firsttry == 1 or label == 17):
                if firsttry == 1:
                    label = 17
                if (AI_pos == [7,3] or AI_pos == [1,1]) and AItry >= 2:
                    if AI_pos == [7,3]:
                        self.row1 = self.row1.replace("1","O")
                    elif AI_pos == [1,1]:
                        self.row3 = self.row3.replace("7","O")
                    if self.row2[0] != "X" and AItry == 3:
                        self.row2 = self.row2.replace("4","O")
                    elif self.row2[0] == "X" and AItry >= 3:
                        self.row2 = self.row2.replace("6","O")
                        if AItry >= 4:
                            if self.row1[4] == "X":
                                if ch8 == 3:
                                    self.row3 = self.row3.replace("9","O")
                                else:
                                    self.row3 = self.row3.replace("8","O")
                            elif self.row3[4] == "X":
                                if ch8 == 3:
                                    self.row3 = self.row3.replace("9","O")
                                else:
                                    self.row1 = self.row1.replace("2","O")
                            else:
                                if ch3 == 0:
                                    self.row1 = self.row1.replace("2","O")
                                elif ch3 == 1:
                                    self.row3 = self.row3.replace("8","O")
                elif AI_pos == [9,3] and AItry >= 2:
                    self.row3 = self.row3.replace("7","O")
                    if self.row3[4] != "X" and AItry == 3:
                        self.row3 = self.row3.replace("8","O")
                    elif self.row3[4] == "X" and AItry >= 3:
                        self.row1 = self.row1.replace("2","O")
                        if AItry >= 4:
                            if pos == [0,1] or pos == [0,2]:
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
            elif (self.row1[8] == "X" and self.row2[8] == "X") and (firsttry == 1 or label == 18):
                if firsttry == 1:
                    label = 18
                self.row3 = self.row3.replace("9","O")
                if self.row1[0] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("1","O")
                elif self.row1[0] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("2","O")
                    if AItry >= 4:
                        if self.row3[4] != "X":
                            self.row3 = self.row3.replace("8","O")
                        else:
                            self.row3 = self.row3.replace("7","O")
            elif (self.row3[0] == "X" and self.row1[8] == "X") and (firsttry == 1 or label == 19):
                if firsttry == 1:
                    label = 19
                if ch3 == 0:
                    self.row1 = self.row1.replace("1","O")
                    if self.row3[8] != "X" and AItry == 3:
                        self.row3 = self.row3.replace("9","O")
                    elif self.row3[8] == "X" and AItry >= 3:
                        if ch4 == 4:
                            self.row2 = self.row2.replace("6","O")
                            AI_pos = [6,2]
                        elif ch4 == 8:
                            self.row3 = self.row3.replace("8","O")
                            AI_pos = [8,3]
                        if AItry >= 4:
                            if AI_pos == [8,3]:
                                if pos == [0,2]:
                                    self.row1 = self.row1.replace("2","O")
                                elif pos == [4,1]:
                                    self.row2 = self.row2.replace("6","O")
                            elif AI_pos == [6,2]:
                                if pos == [4,1]:
                                    self.row2 = self.row2.replace("4","O")
                                elif pos == [0,2]:
                                    self.row3 = self.row3.replace("8","O")                 
                elif ch3 == 1:
                    self.row2 = self.row2.replace("6","O")
                    if self.row2[0] != "X" and AItry == 3:
                        self.row2 = self.row2.replace("4","O")
                    elif self.row2[0] == "X" and AItry >= 3:
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [8,3]:
                                if ch5 == 1:
                                    self.row3 = self.row3.replace("8","O")
                                elif ch5 == 2:
                                    self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
            elif (self.row1[8] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 20):
                if firsttry == 1:
                    label = 20
                self.row3 = self.row3.replace("9","O")
                if self.row1[0] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("1","O")
                elif self.row1[0] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("2","O")
                    if AItry >= 4:
                        if pos == [0,2] or pos == [8,2]:
                            self.row3 = self.row3.replace("7","O")
                        else:
                            self.row2 = self.row2.replace("4","O")
            elif (self.row1[8] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 21):
                if firsttry == 1:
                    label = 21
                self.row2 = self.row2.replace("6","O")
                if self.row2[0] != "X" and AItry == 3:
                    self.row2 = self.row2.replace("4","O")
                elif self.row2[0] == "X" and AItry >= 3:
                    if ch7 == 2:
                        self.row1 = self.row1.replace(str(ch7),"O")
                        AI_pos = [ch7,1]
                    elif ch7 == 8:
                        self.row3=self.row3.replace(str(ch7),"O")
                        AI_pos = [ch7,3]
                    if AItry >= 4:
                        if AI_pos == [2,1]:
                            if self.row3[4] == "X":
                                if ch6 == 8:
                                    self.row1 = self.row1.replace("1","O")
                                elif ch6 == 2:
                                    self.row3 = self.row3.replace("7","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                        elif AI_pos == [8,3]:
                            if self.row1[4] == "X":
                                if ch6 == 8:
                                    self.row3 = self.row3.replace("7","O")
                                elif ch6 == 2:
                                    #draw
                                    self.row1 = self.row1.replace("1","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
            elif (self.row2[0] == "X" and self.row2[4] == "X") and (firsttry == 1 or label == 22):
                if firsttry == 1:
                    label = 22
                self.row2 = self.row2.replace("6","O")
                if AI_pos == [1,1] and AItry >= 3:
                    if (self.row1[4] == "X" and AItry == 3) or slb == 221:
                        slb = 221
                        self.row3 = self.row3.replace("8","O")
                        if AItry >= 4:
                            if pos == [8,1]:
                                self.row3 = self.row3.replace("7","O")
                            else:
                                self.row1 = self.row1.replace("3","O")
                    elif (self.row3[4] == "X" and AItry == 3) or slb == 222:
                        slb = 222
                        self.row1 = self.row1.replace("2","O")
                        if AItry >= 4:
                            if pos != [8,1]:
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row3 = self.row3.replace("7","O")
                    elif (self.row3[0] == "X" and AItry == 3) or slb == 223:
                        slb = 223
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if pos != [4,1]:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (self.row1[8] == "X" and AItry == 3) or slb == 224:
                        slb = 224
                        self.row3 = self.row3.replace("7","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                    elif (self.row3[8] == "X" and AItry == 3) or slb == 225:
                        slb = 225
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                elif AI_pos == [7,3] and AItry >= 3:
                    if (self.row1[4] == "X" and AItry == 3) or slb == 226:
                        slb = 226
                        self.row3 = self.row3.replace("8","O")
                        if AItry >= 4:
                            if pos == [8,3]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (self.row3[4] == "X" and AItry == 3) or slb == 227:
                        slb = 227
                        self.row1 = self.row1.replace("2","O")
                        if AItry >= 4:
                            if pos == [0,1]:
                                self.row3 = self.row3.replace("9","O")
                            else:
                                self.row1 = self.row1.replace("1","O")
                    elif (self.row3[8] == "X" and AItry == 3) or slb == 228:
                        slb = 228
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [4,3]:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                    elif (self.row1[0] == "X" and AItry == 3) or slb == 229:
                        slb = 229
                        self.row3 = self.row3.replace("9","O")
                        if AItry >= 4:
                            if pos == [8,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("3","O")
                    elif (self.row1[8] == "X" and AItry == 3) or slb == 220:
                        slb = 220
                        self.row3 = self.row3.replace("9","O")
                        if AItry >= 4:
                            if pos == [4,3]:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                elif AI_pos == [3,1] and AItry >= 3:
                    if self.row3[8] == "X":
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos != [4,1]:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                    else:
                        self.row3 = self.row3.replace("9","O")
                elif AI_pos == [9,3] and AItry >= 3:
                    if self.row1[8] == "X":
                        self.row3 = self.row3.replace("7","O")
                        if AItry >= 4:
                            if pos != [4,3]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                    else:
                            self.row1 = self.row1.replace("3","O")
            elif (self.row2[0] == "X" and self.row2[8] == "X") and (firsttry == 1 or label == 23):
                if firsttry == 1:
                    label = 23
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("3","O")
                    if AItry >= 4:
                        if pos == [0,3]:
                            self.row1 = self.row1.replace("2","O")
                        else:
                            self.row3 = self.row3.replace("7","O")
            elif (self.row2[0] == "X" and self.row3[0] == "X") and (firsttry == 1 or label == 24):
                if firsttry == 1:
                    label = 24
                self.row1 = self.row1.replace("1","O")
                if self.row3[8] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("9","O")
                elif self.row3[8] == "X" and AItry >= 3:
                    self.row3 = self.row3.replace("8","O")
                    if AItry >= 4:
                        if pos != [4,1]:
                            self.row1 = self.row1.replace("2","O")
                        else:
                            self.row2 = self.row2.replace("6","O")
            elif (self.row2[0] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 25):
                if firsttry == 1:
                    label = 25
                self.row3 = self.row3.replace("7","O")
                if self.row1[8] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("3","O")
                elif self.row1[8] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("1","O")
                    if AItry >= 4:
                        if pos != [8,3]:
                            self.row3 = self.row3.replace("9","O")
                        else:
                            self.row2 = self.row2.replace("6","O")
            elif (self.row2[0] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 26):
                if firsttry == 1:
                    label = 26
                self.row3 = self.row3.replace("8","O")
                if self.row1[4] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("2","O")
                elif self.row1[4] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("3","O")
                    if AItry >= 4:
                        if pos != [0,3]:
                            self.row3 = self.row3.replace("7","O")
                        else:
                            self.row1 = self.row1.replace("1","O")
            elif (self.row2[4] == "X" and self.row2[8] == "X") and (firsttry == 1 or label == 27):
                if firsttry == 1:
                    label = 27
                self.row2 = self.row2.replace("4","O")
                if AI_pos == [1,1] and AItry >= 3:
                    if self.row3[0] == "X":
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if pos != [4,1]:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                    else:
                        self.row3 = self.row3.replace("7","O")
                elif AI_pos == [7,3] and AItry >= 3:
                    if self.row1[0] == "X":
                        self.row3 = self.row3.replace("9","O")
                        if AItry >= 4:
                            if pos != [4,3]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                    else:
                            self.row1 = self.row1.replace("1","O")
                elif AI_pos == [3,1] and AItry >= 3:
                    if (self.row1[4] == "X" and AItry == 3) or slb == 271:
                        slb = 271
                        self.row3 = self.row3.replace("8","O")
                        if AItry >= 4:
                            if pos == [8,3]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (self.row3[4] == "X" and AItry == 3) or slb == 272:
                        slb = 272
                        self.row1 = self.row1.replace("2","O")
                        if AItry >= 4:
                            if pos != [0,1]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (self.row3[0] == "X" and AItry == 3) or slb == 273:
                        slb = 273
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos != [4,1]:
                                self.row1 = self.row1.replace("2","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
                    elif (self.row1[0] == "X" and AItry == 3) or slb == 274:
                        slb = 274
                        self.row3 = self.row3.replace("9","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                    elif (self.row3[8] == "X" and AItry == 3) or slb == 275:
                        slb = 275
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("7","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                elif AI_pos == [9,3] and AItry >= 3:
                    if (self.row1[4] == "X" and AItry == 3) or slb == 276:
                        slb = 276
                        self.row3 = self.row3.replace("8","O")
                        if AItry >= 4:
                            if pos == [0,3]:
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row3 = self.row3.replace("7","O")
                    elif (self.row3[4] == "X" and AItry == 3) or slb == 277:
                        slb = 277
                        self.row1 = self.row1.replace("2","O")
                        if AItry >= 4:
                            if pos == [8,1]:
                                self.row3 = self.row3.replace("7","O")
                            else:
                                self.row1 = self.row1.replace("3","O")
                    elif (self.row3[0] == "X" and AItry == 3) or slb == 278:
                        slb = 278
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                    elif (self.row1[0] == "X" and AItry == 3) or slb == 279:
                        slb = 279
                        self.row3 = self.row3.replace("8","O")
                        if AItry >= 4:
                            if pos == [0,3]:
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row3 = self.row3.replace("7","O")
                    elif (self.row1[8] == "X" and AItry == 3) or slb == 270:
                        slb = 270
                        self.row3 = self.row3.replace("7","O")
                        if AItry >= 4:
                            if pos == [4,3]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row3 = self.row3.replace("8","O")
            elif (self.row2[4] == "X" and self.row3[0] == "X") and (firsttry == 1 or label == 28):
                if firsttry == 1:
                    label = 28
                if (AI_pos == [9,3] or AI_pos == [1,1]) and AItry >= 2:
                    self.row1 = self.row1.replace("3","O")
                    if AI_pos == [1,1]:
                        if self.row1[4] != "X" and AItry == 3:
                            self.row1 = self.row1.replace("2","O")
                        elif self.row1[4] == "X" and AItry >= 3:
                            self.row3 = self.row3.replace("8","O")
                            if AItry >= 4:
                                if self.row2[8] == "X":
                                    if ch8 == 3:
                                        self.row3 = self.row3.replace("9","O")
                                    else:
                                        self.row2 = self.row2.replace("4","O")
                                else:
                                    self.row2 = self.row2.replace("6","O")
                    elif AI_pos == [9,3]:
                        if self.row2[8] != "X" and AItry == 3:
                            self.row2 = self.row2.replace("6","O")
                        elif self.row2[8] == "X" and AItry >= 3:
                            self.row2 = self.row2.replace("4","O")
                            if AItry >= 4:
                                if self.row1[4] == "X":
                                    if ch8 == 3:
                                        self.row1 = self.row1.replace("1","O")
                                    else:
                                        self.row3 = self.row3.replace("8","O")
                                else:
                                    self.row1 = self.row1.replace("2","O")
                elif AI_pos == [3,1] and AItry >= 2:
                    self.row3 = self.row3.replace("9","O")
                    if self.row2[8] != "X" and AItry == 3:
                        self.row2 = self.row2.replace("6","O")
                    elif self.row2[8] == "X" and AItry >= 3:
                        self.row2 = self.row2.replace("4","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
            elif (self.row2[4] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 29):
                if firsttry == 1:
                    label = 29
                self.row1 = self.row1.replace("2","O")
                if AI_pos == [1,1] and AItry >= 3:
                    if self.row1[8] == "X":
                        self.row3 = self.row3.replace("7","O")
                        if AItry >= 4:
                            if pos != [0,2]:
                                self.row2 = self.row2.replace("4","O")
                            else:
                                self.row2 = self.row2.replace("6","O")
                    else:
                        self.row1 = self.row1.replace("3","O")
                elif AI_pos == [3,1] and AItry >= 3:
                    if self.row1[0] == "X":
                        self.row3 = self.row3.replace("9","O")
                        if AItry >= 4:
                            if pos != [8,2]:
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
                    else:
                            self.row1 = self.row1.replace("1","O")
                elif AI_pos == [7,3] and AItry >= 3:
                    if (self.row2[0] == "X" and AItry == 3) or slb == 291:
                        slb = 291
                        self.row2 = self.row2.replace("6","O")
                        if AItry >= 4:
                            if pos == [8,3]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (self.row2[8] == "X" and AItry == 3) or slb == 292:
                        slb = 292
                        self.row2 = self.row2.replace("4","O")
                        if AItry >= 4:
                            if pos != [0,1]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (self.row1[0] == "X" and AItry == 3) or slb == 293:
                        slb = 293
                        self.row3 = self.row3.replace("9","O")
                        if AItry >= 4:
                            if pos == [0,2]:
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
                    elif (self.row1[8] == "X" and AItry == 3) or slb == 294:
                        slb = 294
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [0,2]:
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
                    elif (self.row3[8] == "X" and AItry == 3) or slb == 295:
                        slb = 295
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [0,2]:
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
                elif AI_pos == [9,3] and AItry >= 3:
                    if (self.row2[8] == "X" and AItry == 3) or slb == 296:
                        slb = 296
                        self.row2 = self.row2.replace("4","O")
                        if AItry >= 4:
                            if pos == [0,1]:
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row1 = self.row1.replace("1","O")
                    elif (self.row2[0] == "X" and AItry == 3) or slb == 297:
                        slb = 297
                        self.row2 = self.row2.replace("6","O")
                        if AItry >= 4:
                            if pos != [8,1]:
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row3 = self.row3.replace("7","O")
                    elif (self.row3[0] == "X" and AItry == 3) or slb == 298:
                        slb = 298
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if pos == [8,2]:
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row2 = self.row2.replace("6","O")
                    elif (self.row1[0] == "X" and AItry == 3) or slb == 299:
                        slb = 299
                        self.row1 = self.row1.replace("3","O")
                        if AItry >= 4:
                            if pos == [8,2]:
                                self.row2 = self.row2.replace("4","O")
                            else:
                                self.row2 = self.row2.replace("6","O")
                    elif (self.row1[8] == "X" and AItry == 3) or slb == 290:
                        slb = 290
                        self.row3 = self.row3.replace("7","O")
                        if AItry >= 4:
                            if pos == [0,2]:
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
            elif (self.row2[4] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 30):
                if firsttry == 1:
                    label = 30
                if (AI_pos == [3,1] or AI_pos == [7,3]) and AItry >= 2:
                    self.row1 = self.row1.replace("1","O")
                    if AI_pos == [3,1]:
                        if self.row1[4] != "X" and AItry == 3:
                            self.row1 = self.row1.replace("2","O")
                        elif self.row1[4] == "X" and AItry >= 3:
                            self.row3 = self.row3.replace("8","O")
                            if AItry >= 4:
                                if self.row2[8] == "X":
                                    if ch8 == 3:
                                        self.row3 = self.row3.replace("7","O")
                                    else:
                                        self.row2 = self.row2.replace("4","O")
                                else:
                                    self.row2 = self.row2.replace("6","O")
                    elif AI_pos == [7,3]:
                        if self.row2[0] != "X" and AItry == 3:
                            self.row2 = self.row2.replace("4","O")
                        elif self.row2[0] == "X" and AItry >= 3:
                            self.row2 = self.row2.replace("6","O")
                            if AItry >= 4:
                                if self.row1[4] == "X":
                                    if ch8 == 3:
                                        self.row1 = self.row1.replace("3","O")
                                    else:
                                        self.row3 = self.row3.replace("8","O")
                                else:
                                    self.row1 = self.row1.replace("2","O")
                elif AI_pos == [1,1] and AItry >= 2:
                    self.row3 = self.row3.replace("7","O")
                    if self.row2[0] != "X" and AItry == 3:
                        self.row2 = self.row2.replace("4","O")
                    elif self.row2[0] == "X" and AItry >= 3:
                        self.row2 = self.row2.replace("6","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
            elif (self.row2[8] == "X" and self.row3[0] == "X") and (firsttry == 1 or label == 31):
                if firsttry == 1:
                    label = 31
                self.row1 = self.row1.replace("3","O")
                if ((self.row1[0] != "X" and self.row3[8] != "X" and self.row3[4] != "X") or ulb == 1) and AItry >= 3:
                    ulb = 1
                    if (pos == [4,1] and AItry == 3) or slb == 1:
                        slb = 1
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [8,3]:
                                self.row3 = self.row3.replace("8","O")
                            else:
                                self.row3 = self.row3.replace("9","O")
                    elif (pos != [4,1] and AItry == 3) or slb == 5:
                        slb = 5
                        self.row1 = self.row1.replace("1","O")
                        if AItry >= 4:
                            if pos == [4,1]:
                                self.row3 = self.row3.replace("9","O")
                            else:
                                self.row1 = self.row1.replace("2","O")
                else:
                    if AItry >= 3:
                        if (pos == [0,1] and AItry == 3) or slb == 2:
                            slb = 2
                            self.row2 = self.row2.replace("4","O")
                            if AItry >= 4:
                                if pos == [4,3]:
                                    self.row3 = self.row3.replace("9","O")
                                else:
                                    self.row3 = self.row3.replace("8","O")
                        elif (pos == [4,3] and AItry == 3) or slb == 3:
                            slb = 3
                            self.row3 = self.row3.replace("9","O")
                            if AItry >= 4:
                                if pos == [0,1]:
                                    self.row2 = self.row2.replace("4","O")
                                else:
                                    self.row1 = self.row1.replace("1","O")
                        elif (pos == [8,3] and AItry == 3) or slb == 4:
                            slb = 4
                            self.row3 = self.row3.replace("8","O")
                            if AItry >= 4:
                                if pos == [4,1]:
                                    self.row2 = self.row2.replace("4","O")
                                else:
                                    self.row1 = self.row1.replace("2","O")
            elif (self.row2[8] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 32):
                if firsttry == 1:
                    label = 32
                self.row3 = self.row3.replace("9","O")
                if self.row1[0] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("1","O")
                elif self.row1[0] == "X" and AItry >= 3:
                    self.row1 = self.row1.replace("3","O")
                    if AItry >= 4:
                        if pos != [0,3]:
                            self.row3 = self.row3.replace("7","O")
                        else:
                            self.row2 = self.row2.replace("4","O")
            elif (self.row2[8] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 33):
                if firsttry == 1:
                    label = 33
                self.row1 = self.row1.replace("3","O")
                if self.row3[0] != "X" and AItry == 3:
                    self.row3 = self.row3.replace("7","O")
                elif self.row3[0] == "X" and AItry >= 3:
                    self.row3 = self.row3.replace("8","O")
                    if AItry >= 4:
                        if pos != [4,1]:
                            self.row1 = self.row1.replace("2","O")
                        else:
                            self.row1 = self.row1.replace("1","O")
            elif (self.row3[0] == "X" and self.row3[4] == "X") and (firsttry == 1 or label == 34):
                if firsttry == 1:
                    label = 34
                self.row3 = self.row3.replace("9","O")
                if self.row1[0] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("1","O")
                elif self.row1[0] == "X" and AItry >= 3:
                    if ch9 >= 4 and ch9 <= 6:
                        self.row2 = self.row2.replace(str(ch9),"O")
                        AI_pos = [ch9,2]
                    elif ch9 >= 1 and ch9 <= 3:
                        self.row1 = self.row1.replace(str(ch9),"O")
                        AI_pos = [ch9,1]
                    if AItry >= 4:
                        if AI_pos == [6,2] or AI_pos == [3,1]:
                            if self.row2[0] != "X":
                                self.row2 = self.row2.replace("4","O")
                            else:
                                pass
                        elif AI_pos == [4,2]:
                            if self.row2[8] != "X":
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row1 = self.row1.replace("3","O")
            elif (self.row3[0] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 35):
                if firsttry == 1:
                    label = 35
                self.row3 = self.row3.replace("8","O")
                if self.row1[4] != "X" and AItry == 3:
                    self.row1 =self.row1.replace("2","O")
                elif self.row1[4] == "X" and AItry >= 3:
                    if ch10 == 4 or ch10 == 6:
                        self.row2=self.row2.replace(str(ch10),"O")
                        AI_pos = [ch10,2]
                    elif ch10 == 1 or ch10 == 3:
                        self.row1=self.row1.replace(str(ch10),"O")
                        AI_pos = [ch10,1]
                    if AItry >= 4:
                        if AI_pos == [4,2]:
                            if self.row2[8] == "X":
                                self.row1 = self.row1.replace("3","O")
                            else:
                                self.row2 = self.row2.replace("6","O")
                        elif AI_pos == [6,2]:
                            if self.row2[0] == "X":
                                self.row1 = self.row1.replace("1","O")
                            else:
                                self.row2 = self.row2.replace("4","O")
                        elif AI_pos == [1,1]:
                            if self.row1[8] == "X":
                                self.row2 = self.row2.replace("6","O")
                            else:
                                self.row1 = self.row1.replace("3","O")
                        elif AI_pos == [3,1]:
                            if self.row1[0] == "X":
                                self.row2 = self.row2.replace("4","O")
                            else:
                                self.row1 = self.row1.replace("1","O")
            elif (self.row3[4] == "X" and self.row3[8] == "X") and (firsttry == 1 or label == 36):
                if firsttry == 1:
                    label = 36
                self.row3 = self.row3.replace("7","O")
                if self.row1[8] != "X" and AItry == 3:
                    self.row1 = self.row1.replace("3","O")
                elif self.row1[8] == "X" and AItry >= 3:
                    self.row2 = self.row2.replace("6","O")
                    if AItry >= 4:
                        if self.row2[0] != "X":
                            self.row2 = self.row2.replace("4","O")
                        else:
                            self.row1 = self.row1.replace("1","O")                   
            firsttry = 0   
        AItry += 1
        tries += 1
t1=TicTacToe()