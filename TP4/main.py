import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistemas de Colas")
        self.geometry("1800x900")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.entrys_frame_1 = MyEntryFrame(self, "Parametros de la Simulación", values=["Tiempo a Simular (X)", "Iteracion (i)", "Iteracion (j)"])
        self.entrys_frame_1.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.entrys_frame_1.configure(fg_color="transparent")
        self.entrys_frame_2 = MyEntryFrame(self, "Parametros del Centro", values=["Llegada Personas", "Solicitar documentos personales nuevos", "Entregar documentación requerida previamente", "Consultar requisitos para trámites futuros", "Demora de las Consultas", "% de las personas que se retiran", "Tiempo Actividades Secundarias"])
        self.entrys_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.entrys_frame_2.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        
        self.set_default_values()

    def button_callback(self):
        print("entrys_frame_1:", self.entrys_frame_1.get())
        print("entrys_frame_2:", self.entrys_frame_2.get())
        
    def set_default_values(self):
        # Valores por defecto para entrys_frame_1 (simulación)
        defaults_1 = ["10", "1", "10"]  # Tiempo a simular, i, j
        for entry, value in zip(self.entrys_frame_1.entries, defaults_1):
            entry.delete(0, "end")
            entry.insert(0, value)

        # Valores por defecto para entrys_frame_2 (centro)
        defaults_2 = [
            "4",     # Llegada Personas (cada 4 minutos)
            "45",    # Solicitar documentos (%)
            "45",    # Entregar documentación (%)
            "10",    # Consultas (%)
            "Uniforme(2,5)",  # Demora de consultas
            "60",    # % que se retiran
            "30"     # Tiempo actividades secundarias   
        ]
        for entry, value in zip(self.entrys_frame_2.entries, defaults_2):
            entry.delete(0, "end")
            entry.insert(0, value)

class MyEntryFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=2) 
        self.values = values
        self.entries = [] 

        self.title = customtkinter.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(values):
            label = customtkinter.CTkLabel(self, text=value)
            entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese un valor")

            label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")

            self.entries.append(entry)

    def get(self):
        return [entry.get() for entry in self.entries]
    


        

app = App()
app.mainloop()

