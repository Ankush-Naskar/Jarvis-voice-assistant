import customtkinter as ctk
from PIL import Image, ImageTk
import webbrowser

class HelpPopUpWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.title("Jarvis Help Window")
        self.after(100, self.lift)

        self.how_to_get_api_key()

    def how_to_get_api_key(self):
        ctk.CTkLabel(self, text="How to get API Key?",text_color="#2ABB64", font=("Helvetica", 28, "bold")).pack(pady=(20,0), anchor="n", side="top")

        sframe= ctk.CTkScrollableFrame(self, fg_color="transparent")
        sframe.pack(fill="both", expand=True )

        image_paths=[
                     "gui/media/how_to_get_api_key_1.png",
                     "gui/media/how_to_get_api_key_2.png",
                     "gui/media/how_to_get_api_key_3.png",
                     "gui/media/how_to_get_api_key_4.png",
                     "gui/media/how_to_get_api_key_5.png",
                     "gui/media/how_to_get_api_key_6.png",
                     ]

        for image in image_paths:

            img_file = Image.open(f"{image}")
            self.my_img = ctk.CTkImage(light_image=img_file,
                                        dark_image=img_file,
                                        size=(1000, 550)) # Adjust size as needed

            self.image_label = ctk.CTkLabel(sframe, image=self.my_img, text="", fg_color="#000000", )
            self.image_label.pack(pady=20)

        ctk.CTkButton(sframe, text="Close", fg_color="#0F9F4B", width=80, height=30, command=self.destroy).pack(pady=20)
        ctk.CTkLabel(sframe, text="Get the API key frome here:",text_color="#FFFFFF", font=("Helvetica", 18)).pack(pady=0)
        ctk.CTkButton(sframe, text="Get API Ket", fg_color="#0F9F4B", width=150, height=30, command=self.get_api_key_function).pack(pady=(10, 30))

    def get_api_key_function(self):
        webbrowser.open(f"https://console.groq.com/keys")

