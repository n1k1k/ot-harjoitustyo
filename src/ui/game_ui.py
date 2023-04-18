from tkinter import *
from PIL import Image
from PIL import ImageTk
from game import Game

class GameView:
    def __init__(self, window, game: Game):
        self.display = window
        self.display.title('Blakcjack')
        self.display.geometry('1200x750')
        self.display.configure(background='plum1')
        self.game = game
        self.dealer_spot = 0
        self.player_spot = 0
    
    def start(self):
        main_frame = Frame(self.display, bg='plum1')
        main_frame.pack(pady=20)

        #Card frames
        global dealer_fr, player_fr
        dealer_fr = LabelFrame(main_frame, text='DEALER', font=('Courier New', 16, 'bold'), bg='plum1', bd=0, labelanchor='n')
        dealer_fr.pack(ipadx=20, pady=10)
        player_fr = LabelFrame(main_frame, text='PLAYER', font=('Courier New', 16, 'bold'), bg='plum1', bd=0, labelanchor='n')
        player_fr.pack(padx=20, ipadx=20)

        #Buttons
        button_fr = Frame(self.display, bg='plum1')
        button_fr.pack(pady=20)
        hit_button = Button(button_fr, text='HIT', font = ('Courier New', 14, 'bold'), bg='aquamarine1', bd = 0, command=self.player_hit)
        hit_button.grid(row=0,column=0)
        stand_button = Button(button_fr, text='STAND', font = ('Courier New', 14, 'bold'), activebackground='aquamarine1')
        stand_button.grid(row=0,column=1, padx = 20)
        new_game_button = Button(button_fr, text='NEW GAME', font = ('Courier New', 14, 'bold'), activebackground='aquamarine1')
        new_game_button.grid(row=0,column=2)

        stand_button.config(state='disabled')
        new_game_button.config(state='disabled')

        self.first_round()
    
    def first_round(self):
        self.game.first_round()
        for _ in range(2):
            self.player_hit()
            self.dealer_hit()
    
    def player_hit(self):
        global player_card_1, player_card_img_1, player_card_2, player_card_img_2, player_card_3, player_card_img_3, player_card_4, player_card_img_4, player_card_5, player_card_img_5  
        if self.player_spot <= 5:
            if self.player_spot <= 1:
                if self.player_spot == 0:
                    card = self.game.player.hand[0]
                    player_card_1 = Label(player_fr, text='', bg='plum1')
                    player_card_1.grid(row=1, column=0, pady=20, padx=20)
                    player_card_img_1 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_1.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_1, compound='center')
                    self.player_spot += 1
                elif self.player_spot == 1:
                    card = self.game.player.hand[1]
                    player_card_2 = Label(player_fr, text='', bg='plum1')
                    player_card_2.grid(row=1, column=1, pady=20, padx=20)
                    player_card_img_2 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_2.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_2, compound='center')
                    self.player_spot += 1
            else:
                self.game.deal_card(self.game.player)
                card = self.game.player.hand[-1]
                if self.player_spot == 2:
                    player_card_3 = Label(player_fr, text='', bg='plum1')
                    player_card_3.grid(row=1, column=2, pady=20, padx=20)
                    player_card_img_3 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_3.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_3, compound='center')
                    self.player_spot += 1
                elif self.player_spot == 3:
                    player_card_4 = Label(player_fr, text='', bg='plum1')
                    player_card_4.grid(row=1, column=3, pady=20, padx=20)
                    player_card_img_4 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_4.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_4, compound='center')
                    self.player_spot += 1
                elif self.player_spot == 4:
                    player_card_5 = Label(player_fr, text='', bg='plum1')
                    player_card_5.grid(row=1, column=4, pady=20, padx=20)
                    player_card_img_5 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_5.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_5, compound='center')
                    self.player_spot += 1

    def dealer_hit(self):
        global dealer_card_1, dealer_card_img_1, dealer_card_2, dealer_card_img_2, dealer_card_3, dealer_card_img_3, dealer_card_4, dealer_card_img_4, dealer_card_5, dealer_card_img_5  
        if self.dealer_spot <= 5:
            if self.dealer_spot <= 1:
                if self.dealer_spot == 0:
                    card = self.game.dealer.hand[0]
                    dealer_card_1 = Label(dealer_fr, text='', bg='plum1')
                    dealer_card_1.grid(row=0, column=0, pady=20, padx=20)
                    dealer_card_img_1 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_1.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_1, compound='center')
                    self.dealer_spot += 1
                elif self.dealer_spot == 1:
                    card = self.game.dealer.hand[1]
                    dealer_card_2 = Label(dealer_fr, text='', bg='plum1')
                    dealer_card_2.grid(row=0, column=1, pady=20, padx=20)
                    dealer_card_img_2 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_2.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_2, compound='center')
                    self.dealer_spot += 1
            else:
                self.game.deal_card(self.game.dealer)
                card = self.game.dealer.hand[-1]
                if self.dealer_spot == 2:
                    dealer_card_3 = Label(dealer_fr, text='', bg='plum1')
                    dealer_card_3.grid(row=0, column=2, pady=20, padx=20)
                    dealer_card_img_3 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_3.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_3, compound='center')
                    self.pdealer_spot += 1
                elif self.dealer_spot == 3:
                    dealer_card_4 = Label(dealer_fr, text='', bg='plum1')
                    dealer_card_4.grid(row=0, column=3, pady=20, padx=20)
                    dealer_card_img_4 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_4.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_4, compound='center')
                    self.dealer_spot += 1
                elif self.dealer_spot == 4:
                    dealer_card_5 = Label(dealer_fr, text='', bg='plum1')
                    dealer_card_5.grid(row=0, column=4, pady=20, padx=20)
                    dealer_card_img_5 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_5.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_5, compound='center')
                    self.dealer_spot += 1


    def img_resize(self, card):
        card_img = Image.open(card).resize((150,218))
        global resized_card_img
        resized_card_img = ImageTk.PhotoImage(card_img)

        return resized_card_img
