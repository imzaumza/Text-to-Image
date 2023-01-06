# The code imports the auth_token module, which allows the code to access the functions contained in the module.
from auth import auth_token

# for opening, manipulating, and saving images
from PIL import Image, ImageTk

import tkinter as tk

root = tk.Tk()
root.geometry("532x632")
root.resizable(False,False)
root.title("Text-to-Image")



#A modern and customizable python UI-library based on Tkinter
import customtkinter as ctk



#Requests allows you to send HTTP/1.1 requests extremely easily.
import requests

# pip install openai
import openai

openai.api_key = auth_token

# create the app
# app = tk.Tk()
# app.geometry("532x632")
# app.title("Text-to-Image")
# ctk.set_appearance_mode("light")

main_image = tk.Canvas(root, width=512, height=512)
main_image.place(x=10, y=110)

frame = ctk.CTkEntry(master=root)
# Creates widgets for user input
class Imagespecs():
    def __init__(self,master):
        frame.__init__(self,master)
        self.grid()
        self.y_axis()
        self.x_axis()

prompt_input = ctk.CTkEntry(master=root,
    height=40,
    width=512,
    font=("Arial", 20),
    text_color="white",
    placeholder_text="Enter a prompt.",
    placeholder_text_color="gray",
)
prompt_input.place(x=10, y=10)


def apply_magic():
    global tk_img
    global img

    prompt = prompt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=tk_img)
    print("Image created for prompt:", prompt)


def save_image():
    prompt = prompt_input.get().replace(" ", "_")
    img.save(f"img/{prompt}.png")


magic_button = ctk.CTkButton(master=root,
    height=40,
    width=120,
    text=("Arial", 20),
    text_color="white",
    command=apply_magic,
)
magic_button.configure(text="Generate")
magic_button.place(x=133, y=60)

save_button = ctk.CTkButton(master=root,
    height=40,
    width=120,
    text=("Arial", 20),
    text_color="white",
    command=save_image,
)
save_button.configure(text="Save image")
save_button.place(x=266, y=60)

root.mainloop()