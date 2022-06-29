from tkinter import *
import pandas as pd
import random

# Read Afrikaans words file and save values to list of dictionaries called afr_words
with open('afr_words.csv', 'r') as datafile:
    afr_words_df = pd.read_csv(datafile)
    # Set the first column to the index column
    afr_words_df.set_index('Unnamed: 0', inplace=True)
    afr_words = afr_words_df.to_dict(orient='records')


# Pick random word in afr_words and display the word
def pick_random_word():
    global current_word_txt, language_txt
    random_afr_word = random.choice(afr_words)['Afrikaans']
    canvas.itemconfig(current_word_txt, text=random_afr_word)


# -------------------- UI SETUP -------------------- #
# Initialize window
window = Tk()
window.title('Flashcards - Learn Afrikaans')
window.config(padx=50, pady=50, bg='#B1DDC6')

# Create canvas to display card
canvas = Canvas(window, width=800, height=526)
canvas.config(bg='#B1DDC6', highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

# Add image and text onto canvas
card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_img)
language_txt = canvas.create_text(400, 150, text='Afrikaans', font=('Ariel', 40, 'italic'), fill='#000000')
current_word_txt = canvas.create_text(400, 263, text='môre', font=('Ariel', 60, 'bold'), fill='#000000')

# Create Yes / No images
yes_img = PhotoImage(file='images/right.png')
no_img = PhotoImage(file='images/wrong.png')

# Add Yes / No buttons
yes_btn = Button(image=yes_img, bg='#B1DDC6', borderwidth=0, highlightthickness=0, command=pick_random_word)
yes_btn.grid(row=2, column=1)

no_btn = Button(image=no_img, bg='#B1DDC6', borderwidth=0, highlightthickness=0, command=pick_random_word)
no_btn.grid(row=2, column=2)

# Keep screen open
window.mainloop()
