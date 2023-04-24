import os
import openai
import customtkinter as ctk

# interact with chatGPT
def generate():
    raise Exception("generate function should be implemented")


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
frame = ctk.CTkFrame(master=window)
frame.pack(fill="x", padx=100)

# creating first nested frame
language_frame = ctk.CTkFrame(master=frame)
language_frame.pack(padx=100, pady=(20,5), fill="both")
language_label = ctk.CTkLabel(master=language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
language_label.pack()

# creating dropdown menu
language_dropdown = ctk.CTkComboBox(master=language_frame, values=["Python", "Java", "C++", "Javascript", "Golang"])
language_dropdown.pack(pady=10)

# creating second nested frame
difficulty_frame = ctk.CTkFrame(master=frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(master=difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()

# creating radio buttons
difficulty_value = ctk.StringVar(value="Easy")
radio_button1 = ctk.CTkRadioButton(master=difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radio_button1.pack(side="left", padx=(20,10), pady=10)
radio_button2 = ctk.CTkRadioButton(master=difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radio_button2.pack(side="left", padx=10, pady=10)
radio_button3 = ctk.CTkRadioButton(master=difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radio_button3.pack(side="left", padx=10, pady=10)

# creating feature frame
feature_frame = ctk.CTkFrame(master=frame)
feature_frame.pack(padx=100, pady=5, fill="both")
feature_label = ctk.CTkLabel(master=feature_frame, text="Features", font=ctk.CTkFont(weight="bold"))
feature_label.pack()

# creating checkbox
checkbox1 = ctk.CTkCheckBox(master=feature_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(master=feature_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

# generate button
generate_button = ctk.CTkButton(master=frame, text="Generate Ideas", command=generate)
generate_button.pack(padx=100, fill="x", pady=(5, 20))

# result text box
result = ctk.CTkTextbox(master=window, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

# running
window.mainloop()

