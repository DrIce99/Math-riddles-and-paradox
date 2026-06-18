import random

def simula_monty_hall(numero_porte, numero_simulazioni):
    vittorie_cambiando = 0

    for _ in range(numero_simulazioni):
        # La porta vincente è scelta casualmente
        porta_vincente = random.randint(1, numero_porte)
        # La scelta iniziale dell'utente
        scelta_iniziale = random.randint(1, numero_porte)

        # Se l'utente ha scelto la porta vincente, cambiando perde.
        # Se l'utente ha scelto una porta perdente, il presentatore rimuove
        # tutte le altre porte perdenti. Cambiando, l'utente vince sempre.
        if scelta_iniziale != porta_vincente:
            vittorie_cambiando += 1

    percentuale_vittoria = (vittorie_cambiando / numero_simulazioni) * 100
    return percentuale_vittoria

# --- Configurazione Simulazione ---
n_porte = 3
n_simulazioni = 100000

percentuale = simula_monty_hall(n_porte, n_simulazioni)

print(f"Simulazione Monty Hall con {n_porte} porte.")
print(f"Su {n_simulazioni} simulazioni, la percentuale di vittoria")
print(f"cambiando la porta è circa: {percentuale:.2f}%")