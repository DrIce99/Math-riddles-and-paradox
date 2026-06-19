# MATH RIDDLES & PARADOXES

> [!NOTE]
> 🇬🇧 **English Version Available**: [Read the English version here](./README.en.md).

## ITA

Una piccola repo personale in cui cerco di trovare dei significati logici dietro:
- apparenti sequenze casuali
- ottimizzazioni all'apparenza magiche

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

#### *Paradosso di Bertrand (Scatole e Carte)*

Il paradosso di Bertrand è un celebre problema di probabilità condizionale che mette in luce come l'intuizione umana possa ingannarci di fronte a eventi dipendenti. Esistono due versioni classiche: quella delle **Tre Scatole** e quella delle **Tre Carte**.

> [!IMPORTANT]
> **Versione Scatole:**
> 1. Ci sono tre scatole: una con due monete d'oro (OO), una con due d'argento (AA), e una mista (OA).
> 2. Scegli una scatola a caso ed estrai una moneta a caso.
> 3. Se estrai una moneta d'oro, qual è la probabilità che l'altra moneta nella stessa scatola sia anch'essa d'oro?
>
> **Versione Carte:**
> 1. Ci sono tre carte: una rossa su entrambi i lati (RR), una bianca su entrambi i lati (BB), e una mista (RB).
> 2. Scegli una carta a caso e osservi una faccia a caso.
> 3. Se vedi una faccia rossa, qual è la probabilità che l'altra faccia sia anch'essa rossa?

> [!NOTE]
> L'intuizione suggerirebbe una probabilità del 50%, poiché sembra che restino solo due possibilità equiprobabili. In realtà, la probabilità corretta è **2/3 (circa 66.7%)**. Questo perché estrarre un oro (o vedere un rosso) è due volte più probabile se provieni dalla scatola/carta "doppia" rispetto a quella mista. Il paradosso nasce dal confondere la probabilità dell'oggetto con la probabilità del lato osservato.

> [!TIP]
> Il programma implementa una simulazione interattiva con visualizzazioni animate per entrambi i paradossi:
> 1. Interfaccia grafica con animazioni fluide (Anime.js) per l'estrazione di monete e il ribaltamento delle carte.
> 2. Meccanica di gioco: l'utente estrae/osserva, fa una previsione, e vede il risultato con feedback immediato.
> 3. Terminale integrato che mostra i risultati di 100.000 simulazioni automatiche, confermando statisticamente il 66.7%.
> 4. Rimozione dinamica degli elementi "incompatibili" per visualizzare chiaramente lo spazio campionario condizionato.

Eseguendo il programma e giocando manualmente, noterai che indovinare correttamente richiede di "fidarsi" della statistica contro l'intuizione. La simulazione automatica nel terminale conferma che, su 100.000 prove, la probabilità condizionale converge stabilmente verso 2/3, dimostrando visivamente come il paradosso di Bertrand sfidi le nostre aspettative naturali sulla probabilità.

___

#### *Il paradosso del compleanno*

Il paradosso del compleanno dimostra quanto sia controintuitiva la probabilità quando applicata a grandi numeri. Si basa sulla domanda: quante persone devono essere presenti in una stanza affinché ci sia almeno il 50% di probabilità che due di loro festeggino il compleanno lo stesso giorno?

> [!IMPORTANT]
> 1. Si ipotizza un anno di 365 giorni (senza considerare gli anni bisestili).
> 2. Si assume che ogni giorno dell'anno abbia la stessa probabilità di nascita.
> 3. L'obiettivo è calcolare la probabilità di collisione (due persone con lo stesso compleanno) al variare del numero di persone $n$.
> 
> 

> [!NOTE]
> L'istinto suggerisce che servano molte persone (spesso si pensa a 183, metà dell'anno). In realtà, la soglia del 50% viene superata con sole **23 persone**.

> [!TIP]
> Il programma implementa un'interfaccia interattiva che permette di esplorare il paradosso in tempo reale:
> 1. **Slider dinamico**: Permette di variare il numero di persone senza riavviare la simulazione.
> 2. **Calendario visuale**: Un visualizzatore a 12 mesi mostra le date estratte, evidenziando in modo chiaro (tramite una mappa di calore) i giorni in cui cadono le collisioni.
> 3. **Calcolo statistico**: Esegue migliaia di iterazioni per mostrare la convergenza della probabilità verso il risultato teorico.

Eseguendo la simulazione, vedrai come il numero di "coppie" cresca esponenzialmente all'aumentare dei partecipanti. La visualizzazione grafica trasforma il dato astratto in una mappa colorata dove i "cluster" di compleanni diventano immediatamente visibili, rendendo evidente perché la probabilità di una collisione sia molto più alta di quanto sembri.

<img width="662" height="842" alt="image" src="https://github.com/user-attachments/assets/89a77c51-3ee2-4717-a9ab-a0d6bfbd8645" />

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

<img width="1185" height="1011" alt="image" src="https://github.com/user-attachments/assets/c2f4f522-98f3-4434-928e-ffa5d205c691" />

<img width="1370" height="686" alt="image" src="https://github.com/user-attachments/assets/c0009b16-3bc8-4bfd-ad11-9038ea0191e8" />

___

#### *La Costante di Kaprekar (6174)*

Prendi un qualsiasi numero di 4 cifre (purché non abbia tutte le cifre uguali). Riordinane le cifre in modo decrescente per formare il numero più grande possibile, e in modo crescente per formare il più piccolo. Sottrai il minore dal maggiore e ripeti il processo.

> [!IMPORTANT]
> 1. Scegli un numero di 4 cifre (es. 3524).
> 2. Ordina le sue cifre in ordine decrescente (5432) e crescente (2345).
> 3. Sottrai il numero più piccolo da quello più grande (5432 - 2345 = 3087).
> 4. Ripeti l'operazione con il risultato fino a raggiungere il numero 6174.

> [!NOTE]
> Qualsiasi numero di 4 cifre (con almeno due cifre diverse) raggiungerà la costante 6174 in al massimo 7 iterazioni. Una volta raggiunto 6174, l'operazione diventa un "buco nero" matematico: 7641 - 1467 = 6174. Il ciclo si auto-alimenta all'infinito.

> [!TIP]
> Il programma implementa un visualizzatore interattivo di questa routine:
> 1. Inserisci un numero di partenza per vedere il suo percorso animato a ritroso verso il 6174.
> 2. Il grafo si espande dinamicamente usando un motore fisico (repulsione/attrazione) per evitare sovrapposizioni tra i nodi.
> 3. Puoi esplorare il grafo infinito usando il Pan (trascinamento del mouse) e lo Zoom (rotellina).
> 4. La sezione "Analisi Range" calcola e plotta i passi necessari e il picco massimo raggiunto per qualsiasi intervallo di numeri.

Eseguendo il programma e inserendo diversi numeri di partenza, noterai che tutti i percorsi convergono inevitabilmente verso il nodo rosso centrale (6174). L'analisi statistica rivela inoltre che la maggior parte dei numeri richiede dai 3 ai 5 passi, creando un affascinante pattern a "cascata" nel grafico dei picchi massimi. Questo dimostra visivamente come un'operazione aritmetica apparentemente semplice generi una struttura matematica altamente ordinata e deterministica.

<img width="1051" height="983" alt="Screenshot 2026-06-18 153636" src="https://github.com/user-attachments/assets/bf92409e-3a50-4f0f-9dc9-f5dd97f764de" />

<img width="1367" height="684" alt="image" src="https://github.com/user-attachments/assets/7a5df582-0b8c-48c8-8704-9a70aa5df28a" />

___

#### *Il paradosso di Monty Hall*

Il paradosso di Monty Hall è un famoso problema di teoria della probabilità legato al gioco a premi americano *Let's Make a Deal*. Il gioco si basa su una scelta apparentemente semplice che sfida la nostra intuizione quotidiana:

> [!IMPORTANT]
> 1. Al concorrente vengono mostrate tre porte chiuse: dietro una c'è un'automobile (il premio), dietro le altre due ci sono delle capre.
> 2. Il concorrente sceglie una porta, che inizialmente resta chiusa.
> 3. Il presentatore (Monty Hall), che sa cosa c'è dietro ogni porta, apre una delle altre due porte, rivelando sempre una capra.
> 4. A questo punto, il presentatore offre al concorrente la possibilità di cambiare la propria scelta originaria con l'altra porta rimasta chiusa.

> [!NOTE]
> 
> L'intuizione comune suggerisce che, rimaste solo due porte, le probabilità di vincere l'auto siano del 50% indipendentemente dalla scelta, rendendo il cambio della porta del tutto indifferente.

> [!TIP]
> Il programma esegue una simulazione statistica su larga scala per dimostrare l'efficacia della strategia del cambio:
> 1. Genera casualmente la posizione del premio e la scelta iniziale del giocatore.
> 2. Simula il comportamento del presentatore che scarta una porta perdente.
> 3. Calcola matematicamente e mostra la percentuale di vittorie totali applicando costantemente la strategia di cambiare la porta.

Eseguendo la simulazione, noterai che la probabilità di vittoria cambiando la porta non è del 50%, bensì di circa il 66.6% (2/3)!

Questo accade perché la scelta iniziale del giocatore ha 1 probabilità su 3 di essere corretta e 2 probabilità su 3 di essere errata (cioè di aver scelto una capra). Se il giocatore ha scelto una capra all'inizio, il presentatore è costretto a rivelare l'altra capra rimasta. Di conseguenza, l'ultima porta rimasta conterrà *sempre* l'automobile. Cambiando sempre porta, si trasforma ogni errore iniziale in una vittoria, raddoppiando di fatto le proprie possibilità di successo.

___

#### *Il gioco di Penney*

Due giocatori si sfidano lanciando una moneta equa. Ciascun giocatore sceglie una sequenza di tre risultati (Testa o Croce). La moneta viene lanciata ripetutamente fino a quando una delle due sequenze non appare.

> [!IMPORTANT]
> 1. Il Giocatore 1 sceglie una sequenza di 3 lanci (es. H-H-H).
> 2. Il Giocatore 2, conoscendo la scelta del primo, sceglie una sequenza diversa di 3 lanci (es. T-H-H).
> 3. Si lancia la moneta ripetutamente. Il giocatore la cui sequenza appare per prima nella serie di lanci vince la partita.

> [!NOTE]
> Poiché la moneta è equa e le sequenze hanno la stessa lunghezza, l'intuito suggerisce che il gioco sia perfettamente bilanciato. Ci si aspetterebbe che ogni giocatore abbia esattamente il 50% di probabilità di vincere.

> [!TIP]
> Il programma implementa la strategia ottimale per il Giocatore 2 (basata sull'algoritmo di Conway):
> 1. Il Giocatore 1 sceglie una sequenza A-B-C.
> 2. Il Giocatore 2 sceglie come primo elemento l'opposto del secondo elemento di P1 (non-B).
> 3. Come secondo e terzo elemento, il Giocatore 2 copia i primi due elementi scelti dal Giocatore 1 (A-B).
> 4. La sequenza finale del Giocatore 2 sarà quindi: non-B - A - B.

Eseguendo la simulazione, noterai che il gioco non è affatto bilanciato: il Giocatore 2 vince circa il 66% - 75% delle volte, a seconda della scelta iniziale del Giocatore 1!

Questo accade perché il Gioco di Penney è un gioco *non transitivo*. La strategia del Giocatore 2 è progettata per creare una "sovrapposizione" matematica sfavorevole. Ad esempio, se il Giocatore 1 sceglie H-H-H e il Giocatore 2 sceglie T-H-H, l'unico modo in cui il Giocatore 1 può vincere è che le prime tre monete escano tutte Teste. Se esce anche una sola Croce all'inizio, la sequenza H-H-H è "rotta", ma la sequenza T-H-H è ancora viva e avrà la meglio non appena usciranno due Teste consecutive. Il Giocatore 2 ha sempre un vantaggio matematico garantito, indipendentemente da cosa scelga il Giocatore 1.

___

___

#### *Distanza tra Primi Gemelli*

I numeri primi gemelli sono coppie di numeri primi che differiscono tra loro di esattamente 2 (come $3$ e $5$, $11$ e $13$). L'analisi si concentra sulla "distanza tra le distanze", ovvero lo spazio che separa la fine di una coppia di gemelli dall'inizio della coppia successiva.

> [!IMPORTANT]
> 1. Il programma genera sequenze esclusive di coppie di numeri primi gemelli.
> 2. Calcola lo scarto numerico esistente tra la fine di una coppia e l'inizio di quella immediatamente successiva.
> 3. Traccia statisticamente la frequenza assoluta con cui ogni singola distanza si presenta all'interno della simulazione.

> [!NOTE]
> Sebbene si osservi sperimentalmente che la distanza tra le coppie tenda statisticamente a stabilizzarsi con picchi ricorrenti sul valore 6, questa affermazione non può essere assunta come regola assoluta per le distanze finali, poiché la verifica empirica richiederebbe di reperire coppie di primi gemelli all'infinito (legandosi alla celebre e ancora irrisolta congettura dei primi gemelli).

>
> [!TIP]
> Il programma implementa un sistema di analisi e visualizzazione grafica a doppio asse:
> 1. Generazione dinamica ed esclusiva delle coppie matematiche per evitare sovrapposizioni.
> 2. Calcolo in tempo reale delle frequenze di occorrenza di ogni scarto tramite un contatore statistico.
> 3. Rendering visivo con doppio asse Y per confrontare contemporaneamente la distanza effettiva di ogni punto e il numero di ripetizioni totali di quel valore.

Eseguendo la simulazione su un set di dati sufficientemente ampio, potrai notare visivamente come la distribuzione delle distanze non sia puramente caotica, ma tenda a concentrarsi attorno a valori multipli di 6.

Questo fenomeno riflette le proprietà intrinseche della distribuzione dei numeri primi nella progressione aritmetica: poiché tutti i numeri primi maggiori di 3 devono necessariamente essere della forma $6k \pm 1$, le dinamiche di spaziatura tra le coppie di gemelli risentono fortemente di questa rigidità strutturale di base della teoria dei numeri.

(Guardate solo il log da terminale. Non guardate il grafico, è orrendo.)
___
