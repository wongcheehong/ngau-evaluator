# ngau-evaluator
A program to evaluate your ngau(Card game played in Malaysia) ranking

The "Ox values" of the cards are as follows:<br>
Ace = 1<br>
2,4,5,7,8,9 = respective face values<br>
10,J,Q,K = 10<br>
3 = 3 or 6<br>
6 = 3 or 6<br>

Ranking of Oxen<br>
Here shows the ranking of oxen from lowest to highest:<br>
No Ox: Player is unable to form an Ox, that is no 3 cards sums up to multiple of 10.<br>
Ordinary Ox: ranked by the sum of the other 2 cards (if the sum is greater than 10, take the remainder after subtraction of 10)<br>
Double Ox: if the other 2 cards are equal in face values (not Ox values). ranked by the face value of the double.<br>
Ngau Tonku: if the other 2 cards having Ace spade & picture (J,Q,K). If the Ace is others, that is called nenku and only count as 1.<br>
Five Dukes: if all five cards have values 10.<br>

Example:<br>
Cards in hand: 3,6,8,4,8<br>

3(counted as 6) + 6 + 8 = 20, 4 + 8 = 2 (take remainder)<br>
3 + 6(counted as 3) + 4 = 10, 8 + 8 = Double-Ox Eight<br>
8 + 4 + 8 = 20, 3 + 6 = 9<br>

If one gets cards with face values 6,4,J,9,9 It's a Double-9 Ox.<br>
If one gets cards with face values 10,J,Q,Q,K It's a Five Dukes.<br>

PLease see wikipedia for more detail<br>
https://en.wikipedia.org/wiki/Gnau
