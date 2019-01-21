

trabalho_terca = True


trabalho_quinta = True


if trabalho_terca and trabalho_quinta:
    print("Vai ao shopping")
    print("Compra TV 50º")
    print("Família toma SORVETE\n")

if trabalho_terca or trabalho_quinta:
    print("Vai ao shopping")
    print("Compra TV 32")
    print("Família toma SORVETE\n\n")

if not trabalho_terca and not trabalho_quinta:
    print("Família SAUDÁVEL")

##########

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #XOR, ou exclusivo
mais_saudavel = not sorvete

print("TV50-{} TV32-{} Sorvete-{} Saudavel-{}". format(tv_50, tv_32, sorvete, mais_saudavel))