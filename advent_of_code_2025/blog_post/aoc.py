def solve(page):
    total = 0
    rules = {} 
    parsing_rules = True # the start of the page contains the rules
    for line in page.splitlines():                                          

        if line == "":
            parsing_rules = False
            continue # skip the whiteline

        if parsing_rules:
            x, y = line.split("|")
            rules[x] = rules.get(x, []) + [y]

        else: 
            update = line.split(",")
            valid_update = True
            for i in range(len(update)):
                for j in range(i + 1, len(update)):
                    if update[j] not in rules.get(update[i]):
                        valid_update = False

            if valid_update:
                total += int(update[len(update) // 2])                     
    return total

