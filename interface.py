import customtkinter as ctk
import threading
from main import stop_jarvis_execution, run_jarvis

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainInterface(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x500")
        self.minsize(300, 400)
        self.title("JARVIS")

    def start_jarvis(self):
        self.run = threading.Thread(target=run_jarvis)
        self.run.daemon = True
        self.run.start()
        self.status_label.configure(text="STATUS: ONLINE", font=("Orbitron", 20, "bold"), text_color="#D82B18")

    def stop_jarvis(self):
        stop_jarvis_execution()
        self.status_label.configure(text="STATUS: OFFLINE", font=("Orbitron", 20, "bold"), text_color="#18D8B8")
    
    def toggle_jarvis(self):
        self.current_text =  self.btn.cget("text")

        if "START" in self.current_text:
            # Change to STOP state
            self.btn.configure(text="⏹ STOP", text_color="red", border_color="red")
            self.start_jarvis() 
        else:
            # Change back to START state
            self.btn.configure(text="🔴 START", text_color="#18D8B8", border_color="#00FFDD")
            self.stop_jarvis()

    def interface(self):
        self.settings_btn = ctk.CTkButton(self, text="⚙️", width=40, height=40, compound="right", fg_color="#1D1A1A", text_color="#69CAF0")
        self.settings_btn.pack(anchor="ne", pady=10, padx=10)

        self.status_label = ctk.CTkLabel(self, text="STATUS: OFFLINE", font=("Orbitron", 20, "bold"), text_color="#18D8B8")
        self.status_label.pack(pady=(30, 20))

        self.btn = ctk.CTkButton(
            self, 
            text="🔴 START", 
            font=("Arial", 18, "bold"),
            width=200, 
            height=200, 
            corner_radius=100,
            fg_color="transparent", 
            border_width=4,
            border_color="#00FFDD",
            text_color="#00BFFF",
            hover_color="#333333",
            command=self.toggle_jarvis
            
        )
        self.btn.pack()

app = MainInterface()
app.interface()
app.mainloop()