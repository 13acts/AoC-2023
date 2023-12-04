digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('data/1.txt') as f:
    lines = f.read().split('\n')

sum = 0
for line in lines:
    found_first = found_last = False

    for j in range(len(line)):
        if line[j].isdigit() and not found_first:
            a = line[j]
            found_first = True
            break 
        
        for i, digit in enumerate(digits):
            if line[j:j+len(digit)] in digits and not found_first:
                a = str(digits.index(line[j:j+len(digit)]) + 1)
                found_first = True
                break
    
    try:
        for k in range(len(line)-1, -1, -1):
            if line[k].isdigit() and not found_last:
                b = line[k]
                found_last = True
                break

            for i, digit in enumerate(digits):
                if line[k:k+len(digit)] in digits and not found_last:
                    b = str(digits.index(line[k:k+len(digit)]) + 1)
                    found_last = True
                    break
    except IndexError:
        pass

    sum += int(a+b)

print(sum)