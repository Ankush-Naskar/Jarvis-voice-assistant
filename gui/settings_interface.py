import customtkinter as ctk
from gui.gui_elements import GuiFrameElements, GuiInputElements
from gui.help_window import HelpPopUpWindow
import webbrowser
from modules.data_handler.data_handling import DataHandling

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SettingInterface(GuiInputElements, GuiFrameElements):
    def __init__(self, master=None):
        super().__init__()
        self.master=master

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Initial Frame
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.minsize(500, 700)
        self.title("JARVIS")


        # -------------------- titles ---------------------
        self.title_text_arguments = {
            "font": "Courier New",
             "anchor": "n",
             "weight": "bold"
        }

        self.title_frame_arguments = {
                "height": 35, 
                "color":"#000000", 
                "side": "left", 
                "anchor": "nw",
                "x":30, 
                "bwidth":0,
                "y": 0
        }


        # ====================== Option menu -→ options ======================
        self.voice_models = [
    "en-IN-NeerjaNeural",
    "en-IN-AnanyaNeural",
    "en-IN-PrabhatNeural",
    "en-IN-NeerjaExpressiveNeural"
]
        self.ai_models = [
    "llama-3.1-8b-instant", 
    "llama-3.3-70b-versatile", 
    "mixtral-8x7b-32768"
]
        self.supported_language = [
            "english"
]

        self.parent_keys = DataHandling().parent_key_list
        self.child_key = DataHandling().child_key_list
        self.lable = DataHandling().label_list
        self.type = DataHandling().type_list
        self.default = DataHandling().default_list
  

        # ==================== Storage =======================
        self.storage = []

        self.framework()
        self.gui()

    def framework(self):
        # Background frame
        self.bg=self.main_background()

        # Main Title and Title frame
        self.main_title_frame = self.normal_frame(self.bg, 600, 80, fill="x") # Main title frame
        self.lables(self.main_title_frame, "JARVIS Settings", fsize=28, **self.title_text_arguments) # Main Title

        # Main setting frame
        self.main_frame = self.scrollable_frame(self.bg, 1240 , 650, side="top",  color="#000000", orientation="horizontal")

        # Save cancel button frame and buttons
        self.final_button_frame = self.normal_frame(self.bg, 400, 50, side="bottom", anchor="se")
        self.buttons(self.final_button_frame, "← Cancel", x=(6,3), command=self.cancel_button_function) # cancel button
        self.buttons(self.final_button_frame, "Save →", side="right", x=(3,6), command=self.save_button_function) # Save button

        # Secondary titles and title frames
        self.main_secondary_title_frame= self.normal_frame(self.main_frame, height=30, color="transparent", side="top", anchor="nw", fill="x", bwidth=0, x=0, y=0, corner=0)

        # secondary_titles = ["Basic Settings", "AI Settings", "Command Settings"]
        secondary_titles = list(dict.fromkeys(self.parent_keys))
        for secondary_title in secondary_titles:
            secondary_title_frames= self.normal_frame(self.main_secondary_title_frame, **self.title_frame_arguments)
            secondary_title_frames.pack_propagate(False)
            self.lables(secondary_title_frames, secondary_title, fsize=24, **self.title_text_arguments)


    def gui(self):
       # 1st setting box
       for frame in list(dict.fromkeys(self.parent_keys)):
           setting_frame = self.scrollable_frame(self.main_frame, anchor="nw", y=(0,40))

           for el1, el2, el3, el4, el5 in zip(self.parent_keys, self.child_key, self.lable, self.type, self.default):
               if frame == el1:
                    self.lables(setting_frame, el3)
                    if el4 == "entry":
                       new_entry=self.entrys(setting_frame, el5)
                    elif el4 == "slider":
                        new_entry= self.slider_button(setting_frame, 150, 3600)
                        new_entry.set(el5)
                    elif el4 == "option":
                        if el2 == "voice_model":
                            new_entry = self.option_menu(setting_frame, self.voice_models)
                            new_entry.set(el5)
                        elif el2=="ai_model":
                            new_entry = self.option_menu(setting_frame, self.ai_models)
                            new_entry.set(el5)
                        elif el2 == "language":
                            new_entry = self.option_menu(setting_frame, self.supported_language)
                            new_entry.set(el5)

                    if el2 == "ai_api_key":
                        help_frame = self.normal_frame(setting_frame, 350, 30, side="top", anchor="nw", x=5, y=(0,5))
                        self.buttons(help_frame,"Get API Key",100, 15,  side="right", x=(3,6), command=self.get_api_key_button_function)
                        self.buttons(help_frame, "Help",50 , 15,x=(6,3), command=HelpPopUpWindow)

                    self.storage.append(new_entry)
                        

    def cancel_button_function(self):
        self.destroy() 
        self.master.deiconify()

    def save_button_function(self):
        collected_data = []
        for entry in self.storage:
            value = entry.get() 
            collected_data.append(value)
        
        print(collected_data)
        DataHandling().collecting_entry_values(collected_data)

        self.destroy() 
        self.master.deiconify() 

    def get_api_key_button_function(self):
        webbrowser.open(f"https://console.groq.com/keys")

    

if __name__ == "__main__":
    app = SettingInterface()
    app.mainloop()