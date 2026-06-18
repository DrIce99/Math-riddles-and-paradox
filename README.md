# MATH RIDDLES & PARADOX

## Scegli la lingua / Choose your language

<details>
<summary>🇮🇹 <b>Italiano (Clicca per espandere)</b></summary>
<br>

Una piccola repo personale in cui cerco di trovare dei significati logici dietro:
- apparenti sequenze casuali
-  ottimizzazioni all'apparenza magiche

___

### Programmi:

#### *Il problema dei 100 prigionieri*

Ci sono 100 prigionieri numerati da 1 a 100. Una guardia decide di dare loro un'occasione per uscire di prigione, ma solo in determinate condizioni. Li sottopone alla seguente situazione:

> [!IMPORTANT]
> 1. In una stanza ci sono 100 scatole, ognuna contenente un numero da 1 a 100 (in modo casuale). 
> 2. Ogni prigioniero deve entrare nella stanza e aprire 50 scatole per trovare il numero corrispondente al proprio. 
> 3. Se tutti e 100 i prigionieri trovano il proprio numero, sono tutti liberi. Se anche uno solo fallisce, tutti vengono giustiziati. Non possono comunicare tra loro una volta iniziata la sfida.

> [!NOTE]
> Se ogni prigioniero scegliesse 50 scatole a caso, la probabilità di successo collettivo sarebbe incredibilmente bassa: $(1/2)^{100}$, ovvero praticamente zero.

> [!TIP]
> Il programma implementa la strategia ottimale basata sui cicli di permutazione:
> 1. Il prigioniero apre prima la scatola che ha il suo numero scritto sopra.
> 2. Se trova il suo numero, ha finito.
> 3. Se trova un altro numero, usa quel numero come indice per aprire la scatola successiva.
> 4. Ripete questo processo finché non trova il suo numero o finché non ha aperto 50 scatole.

Eseguendo la simulazione, noterai che la probabilità di successo non è quasi zero, ma è superiore al 30%!

Questo accade perché, seguendo la strategia dei cicli, il successo di ogni prigioniero non è più un evento indipendente: tutti i prigionieri condividono lo stesso destino basato sulla struttura dei cicli presenti nella permutazione casuale delle scatole. Se la permutazione non contiene cicli più lunghi di 50, allora tutti i prigionieri riusciranno a trovare il proprio numero.
___

#### *Congettura di Collatz*

La congettura di Collatz, nota anche come il problema $3n + 1$, è uno dei problemi irrisolti più famosi della matematica. Si applica a qualsiasi numero intero positivo $n$ e segue una regola di trasformazione molto semplice:

> [!IMPORTANT]
> 1. Se il numero è pari, dividilo per 2 ($n / 2$).
> 2. Se il numero è dispari, moltiplicalo per 3 e aggiungi 1 ($3n + 1$).
> 3. Ripeti il processo con il risultato ottenuto.

> [!NOTE]
> La congettura afferma che, indipendentemente dal numero di partenza scelto, la sequenza raggiungerà sempre il ciclo $4 \to 2 \to 1$. Nonostante la semplicità della regola, nessuno è ancora riuscito a dimostrare matematicamente che questo accade per *ogni* numero esistente.

> [!TIP]
> Il programma implementa un visualizzatore grafico dinamico che permette di esplorare la struttura ad albero della congettura:
> 1. Visualizzazione planare che evita l'intreccio dei rami per una lettura chiara del grafo.
> 2. Implementazione di una navigazione "infinita" con supporto a Pan & Zoom.
> 3. Analisi statistica globale che confronta il numero di step necessari per raggiungere il ciclo e la scoperta di nuovi nodi nel grafo.

Eseguendo la simulazione, potrai osservare come i numeri convergano naturalmente verso il ciclo centrale. La struttura si espande come un albero binario inverso, dove ogni numero funge da "radice" per i propri predecessori, rivelando un ordine profondo e geometricamente elegante dietro quello che inizialmente appare come un calcolo caotico.

___

#### *Il paradosso di Monty Hall*

Il paradosso di Monty Hall è un famoso problema di teoria della probabilità legato al gioco a premi americano *Let's Make a Deal*. Il gioco si basa su una scelta apparentemente semplice che sfida la nostra intuizione quotidiana:

> [!IMPORTANT]
> 1. Al concorrente vengono mostrate tre porte chiuse: dietro una c'è un'automobile (il premio), dietro le altre due ci sono delle capre.
> 2. Il concorrente sceglie una porta, che inizialmente resta chiusa.
> 3. Il presentatore (Monty Hall), che sa cosa c'è dietro ogni porta, apre una delle altre due porte, rivelando sempre una capra.
> 4. A questo punto, il presentatore offre al concorrente la possibilità di cambiare la propria scelta originaria con l'altra porta rimasta chiusa.

> [!NOTE]
> L'intuizione comune suggerisce che, rimaste solo due porte, le probabilità di vincere l'auto siano del 50% indipendentemente dalla scelta, rendendo il cambio della porta del tutto indifferente.

> [!TIP]
> Il programma esegue una simulazione statistica su larga scala per dimostrare l'efficacia della strategia del cambio:
> 1. Genera casualmente la posizione del premio e la scelta iniziale del giocatore.
> 2. Simula il comportamento del presentatore che scarta una porta perdente.
> 3. Calcola matematicamente e mostra la percentuale di vittorie totali applicando costantemente la strategia di cambiare la porta.

Eseguendo la simulazione, noterai che la probabilità di vittoria cambiando la porta non è del 50%, bensì di circa il 66.6% (2/3)!

Questo accade perché la scelta iniziale del giocatore ha 1 probabilità su 3 di essere corretta e 2 probabilità su 3 di essere errata (cioè di aver scelto una capra). Se il giocatore ha scelto una capra all'inizio, il presentatore è costretto a rivelare l'altra capra rimasta. Di conseguenza, l'ultima porta rimasta conterrà *sempre* l'automobile. Cambiando sempre porta, si trasforma ogni errore iniziale in una vittoria, raddoppiando di fatto le proprie possibilità di successo.

___

#### *Distanza tra Primi Gemelli*

I numeri primi gemelli sono coppie di numeri primi che differiscono tra loro di esattamente 2 (come $3$ e $5$, $11$ e $13$). L'analisi si concentra sulla "distanza tra le distanze", ovvero lo spazio che separa la fine di una coppia di gemelli dall'inizio della coppia successiva.

> [!IMPORTANT]
> 1. Il programma genera sequenze esclusive di coppie di numeri primi gemelli.
> 2. Calcola lo scarto numerico esistente tra la fine di una coppia e l'inizio di quella immediatamente successiva.
> 3. Traccia statisticamente la frequenza assoluta con cui ogni singola distanza si presenta all'interno della simulazione.

> [!NOTE]
> Sebbene si osservi sperimentalmente che la distanza tra le coppie tenda statisticamente a stabilizzarsi con picchi ricorrenti sul valore 6, questa affermazione non può essere assunta come regola assoluta per le distanze finali, poiché la verifica empirica richiederebbe di reperire coppie di primi gemelli all'infinito (legandosi alla celebre e ancora irrisolta congettura dei primi gemelli).

> [!TIP]
> Il programma implementa un sistema di analisi e visualizzazione grafica a doppio asse:
> 1. Generazione dinamica ed esclusiva delle coppie matematiche per evitare sovrapposizioni.
> 2. Calcolo in tempo reale delle frequenze di occorrenza di ogni scarto tramite un contatore statistico.
> 3. Rendering visivo con doppio asse Y per confrontare contemporaneamente la distanza effettiva di ogni punto e il numero di ripetizioni totali di quel valore.

Eseguendo la simulazione su un set di dati sufficientemente ampio, potrai notare visivamente come la distribuzione delle distanze non sia puramente caotica, ma tenda a concentrarsi attorno a valori multipli di 6.

Questo fenomeno riflette le proprietà intrinseche della distribuzione dei numeri primi nella progressione aritmetica: poiché tutti i numeri primi maggiori di 3 devono necessariamente essere della forma $6k \pm 1$, le dinamiche di spaziatura tra le coppie di gemelli risentono fortemente di questa rigidità strutturale di base della teoria dei numeri.

___

</details>

<details>
<summary>🇬🇧 <b>English (Click to expand)</b></summary>
<br>

A small personal repository where I try to uncover the logical meanings behind:
- apparent random sequences
- seemingly magical optimizations

___

### Programs:

#### *The 100 Prisoners Problem*

> [!NOTE]
> There are 100 prisoners numbered from 1 to 100. A guard decides to offer them a chance to be released from prison, but only under specific conditions. They are subjected to the following situation:

> [!IMPORTANT]
> 1. In a room, there are 100 boxes, each containing a random number from 1 to 100.
> 2. Each prisoner must enter the room and open up to 50 boxes to find the number corresponding to their own.
> 3. If all 100 prisoners find their own number, they are all set free. If even a single prisoner fails, everyone is executed. They cannot communicate with each other once the challenge begins.

> [!WARNING]
> If every prisoner chose 50 boxes completely at random, the probability of collective success would be incredibly low: $(1/2)^{100}$, which is practically zero.

> [!TIP]
> The program implements the optimal strategy based on permutation cycles:
> 1. The prisoner first opens the box labeled with their own number.
> 2. If they find their number inside, they are done.
> 3. If they find another number, they use that number as an index to open the next box.
> 4. They repeat this process until they find their number or until they have opened 50 boxes.

By running the simulation, you will notice that the probability of success is not close to zero, but actually over 30%!

This happens because, by following the cycle strategy, each prisoner's success is no longer an independent event: all prisoners share the same fate based on the structure of the cycles present in the random permutation of the boxes. If the permutation contains no cycles longer than 50, then every single prisoner will succeed in finding their number.
___

#### *The Monty Hall Paradox*

> [!NOTE]
> The Monty Hall paradox is a famous probability puzzle based on the American television game show *Let's Make a Deal*. The game relies on a seemingly simple choice that defies our everyday intuition:

> [!IMPORTANT]
> 1. The contestant is shown three closed doors: behind one is a car (the prize), and behind the other two are goats.
> 2. The contestant picks a door, which initially remains closed.
> 3. The host (Monty Hall), who knows what is behind each door, opens one of the other two doors, always revealing a goat.
> 4. At this point, the host offers the contestant the chance to switch their original choice to the remaining closed door.

> [!WARNING]
> Common intuition suggests that, with only two doors left, the chances of winning the car are 50/50 regardless of the choice, making switching doors completely irrelevant.

> [!TIP]
> The program runs a large-scale statistical simulation to demonstrate the effectiveness of the switching strategy:
> 1. It randomly generates the prize location and the player's initial choice.
> 2. It simulates the host's behavior of discarding a losing door.
> 3. It mathematically calculates and displays the total winning percentage when consistently applying the strategy of switching doors.

By running the simulation, you will notice that the probability of winning by switching is not 50%, but roughly 66.6% (2/3)!

This happens because the player's initial choice has a 1 in 3 chance of being correct and a 2 in 3 chance of being wrong (meaning they chose a goat). If the player picked a goat initially, the host is forced to reveal the other remaining goat. Consequently, the last remaining door will *always* contain the car. By always switching doors, every initial mistake is turned into a victory, effectively doubling the chances of success.
___

#### *Distance Between Twin Primes*

> [!NOTE]
> Twin primes are pairs of prime numbers that differ by exactly 2 (such as $3$ and $5$, $11$ and $13$). This analysis focuses on the "distance between distances"—the gap separating the end of one twin prime pair from the beginning of the next pair.

> [!IMPORTANT]
> 1. The program generates exclusive sequences of twin prime pairs.
> 2. It calculates the numerical gap between the end of one pair and the beginning of the immediately following one.
> 3. It statistically tracks the absolute frequency with which each individual distance appears within the simulation.

> [!WARNING]
> Although it can be observed experimentally that the distance between pairs tends to statistically stabilize with recurring peaks at the value of 6, this statement cannot be taken as an absolute rule for final distances. Empirically proving it would require finding twin prime pairs infinitely (linking it to the famous and still unsolved Twin Prime Conjecture).

> [!TIP]
> The program implements a dual-axis graphical analysis and visualization system:
> 1. Dynamic and exclusive generation of mathematical pairs to avoid overlaps.
> 2. Real-time calculation of the occurrence frequencies of each gap using a statistical counter.
> 3. Visual rendering with a dual Y-axis to simultaneously compare the actual distance of each point and the total number of repetitions for that value.

By running the simulation on a sufficiently large dataset, you will visually notice that the distribution of distances is not purely chaotic, but tends to cluster around multiples of 6.

This phenomenon reflects the intrinsic properties of prime number distribution within arithmetic progression: since all prime numbers greater than 3 must necessarily be of the form $6k \pm 1$, the spacing dynamics between twin pairs are heavily influenced by this fundamental structural rigidity in number theory.
___

#### *Collatz Conjecture*

> [!NOTE]
> The Collatz conjecture, also known as the $3n + 1$ problem, is one of the most famous unsolved problems in mathematics. It applies to any positive integer $n$ and follows a very simple transformation rule:

> [!IMPORTANT]
> 1. If the number is even, divide it by 2 ($n / 2$).
> 2. If the number is odd, multiply it by 3 and add 1 ($3n + 1$).
> 3. Repeat the process with the resulting value.

> [!WARNING]
> The conjecture states that regardless of which starting number is chosen, the sequence will always reach the $4 \to 2 \to 1$ cycle. Despite the simplicity of the rule, no one has yet managed to mathematically prove that this happens for *every* existing number.

> [!TIP]
> The program implements a dynamic graphical visualizer that allows exploring the tree-like structure of the conjecture:
> 1. Planar visualization that avoids overlapping branches for a clear reading of the graph.
> 2. Implementation of an "infinite" navigation with Pan & Zoom support.
> 3. Global statistical analysis comparing the number of steps required to reach the cycle and the discovery of new nodes in the graph.

By running the simulation, you can observe how numbers naturally converge toward the central cycle. The structure expands like an inverted binary tree, where each number acts as a "root" for its predecessors, revealing a deep and geometrically elegant order behind what initially appears to be a chaotic computation.

</details>