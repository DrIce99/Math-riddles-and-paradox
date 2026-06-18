import random
import tkinter as tk
from tkinter import ttk

class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizzatore Paradosso Compleanno")
        self.root.geometry("1400x1000")
        
        # Dati per la conversione Giorno dell'anno -> Mese/Giorno
        self.months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.month_names = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", 
                            "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
        
        # Configurazione Grafica Calendario
        self.cell_size = 14  # Dimensione del quadratino giorno
        self.padding = 5     # Spazio tra i mesi
        self.cols_per_row = 3 # Mesi per riga (3x4 = 12 mesi)
        
        # UI Setup
        frame_controls = ttk.Frame(root)
        frame_controls.pack(pady=10, fill="x")
        
        ttk.Label(frame_controls, text="Numero di persone:").pack(side="left", padx=10)
        self.slider = ttk.Scale(frame_controls, from_=2, to=100, orient="horizontal", command=self.on_slider_change, length=300)
        self.slider.set(23)
        self.slider.pack(side="left", padx=10)
        
        self.label_val = ttk.Label(frame_controls, text="23")
        self.label_val.pack(side="left")

        self.label_res = ttk.Label(root, text="Probabilità: --", font=('Arial', 14, 'bold'))
        self.label_res.pack(pady=5)
        
        # Legenda colori
        legend_frame = ttk.Frame(root)
        legend_frame.pack(pady=5)
        self.create_legend_item(legend_frame, "Nessuno", "#f0f0f0", "black")
        self.create_legend_item(legend_frame, "1 Persona", "#a8d8ea", "black")
        self.create_legend_item(legend_frame, "Collisione (>=2)", "#ff9a9e", "black")

        # Canvas per il disegno
        canvas_width = (self.cell_size * 7 + 30) * 4 # 7 giorni largh + spazio nome, * 3 colonne
        canvas_height = (self.cell_size * 6 + 30) * 6 # 6 righe giorni + spazio nome, * 4 righe
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack(pady=10, padx=10)

        # Calcolo iniziale
        self.update_simulation()

    def create_legend_item(self, parent, text, bg_color, fg_color):
        f = ttk.Frame(parent)
        f.pack(side="left", padx=10)
        lbl = tk.Label(f, text=text, bg=bg_color, fg=fg_color, relief="solid", borderwidth=1, width=12)
        lbl.pack()

    def get_birthdays(self, n):
        return [random.randint(1, 365) for _ in range(int(n))]

    def day_to_month_day(self, day_of_year):
        # Converte un numero da 1 a 365 in (Mese, Giorno)
        current_day = day_of_year
        for i, days in enumerate(self.months_days):
            if current_day <= days:
                return i, current_day - 1 # -1 per indice 0-based
            current_day -= days
        return 11, 30 # Fallback (31 Dic)

    def on_slider_change(self, val):
        self.label_val.config(text=f"{int(float(val))}")
        self.update_simulation()

    def update_simulation(self, event=None):
        n = int(self.slider.get())
        trials = 2000
        matches = 0
        
        # Esegue la simulazione Monte Carlo per la probabilità
        for _ in range(trials):
            birthdays = self.get_birthdays(n)
            if len(set(birthdays)) < len(birthdays):
                matches += 1
        
        prob = matches / trials
        self.label_res.config(text=f"Con {n} persone: {prob:.2%}")
        
        # Genera un set di compleanni per la visualizzazione
        current_birthdays = self.get_birthdays(n)
        self.draw_calendar(current_birthdays)

    def draw_calendar(self, birthdays):
        self.canvas.delete("all")
        
        # Conta quante persone hanno il compleanno in ogni giorno (1-365)
        counts = [0] * 366
        for b in birthdays:
            counts[b] += 1
            
        # Disegna i 12 mesi
        for m_idx in range(12):
            # Calcola posizione della griglia del mese (3 colonne, 4 righe)
            col = m_idx % self.cols_per_row
            row = m_idx // self.cols_per_row
            
            # Offset base per posizionare il mese
            start_x = col * 160 + 20
            start_y = row * 130 + 20
            
            # Titolo del mese
            self.canvas.create_text(start_x + 75, start_y, text=self.month_names[m_idx], font=("Arial", 10, "bold"))
            
            # Disegna i giorni (griglia 7x6 max)
            days_in_month = self.months_days[m_idx]
            
            for d in range(1, days_in_month + 1):
                # Calcola posizione all'interno del mese
                # Griglia semplice: riempie le celle una dopo l'altra
                grid_idx = d - 1
                dx = (grid_idx % 7) * self.cell_size + start_x
                dy = (grid_idx // 7) * self.cell_size + start_y + 15 # +15 per spazio sotto titolo
                
                # Determina colore
                # Per trovare l'indice globale (1-365), sommiamo i giorni dei mesi precedenti
                global_day_idx = sum(self.months_days[:m_idx]) + d
                count = counts[global_day_idx]
                
                color = "#ffffff" # Default bianco
                outline = "#e0e0e0"
                
                if count == 1:
                    color = "#a8d8ea" # Azzurro pastello (1 persona)
                elif count >= 2:
                    color = "#ff9a9e" # Rosso pastello (collisione!)
                
                # Disegna la casella
                self.canvas.create_rectangle(dx, dy, dx + self.cell_size - 1, dy + self.cell_size - 1, 
                                             fill=color, outline=outline)

# Avvio applicazione
root = tk.Tk()
app = BirthdayApp(root)
root.mainloop()