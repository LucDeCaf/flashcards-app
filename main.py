from tkinter import *

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
yes_btn = Button(image=yes_img, bg='#B1DDC6', borderwidth=0, highlightthickness=0)
yes_btn.grid(row=2, column=1)

no_btn = Button(image=no_img, bg='#B1DDC6', borderwidth=0, highlightthickness=0)
no_btn.grid(row=2, column=2)

# Keep screen open
window.mainloop()
