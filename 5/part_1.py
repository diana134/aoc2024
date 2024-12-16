page_order_rules = {}  # "1": ["stuff that comes after 1"]
sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        if line == "\n":
            break

        # process page order rules
        line = line.strip()
        tokens = line.split("|")

        if tokens[0] in page_order_rules.keys():
            page_order_rules[tokens[0]].append(tokens[1])
        else:
            page_order_rules[tokens[0]] = [tokens[1]]

    # process updates
    for line in file:
        line = line.strip()
        tokens = line.split(",")

        valid = True
        for i, page in enumerate(tokens):
            if tokens[i] in page_order_rules.keys() and \
                any(x in page_order_rules[tokens[i]] for x in tokens[:i]):
                # rule was violated
                valid = False
                break

        if valid:
            sum += int(tokens[int(len(tokens) / 2)])

print(sum)