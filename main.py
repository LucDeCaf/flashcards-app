from tkinter import *
import pandas as pd
import random


class FlashcardApp:
    def __init__(self):
        # -------------------- Initialize Variables -------------------- #
        # Read Afrikaans words file and save values to list of dictionaries called afr_words
        with open('afr_words.csv', 'r') as datafile:
            afr_words_df = pd.read_csv(datafile)
            # Set the first column to the index column
            afr_words_df.set_index('Unnamed: 0', inplace=True)
            self.afr_words = afr_words_df.to_dict(orient='records')

        # Initialize random_word as random English/Afrikaans word pair
        self.random_word = random.choice(self.afr_words)

        # -------------------- UI SETUP -------------------- #
        # Initialize window
        self.window = Tk()
        self.window.title('Flashcards - Learn Afrikaans')
        self.window.config(padx=50, pady=50, bg='#B1DDC6')

        # Create canvas to display card
        self.canvas = Canvas(self.window, width=800, height=526)
        self.canvas.config(bg='#B1DDC6', highlightthickness=0)
        self.canvas.grid(row=1, column=1, columnspan=2)

        # Add image and text onto canvas
        self.card_img = PhotoImage(file='images/card_front.png')
        self.canvas.create_image(400, 263, image=self.card_img)
        self.language_txt = self.canvas.create_text(400, 150, text='Afrikaans', font=('Ariel', 40, 'italic'),
                                                    fill='#000000')
        self.current_word_txt = self.canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'),
                                                        fill='#000000')

        # Create Yes / No images
        yes_img = PhotoImage(file='images/right.png')
        no_img = PhotoImage(file='images/wrong.png')

        # Add Yes button
        self.yes_btn = Button(image=yes_img, bg='#B1DDC6', borderwidth=0, highlightthickness=0,
                              command=self.show_afr_word)
        self.yes_btn.grid(row=2, column=1)

        # Add No button
        self.no_btn = Button(image=no_img, bg='#B1DDC6', borderwidth=0, highlightthickness=0,
                             command=self.show_afr_word)
        self.no_btn.grid(row=2, column=2)

        # Keep screen open
        self.window.mainloop()

    def show_afr_word(self) -> None:
        """Pick random Afrikaans word and display the word"""
        # Get random word from afr_words
        self.random_word = random.choice(self.afr_words)

        # Show random Afrikaans word
        random_afr_word = self.random_word['Afrikaans']
        self.canvas.itemconfig(self.language_txt, text='Afrikaans')
        self.canvas.itemconfig(self.current_word_txt, text=random_afr_word)
        self.card_img.config(file='images/card_front.png')

        # Wait 3 seconds, then show english translation
        self.window.after(ms=3000, func=self.show_eng_word)

    def show_eng_word(self):
        random_eng_word = self.random_word['English']
        self.canvas.itemconfig(self.language_txt, text='English')
        self.canvas.itemconfig(self.current_word_txt, text=random_eng_word)
        self.card_img.config(file='images/card_back.png')


application = FlashcardApp()
