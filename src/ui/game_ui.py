from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk


class GameView:
    def __init__(self, window, game):
        self.display = window
        self.display.title('Blakcjack')
        self.display.geometry('1200x750')
        self.display.configure(background='plum1')
        self.game = game
        self.dealer_spot = 0
        self.player_spot = 0
    
    def start(self):
        self.display.title(f'Blakcjack! Cards left in deck: {self.game.deck.cards_left}')
        main_frame = Frame(self.display, bg='plum1')
        main_frame.pack(pady=20)

        #Card frames
        global dealer_fr, player_fr
        dealer_fr = LabelFrame(main_frame, text=f'DEALER', font=('Courier New', 16, 'bold'), bg='plum1', bd=0, labelanchor='n')
        dealer_fr.pack(ipadx=20, pady=10)
        player_fr = LabelFrame(main_frame, text=f'PLAYER', font=('Courier New', 16, 'bold'), bg='plum1', bd=0, labelanchor='n')
        player_fr.pack(padx=20, ipadx=20)

        #Buttons
        global new_game_button, hit_button, stand_button, new_deck_button
        button_fr = Frame(self.display, bg='plum1')
        button_fr.pack(pady=20)
        hit_button = Button(button_fr, text='HIT', font = ('Courier New', 14, 'bold'), bg='aquamarine1', bd = 0, command=self.deal_to_player)
        hit_button.grid(row=0,column=0)
        stand_button = Button(button_fr, text='STAND', font = ('Courier New', 14, 'bold'), bg='aquamarine1', command=self.stand)
        stand_button.grid(row=0,column=1, padx = 20)
        new_game_button = Button(button_fr, text='NEW GAME', font = ('Courier New', 14, 'bold'), bg='aquamarine1', command=self.new_game)
        new_game_button.grid(row=0,column=2)
        new_deck_button = Button(button_fr, text='NEW DECK', font = ('Courier New', 14, 'bold'), bg='aquamarine1', command=self.first_round)
        new_deck_button.grid(row=0,column=3, padx = 20)

        global dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, dealer_card_5
        dealer_card_1 = Label(dealer_fr, text='', bg='plum1')
        dealer_card_1.grid(row=0, column=0, pady=20, padx=20)
        dealer_card_2 = Label(dealer_fr, text='', bg='plum1')
        dealer_card_2.grid(row=0, column=1, pady=20, padx=20)
        dealer_card_3 = Label(dealer_fr, text='', bg='plum1')
        dealer_card_3.grid(row=0, column=2, pady=20, padx=20)
        dealer_card_4 = Label(dealer_fr, text='', bg='plum1')
        dealer_card_4.grid(row=0, column=3, pady=20, padx=20)
        dealer_card_5 = Label(dealer_fr, text='', bg='plum1')
        dealer_card_5.grid(row=0, column=4, pady=20, padx=20)

        global player_card_1, player_card_2, player_card_3, player_card_4, player_card_5
        player_card_1 = Label(player_fr, text='', bg='plum1')
        player_card_1.grid(row=1, column=0, pady=20, padx=20)
        player_card_2 = Label(player_fr, text='', bg='plum1')
        player_card_2.grid(row=1, column=1, pady=20, padx=20)
        player_card_3 = Label(player_fr, text='', bg='plum1')
        player_card_3.grid(row=1, column=2, pady=20, padx=20)
        player_card_4 = Label(player_fr, text='', bg='plum1')
        player_card_4.grid(row=1, column=3, pady=20, padx=20)
        player_card_5 = Label(player_fr, text='', bg='plum1')
        player_card_5.grid(row=1, column=4, pady=20, padx=20)

        self.first_round()
    
    def first_round(self):
        self.game.first_round()
        self.new_game()
    
    def new_game(self):
        try:
            self.game.deal_new_game()
        except:
            self.no_cards_left()
        self.remove_card_imgs()
    
        hit_button.config(state="normal")
        stand_button.config(state="normal")
        new_game_button.config(state="disabled")


        for _ in range(2):
            self.deal_to_player()
            self.deal_to_dealer()
        #print(self.game.dealer.status)
        #print(self.game.player.status)
        
        if self.game.dealer.status == "Blackjack" and self.game.player.status == "Blackjack":
            messagebox.showinfo("Push!", "Both dealer and player have a blackjack! It's a Tie!")
            hit_button.config(state="disabled")
            stand_button.config(state="disabled")
            new_game_button.config(state="normal")
        elif self.game.dealer.status == "Blackjack":
            messagebox.showinfo("Blackjack!", "Dealer wins!")
            hit_button.config(state="disabled")
            stand_button.config(state="disabled")
            new_game_button.config(state="normal")
        elif self.game.player.status == "Blackjack":
            messagebox.showinfo("Blackjack!", "Player wins!")
            hit_button.config(state="disabled")
            stand_button.config(state="disabled")
            new_game_button.config(state="normal")
        
        self.display.title(f'Blakcjack! Cards left in deck: {self.game.deck.cards_left}')
    
    def stand(self):
        hit_button.config(state="disabled")
        stand_button.config(state="disabled")

        self.game.stand()

        if self.game.dealer.score < 17:
            if self.game.dealer.status == "Win":
                messagebox.showinfo("Dealer Wins!", f"Dealer Wins! Dealer: {self.game.dealer.score} Player: {self.game.player.score}")
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                new_game_button.config(state="normal")
            else:
                self.deal_to_dealer()
                dealer_fr.config(text=f'DEALER {self.game.dealer.score}')
                self.stand()
        else:
            if self.game.dealer.status == "Win":
                messagebox.showinfo("Dealer Wins!", f"Dealer Wins! Dealer: {self.game.dealer.score} Player: {self.game.player.score}")
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                new_game_button.config(state="normal")
            elif self.game.dealer.status == "Tie":
                messagebox.showinfo("Tie!", f"It's a Tie! Dealer: {self.game.dealer.score} Player: {self.game.player.score}")
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                new_game_button.config(state="normal")
            else:
                messagebox.showinfo("Player Wins!", f"Player Wins! Dealer: {self.game.dealer.score} Player: {self.game.player.score}")
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                new_game_button.config(state="normal")  
    
    def deal_to_player(self):
        global player_card_1, player_card_img_1, player_card_2, player_card_img_2, player_card_3, player_card_img_3, player_card_4, player_card_img_4, player_card_5, player_card_img_5  
        if self.player_spot < 5:
            if self.player_spot <= 1:
                if self.player_spot == 0:
                    card = self.game.player.hand[0]
                    player_card_img_1 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_1.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_1, compound='center')
                    self.player_spot += 1
                elif self.player_spot == 1:
                    card = self.game.player.hand[1]
                    player_card_img_2 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_2.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_2, compound='center')
                    self.player_spot += 1
            else:
                try:
                    self.game.deal_card(self.game.player)
                except:
                    self.no_cards_left()
                card = self.game.player.hand[-1]
                if self.player_spot == 2:
                    player_card_img_3 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_3.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_3, compound='center')
                    self.player_spot += 1
                elif self.player_spot == 3:
                    player_card_img_4 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_4.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_4, compound='center')
                    self.player_spot += 1
                elif self.player_spot == 4:
                    player_card_img_5 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    player_card_5.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=player_card_img_5, compound='center')
                    self.player_spot += 1
            player_fr.config(text=f'PLAYER {self.game.player.score}')
            self.game.check_for_bust()
            if self.game.player.status == "Bust":
                messagebox.showinfo("BUST!", f"Dealer wins! Dealer: {self.game.dealer.score} Player: {self.game.player.score}")
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                new_game_button.config(state="normal")
        else:
            messagebox.showinfo("Player Wins!", f"Player Wins! Player wins if they get five card without busting! Dealer: {self.game.dealer.score} Player: {self.game.player.score}")
            hit_button.config(state="disabled")
            stand_button.config(state="disabled")
            new_game_button.config(state="normal")
        self.display.title(f'Blakcjack! Cards left in deck: {self.game.deck.cards_left}')   
                
    def deal_to_dealer(self):
        global dealer_card_1, dealer_card_img_1, dealer_card_2, dealer_card_img_2, dealer_card_3, dealer_card_img_3, dealer_card_4, dealer_card_img_4, dealer_card_5, dealer_card_img_5  
        if self.dealer_spot < 5:
            if self.dealer_spot <= 1:
                if self.dealer_spot == 0:
                    card = self.game.dealer.hand[0]
                    dealer_card_img_1 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_1.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_1, compound='center')
                    self.dealer_spot += 1
                elif self.dealer_spot == 1:
                    card = self.game.dealer.hand[1]
                    dealer_card_img_2 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_2.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_2, compound='center')
                    self.dealer_spot += 1
            else:
                try:
                    self.game.deal_card(self.game.dealer)
                except:
                    self.no_cards_left()
                card = self.game.dealer.hand[-1]
                if self.dealer_spot == 2:
                    dealer_card_img_3 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_3.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_3, compound='center')
                    self.dealer_spot += 1
                elif self.dealer_spot == 3:
                    dealer_card_img_4 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_4.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_4, compound='center')
                    self.dealer_spot += 1
                elif self.dealer_spot == 4:
                    dealer_card_img_5 = self.img_resize(f"src/ui/images/{card.suit}.png")
                    dealer_card_5.config(text=f'{card.rank}', fg = 'white', font=('Courier New', 25, 'bold'), image=dealer_card_img_5, compound='center')
                    self.dealer_spot += 1
            dealer_fr.config(text=f'DEALER {self.game.dealer.score}')
        self.display.title(f'Blakcjack! Cards left in deck: {self.game.deck.cards_left}')

    def img_resize(self, card):
        card_img = Image.open(card).resize((140,210))
        global resized_card_img
        resized_card_img = ImageTk.PhotoImage(card_img)

        return resized_card_img

    def no_cards_left(self):
        hit_button.config(state="disabled")
        stand_button.config(state="disabled")
        new_game_button.config(state="disabled")
        messagebox.showinfo("No cards left", "There are no cards left in the deck. Press the 'NEW DECK'-button to continue playing")

        self.remove_card_imgs()
    
    def remove_card_imgs(self):
        self.dealer_spot = 0
        self.player_spot = 0

        dealer_card_1.config(text='', image='')
        dealer_card_2.config(text='', image='')
        dealer_card_3.config(text='', image='')
        dealer_card_4.config(text='', image='')
        dealer_card_5.config(text='', image='')

        player_card_1.config(text='', image='')
        player_card_2.config(text='', image='')
        player_card_3.config(text='', image='')
        player_card_4.config(text='', image='')
        player_card_5.config(text='', image='')