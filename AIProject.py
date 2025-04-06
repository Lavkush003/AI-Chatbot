import tkinter as tk
from tkinter import messagebox, scrolledtext
import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyD6bTQ1NbxvKaIfybTWxcjS8epl1tYQufc")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_grocery_list():
    meal_input = meal_entry.get("1.0", tk.END).strip()
    if not meal_input:
        messagebox.showwarning("Input Error", "Please enter some meals.")
        return

    try:
        prompt = (
            f"Generate a grocery list for the following meals. "
            f"Group similar ingredients together and remove duplicates.\n"
            f"Meals: {meal_input}"
        )

        response = model.generate_content(prompt)

        ingredients = response.text.strip()
        result_text.config(state='normal')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, ingredients)
        result_text.config(state='disabled')

    except Exception as e:
        messagebox.showerror("Gemini API Error", f"Error calling Gemini API:\n{e}")

# GUI setup
root = tk.Tk()
root.title("AI Grocery List Generator (Gemini)")
root.geometry("600x500")
root.config(padx=20, pady=20)

title_label = tk.Label(root, text="Enter your Meal Plan", font=("Helvetica", 16))
title_label.pack(pady=10)

meal_entry = scrolledtext.ScrolledText(root, height=6, font=("Helvetica", 12))
meal_entry.pack(fill="both", pady=10)

generate_button = tk.Button(
    root, text="Generate Grocery List", command=generate_grocery_list,
    font=("Helvetica", 12), bg="blue", fg="white"
)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Your Grocery List:", font=("Helvetica", 14))
result_label.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, height=12, font=("Helvetica", 12), state='disabled')
result_text.pack(fill="both", expand=True)

root.mainloop()