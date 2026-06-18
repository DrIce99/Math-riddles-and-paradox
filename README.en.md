## ENG

> [!NOTE]
> 🇮🇹 **Versione Italiana Disponibile**: [Leggi la versione in italiano](./README.md).

A small personal repository where I try to uncover the logical meanings behind:
- apparent random sequences
- seemingly magical optimizations

___

### Programs:

#### *The 100 Prisoners Problem*

There are 100 prisoners numbered from 1 to 100. A guard decides to offer them a chance to be released from prison, but only under specific conditions. They are subjected to the following situation:

> [!IMPORTANT]
> 1. In a room, there are 100 boxes, each containing a random number from 1 to 100.
> 2. Each prisoner must enter the room and open up to 50 boxes to find the number corresponding to their own.
> 3. If all 100 prisoners find their own number, they are all set free. If even a single prisoner fails, everyone is executed. They cannot communicate with each other once the challenge begins.

> [!NOTE]
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

#### *The Birthday Paradox*

The birthday paradox demonstrates how counterintuitive probability can be when applied to large numbers. It is based on the question: how many people must be in a room for there to be at least a 50% chance that two of them share the same birthday?

> [!IMPORTANT]
> 1. We assume a 365-day year (ignoring leap years).
> 2. We assume that every day of the year has an equal probability of being a birthday.
> 3. The goal is to calculate the probability of a collision (two people sharing a birthday) as the number of people $n$ varies.
> 
> 

> [!NOTE]
> Intuition suggests you would need many people (often thinking of 183, half the year). In reality, the 50% threshold is crossed with just **23 people**.

> [!TIP]
> The program implements an interactive interface that allows you to explore the paradox in real-time:
> 1. **Dynamic Slider**: Allows you to change the number of people without restarting the simulation.
> 2. **Visual Calendar**: A 12-month viewer displays the generated dates, clearly highlighting (via a heatmap) the days where collisions occur.
> 3. **Statistical Calculation**: Runs thousands of iterations to show the convergence of the probability toward the theoretical result.
> 
> 

By running the simulation, you will see how the number of "pairs" grows exponentially as the number of participants increases. The graphic visualization transforms the abstract data into a color-coded map where "birthday clusters" become immediately visible, making it clear why the probability of a collision is much higher than it seems.


___

#### *The Monty Hall Paradox*

The Monty Hall paradox is a famous probability puzzle based on the American television game show *Let's Make a Deal*. The game relies on a seemingly simple choice that defies our everyday intuition:

> [!IMPORTANT]
> 1. The contestant is shown three closed doors: behind one is a car (the prize), and behind the other two are goats.
> 2. The contestant picks a door, which initially remains closed.
> 3. The host (Monty Hall), who knows what is behind each door, opens one of the other two doors, always revealing a goat.
> 4. At this point, the host offers the contestant the chance to switch their original choice to the remaining closed door.

> [!NOTE]
> Common intuition suggests that, with only two doors left, the chances of winning the car are 50/50 regardless of the choice, making switching doors completely irrelevant.

> [!TIP]
> The program runs a large-scale statistical simulation to demonstrate the effectiveness of the switching strategy:
> 1. It randomly generates the prize location and the player's initial choice.
> 2. It simulates the host's behavior of discarding a losing door.
> 3. It mathematically calculates and displays the total winning percentage when consistently applying the strategy of switching doors.

By running the simulation, you will notice that the probability of winning by switching is not 50%, but roughly 66.6% (2/3)!

This happens because the player's initial choice has a 1 in 3 chance of being correct and a 2 in 3 chance of being wrong (meaning they chose a goat). If the player picked a goat initially, the host is forced to reveal the other remaining goat. Consequently, the last remaining door will *always* contain the car. By always switching doors, every initial mistake is turned into a victory, effectively doubling the chances of success.

___

#### *Penney's Game*

Two players compete by flipping a fair coin. Each player chooses a sequence of three outcomes (Heads or Tails). The coin is flipped repeatedly until one of the two sequences appears.

> [!IMPORTANT]
> 1. Player 1 chooses a sequence of 3 flips (e.g., H-H-H).
> 2. Player 2, knowing Player 1's choice, selects a different sequence of 3 flips (e.g., T-H-H).
> 3. The coin is flipped repeatedly. The player whose sequence appears first in the series of flips wins the game.

> [!NOTE]
> Since the coin is fair and the sequences have the same length, intuition suggests the game is perfectly balanced. One would expect each player to have exactly a 50% chance of winning.

> [!TIP]
> The program implements the optimal strategy for Player 2 (based on Conway's algorithm):
> 1. Player 1 chooses a sequence A-B-C.
> 2. Player 2 chooses as the first element the opposite of Player 1's second element (not-B).
> 3. As the second and third elements, Player 2 copies the first two elements chosen by Player 1 (A-B).
> 4. Player 2's final sequence will therefore be: not-B - A - B.

Running the simulation, you'll notice that the game is not balanced at all: Player 2 wins about 66% - 75% of the time, depending on Player 1's initial choice!

This happens because Penney's Game is a *non-transitive* game. Player 2's strategy is designed to create an unfavorable mathematical "overlap." For example, if Player 1 chooses H-H-H and Player 2 chooses T-H-H, the only way Player 1 can win is if the first three coins all come up Heads. If even a single Tail appears early on, the H-H-H sequence is "broken," but the T-H-H sequence is still alive and will prevail as soon as two consecutive Heads appear. Player 2 always has a guaranteed mathematical advantage, regardless of what Player 1 chooses.

___

#### *Distance Between Twin Primes*

Twin primes are pairs of prime numbers that differ by exactly 2 (such as $3$ and $5$, $11$ and $13$). This analysis focuses on the "distance between distances"—the gap separating the end of one twin prime pair from the beginning of the next pair.

> [!IMPORTANT]
> 1. The program generates exclusive sequences of twin prime pairs.
> 2. It calculates the numerical gap between the end of one pair and the beginning of the immediately following one.
> 3. It statistically tracks the absolute frequency with which each individual distance appears within the simulation.

> [!NOTE]
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

The Collatz conjecture, also known as the $3n + 1$ problem, is one of the most famous unsolved problems in mathematics. It applies to any positive integer $n$ and follows a very simple transformation rule:

> [!IMPORTANT]
> 1. If the number is even, divide it by 2 ($n / 2$).
> 2. If the number is odd, multiply it by 3 and add 1 ($3n + 1$).
> 3. Repeat the process with the resulting value.

> [!NOTE]
> The conjecture states that regardless of which starting number is chosen, the sequence will always reach the $4 \to 2 \to 1$ cycle. Despite the simplicity of the rule, no one has yet managed to mathematically prove that this happens for *every* existing number.

> [!TIP]
> The program implements a dynamic graphical visualizer that allows exploring the tree-like structure of the conjecture:
> 1. Planar visualization that avoids overlapping branches for a clear reading of the graph.
> 2. Implementation of an "infinite" navigation with Pan & Zoom support.
> 3. Global statistical analysis comparing the number of steps required to reach the cycle and the discovery of new nodes in the graph.

By running the simulation, you can observe how numbers naturally converge toward the central cycle. The structure expands like an inverted binary tree, where each number acts as a "root" for its predecessors, revealing a deep and geometrically elegant order behind what initially appears to be a chaotic computation.
