import os
import openai
import customtkinter as ctk


def py_func():
    raise Exception('py_func function should be implemented')


# create a window
window = ctk.CTk()
window.geometry("750x550")
window.title("ChatGPT Project Idea Generator")

# dark mode window
ctk.set_appearance_mode("dark")

# label
title_label = ctk.CTkLabel(master=window, text="Project Idea Generator", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(49, 20))

# frame
frame = ctk.CTkFrame(master=window, bg_color="white")
frame.pack(fill="x", padx=100)

# button
python_button = ctk.CTkButton(master=window, text="Python", command=py_func)
python_button.pack(pady=50)
# running
window.mainloop()

