import tkinter as tk
import chessEngine

class App():
    #Funcions
    def __init__(self, L_QUADRADO): #Cada vegada que instanciem una classe
        self.gs = chessEngine.GameState() #Accedim a la classe de l'arxiu chessEngine
        self.L_QUADRADO = L_QUADRADO

        self.ventana = tk.Tk()
        self.ventana.title("Ajedrez Josafinha") #Titol de la finestra
        self.ventana.iconbitmap("ChessIcons/chessIco.ico") #Icono superior esquerre de la finestra
        self.ventana.geometry(f"{str(L_QUADRADO * 8)}x{str(L_QUADRADO * 8)}") #Geometria de la finestra
        self.ventana.resizable(0,0) #Tamany del tauler predefinit (no es pot redimensionar)

        self.Interfaz = tk.Canvas(self.ventana) #Per a crear i editar la interfaz fem servir Canvas i ho vincularem a la ventana de la nostra APP
        self.Interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def dibujarTablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.Interfaz.create_rectangle(i*self.L_QUADRADO, j*self.L_QUADRADO,(i+1)*self.L_QUADRADO, (j+1)*self.L_QUADRADO, fill="#dfc07f") #Crearem el tauler de les blanques mitjançant les coordenades i, j
                else:
                    self.Interfaz.create_rectangle(i * self.L_QUADRADO, j * self.L_QUADRADO, (i + 1) * self.L_QUADRADO, (j + 1) * self.L_QUADRADO, fill="#7a4f37") #Crearem el tauler de les negres mitjançant les coordenades i+1, j+1

    def cargarImagenes(self):
        tablero = ["pb","cb","ab","tb","qb","kb","pn","cn","an","tn","qn","kn"] #Pngs de les peçes de l'ajedrez dins la llista
        for pieza in tablero:
            self.imagenes[pieza] = tk.PhotoImage(file="./ChessIcons/" + pieza + ".png").zoom(self.L_QUADRADO).subsample()

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.tablero):
            for indice_j in enumerate(i):   #I guarda cadascuna de les llistes de la classe del tauler
                if j != "--":
                    self.interfaz.create_image(indice_j * self.L_QUADRADO, indice_i * self.L_QUADRADO, image=self.imagenes[j], anchor="nw") #Aqui carregarem les imatges calculant les posicions del tauler on s'imprimira l'imatge especifica de les llistes de chessEngine/GameState



#Metodos
MotorDeAjedrez = App(100)
MotorDeAjedrez.dibujarTablero() #Metodo per a cridar la funcio dibujarTablero
MotorDeAjedrez.cargarImagenes() #Metodo per cridar la funcio cargarImagenes
MotorDeAjedrez.mostrarPiezas() #Metodo per a cridar la funcio mostrarPiezas
MotorDeAjedrez()