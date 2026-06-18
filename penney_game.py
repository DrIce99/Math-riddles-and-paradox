import random

simulations = 10000

def penny_game_simulation(seq1, seq2, trials=simulations):
    s1_wins = 0
    
    for _ in range(trials):
        # Generiamo una lunga sequenza di lanci finché uno vince
        # (Per efficienza ne generiamo un po' alla volta, ma qui facciamo semplicemente)
        flips = ""
        while True:
            flips += "H" if random.random() < 0.5 else "T" # H=Head, T=Tail
            
            # Controlliamo chi ha vinto
            if flips.endswith(seq1):
                s1_wins += 1
                break
            if flips.endswith(seq2):
                break # Seq2 vince
                
    return s1_wins / trials

# Strategia ottima per il Giocatore 2 contro la scelta del Giocatore 1:
# Se Giocatore 1 sceglie A-B-C, Giocatore 2 sceglie "opposto(A)-A-B"
i = 0;
p1_seq= ""
while i!=3:
    p1_seq += "H" if random.random() < 0.5 else "T"
    i+=1
# Random tranne il secondo
p2_seq = "T" if p1_seq[1] == "H" else "H" 
p2_seq += "H" if p1_seq[0] == "H" else "T" 
p2_seq += "H" if p1_seq[1] == "H" else "T" 

prob_p1 = penny_game_simulation(p1_seq, p2_seq)
print(f"Sequenza Giocatore 1: {p1_seq}")
print(f"Sequenza Giocatore 2: {p2_seq}")
print(f"Probabilità che vinca il Giocatore 1: {prob_p1:.2%}")
print(f"Probabilità che vinca il Giocatore 2: {1-prob_p1:.2%}")