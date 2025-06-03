def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase for case-insensitive comparison
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    total = 0
    for char in "true":
        count = combined_names.count(char)
        total += count

    # Count letters in "LOVE"
    love_count = sum(combined_names.count(char) for char in "love")

    # Combine counts to form the love score
    love_score = int(f"{total}{love_count}")

    print(f"Love Score = {love_score}")



def calculate_love_score2():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    # Names ke choto hater kore nilam
    name1 = name1.lower()
    name2 = name2.lower()

    # Duita name jog kore ekta string banalam
    combined = name1 + name2

    # TRUE letter gulor count
    t = combined.count('t')
    r = combined.count('r')
    u = combined.count('u')
    e = combined.count('e')

    true_total = t + r + u + e

    # LOVE letter gulor count
    l = combined.count('l')
    o = combined.count('o')
    v = combined.count('v')
    e = combined.count('e')  # abar e, karon 'e' both side a ase

    love_total = l + o + v + e

    # 2 digit score ber korlam
    love_score = int(str(true_total) + str(love_total))

    print("Love Score =", love_score)

calculate_love_score("Jia" , "Luke")