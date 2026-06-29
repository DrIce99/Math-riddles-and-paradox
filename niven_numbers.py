import matplotlib.pyplot as plt
import numpy as np

def is_niven(n):
    return n % sum(int(d) for d in str(n)) == 0

# ============================================================
# PARAMETRI
# ============================================================
max_range = 15000
window = 1000          # finestra per densità locale
step_campionamento = 100

# ============================================================
# PRECALCOLO: tabella booleana dei Niven (per efficienza)
# ============================================================
niven_table = [False] * (max_range + 1)
for i in range(1, max_range + 1):
    niven_table[i] = is_niven(i)

# ============================================================
# FASE 1: Trovare i Niven Primitivi e i punti di rottura
# ============================================================
primitives_ge10 = []
niven_primi = []
moltiplicatori_interruzione = []
punti_rottura = {}

print("=== SCHERMATA DI VISUALIZZAZIONE SECONDARIA: LE LINEE TEMPORALI ===")
print("{:<12} {:<60} {}".format("Niven Primo", "Linea Temporale (Progressione Multipli)", "Punto di Rottura (k)"))
print("-" * 95)

for n in range(10, max_range):
    if niven_table[n]:
        # Verifichiamo la divisibilità solo con i primitivi >= 10
        is_prim = True
        for p in primitives_ge10:
            if n % p == 0:
                is_prim = False
                break

        if is_prim:
            primitives_ge10.append(n)

            # Cerchiamo il punto in cui la linea temporale si interrompe
            k = 2
            while k * n <= max_range:
                if not niven_table[k * n]:
                    break
                k += 1

            punti_rottura[n] = k * n
            niven_primi.append(n)
            moltiplicatori_interruzione.append(k)

            # Stampiamo solo i primi 20
            if len(niven_primi) <= 20:
                timeline_visiva = "—" * (k - 1) + "❌"
                print("{:<12} {:<60} k = {}".format(f"Num {n}", timeline_visiva, k))

print(f"\nTotale Niven Primitivi trovati: {len(niven_primi)}")

# ============================================================
# FASE 2: Campionamento per i grafici
# ============================================================
x_valori = []
y_totale_primi = []
y_linee_attive = []
y_densita_locale = []
y_rapporto_niven_attive = []

# --- Cumulativa: parte da 10 ---
for n in range(10, max_range, step_campionamento):
    x_valori.append(n)

    # 1. Quanti niven primi sono nati fino a 'n'
    nati_fino_a_n = [p for p in primitives_ge10 if p <= n]
    y_totale_primi.append(len(nati_fino_a_n))

    # 2. Quante linee sono ancora ATTIVE al numero 'n'
    attive_a_n = [p for p in nati_fino_a_n if punti_rottura[p] > n]
    y_linee_attive.append(len(attive_a_n))

# --- Densità locale e rapporto: parte da 'window' ---
x_densita = []
for n in range(window, max_range, step_campionamento):
    x_densita.append(n)

    # Conta Niven nella finestra [n-window+1 .. n]
    count_niven_window = sum(1 for i in range(n - window + 1, n + 1) if niven_table[i])
    densita = count_niven_window / window * 100
    y_densita_locale.append(densita)

    # Rapporto: Niven nella finestra / linee attive a n
    nati_fino_a_n = [p for p in primitives_ge10 if p <= n]
    attive_a_n = [p for p in nati_fino_a_n if punti_rottura[p] > n]
    num_attive = len(attive_a_n)

    if num_attive > 0:
        y_rapporto_niven_attive.append(count_niven_window / num_attive)
    else:
        y_rapporto_niven_attive.append(0)

# ============================================================
# FASE 3: Generazione del grafico con assi gemelli
# ============================================================
fig, ax1 = plt.subplots(figsize=(14, 7))

# --- Asse sinistro: conteggi assoluti ---
ax1.plot(x_valori, y_totale_primi, color='royalblue', linewidth=2.5,
         label='Totale Niven Primi Scoperti (Linee nate)')
ax1.plot(x_valori, y_linee_attive, color='forestgreen', linewidth=2.5, linestyle='-',
         label='Linee Temporali Attive (Sopravvissute)')
ax1.set_xlabel('Progressione Numerica (N)', fontsize=12)
ax1.set_ylabel('Quantità (conteggi)', fontsize=12, color='darkslategray')
ax1.tick_params(axis='y', labelcolor='darkslategray')
ax1.grid(True, linestyle=':', alpha=0.6)

# --- Asse destro: percentuali e rapporto ---
ax2 = ax1.twinx()

ax2.plot(x_densita, y_densita_locale, color='crimson', linewidth=2, linestyle='--',
         label=f'Densità Locale Niven (finestra={window})')
ax2.plot(x_densita, y_rapporto_niven_attive, color='darkorange', linewidth=2, linestyle='-.',
         label='Rapporto Niven/Linee Attive (finestra)')
ax2.set_ylabel('Percentuale (%) / Rapporto', fontsize=12, color='crimson')
ax2.tick_params(axis='y', labelcolor='crimson')

# --- Legenda combinata ---
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='upper left')

plt.title('Ecosistema Niven: Nascite, Sopravvivenze, Densità Locale e Rapporto',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ============================================================
# FASE 4: Statistiche riassuntive
# ============================================================
print("\n=== STATISTICHE RIEPILOGATIVE ===")
print(f"Range analizzato: 10 → {max_range}")
print(f"Niven Primitivi totali: {len(niven_primi)}")
print(f"Niven totali nel range: {sum(niven_table[10:max_range+1])}")
print(f"Densità locale media (ultimi {window} numeri): {y_densita_locale[-1]:.2f}%")
print(f"Linee ancora attive a N={max_range}: {y_linee_attive[-1]}")
if y_rapporto_niven_attive[-1] > 0:
    print(f"Rapporto Niven/Attive (ultima finestra): {y_rapporto_niven_attive[-1]:.2f}")