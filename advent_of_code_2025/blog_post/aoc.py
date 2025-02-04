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
            for i in range(len(update)):
                for j in range(i + 1, len(update)):
                    if update[j] not in rules.get(update[i]):
                        break  # break inner loop when invalid pair found
                else:
                    continue  # if inner loop completed without break, continue outer loop
                break  # if inner loop broke, break outer loop too
            else:
                # if outer loop completed without break, update is valid
                total += int(update[len(update) // 2])
    return total
