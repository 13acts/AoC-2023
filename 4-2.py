with open('data/4.txt') as f:
    cards = f.read().split('\n')

card_count = {k: 1 for k in range(len(cards))}

for i, card in enumerate(cards):
    card = card.split(': ')[1]
    win, have = card.split(' | ')
    win = win.split()
    have = have.split()

    cards_win = len([x for x in have if x in win])
    if cards_win:
        for x in range(i+1, i+1+cards_win):
            card_count[x] += card_count[i]

print(sum(card_count.values()))
