import pickletools
import tkinter as tk
import chessEngine




AMPLADA = ALTURA = 512
DIMENSIO = 8
TAMANY_TAULER = ALTURA // DIMENSIO
MAX_FPS = 60
IMATGES = {}

def cargarImatges(): #Funció carregar imatges
    pieza = ['pb','cb','ab','tb','qb','kb','pn','cn','an','tn','qn','kn']

    for pieza in piezas:
        IMATGES['pb'] = p.image.load("./ChessIcons/" + pieza + ".png"), (TAMANY_TAULER,TAMANY_TAULER)
        #Podem accedir a les imatges cridant al diccionari 'IMATGES['pb']


"""Driver principal del codi"""
def main():

    pantalla = tk.display.set_mode((AMPLADA, ALTURA))
    clock = tk.time.Rellotge()
    pantalla.fill(p.Color("white"))
    gs = chessEngine.GameState()
    cargarImatges()
    running = True
    while running:
        for e in tk.event.get():
            if e.type == p.QUIT:
                running = False

            clock.tick(MAX_FPS)
            tk.display.flip()


"""Responsable dels grafics de la partida"""
def dibuixarEstatJoc(pantalla, gs):
    dibuixarTauler(pantalla) #Dibuixa els quadrats a la pantalla
    dibuixarPeces(pantalla, gs.tauler) #Dibuixa les peces

"""Dibuixa el tauler de joc, el quadrat de dalt a l'esquerra sempre serà blanc"""
def dibuixarTauler(pantalla):
    colors = [tk.Color("blanc"), tk.Color("negre")]
    for r in rango(DIMENSIO):
        for c in rango(DIMENSIO):
            [((r+c)%2)]


def dibuixarPeces(pantalla, tauler):
    pass

"""if __name__ == "__main__":
    main()"""


class App():
    #Funcions
    def __init__(self, L_QUADRADO): #Cada vegada que instanciem una classe
        self.gs = chessEngine.GameState() #Accedim a la classe de l'arxiu chessEngine
        self.L_QUADRADO = L_QUADRADO

        self.ventana = tk.Tk()
        self.ventana.title("Ajedrez Python") #Titol de la finestra
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

#No funciona
    """"
    def cargarImagenes(self):
        tablero = ["pb","cb","ab","tb","qb","kb","pn","cn","an","tn","qn","kn"] #Pngs de les peçes de l'ajedrez dins la llista
        for pieza in tablero:
            self.imagenes[pieza] = tk.PhotoImage(file="./ChessIcons/" + pieza + ".png").zoom(self.L_QUADRADO).subsample()

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.tablero):
            for indice_j in enumerate(i):   #I guarda cadascuna de les llistes de la classe del tauler
                if j != "--":
                    self.interfaz.create_image(indice_j * self.L_QUADRADO, indice_i * self.L_QUADRADO, image=self.imagenes[j], anchor="nw") #Aqui carregarem les imatges calculant les posicions del tauler on s'imprimira l'imatge especifica de les llistes de chessEngine/GameState
    """""

#Metodos
MotorDeAjedrez = App(100)
MotorDeAjedrez.dibujarTablero() #Metodo per a cridar la funcio dibujarTablero
"MotorDeAjedrez.cargarImagenes() #Metodo per cridar la funcio cargarImagenes"
"MotorDeAjedrez.mostrarPiezas() #Metodo per a cridar la funcio mostrarPiezas"
MotorDeAjedrez()
