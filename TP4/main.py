import customtkinter

# Configuración general de estilo
customtkinter.set_appearance_mode("dark")  # "light", "dark", or "system"
customtkinter.set_default_color_theme("blue")  # También "green", "dark-blue", etc.

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistemas de Colas")
        self.geometry("1800x900")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame de parámetros de simulación
        self.entrys_frame_1 = MyEntryFrame(
            self,
            "Parámetros de la Simulación",
            values=["Tiempo a Simular (X)", "Iteración (i)", "Iteración (j)"]
        )
        self.entrys_frame_1.grid(row=0, column=0, padx=(30, 15), pady=20, sticky="nsew")

        # Frame de parámetros del centro
        self.entrys_frame_2 = MyEntryFrame(
            self,
            "Parámetros del Centro",
            values=[
                "Llegada Personas",
                "Solicitar documentos personales nuevos",
                "Entregar documentación requerida previamente",
                "Consultar requisitos para trámites futuros",
                "Demora de las Consultas",
                "% de las personas que se retiran",
                "Tiempo Actividades Secundarias"
            ],
            show_test_button=True
        )
        self.entrys_frame_2.grid(row=0, column=1, padx=(15, 30), pady=20, sticky="nsew")
        
        # Botón de acción principal
        self.button = customtkinter.CTkButton(
            self,
            text="Iniciar Simulación",
            font=("Arial", 16, "bold"),
            command=self.button_callback
        )
        self.button.grid(row=3, column=0, columnspan=2, padx=30, pady=15, sticky="ew")


    def button_callback(self):
        print("Parámetros Simulación:", self.entrys_frame_1.get())
        print("Parámetros Centro:", self.entrys_frame_2.get())

    def set_default_values(self):
        defaults_1 = ["60", "10", "5"]  # Tiempo, i, j
        for entry, value in zip(self.entrys_frame_1.entries, defaults_1):
            entry.delete(0, "end")
            entry.insert(0, value)

        defaults_2 = [
            "4", "45", "45", "10", "Uniforme(2,5)", "60", "30"
        ]
        for entry, value in zip(self.entrys_frame_2.entries, defaults_2):
            entry.delete(0, "end")
            entry.insert(0, value)


class MyEntryFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values, show_test_button=False):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.entries = []

        # Título
        self.title = customtkinter.CTkLabel(
            self,
            text=title,
            font=("Arial", 18, "bold"),
            fg_color="#444444",
            text_color="white",
            corner_radius=6,
            height=30
        )
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="ew")

        # Campos
        for i, value in enumerate(values):
            label = customtkinter.CTkLabel(self, text=value, font=("Arial", 15))
            entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese un valor", font=("Arial", 14))
            label.grid(row=i+1, column=0, padx=10, pady=8, sticky="w")
            entry.grid(row=i+1, column=1, padx=10, pady=8, sticky="ew")
            self.entries.append(entry)

        # Botón interno (si se solicita)
        if show_test_button:
            self.test_button = customtkinter.CTkButton(
                self,
                text="Cargar Valores de Prueba",
                font=("Arial", 14),
                command=master.set_default_values  # importante: llama a la función del App
            )
            self.test_button.grid(row=len(values)+2, column=0, columnspan=2, padx=10, pady=15, sticky="ew")

    def get(self):
        return [entry.get() for entry in self.entries]



if __name__ == "__main__":
    app = App()
    app.mainloop()
