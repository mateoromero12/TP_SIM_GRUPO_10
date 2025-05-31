import subprocess
import sys
import os
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class BienvenidaApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simulación de Sistemas de Colas")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        self.configure(padx=40, pady=40)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # ---------- Sección 1: Encabezado ----------
        header_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="nsew")
        header_frame.grid_columnconfigure(0, weight=1)

        # Logo
        try:
            image = Image.open("images/utn_logo.png")
            logo = customtkinter.CTkImage(image, size=(180, 90))
            customtkinter.CTkLabel(header_frame, image=logo, text="").pack(pady=10)
        except:
            customtkinter.CTkLabel(header_frame, text="[Logo UTN]", font=("Arial", 24)).pack()

        # Títulos
        customtkinter.CTkLabel(header_frame, text="Trabajo Práctico N°4", font=("Arial", 26, "bold")).pack()
        customtkinter.CTkLabel(header_frame, text="Modelos de Simulación Dinámicos", font=("Arial", 20)).pack()
        customtkinter.CTkLabel(header_frame, text="Simulación de líneas de espera/colas", font=("Arial", 18, "italic")).pack()
        customtkinter.CTkLabel(header_frame, text="“Centro de Documentación Municipal”", font=("Arial", 16)).pack(pady=(0, 20))

        # Materia
        customtkinter.CTkLabel(header_frame, text="Materia: Simulación", font=("Arial", 14)).pack()

        # ---------- Sección 2: Cuerpo principal ----------
        body_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        body_frame.grid(row=1, column=0, sticky="nsew", pady=10)
        body_frame.grid_columnconfigure((0, 1), weight=1)

        # ----- Profesores -----
        prof_frame = customtkinter.CTkFrame(body_frame, corner_radius=10)
        prof_frame.grid(row=0, column=0, padx=20, sticky="nsew")
        customtkinter.CTkLabel(prof_frame, text="Profesores", font=("Arial", 16, "bold")).pack(pady=(10, 5))
        for prof in ["Auquer, Marcelo", "Berotarán, Juan José", "Magris, Sergio Víctor"]:
            customtkinter.CTkLabel(prof_frame, text=prof, font=("Arial", 13)).pack(anchor="center", pady=2)

        # ----- Estudiantes -----
        alum_frame = customtkinter.CTkFrame(body_frame, corner_radius=10)
        alum_frame.grid(row=0, column=1, padx=20, sticky="nsew")
        customtkinter.CTkLabel(alum_frame, text="Estudiantes", font=("Arial", 16, "bold")).pack(pady=(10, 5))

        alumnos = [
            ("94269", "Adragna, Jimena Sofía"),
            ("68719", "Albarracín, Gonzalo"),
            ("89978", "Costamagna, Maria Paz"),
            ("90812", "Fernandez Romero, Lisandro"),
            ("89765", "Gil, Matías Ezequiel"),
            ("87440", "Mazzucco, Giuliano"),
            ("83009", "Romero Plaza, Mateo"),
            ("95794", "Saggiorato, Gina")
        ]

        table = customtkinter.CTkFrame(alum_frame, fg_color="transparent")
        table.pack(padx=10, pady=10)

        # Filas
        for i, (legajo, nombre) in enumerate(alumnos, start=1):
            customtkinter.CTkLabel(table, text=legajo, font=("Arial", 12)).grid(row=i, column=0, padx=20, sticky="w")
            customtkinter.CTkLabel(table, text=nombre, font=("Arial", 12)).grid(row=i, column=1, sticky="w")

        # ---------- Sección 3: Botón ----------
        footer_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        footer_frame.grid(row=2, column=0, sticky="nsew")
        footer_frame.grid_columnconfigure(0, weight=1)

        customtkinter.CTkLabel(footer_frame, text="Grupo: 10     Curso: 4K2", font=("Arial", 13)).pack()

        customtkinter.CTkButton(
            footer_frame,
            text="Ingresar al Programa",
            font=("Arial", 16, "bold"),
            height=80,
            width=250,
            command=self.abrir_app
        ).pack(pady=20)


    def abrir_app(self):
        self.destroy()
        ruta = os.path.join(os.path.dirname(__file__), "main.py")
        subprocess.Popen([sys.executable, ruta])


if __name__ == "__main__":
    app = BienvenidaApp()
    app.mainloop()
