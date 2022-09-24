## Programme du 22/09/2022
## Dernière modification le 24/09/2022

# Pendu
letter = "A - O - M - N"

step0 = f"""
      
      
      
      
     
     {letter}
"""

step1 = f"""   
      
      
      
      
     ________
     {letter}
     """

step2 = f"""
      
      |
      |
      |
      |
     _|_______
     {letter}
     """
     
step3 = f"""
      _______
      |
      |
      |
      |
     _|_______
     {letter}
"""

step4 = f"""
      _______
      |/    |
      |
      |
      |
     _|_______
     {letter}
"""

step5 = f"""
      _______
      |/    |
      |     O
      |
      |
     _|_______
     {letter}
"""

step6 = f"""
      _______
      |/    |
      |     O
      |     |
      |
     _|_______
     {letter}
"""

step7 = f"""
      _______
      |/    |
      |     O
      |    /|\\
      |
     _|_______
     {letter}
"""

step8 = f"""
      _______
      |/    |
      |     O
      |    /|\\
      |    / \\
     _|_______
     {letter}
"""
err = 9 #Testing
print(step4)

if err == 0:
    print(step0)
elif err == 1:
    print(step1)
elif err == 2:
    print(step2)
elif err == 3:
    print(step3)
elif err == 4:
    print(step4)
elif err == 5:
    print(step5)
elif err == 6:
    print(step6)
elif err == 7:
    print(step7)
elif err == 8:
    print(step8)