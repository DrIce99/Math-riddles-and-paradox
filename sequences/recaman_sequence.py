import tkinter as tk
import colorsys

class RecamanVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("La Sequenza di Recamán - Numberphile Style")
        
        # Finestra a tutto schermo o quasi
        self.width = 1200
        self.height = 700
        
        # Creazione del Canvas (Sfondo scuro per far risaltare i colori)
        self.canvas = tk.Canvas(root, bg="#111111", width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Stato della Sequenza di Recamán
        self.sequence = [0]
        self.used_numbers = {0}
        self.current_step = 0
        self.max_steps = 400  # Numero massimo di iterazioni per l'animazione
        
        # Variabili per la trasformazione geometrica (Pan & Zoom)
        self.scale = 4.0        # Pixel per singola unità matematica
        self.offset_x = 50.0    # Spostamento orizzontale iniziale
        self.offset_y = self.height // 2  # L'asse centrale (Y)
        
        # Memoria per il trascinamento del mouse (Pan)
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        
        # Bind degli eventi del mouse per Pan & Zoom
        self.canvas.bind("<ButtonPress-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan)
        self.canvas.bind("<MouseWheel>", self.zoom)       # Windows / macOS
        self.canvas.bind("<Button-4>", self.zoom)         # Linux (Scroll Up)
        self.canvas.bind("<Button-5>", self.zoom)         # Linux (Scroll Down)
        
        # UI di istruzioni testuali
        self.info_text = self.canvas.create_text(
            20, 20, anchor="nw", fill="white", font=("Courier", 12),
            text="Istruzioni:\n- Click sinistro + Trascina per spostarti (Pan)\n- Rotella del mouse per ingrandire (Zoom)"
        )
        
        # Avvio dell'animazione a ciclo continuo
        self.animate()

    def step_recaman(self):
        """Calcola il prossimo elemento della sequenza di Recamán."""
        self.current_step += 1
        last_val = self.sequence[-1]
        
        # Regola di Recamán: prova a sottrarre, altrimenti somma
        backward = last_val - self.current_step
        if backward > 0 and backward not in self.used_numbers:
            next_val = backward
        else:
            next_val = last_val + self.current_step
            
        self.sequence.append(next_val)
        self.used_numbers.add(next_val)

    def redraw(self):
        """Svuota il canvas e ridisegna tutto in base a zoom e offset correnti."""
        # Rimuove tutti gli elementi tranne il testo di aiuto
        self.canvas.delete("graph_element")
        
        # 1. Disegna l'asse centrale (linea di riferimento)
        self.canvas.create_line(
            0, self.offset_y, self.width * 10, self.offset_y, 
            fill="#333333", width=1, tags="graph_element"
        )
        
        # 2. Disegna gli archi della sequenza
        for i in range(1, len(self.sequence)):
            p1 = self.sequence[i-1]
            p2 = self.sequence[i]
            
            # Conversione in coordinate dello schermo (World to Screen)
            x1 = p1 * self.scale + self.offset_x
            x2 = p2 * self.scale + self.offset_x
            
            # Calcolo del centro e del raggio dell'arco
            center_x = (x1 + x2) / 2
            radius = abs(x2 - x1) / 2
            
            # Definizione del rettangolo di contenimento (Bounding Box) per l'arco
            bbox_x1 = center_x - radius
            bbox_y1 = self.offset_y - radius
            bbox_x2 = center_x + radius
            bbox_y2 = self.offset_y + radius
            
            # Alternanza degli archi: i passi dispari vanno sopra, i pari vanno sotto
            if i % 2 == 1:
                start_angle = 0
                extent_angle = 180
            else:
                start_angle = 180
                extent_angle = 180
            
            # Generazione di un colore arcobaleno dinamico basato sull'indice del passo
            hue = (i * 0.005) % 1.0
            rgb = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
            hex_color = f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"
            
            # Spessore della linea dinamico (diventa leggermente più sottile man mano che cresce)
            line_width = max(1, min(3, int(10 / (radius + 1))))
            
            # Disegno dell'arco sul Canvas
            self.canvas.create_arc(
                bbox_x1, bbox_y1, bbox_x2, bbox_y2,
                start=start_angle, extent=extent_angle,
                style="arc", outline=hex_color, width=line_width, tags="graph_element"
            )
            
        # Metti il testo sempre in primo piano
        self.canvas.tag_raise(self.info_text)

    def animate(self):
        """Gestisce il loop dell'animazione passo dopo passo."""
        if self.current_step < self.max_steps:
            self.step_recaman()
            self.redraw()
            # Frequenza di aggiornamento in millisecondi (minore = più veloce)
            self.root.after(80, self.animate)

    # --- GESTIONE PAN (Spostamento della visuale) ---
    def start_pan(self, event):
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y

    def pan(self, event):
        delta_x = event.x - self.last_mouse_x
        delta_y = event.y - self.last_mouse_y
        
        self.offset_x += delta_x
        self.offset_y += delta_y
        
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y
        self.redraw()

    # --- GESTIONE ZOOM (Ingrandimento centrato sul mouse) ---
    def zoom(self, event):
        # Riconoscimento della direzione dello scroll (multi-piattaforma)
        if event.num == 4 or event.delta > 0:
            zoom_factor = 1.15
        elif event.num == 5 or event.delta < 0:
            zoom_factor = 0.85
        else:
            zoom_factor = 1.0
            
        mouse_x = event.x
        mouse_y = event.y
        
        # Modifica dei parametri di offset per fare in modo che lo zoom punti al cursore
        self.offset_x = mouse_x - (mouse_x - self.offset_x) * zoom_factor
        self.offset_y = mouse_y - (mouse_y - self.offset_y) * zoom_factor
        self.scale *= zoom_factor
        
        self.redraw()

# Inizializzazione dell'applicazione
if __name__ == "__main__":
    root = tk.Tk()
    app = RecamanVisualizer(root)
    root.mainloop()