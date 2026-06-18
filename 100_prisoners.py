import random

def simulate_cycle_strategy(num_prisoners=100, max_boxes=50):
    boxes = list(range(1, num_prisoners + 1))
    random.shuffle(boxes)
    for prisoner in range(1, num_prisoners + 1):
        current_box = prisoner
        found = False
        for _ in range(max_boxes):
            ticket = boxes[current_box - 1]
            if ticket == prisoner:
                found = True
                break
            current_box = ticket
        if not found:
            return False
    return True

def simulate_random_strategy(num_prisoners=100, max_boxes=50):
    boxes = list(range(1, num_prisoners + 1))
    random.shuffle(boxes)
    # Ogni prigioniero sceglie 50 scatole a caso indipendentemente
    for prisoner in range(1, num_prisoners + 1):
        choices = random.sample(range(num_prisoners), max_boxes)
        found = False
        for box_index in choices:
            if boxes[box_index] == prisoner:
                found = True
                break
        if not found:
            return False
    return True

def run_comparative_simulations(simulations=10000):
    success_cycle = 0
    success_random = 0

    for _ in range(simulations):
        if simulate_cycle_strategy():
            success_cycle += 1
        if simulate_random_strategy():
            success_random += 1

    print(f"Simulazioni eseguite: {simulations}")
    print("-" * 30)
    print(f"Strategia Cicli: {success_cycle/simulations:.4%}")
    print(f"Strategia Casuale: {success_random/simulations:.4%}")

if __name__ == "__main__":
    # Nota: Ho abbassato a 10.000 simulazioni perché la strategia 
    # casuale è vicinissima allo zero e richiede molto tempo per 
    # vederne una riuscita per caso.
    run_comparative_simulations(10000)