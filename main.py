import os
import openai
import customtkinter as ctk


def py_func():
    raise Exception('py_func function should be implemented!')


def java_func():
    raise Exception("Java_func should be implemented!")


def script_func():
    raise Exception("script_func should be implemented!")


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

# creating nested frames, lable
language_frame = ctk.CTkFrame(master=frame)
language_frame.pack(padx=100, pady=(20,5), fill="both")
language_label = ctk.CTkLabel(master=language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
language_label.pack()
# running
window.mainloop()

