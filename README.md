# MATH RIDDLES & PARADOX

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

___
