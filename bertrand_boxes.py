import webview
import random
import json
import threading

# ==========================================
# LOGICA BACKEND (Python) - CORRETTA
# ==========================================
class Api:
    def sim_boxes(self):
        trials = 100000
        gg_other = ss_other = gold_drawn = silver_drawn = 0
        boxes = [['Oro', 'Oro'], ['Argento', 'Argento'], ['Oro', 'Argento']]
        for _ in range(trials):
            box = random.choice(boxes)
            coin = random.choice(box)
            if coin == 'Oro':
                gold_drawn += 1
                # Se ho tirato oro, l'altra è oro solo se la scatola è OO
                if box == ['Oro', 'Oro']: 
                    gg_other += 1
            else:
                silver_drawn += 1
                # Se ho tirato argento, l'altra è argento solo se la scatola è AA
                if box == ['Argento', 'Argento']: 
                    ss_other += 1
        return f"--- Scatole ({trials} prove) ---\nP(altra sia Oro | hai tirato Oro): {gg_other/gold_drawn:.2%}\nP(altra sia Argento | hai tirato Argento): {ss_other/silver_drawn:.2%}\n"

    def sim_cards(self):
        trials = 100000
        rr_other = ww_other = red_drawn = white_drawn = 0
        cards = [['Rosso', 'Rosso'], ['Rosso', 'Bianco'], ['Bianco', 'Bianco']]
        for _ in range(trials):
            card = random.choice(cards)
            face = random.choice(card)
            if face == 'Rosso':
                red_drawn += 1
                # Se vedo rosso, l'altra faccia è rossa solo se la carta è RR
                if card == ['Rosso', 'Rosso']: 
                    rr_other += 1
            else:
                white_drawn += 1
                # Se vedo bianco, l'altra faccia è bianca solo se la carta è BB
                if card == ['Bianco', 'Bianco']: 
                    ww_other += 1
        return f"--- Carte ({trials} prove) ---\nP(altra sia Rosso | vedi Rosso): {rr_other/red_drawn:.2%}\nP(altra sia Bianco | vedi Bianco): {ww_other/white_drawn:.2%}\n"

# ==========================================
# FRONTEND (HTML/CSS/JS + Anime.js)
# ==========================================
HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paradosso di Bertrand</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js"></script>
    <style>
        :root {
            --bg-dark: #2c3e50; --bg-darker: #1e272e; --bg-canvas: #34495e;
            --purple: #8e44ad; --orange: #d35400; --blue: #2980b9;
            --green: #2ecc71; --red: #e74c3c; --white: #ecf0f1;
            --silver: #bdc3c7; --gold: #f1c40f;
        }
        body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg-dark); color: white; overflow: hidden; height: 100vh; display: flex; flex-direction: column;}
        
        nav { background: var(--bg-darker); padding: 15px; display: flex; gap: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); z-index: 100;}
        .nav-btn { background: var(--purple); color: white; border: none; padding: 10px 20px; font-size: 16px; font-weight: bold; border-radius: 5px; cursor: pointer; transition: 0.3s; }
        .nav-btn.active { background: var(--blue); }
        .nav-btn:hover { opacity: 0.8; }

        .container { flex: 1; display: flex; flex-direction: column; align-items: center; padding: 20px; position: relative; }
        .screen { display: none; flex-direction: column; align-items: center; width: 100%; height: 100%; justify-content: center; }
        .screen.active { display: flex; }
        
        h2 { margin: 0 0 20px 0; }
        #instruction { font-size: 1.2em; margin-bottom: 30px; min-height: 30px; text-align: center; color: var(--gold); }

        .play-area { display: flex; justify-content: center; gap: 80px; margin-bottom: 40px; height: 200px; align-items: center; position: relative; }

        /* Scatole */
        .box-container { display: flex; flex-direction: column; align-items: center; cursor: pointer; }
        .box-lid { width: 100px; height: 15px; background: #9b59b6; border-radius: 5px 5px 0 0; transition: 0.3s; }
        .box-body { width: 90px; height: 90px; background: var(--purple); border-radius: 0 0 5px 5px; display: flex; justify-content: center; align-items: center; transition: 0.3s; position: relative; }
        .box-container.open .box-lid { background: var(--orange); transform: translateY(-20px) rotateZ(-15deg); }
        .box-container.open .box-body { background: var(--orange); }
        .coin { width: 50px; height: 50px; border-radius: 50%; display: none; justify-content: center; align-items: center; font-weight: bold; font-size: 20px; border: 3px solid white; box-shadow: inset 0 0 10px rgba(0,0,0,0.2); position: absolute; }
        .coin.gold { background: var(--gold); color: #7d6608; }
        .coin.silver { background: var(--silver); color: #7f8c8d; }

        /* Carte */
        .card { width: 100px; height: 150px; border-radius: 8px; border: 3px solid white; display: flex; flex-direction: column; justify-content: center; align-items: center; font-size: 24px; font-weight: bold; cursor: pointer; box-shadow: 0 10px 20px rgba(0,0,0,0.4); transition: background 0.3s;}
        .card.back { background: var(--blue); color: white; }
        .card.front-red { background: var(--red); color: white; }
        .card.front-white { background: white; color: black; border-color: #ccc; }
        .card.reveal { background: linear-gradient(to bottom, var(--red) 50%, white 50%); border-color: #ccc; }
        .card.reveal span { font-size: 20px; line-height: 150px; color: rgba(0,0,0,0.8); text-shadow: 0 0 5px white;}

        .guess-buttons { display: none; gap: 30px; margin-top: 20px; }
        .guess-btn { padding: 15px 30px; font-size: 18px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .guess-btn:hover { transform: translateY(-2px); }
        
        .terminal-container { width: 100%; background: var(--bg-darker); border-top: 2px solid var(--blue); padding: 10px; box-sizing: border-box; height: 150px; overflow-y: auto; }
        .terminal-container p { margin: 5px 0; font-family: 'Consolas', monospace; color: var(--green); font-size: 14px; }
    </style>
</head>
<body>

    <nav>
        <button class="nav-btn active" onclick="showScreen('boxes')">🎯 Scatole</button>
        <button class="nav-btn" onclick="showScreen('cards')">🃏 Carte</button>
    </nav>

    <div class="container">
        <div id="boxes-screen" class="screen active">
            <h2>Paradosso delle Tre Scatole</h2>
            <div id="instruction-boxes">Clicca su una scatola per estrarre una moneta.</div>
            <div class="play-area" id="boxes-area">
                <div class="box-container" onclick="clickBox(0)"><div class="box-lid"></div><div class="box-body"><div class="coin" id="coin-0-0"></div></div></div>
                <div class="box-container" onclick="clickBox(1)"><div class="box-lid"></div><div class="box-body"><div class="coin" id="coin-1-0"></div></div></div>
                <div class="box-container" onclick="clickBox(2)"><div class="box-lid"></div><div class="box-body"><div class="coin" id="coin-2-0"></div></div></div>
            </div>
            <div class="guess-buttons" id="guess-boxes">
                <button class="guess-btn" style="background:var(--gold); color:#7d6608;" onclick="guessBox('Oro')">È Oro</button>
                <button class="guess-btn" style="background:var(--silver); color:#7f8c8d;" onclick="guessBox('Argento')">È Argento</button>
            </div>
        </div>

        <div id="cards-screen" class="screen">
            <h2>Paradosso delle Tre Carte</h2>
            <div id="instruction-cards">Preparazione carte...</div>
            <div class="play-area" id="cards-area">
                <div class="card back" id="card-0" onclick="clickCard(0)">?</div>
                <div class="card back" id="card-1" onclick="clickCard(1)">?</div>
                <div class="card back" id="card-2" onclick="clickCard(2)">?</div>
            </div>
            <div class="guess-buttons" id="guess-cards">
                <button class="guess-btn" style="background:var(--red); color:white;" onclick="guessCard('Rosso')">È Rossa</button>
                <button class="guess-btn" style="background:white; color:black;" onclick="guessCard('Bianco')">È Bianca</button>
            </div>
        </div>
    </div>

    <div class="terminal-container" id="terminal"></div>

    <script>
        let isAnimating = false;
        let boxesData = [['Oro', 'Oro'], ['Argento', 'Argento'], ['Oro', 'Argento']];
        let cardsData = [
            {sides: ['Rosso', 'Rosso'], visible: 'Rosso'},
            {sides: ['Rosso', 'Bianco'], visible: 'Rosso'},
            {sides: ['Bianco', 'Bianco'], visible: 'Bianco'}
        ];
        let currentBoxClicked = -1;
        let currentCardClicked = -1;
        let drawnCoin = '';
        let simRun = {boxes: false, cards: false};

        function showScreen(type) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            
            if(type === 'boxes') {
                document.getElementById('boxes-screen').classList.add('active');
                document.querySelectorAll('.nav-btn')[0].classList.add('active');
                resetBoxes();
                runSim('boxes');
            } else {
                document.getElementById('cards-screen').classList.add('active');
                document.querySelectorAll('.nav-btn')[1].classList.add('active');
                resetCards();
                runSim('cards');
                setTimeout(startCardSequence, 500);
            }
        }

        function log(text) {
            const term = document.getElementById('terminal');
            term.innerHTML += `<p>${text}</p>`;
            term.scrollTop = term.scrollHeight;
        }

        function runSim(type) {
            if(!simRun[type]) {
                simRun[type] = true;
                const func = type === 'boxes' ? pywebview.api.sim_boxes : pywebview.api.sim_cards;
                func().then(res => log(res));
            }
        }

        // --- SCATOLE ---
        function resetBoxes() {
            isAnimating = false;
            currentBoxClicked = -1;
            document.getElementById('guess-boxes').style.display = 'none';
            document.getElementById('instruction-boxes').innerText = "Clicca su una scatola per estrarre una moneta.";
            document.getElementById('instruction-boxes').style.color = 'var(--gold)';
            
            const containers = document.querySelectorAll('.box-container');
            containers.forEach((cont, i) => {
                cont.style.display = 'flex';
                cont.classList.remove('open');
                cont.style.opacity = 1;
                cont.style.transform = '';
                const c1 = document.getElementById(`coin-${i}-0`);
                c1.style.display = 'none';
                c1.className = 'coin';
                c1.style.transform = '';
                const second = cont.querySelector('.second-coin');
                if(second) second.remove();
            });
        }

        function clickBox(index) {
            if(isAnimating) return;
            isAnimating = true;
            currentBoxClicked = index;
            const box = boxesData[index];
            
            drawnCoin = Math.random() < 0.5 ? box[0] : box[1];
            
            const cont = document.querySelectorAll('.box-container')[index];
            cont.classList.add('open');
            const coinEl = document.getElementById(`coin-${index}-0`);
            coinEl.classList.add(drawnCoin === 'Oro' ? 'gold' : 'silver');
            coinEl.innerText = drawnCoin === 'Oro' ? 'O' : 'A';
            
            anime({
                targets: coinEl,
                scale: [0, 1],
                duration: 500,
                easing: 'easeOutElastic(1, .5)',
                begin: () => coinEl.style.display = 'flex'
            });

            setTimeout(() => {
                const toRemoveIndex = drawnCoin === 'Oro' ? 1 : 0;
                const targetCont = document.querySelectorAll('.box-container')[toRemoveIndex];
                document.getElementById('instruction-boxes').innerText = `Hai estratto ${drawnCoin}. Rimuovo la scatola contraria...`;
                
                anime({
                    targets: targetCont,
                    translateY: -300,
                    opacity: 0,
                    duration: 800,
                    easing: 'easeInQuad',
                    complete: () => {
                        targetCont.style.display = 'none';
                        isAnimating = false;
                        document.getElementById('instruction-boxes').innerText = "Qual è l'altra moneta nella scatola scelta?";
                        document.getElementById('guess-boxes').style.display = 'flex';
                    }
                });
            }, 1000);
        }

        function guessBox(guess) {
            // Rimossa la guardia if(isAnimating) return; da qui
            document.getElementById('guess-boxes').style.display = 'none';
            isAnimating = true; // Lo attiviamo ora per bloccare il canvas
            
            const box = boxesData[currentBoxClicked];
            const otherCoin = box[0] === drawnCoin ? box[1] : box[0];
            const isCorrect = guess === otherCoin;
            
            const inst = document.getElementById('instruction-boxes');
            inst.innerText = isCorrect ? `Corretto! L'altra era ${otherCoin}.` : `Sbagliato! L'altra era ${otherCoin}.`;
            inst.style.color = isCorrect ? 'var(--green)' : 'var(--red)';
            log(`[Scatole] Tirato ${drawnCoin}, indovinato ${guess} -> ${otherCoin}`);

            const cont = document.querySelectorAll('.box-container')[currentBoxClicked];
            const newCoin = document.createElement('div');
            newCoin.className = `coin second-coin ${otherCoin === 'Oro' ? 'gold' : 'silver'}`;
            newCoin.innerText = otherCoin === 'Oro' ? 'O' : 'A';
            cont.querySelector('.box-body').appendChild(newCoin);
            
            anime({
                targets: newCoin,
                scale: [0, 1],
                translateX: [0, -40],
                duration: 500,
                easing: 'easeOutElastic(1, .5)'
            });

            setTimeout(resetBoxes, 3000);
        }

        // --- CARTE ---
        function resetCards() {
            isAnimating = false;
            currentCardClicked = -1;
            document.getElementById('guess-cards').style.display = 'none';
            document.getElementById('instruction-cards').innerText = "Preparazione carte...";
            document.getElementById('instruction-cards').style.color = 'var(--gold)';
            
            cardsData = [
                {sides: ['Rosso', 'Rosso'], visible: 'Rosso'},
                {sides: ['Rosso', 'Bianco'], visible: 'Rosso'},
                {sides: ['Bianco', 'Bianco'], visible: 'Bianco'}
            ];

            for(let i=0; i<3; i++) {
                const card = document.getElementById(`card-${i}`);
                card.className = 'card back';
                card.innerHTML = '?';
                card.style.display = 'flex';
                card.style.opacity = 1;
                card.style.transform = '';
            }
        }

        function startCardSequence() {
            isAnimating = true;
            document.getElementById('instruction-cards').innerText = "Ecco le tre carte (coperte)...";
            
            setTimeout(() => {
                document.getElementById('instruction-cards').innerText = "Le giro. Attenzione: due rosse e una bianca!";
                for(let i=0; i<3; i++) {
                    const card = document.getElementById(`card-${i}`);
                    const colorClass = cardsData[i].visible === 'Rosso' ? 'front-red' : 'front-white';
                    card.className = `card ${colorClass}`;
                    card.innerHTML = cardsData[i].visible[0];
                }
                setTimeout(shuffleCards, 2000);
            }, 1500);
        }

        function shuffleCards() {
            document.getElementById('instruction-cards').innerText = "Mescolo e ruoto le carte...";
            
            anime({
                targets: '.card',
                translateX: function() { return anime.random(-80, 80); },
                translateY: function() { return anime.random(-20, 20); },
                rotate: function() { return anime.random(-15, 15); },
                duration: 400,
                easing: 'easeInOutSine',
                complete: function(anim) {
                    anime({
                        targets: '.card',
                        translateX: 0,
                        translateY: 0,
                        rotate: 0,
                        duration: 600,
                        easing: 'easeOutQuad',
                        complete: removeMismatchCard
                    });
                }
            });
        }

        function removeMismatchCard() {
            document.getElementById('instruction-cards').innerText = "Rimuovo la carta con la faccia diversa (Bianca)...";
            const target = document.getElementById('card-2'); // La bianca
            
            anime({
                targets: target,
                translateY: -300,
                opacity: 0,
                duration: 800,
                easing: 'easeInQuad',
                complete: () => {
                    target.style.display = 'none';
                    isAnimating = false;
                    document.getElementById('instruction-cards').innerText = "Scegli una delle due carte rosse rimaste.";
                }
            });
        }

        function clickCard(index) {
            if(isAnimating || index === 2) return; 
            isAnimating = true;
            currentCardClicked = index;
            document.getElementById('instruction-cards').innerText = "Hai scelto questa. Quale colore ha la faccia nascosta?";
            document.getElementById('guess-cards').style.display = 'flex';
        }

        function guessCard(guess) {
            // Rimossa la guardia if(isAnimating) return; da qui
            document.getElementById('guess-cards').style.display = 'none';
            isAnimating = true; // Lo attiviamo ora per bloccare le altre carte
            
            const card = cardsData[currentCardClicked];
            const otherSide = card.sides[0] === card.visible ? card.sides[1] : card.sides[0];
            const isCorrect = guess === otherSide;
            
            const inst = document.getElementById('instruction-cards');
            inst.innerText = isCorrect ? `Corretto! Dietro c'era ${otherSide}.` : `Sbagliato! Dietro c'era ${otherSide}.`;
            inst.style.color = isCorrect ? 'var(--green)' : 'var(--red)';
            log(`[Carte] Visibile ${card.visible}, indovinato ${guess} -> ${otherSide}`);

            const cardEl = document.getElementById(`card-${currentCardClicked}`);
            anime({
                targets: cardEl,
                rotateY: 90,
                duration: 400,
                easing: 'easeInQuad',
                complete: () => {
                    cardEl.className = 'card reveal';
                    cardEl.innerHTML = `<span style="color:white; margin-top:35px">Rosso</span><span style="color:black; margin-bottom:35px">${otherSide === 'Rosso' ? 'Rosso' : 'Bianco'}</span>`;
                    anime({
                        targets: cardEl,
                        rotateY: 0,
                        duration: 400,
                        easing: 'easeOutQuad'
                    });
                }
            });

            setTimeout(resetCards, 3000);
        }
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Paradosso di Bertrand', html=HTML_FRONTEND, js_api=api, width=800, height=700, resizable=False)
    webview.start()