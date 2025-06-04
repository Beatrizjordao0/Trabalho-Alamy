#/////////////////////////////////////////////////////////////////////////////////////
                    # ***** IMPORTAÇÕES *****
from sympy import symbols, sympify, simplify, log, sqrt, N
import customtkinter as ctk
from PIL import Image, ImageTk
import math
import re

#//////////////////////////////////////////////////////////////////////////////////

                    # ***** CONFIGURAÇÕES DE TELA *****
app = ctk.CTk()
app.geometry("1500x750")
app.title("Matriz")
app.configure(fg_color="#7B4626")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---> CONFIGURAÇÕES DO BACKGROUND

bg_image = Image.open("1Periodo-CDC\Python\Alamy\Trabalho\Background.png") 
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(relwidth=1, relheight=1)

# ---> BACKGROUND DO RESULTADO

conteudo_frame = ctk.CTkFrame(app, width=375, height=200, fg_color="#F8E2B8", corner_radius=0)
conteudo_frame.place(relx=0.65, rely=0.4, anchor="center")

#///////////////////////////////////////////////////////////////////////////////////
# ***** VARIÁVEIS ÚTEIS *****
fonte_matriz = ("Fredoka One", 25, 'bold')
fonte_geral = ("Fredoka One", 40, 'bold')
fonte_resultado = ("Fredoka One", 60, 'bold')
cor_escura = "#7B4626"
cor_clara = "#F2D3AC"
reset_cor = "#E07A6B"
cor_determinante = "#C59C69"
cor_fonte = "#8E542B"
x = symbols('x')
#///////////////////////////////////////////////////////////////////////////////////

                        # ***** FUNÇÕES ÚTEIS *****

#Possibilita diferentes espressões matemáticas inseridas pelo usuário
def avaliar_expressao(expr_str):
    try:
        # Substitui ^ por ** para potenciação
        expr_str = expr_str.replace("^", "**")

        # Coloca '*' entre número e variável (ex: 3x vira 3*x)
        expr_str = re.sub(r"(\d)([a-zA-Z](?![a-zA-Z]))", r"\1*\2", expr_str)

        # Faz o sympify passar funções matemáticas
        expr = sympify(expr_str, {"log": log, "sqrt": sqrt})

        # Simplifica a expressão
        expr_simplificada = simplify(expr)

        # Se tem símbolos (variáveis), retorna a expressão simplificada (ex: 13*x - 21)
        if expr_simplificada.free_symbols:
            return expr_simplificada
        
        # Se não tem símbolos, tenta converter para float e retornar número
        try:
            valor_num = float(expr_simplificada)
            return valor_num
        except (TypeError, ValueError):
            # Caso não consiga converter para float, retorna expressão simplificada
            return expr_simplificada
        
    # Captura o erro e guarda na variável e
    except Exception as erro:
        print(f"Erro ao avaliar expressão '{expr_str}': {erro}")
        return None

def limitar_casas(expr, casas=2):
    #Arredonda os números da expressão simbólica para o número de casas decimais.
    return N(expr, casas)

def calcular_determinante():

    # Pega o valor de entrada no CTKEntry e gaurda nas respectivas variáveis
    a1 = avaliar_expressao(a.get())
    a2 = avaliar_expressao(b.get())
    a3 = avaliar_expressao(c.get())
    b1 = avaliar_expressao(d.get())
    b2 = avaliar_expressao(e.get())
    b3 = avaliar_expressao(f.get())
    c1 = avaliar_expressao(g.get())
    c2 = avaliar_expressao(h.get())
    c3 = avaliar_expressao(i.get())

    #Retorna erro se não tiver tuod preenchido
    if None in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
        resultado_label.configure(text="Erro na expressão")
        return
    # Calcula a determinante
    det = a1 * (b2 * c3 - b3 * c2) - a2 * (b1 * c3 - b3 * c1) + a3 * (b1 * c2 - b2 * c1)

    # Se tiver variáveis, arredondar apenas a parte numérica
    if hasattr(det, "free_symbols") and det.free_symbols:#hasattr checa se um elemento tem um determinado atributo
        # Limita a parte numérica para até duas casas decimais
        det_limitado = limitar_casas(det, 2)
        # Mostra o resultado
        resultado_label.configure(text=str(det_limitado))
    else:
        # Se não tiver variável, arredonda livremente para 2 casas
        resultado_label.configure(text=f"{float(det):.2f}")

# Função para limpar todas as entradas e o resultado
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

#////////////////////////////////////////////////////////////////////////////////

                        # ***** ENTRADAS *****

a = ctk.CTkEntry(app, 
                 width=80, # largura
                 height=80, # Altura
                 placeholder_text="a", # Texto exemplo/dica
                 font=fonte_matriz, #fonte
                 text_color= cor_escura, # Cor da fonte
                 fg_color=cor_clara, # Fundo da entrada
                 border_color=cor_escura, # Borda
                 border_width=5) # Espessura da borda

# A mesma coisa acontece até o i

b = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="b", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

c = ctk.CTkEntry(app, 
                 width=80, 
                 height=80,
                 placeholder_text="c", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

d = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="d", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

e = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="e", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

f = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="f", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

g = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="g", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

h = ctk.CTkEntry(app, 
                 width=80, 
                 height=80,
                 placeholder_text="h", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)

i = ctk.CTkEntry(app, 
                 width=80,
                 height=80, 
                 placeholder_text="i", 
                 font=fonte_matriz,
                 text_color= cor_escura,
                 fg_color=cor_clara,
                 border_color=cor_escura,
                 border_width=5)
#/////////////////////////////////////////////////////////////////////////////////////

                    # ***** AJUSTE DE POSIÇÃO DA MATRIZ *****

# Posicionamento de X e Y para matriz
a.place(relx=0.274, rely=0.33, anchor="e")
b.place(relx=0.362, rely=0.33, anchor="e")
c.place(relx=0.447, rely=0.33, anchor="e")

d.place(relx=0.274, rely=0.5, anchor="e")
e.place(relx=0.362, rely=0.5, anchor="e")
f.place(relx=0.447, rely=0.5, anchor="e")

g.place(relx=0.274, rely=0.67, anchor="e")
h.place(relx=0.362, rely=0.67, anchor="e")
i.place(relx=0.447, rely=0.67, anchor="e")

#////////////////////////////////////////////////////////////////////////////////////////

                    # ***** BOTÕES E SUAS POSIÇÕES *****

# Botão que aciona a função de calcular a determinante
botao = ctk.CTkButton(app, # Referente à de quem o botão deriva
                      text="CALCULAR", # Texto do botão
                      command=calcular_determinante, # Função que o botão vai acionar
                      fg_color= cor_determinante, # Cor do botão
                      hover_color="#BC7E4C", # Cor ao clicar no botão
                      font=fonte_geral, # Fonte do texto
                      text_color= cor_escura, # Cor do texto
                      width=310, # Largura
                      height=105, # Altura
                      border_color=cor_escura, # Cor da borda
                      border_width=10) # Espessura da borda

# Posição do botão na tela
botao.place(relx=0.537, rely=0.70, anchor="w")
# Texto que mostra o resultado
# Abaixo é a mesma funcionalidade de ajuste de texto, fonte etc.
resultado_label = ctk.CTkLabel(conteudo_frame, 
                               text="", 
                               font=fonte_resultado,
                               text_color= cor_escura,
                               fg_color="transparent"
                               )
# Posição do resultado
resultado_label.place(relx=0.5, rely=0.5, anchor="center")

# Botão que aciona a função limpar_entradas e sua personalização

botao_limpar = ctk.CTkButton(bg_label,
                             text="❌",
                             command=limpar_entradas,
                             fg_color=reset_cor,
                             hover_color="#F25A3C",
                             font=fonte_geral,
                             text_color=cor_escura,
                             width=120,
                             height=110,
                             border_color=cor_escura,
                             border_width=10)

# Posição do botão limpar
botao_limpar.place(relx=0.782, rely=0.18, anchor="w")

#////////////////////////////////////////////////////////////////////////////////////
                    # ***** RODANDO A TELA *****

# Função que faz rodar a tela.
app.mainloop()
