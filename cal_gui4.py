import tkinter as tk
from tkinter import messagebox
import os

class CalculadoraTograficaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Tografica")
        
        self.caixa_superior = tk.Frame(self.master, bg="#225", padx=10, pady=10)
        self.caixa_superior.pack(side=tk.TOP, fill=tk.X)
        
        self.titulo_fonte = ("Helvetica", 16)
        self.titulo = tk.Label(self.caixa_superior, text="Calculadora Tografica", fg="white", bg="#225", font=self.titulo_fonte)
        self.titulo.pack()
        
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
        
        self.quadro_coordenada = None
        self.figura = None
        self.canvas = None
    
    def botao_clicado(self, texto_botao):
        if texto_botao == "Coordenada":
            self.abrir_coordenada()
        elif texto_botao == "Gráfico":
            self.plotar_grafico()
        # Implementações para os outros botões
    
    def abrir_coordenada(self):
        self.limpar_janela_principal()
        self.quadro_coordenada = tk.Frame(self.master)
        self.quadro_coordenada.pack(pady=10)
        # Adicione aqui a lógica para abrir a janela de coordenadas
    
    def plotar_grafico(self):
        if self.figura is None:
            self.figura = Figure(figsize=(5, 4), dpi=100)
            self.canvas = FigureCanvasTkAgg(self.figura, self.master)
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        ax = self.figura.add_subplot(111)
        ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        self.canvas.draw()
    
    def limpar_janela_principal(self):
        if self.quadro_coordenada:
            self.quadro_coordenada.destroy()
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
            self.figura = None

# Lista de poligonais
poligonais = []

# Criar a aplicação
root = tk.Tk()
app = CalculadoraTograficaApp(root)
root.mainloop()
