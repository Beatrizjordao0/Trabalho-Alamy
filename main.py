import customtkinter as ctk
from PIL import Image, ImageTk
import math

app = ctk.CTk()
app.geometry("600x600")
app.title("Matriz")
app.configure(fg_color="#7B4626")
fonte_matriz = ("Fredoka One", 35)
fonte_geral = ("Fredoka One", 40, 'bold')
fonte_resultado = ("Fredoka One", 90, 'bold')
cor_escura = "#7B4626"
cor_clara = "#F2D3AC"
reset_cor = "#E07A6B"
cor_determinante = "#C59C69"
cor_fonte = "#8E542B"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

bg_image = Image.open("1Periodo-CDC\Python\Alamy\Trabalho\Background.png") 
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(relwidth=1, relheight=1)

conteudo_frame = ctk.CTkFrame(app, width=375, height=200, fg_color="#F8E2B8", corner_radius=0)
conteudo_frame.place(relx=0.65, rely=0.4, anchor="center")

# Função para calcular a determinante
def calcular_determinante():
    a1 = float(a.get())
    a2 = float(b.get())
    a3 = float(c.get())
    b1 = float(d.get())
    b2 = float(e.get())
    b3 = float(f.get())
    c1 = float(g.get())
    c2 = float(h.get())
    c3 = float(i.get())

    det = a1 * (b2 * c3 - b3 * c2) - a2 * (b1 * c3 - b3 * c1) + a3 * (b1 * c2 - b2 * c1)
    resultado_label.configure(text=f"{det}")


def limpar_entradas():
    a.delete(0, "end")
    b.delete(0, "end")
    c.delete(0, "end")
    d.delete(0, "end")
    e.delete(0, "end")
    f.delete(0, "end")
    g.delete(0, "end")
    h.delete(0, "end")
    i.delete(0, "end")
    resultado_label.configure(text="")


# Entradas (CTkEntry)
a = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="1,1", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

b = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="1,2", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

c = ctk.CTkEntry(app, 
                 width=80, 
                 height=80,
                 placeholder_text="1,3", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

d = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="2,1", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

e = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="2,2", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

f = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="2,3", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

g = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="3,1", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

h = ctk.CTkEntry(app, 
                 width=80, 
                 height=80,
                 placeholder_text="3,2", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

i = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="3,3", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

# Posicionamento com grid (dentro do frame central)
a.place(relx=0.279, rely=0.348, anchor="e")
b.place(relx=0.365, rely=0.348, anchor="e")
c.place(relx=0.449, rely=0.348, anchor="e")

d.place(relx=0.279, rely=0.5, anchor="e")
e.place(relx=0.365, rely=0.5, anchor="e")
f.place(relx=0.449, rely=0.5, anchor="e")

g.place(relx=0.279, rely=0.66, anchor="e")
h.place(relx=0.365, rely=0.66, anchor="e")
i.place(relx=0.449, rely=0.66, anchor="e")

# Botão e label de resultado
botao = ctk.CTkButton(app, 
                      text="CALCULAR", 
                      command=calcular_determinante, 
                      fg_color= cor_determinante,
                      hover_color="#BC7E4C",
                      font=fonte_geral,
                      text_color= cor_escura,
                      width=310,
                      height=105,
                      border_color=cor_escura,
                      border_width=10)


botao.place(relx=0.537, 
            rely=0.69, 
            anchor="w")

resultado_label = ctk.CTkLabel(conteudo_frame, 
                               text="", 
                               font=fonte_resultado,
                               text_color= cor_escura,
                               fg_color="transparent"
                               )
resultado_label.place(relx=0.5, rely=0.5, anchor="center")

botao_limpar = ctk.CTkButton(bg_label,
                             text="❌",
                             command=limpar_entradas,
                             fg_color=reset_cor,
                             hover_color="#F25A3C",
                             font=fonte_geral,
                             text_color=cor_escura,
                             width=120,
                             height=105,
                             border_color=cor_escura,
                             border_width=10)
botao_limpar.place(relx=0.778, rely=0.2, anchor="w")

app.mainloop()
