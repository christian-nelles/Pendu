import random
import os

l = ["abaisse", "abandon", "abandonner", "abimer", "abonné", "abord", "aborder", "abri", "abstrait", "accepter", "accident", "acier", "addition", "adieu"]
b = random.choice(l)
d = "_" * len(b)
c = 10
a = None
l = []
print(d)
while c != 0:
    if d == b:
        print("c gagné")
        break
    else:
        a = input("met un truc : ").lower()
        l.append(a)
        if a == b:
            d == b
        for i in range (len(b)):
            if a == b[i]:
                d = d[:i] + a + d[i+1:]
            else:
                continue 
        if a not in b:
            c -= 1
        if c == 10:
            p = f"""





        =========   {l}"""
        if c == 9:
            p = f"""

          |
          |
          |
          |
        =========   {l}"""
        if c == 8:
            p = f"""
          ______
          |
          |
          |
          |
        =========   {l}"""
        if c == 7:
            p = f"""
          ______
          |    | 
          |
          |
          | 
        =========   {l}"""
        if c == 6:
            p = f"""
          ______
          |    | 
          |    O 
          |
          |
        =========   {l}"""
        if c == 5:
            p = f"""
          ______
          |    | 
          |    O 
          |    |
          |
        =========   {l}"""
        if c == 4:
            p = f"""
          ______
          |    | 
          |    O 
          |   /|
          |
        =========   {l}"""
        if c == 3:
            p = f"""
          ______
          |    | 
          |    O 
          |   /|\ 
          | 
        =========   {l}"""
        if c == 2:
            p = f"""
          ______
          |    | 
          |    O 
          |   /|\ 
          |   /
        =========   {l}"""
        if c == 1:
            p = f"""
          ______
          |    | 
          |    O 
          |   /|\ 
          |   / \ 
        =========   {l}"""
        os.system('cls')
        print(f"""{d} 
{p}""")
if c == 0:
    print(f"le mot était {b}")

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mots.txt'), 'a') as file:
        file.write(f"mots: {b}\n\n")