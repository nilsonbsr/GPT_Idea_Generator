import os
import openai
import customtkinter as ctk


<<<<<<< Updated upstream
def py_func():
    raise Exception('py_func function should be implemented')
=======
# interact with chatGPT
def generate():
    prompt = "Please generate 10 ideas for coding project. "
    language = language_dropdown.get()
    prompt += "The programming language is " + language + ". "
    difficulty = difficulty_value.get()
    prompt += "The difficulty is " + difficulty + ". "

    if checkbox1.get():
        prompt += "The project should include a database."
    if checkbox2.get():
        prompt += "The project should include an API"

    print(prompt)
    # get the key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # send a request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "prompt"}
        ]
    )
    # get the answer provided by chatgpt
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)

>>>>>>> Stashed changes


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

