with open('data/4.txt') as f:
    cards = f.read().split('\n')

total = 0
for card in cards:
    card = card.split(': ')[1]
    win, have = card.split(' | ')
    win = win.split()
    have = have.split()

    cards_win = len([x for x in have if x in win])
    if cards_win:
        total += 2 ** (cards_win-1)

print(total)
