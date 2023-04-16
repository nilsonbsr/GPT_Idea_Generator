import os
import openai
import customtkinter as ctk

# create window
window = ctk.CTk()
window.geometry("750x550")
window.title("ChatGPT Project Idea Generator")

# dark mode window
ctk.set_appearance_mode("dark")

# label
title_label = ctk.CTkLabel(master=window, text="Project Idea Generator", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10 , pady=(49, 20))

# frame
frame = ctk.CTkFrame(master=window, bg_color="white").pack()
# running
window.mainloop()