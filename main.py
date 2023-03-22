import tkinter
from tkinter import *
from tkinter import ttk


#----------------colors -----------------------------

co0 = "#FFFFFF" # White
co1 = "#333333" #dark black
co2 = "#fcc058" #orange
co3 = "#38576b" #value
co4 = "#3297a8" #blue
co5 = "#fff873" #yellow
co6 = "#fcc058" #orange
co7 = "#e85151" #red
co8 = co4 # + green
co10 = "#fcfbf7"
back = "#3b3b3b" # black


# create main window
window = Tk()
window.title('')
window.geometry('260x370')
window.configure(bg=back)


#----------------Divide window in 2 frame ----------------

frame_up = Frame(window, width=240, height=100, bg=co1, relief="raised")
frame_up.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_down = Frame(window, width=240, height=300, bg=back, relief="flat")
frame_down.grid(row=1, column=0, sticky=NW)

#----------------Config frame up --------------------------
app_x = Label(frame_up, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_up, text='Player one', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_scores= Label(frame_up, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_scores.place(x=80, y=20)

app_split = Label(frame_up, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_split.place(x=110, y=20)

app_o = Label(frame_up, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_up, text='Player two', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_scores= Label(frame_up, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_scores.place(x=130, y=20)

#----------------Config frame down --------------------------

#----------------creating app logic -----------------------
player_1 = "X"
player_2 = "O"

score_1 = 0
score_2 = 0

table = [['1','2','3'],['4','5','6'],['7','8','9']]

playing = 'X'
play = ''
counter = 0
round_counter = 0

def start_game():
    b_play.place(x=800, y=300)
    # To start the game
    def control(i):
        global playing
        global counter
        global play

        #comparing value received
        if i == str(1):
            #checking if that position is empty or not
            if b_0['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_0['fg'] = color
                b_0['text'] = playing
                table[0][0] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1
         
        if i == str(2):

            #checking if that position is empty or not
            if b_1['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_1['fg'] = color
                b_1['text'] = playing
                table[0][1] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1

        if i == str(3):
            #checking if that position is empty or not
            if b_2['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_2['fg'] = color
                b_2['text'] = playing
                table[0][2] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1        

        if i == str(4):
            #checking if that position is empty or not
            if b_3['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_3['fg'] = color
                b_3['text'] = playing
                table[1][0] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1

        if i == str(5):
            #checking if that position is empty or not
            if b_4['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_4['fg'] = color
                b_4['text'] = playing
                table[1][1] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1
         
        if i == str(6):

            #checking if that position is empty or not
            if b_5['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_5['fg'] = color
                b_5['text'] = playing
                table[1][2] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1
  
        if i == str(7):
            #checking if that position is empty or not
            if b_6['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_6['fg'] = color
                b_6['text'] = playing
                table[2][0] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1      

        if i == str(8):
            #checking if that position is empty or not
            if b_7['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_7['fg'] = color
                b_7['text'] = playing
                table[2][1] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1  
        
        if i == str(9):
            #checking if that position is empty or not
            if b_8['text']=='':
                #checking who is playing and thus defining the color of the symbol
                if playing == 'X':
                    color = co7
                if playing == 'O':
                    color = co8
                
                #defining the color of the text of the button and 
                #marking that position of the table with the value of the current player

                b_8['fg'] = color
                b_8['text'] = playing
                table[2][2] = playing

                #checking who is playing in order to switch players
                if playing == 'X':
                    playing = 'O'
                    play = 'player one'
                else:
                    playing = 'X'
                    play = 'player two'

                #increment counter for next round
                counter+=1

               #after the counter is greater than or equal to 5, 
               #check if there is any winner according 
               #to the following standards within the table

        if counter>=5:
                    #lines
            if table[0][0]==table[0][1]==table[0][2]!="":
                winner(playing)
            elif table[1][0]==table[1][1]==table[1][2]!="":
                winner(playing)
            elif table[2][0]==table[2][1]==table[2][2]!="":
                winner(playing)
                    
                    #columns 
            if table[0][0]==table[1][0]==table[2][0]!="":
                winner(playing)
            elif table[0][1]==table[1][1]==table[2][1]!="":
                winner(playing)
            elif table[0][2]==table[1][2]==table[2][2]!="":
                winner(playing)
                    
                    #diagonals 
            if table[0][0]==table[1][1]==table[2][2]!="":
                        winner(playing)
            elif table[0][2]==table[1][1]==table[2][0]!="":
                winner(playing)

                    # a tie
            if counter>=9:
                winner('It was a draw')    

        
    # To decide the winner
    def winner(i):
        global table
        global score_1
        global score_2
        global round_counter
        global counter
        
        #blocking the buttons
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'


        app_winner = Label(frame_down, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_winner.place(x=40, y=220)

        if i == 'X':
            score_2+=1
            app_winner['text'] = 'Player two win'
            app_o_scores['text'] = score_2

        
        if i == 'O':
            score_1+=1
            app_winner['text'] = 'Player one win'
            app_x_scores['text'] = score_1
        
        if i == 'It was a draw':
            app_winner['text'] = 'It was a draw'

        def restart():
            
        #cleaning the buttons
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''

            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal' 
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'

            app_winner.destroy()
            b_play.destroy()
            


        #Play again button
        b_play = Button(frame_down, command=restart, text='Next round', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=back, fg=co0)
        b_play.place(x=80, y=188)

        def gameOver():
            b_play.destroy()
            app_winner.destroy()

            end()

        if round_counter >=5:
            gameOver()
        else:
            round_counter+=1
            #restarting the table
            table = [['1','2','3'],['4','5','6'],['7','8','9']]
            counter = 0

    # To end the game
    def end():
        global table
        global round_counter
        global score_1
        global score_2
        global counter

        table = [['1','2','3'],['4','5','6'],['7','8','9']]
        round_counter = 0
        score_1 = 0
        score_2 = 0
        counter = 0

         #blocking the buttons
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'


        app_end = Label(frame_down, text='Game Over', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_end.place(x=25, y=90)

        #play again

        def play_again():
            app_x_scores['text'] = '0'
            app_o_scores['text'] = '0'
            app_end.destroy()
            b_play.destroy()

            #calling start game
            start_game()

        b_play = Button(frame_down, command=play_again, text='Play again', font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=back, fg=co0)
        b_play.place(x=80, y=197)


    #vertical lines
    app_ = Label(frame_down, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=90, y=15)
    app_ = Label(frame_down, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=157, y=15)

    #horizontal lines
    app_ = Label(frame_down, text='', width=46, relief='flat', padx=2, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=30, y=63)
    app_ = Label(frame_down, text='', width=46, relief='flat', padx=2, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=30, y=123)


    #line 0
    b_0 = Button(frame_down, command=lambda:control('1'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_0.place(x=30, y=15)
    b_1 = Button(frame_down, command=lambda:control('2'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_1.place(x=96, y=15)
    b_2 = Button(frame_down, command=lambda:control('3'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_2.place(x=163, y=15)

    #line 1
    b_3 = Button(frame_down, command=lambda:control('4'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_3.place(x=30, y=75)
    b_4 = Button(frame_down, command=lambda:control('5'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_4.place(x=96, y=75)
    b_5 = Button(frame_down, command=lambda:control('6'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_5.place(x=163, y=75)

    #line 2
    b_6 = Button(frame_down, command=lambda:control('7'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_6.place(x=30, y=135)
    b_7 = Button(frame_down, command=lambda:control('8'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_7.place(x=96, y=135)
    b_8 = Button(frame_down, command=lambda:control('9'),  text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=back, fg=co7)
    b_8.place(x=163, y=135) 

    #Play Button
b_play = Button(frame_down, command=start_game, text='Play', width=10, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=back, fg=co0)
b_play.place(x=80, y=197)


window.mainloop()