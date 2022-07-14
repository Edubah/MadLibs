# receber entradas do usuário, trabalhar com f-strings (strings com formatação)
# e ver seus resultados impressos no console.
# Supondo que eu queira criar a string que diga: Subscribe to ____
#
# youtuber = "Eduardo S." #Alguma variável string
#
# # Algumas maneiras de fazer isso
# print("Subscribe To " + youtuber)
# print("Subscribe To {}".format(youtuber))
# print(f"Subscribe To {youtuber}")

adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
famous_person = input("Pessoa famosa: ")
madlib = f"Programação computacional é tão {adj} e me deixa muito excitado todo tempo porque " \
f"eu amo {verb1}. Fique hidratado e {verb2} como o {famous_person}!"

print(madlib)