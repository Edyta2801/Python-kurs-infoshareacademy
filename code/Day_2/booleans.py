# bool

print(True)
print(False)

print(True and True)
print(True or False)
print(True and False)

# mozemy zaprzeczac
print(not True)

print(5 > 4)

# mozna laczyc operatory
print(3 < 2 and not 4 == 3 or 2 != 0)

# a tu chcemy aby kursor nie zszedl nizej
# pamietamy o spacji po dwukropku, bo Python zrobi dokladnie to co mu powiedzielismy

# ze spacją
print("skomplikowane: ", end='')
print(3 < 2 and not 4 == 3 or 2 != 0)

# vs bez spacji
print("skomplikowane:", end='')
print(3 < 2 and not 4 == 3 or 2 != 0)

# po prostu pusta linia
print()

# jak w arytmetyce mozemy uzywac nawiasow
print("skomplikowane z nawiasami: ", end='')
print(3 < 2 and not (4 == 3 or 2 != 0))

# mozemy wstawic znak nowej lini na poczatku, albo na srodku, gdzie chcemy
print("\nints")
print("\ni\nn\nt\ns\n")

# mamy float
x = 23.00

# ale jest on integerem
print(x.is_integer())
