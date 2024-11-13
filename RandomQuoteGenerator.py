import tkinter as tk
import random

# List of quotes
quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "सफलता की कहानियाँ मत सुनो, उससे सिर्फ संदेश मिलेगा। असफलता की कहानियाँ सुनो, उससे सफलता के नए विचार मिलेंगे। - अब्दुल कलाम",
    "कर्म किए जा, फल की चिंता मत कर। - श्रीमद्भगवद्गीता",
    "जहाँ चाह है, वहाँ राह है। - हिंदी कहावत",
    "जो व्यक्ति सत्य के मार्ग पर चलता है, उसकी सदैव विजय होती है। - महात्मा गांधी",
    "असफलता ही सफलता की पहली सीढ़ी होती है। - हिंदी कहावत",
    "जैसा सोचोगे, वैसा बनोगे। - भगवान बुद्ध",
    "सपने वो नहीं जो हम सोते हुए देखते हैं, सपने वो हैं जो हमें सोने नहीं देते। - ए पी जे अब्दुल कलाम",
    "जिंदगी में कभी किसी को दोष मत दो, अच्छे लोग खुशियाँ लाते हैं और बुरे लोग अनुभव। - हिंदी कहावत",
    "यदि आप समय का सदुपयोग नहीं करते, तो आप जीवन का सदुपयोग नहीं कर सकते। - हिंदी कहावत"
]

# List to store favorite quotes
favorite_quotes = []
current_quote = None

# Function to generate a random quote
def generate_quote():
    global current_quote
    current_quote = random.choice(quotes)
    quote_label.config(text=current_quote)

# Function to add the current quote to favorites
def add_favorite():
    if current_quote and current_quote not in favorite_quotes:
        favorite_quotes.append(current_quote)
        status_label.config(text="Quote added to favorites!", fg="white")
    else:
        status_label.config(text="Quote is already in favorites or no quote generated!", fg="red")

# Function to display favorite quotes
def show_favorites():
    if favorite_quotes:
        favorites_window = tk.Toplevel(root)
        favorites_window.title("Favorite Quotes")
        favorites_window.geometry("500x300")
        for idx, quote in enumerate(favorite_quotes, start=1):
            tk.Label(favorites_window, text=f"{idx}. {quote}", wraplength=400, font=("Helvetica", 10), justify="center").pack(pady=5)
    else:
        status_label.config(text="No favorite quotes to display.", fg="red")

# Function to copy the current quote to the clipboard
def copy_quote():
    if current_quote:
        root.clipboard_clear()
        root.clipboard_append(current_quote)
        status_label.config(text="Quote copied to clipboard!", fg="green")
    else:
        status_label.config(text="No quote to copy.", fg="red")

# Initialize Tkinter window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x500")
root.configure(bg="dim gray")  # Dark background for the main window

# Set up widgets with color names
title_label = tk.Label(root, text="Random Quote Generator", font=("Helvetica", 16, "bold"), bg="dim gray", fg="white")
title_label.pack(pady=20)

quote_label = tk.Label(root, text="", wraplength=400, font=("Helvetica", 14, "italic"), justify="center",
                       bg="black", fg="gold", width=40, height=5, highlightbackground="white", highlightthickness=2)
quote_label.pack(pady=20)

generate_button = tk.Button(root, text="New Quote", command=generate_quote, font=("Helvetica", 12, "bold"), bg="blue", fg="white")
generate_button.pack(pady=5)

favorite_button = tk.Button(root, text="Save Favorite", command=add_favorite, font=("Helvetica", 12, "bold"), bg="green", fg="white")
favorite_button.pack(pady=5)

show_favorites_button = tk.Button(root, text="Show Favorites", command=show_favorites, font=("Helvetica", 12, "bold"), bg="orange", fg="white")
show_favorites_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_quote, font=("Helvetica", 12, "bold"), bg="purple", fg="white")
copy_button.pack(pady=5)

# Label for status messages
status_label = tk.Label(root, text="", font=("Helvetica", 10), bg="dim gray", fg="white")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
