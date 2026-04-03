import customtkinter as ctk
import threading

class GuiFrameElements(ctk.CTk):
    def __init__(self):
        super().__init__()

    # ================ Main background frame ================
    def main_background(self):
        background= ctk.CTkFrame(self, fg_color="transparent")
        background.pack()
        return background

    # ================ Normal frame ================
    def normal_frame(self, parent, width=350, height=600, color="#000000", corner=10, bwidth=1, side="top", anchor="n", fill=None, x=30, y=10,):
        nframe= ctk.CTkFrame(
                            parent,
                            width=width,
                            height=height,
                            fg_color=color,
                            corner_radius=corner,

                            border_width=bwidth,
                            border_color="#7ed6df"
                             )
        nframe.pack(fill=fill, side=side, anchor=anchor, padx=x, pady=y,  expand=True )
        return nframe

    # ================ Scrollable frame ================
    def scrollable_frame(self,  parent, width=300, height=500, color="#535c68", corner=30, y=10,  side="left", anchor="n", fill=None, orientation="vertical"):

        sframe= ctk.CTkScrollableFrame(
                    parent,
                    width=width,
                    height=height,
                    fg_color=color,
                    corner_radius=corner,
                    orientation=orientation,

                    border_width=1,
                    border_color="#7ed6df"
                    )
        sframe.pack(padx=30, pady=y, side=side, anchor=anchor, fill=fill, expand=True )
        return sframe

    # ================ Button ================
    def buttons(self, parent,  text, width=150, height=30, bwidth=1, bcolor="#000000", color="#075B5E", side="left", x=4, command=None):

        button=ctk.CTkButton(
                    parent, 
                    text=text, 
                    width=width, 
                    height=height, 
                    border_width=bwidth,
                    border_color=bcolor, 
                    fg_color=color,
                    command=command,

                    text_color="#F9F6C4",
                    )
        
        button.pack(anchor="se", side=side, expand=False, padx=x, pady=6)
        return button

    # ================ text lables ================
    def lables(self, parent, text, font="Roboto", fsize=18, side="top", anchor="nw", color="#E1FFBB", weight="normal"):
        lable= ctk.CTkLabel(
            parent, 
            text=text, 
            text_color=color, 
            font=(font, fsize, weight)
            ).pack(padx=5, pady=5, side=side, anchor=anchor)
        

class GuiInputElements(ctk.CTk):
    def __init__(self):
        super().__init__()
        
    # ================== Entry box ====================
    def entrys(self, parent, text):
        entry = ctk.CTkEntry(
            parent,
            width=250,
            height=35,
            placeholder_text=text,
            placeholder_text_color="#12182A",
        )
        entry.pack(padx=5, pady=5, side="top", anchor="nw")
        return entry
    # ==================== Text Box ======================
    def text_box(self, parent, text):
        textbox = ctk.CTkTextbox(
            parent,
            width=250,
            height=250,
            fg_color="#343638",
            text_color="#12182A"
        )
        textbox.insert("0.0", text)
        textbox.pack(padx=5, pady=5, side="top", anchor="nw")
        return textbox

    # ========================Option menu=========================
    def option_menu(self, parent, values):
        optionmenu= ctk.CTkOptionMenu(
            parent, 
            width=250,
            height=35,
            values=values,
            fg_color="#343638",
            button_color="#075B5E",
            text_color="#12182A"
            )
        optionmenu.pack(padx=5, pady=5, side="top", anchor="nw")
        return optionmenu
    
    # ========================= Slider Button =============================
    def slider_button(self, parent, starting, ending):
        sliderbutton = ctk.CTkSlider(
            parent, 
            width=250,
            height=20,
            from_=starting,
            to=ending,
            )
        sliderbutton.pack(padx=5, pady=5, side="top", anchor="nw")
        return sliderbutton