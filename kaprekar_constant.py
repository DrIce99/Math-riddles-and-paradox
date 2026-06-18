import tkinter as tk
import math
import random

class KaprekarVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaprekar Constant (6174) - Infinite Graph Visualizer")
        self.root.geometry("1100x800")
        
        # --- Stato di Pan & Zoom Window Principale ---
        self.scale = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.pan_start_x = 0
        self.pan_start_y = 0
        
        # --- Pannello di Controllo superiore ---
        self.control_frame = tk.Frame(root, bg="#111827", pady=10)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.label = tk.Label(self.control_frame, text="Inserisci numero (4 cifre):", fg="white", bg="#111827", font=("Helvetica", 12, "bold"))
        self.label.pack(side=tk.LEFT, padx=10)
        
        self.entry = tk.Entry(self.control_frame, font=("Helvetica", 12), width=8, bg="#374151", fg="white", insertbackground="white")
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.insert(0, "1234") # Default
        
        # --- NUOVO PULSANTE: GENERA CASUALE ---
        self.btn_rand = tk.Button(self.control_frame, text="Casuale", font=("Helvetica", 11, "bold"), bg="#6366f1", fg="white", command=self.generate_random)
        self.btn_rand.pack(side=tk.LEFT, padx=5)
        # ---------------------------------------
        
        self.btn = tk.Button(self.control_frame, text="Avvia Routine", font=("Helvetica", 11, "bold"), bg="#3b82f6", fg="white", command=self.start_sequence)
        self.btn.pack(side=tk.LEFT, padx=10)
        
        # Pulsante per le statistiche
        self.stats_btn = tk.Button(self.control_frame, text="Analisi Range", font=("Helvetica", 11, "bold"), bg="#10b981", fg="white", command=self.open_stats_window)
        self.stats_btn.pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(self.control_frame, text="[Trascina per spostare • Rotellina per Zoom]", fg="#9ca3af", bg="#111827", font=("Helvetica", 10, "italic"))
        self.info_label.pack(side=tk.RIGHT, padx=15)
        
        # --- Canvas per il grafico ---
        self.canvas = tk.Canvas(root, width=1000, height=700, bg="#1e293b", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # --- Bindings Mouse per Pan & Zoom ---
        self.canvas.bind("<ButtonPress-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan)
        self.canvas.bind("<MouseWheel>", self.zoom)       
        self.canvas.bind("<Button-4>", self.zoom)         
        self.canvas.bind("<Button-5>", self.zoom)         
        
        # --- Strutture Dati del Grafo ---
        self.nodes = {}  
        self.edges = set()  
        
        # Inizializziamo con il nodo "fisso" 6174 al centro
        self.add_node_immediate(6174, 500, 350)
        
        self.update_physics()
        
    def add_node_immediate(self, num, x, y):
        if num not in self.nodes:
            self.nodes[num] = {'x': x, 'y': y, 'vx': 0, 'vy': 0, 'highlight': 0}

    def get_kaprekar_next(self, n):
        """Calcola il prossimo numero secondo la routine di Kaprekar"""
        s = str(n).zfill(4)
        if len(set(s)) < 2: 
            return None # Cifre uguali (es. 2222), routine non prosegue
            
        asc = int("".join(sorted(s)))
        desc = int("".join(sorted(s, reverse=True)))
        return desc - asc

    # --- NUOVA FUNZIONE: Genera Random ---
    def generate_random(self):
        # Genera un numero tra 1000 e 9998 (evitiamo 9999 che diventa 0 immediatamente per pulizia visiva)
        rand_num = random.randint(1000, 9998)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(rand_num))
    # ------------------------------------

    # --- Gestione PAN & ZOOM ---
    def start_pan(self, event):
        self.pan_start_x = event.x
        self.pan_start_y = event.y

    def pan(self, event):
        dx = event.x - self.pan_start_x
        dy = event.y - self.pan_start_y
        self.offset_x += dx
        self.offset_y += dy
        self.pan_start_x = event.x
        self.pan_start_y = event.y

    def zoom(self, event):
        if event.num == 4 or event.delta > 0:
            zoom_factor = 1.1
        elif event.num == 5 or event.delta < 0:
            zoom_factor = 0.9
        else:
            zoom_factor = 1.0
            
        old_scale = self.scale
        self.scale *= zoom_factor
        self.scale = max(0.1, min(10.0, self.scale))
        
        mx, my = event.x, event.y
        self.offset_x = mx - (mx - self.offset_x) * (self.scale / old_scale)
        self.offset_y = my - (my - self.offset_y) * (self.scale / old_scale)

    # --- Logica Sequenza di Kaprekar ---
    def start_sequence(self):
        try:
            val = int(self.entry.get())
            if val < 1 or val > 9999: 
                print("Inserisci un numero tra 1 e 9999")
                return
        except ValueError:
            return 
        
        # Calcola il percorso completo
        path = []
        curr = val
        
        # Se partiamo da un numero già nel grafo, non fare nulla o visualizzalo
        # Qui assumiamo che l'utente voglia vedere il percorso
        
        while True:
            path.append(curr)
            if curr == 6174:
                break # Arrivati alla meta
            
            # Se il prossimo numero è già nel grafo, ci fermiamo lì per l'animazione
            # (il resto del percorso è già disegnato)
            next_val = self.get_kaprekar_next(curr)
            
            if next_val is None:
                # Caso repelling (es. 2222), non prosegue
                print(f"Routine bloccata per {curr} (cifre uguali)")
                break
            
            if next_val in self.nodes:
                path.append(next_val)
                break
            
            curr = next_val

        # L'animazione procede al contrario: dall'ultimo nodo (che esiste) 
        # costruisce a ritroso verso il nuovo input
        path.reverse()
        self.animate_next_step(path)

    def animate_next_step(self, path_seq):
        if len(path_seq) < 2:
            return
            
        target = path_seq[0]  # Il nodo verso cui puntiamo (esiste già)
        new_node = path_seq[1] # Il nodo da creare
        
        if new_node not in self.nodes:
            # Calcola posizione: parte dal target e va all'indietro o in una direzione casuale
            # Per creare un effetto "albero", cerchiamo di disperdere i nodi
            
            # Cerca un "genitore" logico per l'angolazione
            parent_angle = 0
            if len(path_seq) > 2:
                parent_node = path_seq[2]
                if parent_node in self.nodes:
                    dx = self.nodes[parent_node]['x'] - self.nodes[target]['x']
                    dy = self.nodes[parent_node]['y'] - self.nodes[target]['y']
                    parent_angle = math.atan2(dy, dx)
            
            # Aggiungi un offset angolare casuale ma controllato per evitare sovrapposizioni
            offset = random.uniform(-0.5, 0.5)
            final_angle = parent_angle + offset + math.pi # Punto all'opposto del genitore
            
            # Se è il primo passo (target è 6174), usa angolo casuale
            if target == 6174:
                final_angle = random.uniform(0, 2 * math.pi)
                
            distance = 60
            base_x = self.nodes[target]['x'] + math.cos(final_angle) * distance
            base_y = self.nodes[target]['y'] + math.sin(final_angle) * distance
                
            self.nodes[new_node] = {'x': base_x, 'y': base_y, 'vx': 0, 'vy': 0, 'highlight': 25}
        else:
            # Il nodo esiste già, lo illuminiamo
            self.nodes[new_node]['highlight'] = 25  
            
        self.edges.add((new_node, target))
        self.root.after(150, lambda: self.animate_next_step(path_seq[1:]))

    def update_physics(self):
        keys = list(self.nodes.keys())
        
        # 1. Repulsione (Nodi si respingono a vicenda)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                u, v = keys[i], keys[j]
                dx = self.nodes[u]['x'] - self.nodes[v]['x']
                dy = self.nodes[u]['y'] - self.nodes[v]['y']
                dist = math.hypot(dx, dy) + 0.1
                
                repulsion_radius = 120
                if dist < repulsion_radius:  
                    force = (repulsion_radius - dist) * 0.05
                    fx = (dx / dist) * force
                    fy = (dy / dist) * force
                    
                    # 6174 è fisso al centro (o molto pesante)
                    if u != 6174:
                        self.nodes[u]['vx'] += fx
                        self.nodes[u]['vy'] += fy
                    if v != 6174:
                        self.nodes[v]['vx'] -= fx
                        self.nodes[v]['vy'] -= fy

        # 2. Attrazione (Archi tirano i nodi vicini)
        for u, v in list(self.edges):
            if u not in self.nodes or v not in self.nodes:
                continue
            dx = self.nodes[v]['x'] - self.nodes[u]['x']
            dy = self.nodes[v]['y'] - self.nodes[u]['y']
            dist = math.hypot(dx, dy) + 0.1
            desired_dist = 50  
            if dist > desired_dist:
                force = (dist - desired_dist) * 0.03
                fx = (dx / dist) * force
                fy = (dy / dist) * force
                if u != 6174:
                    self.nodes[u]['vx'] += fx
                    self.nodes[u]['vy'] += fy
                if v != 6174:
                    self.nodes[v]['vx'] -= fx
                    self.nodes[v]['vy'] -= fy

        # 3. Aggiornamento posizione e smorzamento
        for u in self.nodes:
            self.nodes[u]['x'] += self.nodes[u]['vx']
            self.nodes[u]['y'] += self.nodes[u]['vy']
            self.nodes[u]['vx'] *= 0.70
            self.nodes[u]['vy'] *= 0.70
            
            # Decadimento highlight
            if self.nodes[u]['highlight'] > 0:
                self.nodes[u]['highlight'] -= 1

        self.draw_graph()
        self.root.after(30, self.update_physics)

    def draw_graph(self):
        self.canvas.delete("all")
        
        # Sfondo testo
        bg_txt_x = 500 * self.scale + self.offset_x
        bg_txt_y = 100 * self.scale + self.offset_y
        font_size_bg = max(10, int(40 * self.scale))
        if 5 < font_size_bg < 100:
            self.canvas.create_text(bg_txt_x, bg_txt_y, text="6174", fill="#1e293b", font=("Helvetica", font_size_bg, "bold"))
        
        # Disegna Archi
        for u, v in self.edges:
            if u not in self.nodes or v not in self.nodes:
                continue
            x1 = self.nodes[u]['x'] * self.scale + self.offset_x
            y1 = self.nodes[u]['y'] * self.scale + self.offset_y
            x2 = self.nodes[v]['x'] * self.scale + self.offset_x
            y2 = self.nodes[v]['y'] * self.scale + self.offset_y
            
            dist = math.hypot(x2 - x1, y2 - y1) + 0.1
            r = 16 * self.scale  
            
            # Calcola punti di bordo per le frecce
            if dist > r * 2:
                x1_edge = x1 + (x2 - x1) * (r / dist)
                x2_edge = x2 - (x2 - x1) * (r / dist)
                y1_edge = y1 + (y2 - y1) * (r / dist)
                y2_edge = y2 - (y2 - y1) * (r / dist)
                
                w = max(1, int(2 * self.scale))
                # Colore freccia diverso per 6174
                arrow_col = "#f87171" if v == 6174 else "#38bdf8"
                
                self.canvas.create_line(x1_edge, y1_edge, x2_edge, y2_edge, fill=arrow_col, arrow=tk.LAST, width=w)
        
        # Disegna Nodi
        for num, data in self.nodes.items():
            x = data['x'] * self.scale + self.offset_x
            y = data['y'] * self.scale + self.offset_y
            r = 16 * self.scale
            
            # Ottimizzazione: non disegnare fuori schermo
            if x < -r or x > 1000 + r or y < -r or y > 700 + r:
                continue
                
            if data['highlight'] > 0:
                bg_color = "#facc15"    # Giallo se evidenziato
                text_color = "#000000"
                outline_color = "#ffffff"
                r = r * 1.2 # Leggermente più grande
            elif num == 6174:
                bg_color = "#ef4444"    # Rosso per 6174
                text_color = "#ffffff"
                outline_color = "#fca5a5"
            else:
                # Colore basato sulla parità (come Collatz) o gradiente
                bg_color = "#3b82f6" if num % 2 == 0 else "#818cf8"
                text_color = "#0f172a"
                outline_color = "#93c5fd"
            
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=bg_color, outline=outline_color, width=max(1, 1.5 * self.scale))
            
            base_f_size = 9 if num > 999 else (10 if num > 99 else 11)
            font_size = int(base_f_size * self.scale)
            if font_size > 4:
                self.canvas.create_text(x, y, text=str(num), fill=text_color, font=("Helvetica", font_size, "bold"))

    # ==========================================
    # FINESTRA STATISTICHE (ADATTATA KAPREKAR)
    # ==========================================
    def open_stats_window(self):
        stats_win = tk.Toplevel(self.root)
        stats_win.title("Kaprekar Analytics")
        stats_win.geometry("1100x550")
        stats_win.configure(bg="#111827")
        
        top_bar = tk.Frame(stats_win, bg="#1f2937", pady=8)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        
        range_label = tk.Label(top_bar, text="Analisi range da:", fg="white", bg="#1f2937", font=("Helvetica", 11, "bold"))
        range_label.pack(side=tk.LEFT, padx=10)
        
        range_entry = tk.Entry(top_bar, font=("Helvetica", 11), width=5, bg="#374151", fg="white", insertbackground="white")
        range_entry.pack(side=tk.LEFT, padx=5)
        range_entry.insert(0, "1000")
        
        to_label = tk.Label(top_bar, text="a", fg="white", bg="#1f2937", font=("Helvetica", 11))
        to_label.pack(side=tk.LEFT, padx=5)
        
        range_entry_end = tk.Entry(top_bar, font=("Helvetica", 11), width=5, bg="#374151", fg="white", insertbackground="white")
        range_entry_end.pack(side=tk.LEFT, padx=5)
        range_entry_end.insert(0, "1999")
        
        graphs_frame = tk.Frame(stats_win, bg="#111827")
        graphs_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas_steps = tk.Canvas(graphs_frame, width=520, height=450, bg="#1e293b", highlightthickness=0)
        canvas_steps.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        canvas_peaks = tk.Canvas(graphs_frame, width=520, height=450, bg="#1e293b", highlightthickness=0)
        canvas_peaks.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        def run_analysis():
            try:
                start_val = int(range_entry.get())
                end_val = int(range_entry_end.get())
                if start_val < 1 or end_val < start_val: return
            except ValueError:
                return
            
            steps_data = []
            peaks_data = []
            
            for i in range(start_val, end_val + 1):
                curr = i
                steps = 0
                max_val = i
                visited = set()
                
                while True:
                    if curr in visited: # Loop infinito (teoricamente impossibile per 4 cifre non repelling)
                        break
                    visited.add(curr)
                    if curr == 6174:
                        break
                    
                    next_curr = self.get_kaprekar_next(curr)
                    if next_curr is None: # Repelling
                        break
                        
                    if next_curr > max_val:
                        max_val = next_curr
                        
                    curr = next_curr
                    steps += 1
                
                steps_data.append((i, steps))
                peaks_data.append((i, max_val))
            
            self.draw_custom_plot(canvas_steps, steps_data, "Passaggi fino a 6174", "Numero di partenza", "Passi", "#f59e0b")
            self.draw_custom_plot(canvas_peaks, peaks_data, "Picco Massimo Raggiunto", "Numero di partenza", "Valore Massimo", "#a855f7")

        calc_btn = tk.Button(top_bar, text="Calcola Grafici", font=("Helvetica", 10, "bold"), bg="#10b981", fg="white", command=run_analysis)
        calc_btn.pack(side=tk.LEFT, padx=15)
        
        stats_win.after(100, run_analysis)

    def draw_custom_plot(self, canvas, data, title, x_label, y_label, dot_color):
        canvas.delete("all")
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        if w < 100: w = 520
        if h < 100: h = 450
        
        pad_l, pad_r, pad_t, pad_b = 60, 25, 45, 45
        plot_w = w - pad_l - pad_r
        plot_h = h - pad_t - pad_b
        
        if not data: return

        max_x = max([d[0] for d in data])
        max_y = max([d[1] for d in data])
        if max_y == 0: max_y = 1
        
        # Assi
        canvas.create_line(pad_l, h - pad_b, w - pad_r, h - pad_b, fill="#4b5563", width=2)
        canvas.create_line(pad_l, pad_t, pad_l, h - pad_b, fill="#4b5563", width=2)
        
        canvas.create_text(w/2, 20, text=title, fill="white", font=("Helvetica", 12, "bold"))
        canvas.create_text(w/2, h - 15, text=x_label, fill="#9ca3af", font=("Helvetica", 10))
        canvas.create_text(18, h/2, text=y_label, fill="#9ca3af", font=("Helvetica", 10), angle=90)
        
        # Ticks Y
        canvas.create_text(pad_l - 25, pad_t, text=str(max_y), fill="#9ca3af", font=("Helvetica", 9))
        canvas.create_text(pad_l - 25, h - pad_b, text="0", fill="#9ca3af", font=("Helvetica", 9))
        
        # Ticks X
        canvas.create_text(w - pad_r, h - pad_b + 15, text=str(max_x), fill="#9ca3af", font=("Helvetica", 9))
        canvas.create_text(pad_l, h - pad_b + 15, text=str(min([d[0] for d in data])), fill="#9ca3af", font=("Helvetica", 9))

        # Punti
        for x, y in data:
            cx = pad_l + ((x - min([d[0] for d in data])) / (max_x - min([d[0] for d in data]))) * plot_w
            cy = h - pad_b - (y / max_y) * plot_h
            
            canvas.create_rectangle(cx - 1.5, cy - 1.5, cx + 1.5, cy + 1.5, fill=dot_color, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = KaprekarVisualizer(root)
    root.mainloop()