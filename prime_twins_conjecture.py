# LA DISTANZA TRA LE DISTANZE CAMBIA FINO A STABILIZZARSI SEMPRE A 6!
# Attenzione: questa affermazione può non essere seguita nelle distanze finali in quanto, per provarla, si dovrebbe tendere a reperire Primi Gemelli all'infinito
import matplotlib.pyplot as plt
from collections import Counter

def è_primo(n):
    """Verifica se un numero è primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def genera_coppie_gemelli_esclusive(quante_coppie):
    coppie = []
    numero = 3
    while len(coppie) < quante_coppie:
        if è_primo(numero) and è_primo(numero + 2):
            coppie.append((numero, numero + 2))
            numero += 3 
        else:
            numero += 1
    return coppie

def calcola_e_grafica_gemelli_con_frequenza(numero_coppie):
    coppie = genera_coppie_gemelli_esclusive(numero_coppie)
    
    punti_x = []       # Numero di mezzo della coppia
    distanze_y = []    # Distanza dalla coppia successiva
    
    # Primo passaggio: calcoliamo tutte le distanze della sequenza
    for i in range(len(coppie) - 1):
        secondo_corrente = coppie[i][1]
        primo_successivo = coppie[i+1][0]
        distanza = primo_successivo - secondo_corrente
        
        numero_di_mezzo = (coppie[i][0] + coppie[i][1]) / 2
        
        punti_x.append(numero_di_mezzo)
        distanze_y.append(distanza)

    # Calcoliamo quante volte compare ogni distanza nella simulazione
    conteggio_distanze = Counter(distanze_y)
    
    # Generiamo la lista delle frequenze corrispondente a ogni punto
    frequenze_y2 = [conteggio_distanze[d] for d in distanze_y]

    # Stampa i risultati testuali
    print("Resoconto distanze nella simulazione:")
    for dist in sorted(conteggio_distanze.keys()):
        freq = conteggio_distanze[dist]
        print(f"La distanza {dist} si ripete {freq} volte.")
    print("-" * 40)

    # Creazione del grafico con doppio asse Y
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Primo asse (Sinistra) - Distanza effettiva
    colore_dist = 'crimson'
    ax1.set_xlabel("Numero di mezzo della coppia di partenza", fontsize=12)
    ax1.set_ylabel("Distanza dall'inizio della coppia successiva", color=colore_dist, fontsize=12)
    linea1 = ax1.plot(punti_x, distanze_y, marker='', linestyle='-', color=colore_dist, label='Distanza Effettiva')
    ax1.tick_params(axis='y', labelcolor=colore_dist)
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Secondo asse (Destra) - Ripetizioni totali di quella distanza
    ax2 = ax1.twinx()  
    colore_freq = 'royalblue'
    ax2.set_ylabel("Numero di ripetizioni totali di quella distanza nella simulazione", color=colore_freq, fontsize=12)
    linea2 = ax2.plot(punti_x, frequenze_y2, marker='', linestyle='--', color=colore_freq, label='Ripetizioni totali della distanza')
    ax2.tick_params(axis='y', labelcolor=colore_freq)

    # Uniamo le legende di entrambi gli assi in un unico box
    linee = linea1 + linea2
    etichette = [l.get_label() for l in linee]
    ax1.legend(linee, etichette, loc='upper left')

    plt.title("Analisi delle distanze e delle loro frequenze nei Primi Gemelli", fontsize=14)
    plt.show()

# Imposta un numero più alto (es. 50) per raccogliere abbastanza dati e vedere le ripetizioni
quante_coppie = 100
calcola_e_grafica_gemelli_con_frequenza(quante_coppie)