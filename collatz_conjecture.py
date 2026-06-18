import tkinter as tk
import math
import random

class CollatzInfiniteVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Collatz Conjecture - Infinite Planar Graph & Analytics")
        
        # --- Stato di Pan & Zoom Window Principale ---
        self.scale = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.pan_start_x = 0
        self.pan_start_y = 0
        
        # --- Pannello di Controllo superiore ---
        self.control_frame = tk.Frame(root, bg="#111827", pady=10)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.label = tk.Label(self.control_frame, text="Inserisci x:", fg="white", bg="#111827", font=("Helvetica", 12, "bold"))
        self.label.pack(side=tk.LEFT, padx=10)
        
        self.entry = tk.Entry(self.control_frame, font=("Helvetica", 12), width=10, bg="#374151", fg="white", insertbackground="white")
        self.entry.pack(side=tk.LEFT, padx=5)
        
        self.btn = tk.Button(self.control_frame, text="Next Number (x)", font=("Helvetica", 11, "bold"), bg="#3b82f6", fg="white", command=self.start_sequence)
        self.btn.pack(side=tk.LEFT, padx=10)
        
        # NUOVO: Pulsante per aprire la finestra delle statistiche globali
        self.stats_btn = tk.Button(self.control_frame, text="Analisi Range (Grafici)", font=("Helvetica", 11, "bold"), bg="#10b981", fg="white", command=self.open_stats_window)
        self.stats_btn.pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(self.control_frame, text="[Trascina il mouse per muoverti • Usa la rotellina per lo Zoom]", fg="#9ca3af", bg="#111827", font=("Helvetica", 10, "italic"))
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
        
        # Posizionamento iniziale ad anello largo per il ciclo 4-2-1
        self.add_node_immediate(1, 500, 380)
        self.add_node_immediate(2, 440, 310)
        self.add_node_immediate(4, 560, 310)
        self.edges.add((4, 2))
        self.edges.add((2, 1))
        self.edges.add((1, 4))
        
        self.update_entry_with_next_lowest()
        self.update_physics()
        
    def add_node_immediate(self, num, x, y):
        if num not in self.nodes:
            self.nodes[num] = {'x': x, 'y': y, 'vx': 0, 'vy': 0, 'highlight': 0}

    def update_entry_with_next_lowest(self):
        candidate = 1
        while candidate in self.nodes:
            candidate += 1
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(candidate))

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

    # --- Logica Sequenza di Gioco ---
    def start_sequence(self):
        try:
            val = int(self.entry.get())
            if val <= 0: return
        except ValueError:
            return 
        
        curr = val
        seq = []
        visited = set()
        
        while curr not in self.nodes and curr not in visited:
            seq.append(curr)
            visited.add(curr)
            if curr % 2 == 0:
                nxt = curr // 2
            else:
                nxt = 3 * curr + 1
            curr = nxt
            
        if curr in self.nodes:
            seq.append(curr)  
            
        seq.reverse()
        self.animate_next_step(seq)

    def animate_next_step(self, seq):
        if len(seq) < 2:
            self.update_entry_with_next_lowest()
            return
            
        v = seq[0]  
        u = seq[1]  
        
        if u not in self.nodes:
            parent_target = None
            for edge_u, edge_v in self.edges:
                if edge_u == v:
                    parent_target = edge_v
                    break
            
            if parent_target in self.nodes:
                dx = self.nodes[v]['x'] - self.nodes[parent_target]['x']
                dy = self.nodes[v]['y'] - self.nodes[parent_target]['y']
                base_angle = math.atan2(dy, dx)
            else:
                base_angle = math.atan2(self.nodes[v]['y'] - 380, self.nodes[v]['x'] - 500)
            
            branch_angle = 0.52 if u % 2 == 0 else -0.78  
            final_angle = base_angle + branch_angle
            
            distance = 60
            base_x = self.nodes[v]['x'] + math.cos(final_angle) * distance
            base_y = self.nodes[v]['y'] + math.sin(final_angle) * distance
                
            self.nodes[u] = {'x': base_x, 'y': base_y, 'vx': 0, 'vy': 0, 'highlight': 25}
        else:
            self.nodes[u]['highlight'] = 25  
            
        self.edges.add((u, v))
        self.root.after(200, lambda: self.animate_next_step(seq[1:]))

    def update_physics(self):
        keys = list(self.nodes.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                u, v = keys[i], keys[j]
                dx = self.nodes[u]['x'] - self.nodes[v]['x']
                dy = self.nodes[u]['y'] - self.nodes[v]['y']
                dist = math.hypot(dx, dy) + 0.1
                
                repulsion_radius = 110
                if dist < repulsion_radius:  
                    force = (repulsion_radius - dist) * 0.08
                    fx = (dx / dist) * force
                    fy = (dy / dist) * force
                    
                    if u not in (1, 2, 4):
                        self.nodes[u]['vx'] += fx
                        self.nodes[u]['vy'] += fy
                    if v not in (1, 2, 4):
                        self.nodes[v]['vx'] -= fx
                        self.nodes[v]['vy'] -= fy

        for u, v in list(self.edges):
            if u not in self.nodes or v not in self.nodes:
                continue
            dx = self.nodes[v]['x'] - self.nodes[u]['x']
            dy = self.nodes[v]['y'] - self.nodes[u]['y']
            dist = math.hypot(dx, dy) + 0.1
            desired_dist = 50  
            if dist > desired_dist:
                force = (dist - desired_dist) * 0.04
                fx = (dx / dist) * force
                fy = (dy / dist) * force
                if u not in (1, 2, 4):
                    self.nodes[u]['vx'] += fx
                    self.nodes[u]['vy'] += fy
                if v not in (1, 2, 4):
                    self.nodes[v]['vx'] -= fx
                    self.nodes[v]['vy'] -= fy

        for u in self.nodes:
            self.nodes[u]['x'] += self.nodes[u]['vx']
            self.nodes[u]['y'] += self.nodes[u]['vy']
            self.nodes[u]['vx'] *= 0.70
            self.nodes[u]['vy'] *= 0.70
            if self.nodes[u]['highlight'] > 0:
                self.nodes[u]['highlight'] -= 1

        self.draw_graph()
        self.root.after(30, self.update_physics)

    def draw_graph(self):
        self.canvas.delete("all")
        bg_txt_x = 500 * self.scale + self.offset_x
        bg_txt_y = 120 * self.scale + self.offset_y
        font_size_bg = max(10, int(42 * self.scale))
        if 5 < font_size_bg < 100:
            self.canvas.create_text(bg_txt_x, bg_txt_y, text="y = 3x + 1", fill="#233044", font=("Helvetica", font_size_bg, "bold"))
        
        for u, v in self.edges:
            if u not in self.nodes or v not in self.nodes:
                continue
            x1 = self.nodes[u]['x'] * self.scale + self.offset_x
            y1 = self.nodes[u]['y'] * self.scale + self.offset_y
            x2 = self.nodes[v]['x'] * self.scale + self.offset_x
            y2 = self.nodes[v]['y'] * self.scale + self.offset_y
            dist = math.hypot(x2 - x1, y2 - y1) + 0.1
            r = 16 * self.scale  
            if dist > r * 2:
                x1_edge = x1 + (x2 - x1) * (r / dist)
                x2_edge = x2 - (x2 - x1) * (r / dist)
                y1_edge = y1 + (y2 - y1) * (r / dist)
                y2_edge = y2 - (y2 - y1) * (r / dist)
                w = max(1, int(2 * self.scale))
                self.canvas.create_line(x1_edge, y1_edge, x2_edge, y2_edge, fill="#38bdf8", arrow=tk.LAST, width=w, arrowshape=(int(7*self.scale)+1, int(9*self.scale)+1, int(3*self.scale)+1))
        
        for num, data in self.nodes.items():
            x = data['x'] * self.scale + self.offset_x
            y = data['y'] * self.scale + self.offset_y
            r = 16 * self.scale
            if x < -r or x > 1000 + r or y < -r or y > 700 + r:
                continue
            if data['highlight'] > 0:
                bg_color = "#22c55e"    
                text_color = "#ffffff"  
                outline_color = "#86efac"
            else:
                bg_color = "#60a5fa" if num % 2 == 0 else "#818cf8"
                text_color = "#0f172a"
                outline_color = "#93c5fd"
            
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=bg_color, outline=outline_color, width=max(1, 1.5 * self.scale))
            base_f_size = 9 if num > 99 else (10 if num > 9 else 11)
            font_size = int(base_f_size * self.scale)
            if font_size > 4:
                self.canvas.create_text(x, y, text=str(num), fill=text_color, font=("Helvetica", font_size, "bold"))

    # ==========================================
    # NUOVA SEZIONE: FINESTRA STATISTICHE RANGE
    # ==========================================
    def open_stats_window(self):
        # Finestra Toplevel indipendente
        stats_win = tk.Toplevel(self.root)
        stats_win.title("Collatz Global Range Analytics")
        stats_win.geometry("1100x550")
        stats_win.configure(bg="#111827")
        
        # Top bar interna della nuova finestra
        top_bar = tk.Frame(stats_win, bg="#1f2937", pady=8)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        
        range_label = tk.Label(top_bar, text="Calcola da 1 fino a:", fg="white", bg="#1f2937", font=("Helvetica", 11, "bold"))
        range_label.pack(side=tk.LEFT, padx=10)
        
        range_entry = tk.Entry(top_bar, font=("Helvetica", 11), width=8, bg="#374151", fg="white", insertbackground="white")
        range_entry.pack(side=tk.LEFT, padx=5)
        range_entry.insert(0, "1000") # Valore di default consigliato e fulmineo
        
        # Frame contenitore dei due grafici affiancati
        graphs_frame = tk.Frame(stats_win, bg="#111827")
        graphs_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Canvas 1 (Step Totali)
        canvas_steps = tk.Canvas(graphs_frame, width=520, height=450, bg="#1e293b", highlightthickness=0)
        canvas_steps.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Canvas 2 (Nodi Nuovi)
        canvas_new_nodes = tk.Canvas(graphs_frame, width=520, height=450, bg="#1e293b", highlightthickness=0)
        canvas_new_nodes.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        def run_analysis():
            try:
                max_val = int(range_entry.get())
                if max_val < 1: return
            except ValueError:
                return
            
            steps_data = []
            new_nodes_data = []
            global_seen = {1, 2, 4} # Base di partenza fissa
            
            # Calcolo istantaneo di tutto il blocco numerico richiesto
            for i in range(1, max_val + 1):
                # 1. Calcolo degli step totali per chiudere sul ciclo
                curr = i
                steps = 0
                seq_this_run = []
                while curr not in (1, 2, 4) and curr not in seq_this_run:
                    seq_this_run.append(curr)
                    curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
                    steps += 1
                if i in (1, 2, 4): 
                    steps = 0
                steps_data.append((i, steps))
                
                # 2. Calcolo dei nodi effettivamente "nuovi" scoperti da questo intero
                curr = i
                full_path = []
                while curr not in (1, 2, 4) and curr not in full_path:
                    full_path.append(curr)
                    curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
                if curr in (1, 2, 4):
                    full_path.append(curr)
                
                new_discoveries = 0
                for n in full_path:
                    if n not in global_seen:
                        new_discoveries += 1
                        global_seen.add(n)
                new_nodes_data.append((i, new_discoveries))
            
            # Rendering grafico personalizzato vettoriale su Canvas
            self.draw_custom_plot(canvas_steps, steps_data, "Total Steps to 4-2-1 Cycle", "Starting Number (x)", "Steps Count (y)", "#f59e0b")
            self.draw_custom_plot(canvas_new_nodes, new_nodes_data, "New Unique Numbers Discovered", "Starting Number (x)", "New Numbers Added (y)", "#a855f7")

        calc_btn = tk.Button(top_bar, text="Genera Grafici", font=("Helvetica", 10, "bold"), bg="#10b981", fg="white", command=run_analysis)
        calc_btn.pack(side=tk.LEFT, padx=15)
        
        # Avvia il primo calcolo automatico all'apertura
        stats_win.after(100, run_analysis)

    def draw_custom_plot(self, canvas, data, title, x_label, y_label, dot_color):
        canvas.delete("all")
        
        # Coordinate e dimensioni dinamiche del grafico
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        if w < 100: w = 520  # Fallback di sicurezza prima del mapping geometrico di Tkinter
        if h < 100: h = 450
        
        pad_l, pad_r, pad_t, pad_b = 55, 25, 45, 45
        plot_w = w - pad_l - pad_r
        plot_h = h - pad_t - pad_b
        
        max_x = max([d[0] for d in data]) if data else 1
        max_y = max([d[1] for d in data]) if data else 1
        if max_y == 0: max_y = 1
        
        # --- Disegno Assi e Griglia di Sfondo ---
        canvas.create_line(pad_l, h - pad_b, w - pad_r, h - pad_b, fill="#4b5563", width=2) # Asse X
        canvas.create_line(pad_l, pad_t, pad_l, h - pad_b, fill="#4b5563", width=2)         # Asse Y
        
        # Testi e descrizioni assi
        canvas.create_text(w/2, 20, text=title, fill="white", font=("Helvetica", 12, "bold"))
        canvas.create_text(w/2, h - 15, text=x_label, fill="#9ca3af", font=("Helvetica", 10))
        
        # Asse Y ruotato artificialmente per una lettura pulita
        canvas.create_text(18, h/2, text=y_label, fill="#9ca3af", font=("Helvetica", 10), angle=90)
        
        # --- Tacche di riferimento quantitative (Ticks) ---
        # Y Massimo
        canvas.create_text(pad_l - 18, pad_t, text=str(max_y), fill="#9ca3af", font=("Helvetica", 9))
        canvas.create_line(pad_l - 5, pad_t, pad_l, pad_t, fill="#4b5563")
        # Metà Y
        canvas.create_text(pad_l - 18, pad_t + plot_h/2, text=str(max_y//2), fill="#4b5563", font=("Helvetica", 9))
        canvas.create_line(pad_l, pad_t + plot_h/2, w - pad_r, pad_t + plot_h/2, fill="#334155", dash=(4,4))
        # Zero
        canvas.create_text(pad_l - 18, h - pad_b, text="0", fill="#9ca3af", font=("Helvetica", 9))
        
        # X Massimo
        canvas.create_text(w - pad_r, h - pad_b + 15, text=str(max_x), fill="#9ca3af", font=("Helvetica", 9))
        canvas.create_line(w - pad_r, h - pad_b, w - pad_r, h - pad_b + 5, fill="#4b5563")
        
        # --- Rendering dei Punti Statistici ---
        for x, y in data:
            cx = pad_l + (x / max_x) * plot_w
            cy = h - pad_b - (y / max_y) * plot_h
            
            # Disegna pixel/rettangoli piccolissimi per garantire un'altissima fluidità di disegno
            canvas.create_rectangle(cx - 1, cy - 1, cx + 1, cy + 1, fill=dot_color, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CollatzInfiniteVisualizer(root)
    root.mainloop()