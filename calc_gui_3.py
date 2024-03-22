import tkinter as tk
from tkinter import messagebox
#from calc_gui_2 import *

class CalculadoraTograficaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Tografica")
        
        # Caixa na parte superior
        self.caixa_superior = tk.Frame(self.master, bg="#225", padx=10, pady=10)
        self.caixa_superior.pack(side=tk.TOP, fill=tk.X)
        
        # Título da caixa
        self.titulo_fonte = ("Helvetica", 16)
        self.titulo = tk.Label(self.caixa_superior, text="Calculadora Tografica", fg="white", bg="#225", font=self.titulo_fonte)
        self.titulo.pack()
        
        # Botoes
        botoes = [
            "Coordenada",
            "Poligonal",
            "Objeto",
            "Cálculo",
            "Altura",
            "Gráfico"
        ]
        
        self.caixa_botoes = tk.Frame(self.master)
        self.caixa_botoes.pack(pady=10)
        
        for texto in botoes:
            botao_fonte = ("Helvetica", 12)
            botao = tk.Button(self.caixa_botoes, text=texto, width=15, font=botao_fonte, command=lambda t=texto: self.botao_clicado(t))
            botao.pack(side=tk.LEFT, padx=5)
        
        # Quadro de coordenadas
        self.quadro_coordenada = None
    
    def botao_clicado(self, texto_botao):
        if texto_botao == "Coordenada":
            self.abrir_coordenada()
        elif texto_botao == "Poligonal":
            self.abrir_poligonal()
        elif texto_botao == "Objeto":
            self.abrir_objeto()
        elif texto_botao == "Cálculo":
            self.abrir_calculo()
        elif texto_botao == "Altura":
            self.abrir_altura()
        elif texto_botao == "Gráfico":
            self.plotar_grafico()
    
    def abrir_coordenada(self):
        # Limpa a janela principal
        self.limpar_janela_principal()
        
        # Criar novo quadro
        self.quadro_coordenada = tk.Frame(self.master)
        self.quadro_coordenada.pack(pady=10)
        
        # Entradas de texto
        self.lbl_norte = tk.Label(self.quadro_coordenada, text="Norte:", font=("Helvetica", 12))
        self.lbl_norte.grid(row=0, column=0, padx=5, pady=5)
        self.entry_norte = tk.Entry(self.quadro_coordenada)
        self.entry_norte.grid(row=0, column=1, padx=5, pady=5)
        
        self.lbl_leste = tk.Label(self.quadro_coordenada, text="Leste:", font=("Helvetica", 12))
        self.lbl_leste.grid(row=1, column=0, padx=5, pady=5)
        self.entry_leste = tk.Entry(self.quadro_coordenada)
        self.entry_leste.grid(row=1, column=1, padx=5, pady=5)
        
        self.lbl_altura = tk.Label(self.quadro_coordenada, text="Altura:", font=("Helvetica", 12))
        self.lbl_altura.grid(row=2, column=0, padx=5, pady=5)
        self.entry_altura = tk.Entry(self.quadro_coordenada)
        self.entry_altura.grid(row=2, column=1, padx=5, pady=5)
        
        # Botão Salvar
        self.btn_salvar = tk.Button(self.quadro_coordenada, text="Salvar", font=("Helvetica", 12), command=self.salvar_coordenada)
        self.btn_salvar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        # Label para mensagem de salvo
        self.lbl_mensagem = tk.Label(self.quadro_coordenada, text="", fg="green", font=("Helvetica", 12))
        self.lbl_mensagem.grid(row=4, column=0, columnspan=2)
    
    def salvar_coordenada(self):
        norte_texto = self.entry_norte.get()
        leste_texto = self.entry_leste.get()
        altura_texto = self.entry_altura.get()
        
        # Check if any field is empty
        if norte_texto == "" or leste_texto == "" or altura_texto == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        
        # Validate input before conversion
        try:
            norte = float(norte_texto)
            leste = float(leste_texto)
            altura = float(altura_texto)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")
            return
        ponto = (norte, leste, altura)
        poligonais.append(ponto)
        messagebox.showinfo("Sucesso", "Coordenadas adicionadas com sucesso!")
            
    # Funções para abrir diferentes funcionalidades (substitua com suas próprias implementações)
    def abrir_poligonal(self):
        print("Abrir poligonal")
    
    def abrir_objeto(self):
        print("Abrir objeto")
    
    def abrir_calculo(self):
        print("Abrir cálculo")
    
    def abrir_altura(self):
        print("Abrir altura")
    
    def plotar_grafico(self):
        print("Plotar gráfico")
    
    def limpar_janela_principal(self):
        if self.quadro_coordenada:
            self.quadro_coordenada.destroy()

# Lista de poligonais
poligonais = []

# Criar a aplicação
root = tk.Tk()
app = CalculadoraTograficaApp(root)
root.mainloop()
