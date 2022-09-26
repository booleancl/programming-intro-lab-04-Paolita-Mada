print("Bienvenidos a los Signos del Zodiaco")

def menu():
  print("Ingresa tu opción zodiacal")
  print("1","Aries")
  print("2","Tauro")
  print("3","Geminis")
  print("4", "Cancer")
  print("5", "Leo")
  print("6", "Virgo")
  print("7", "Libra")
  print("8", "Escorpio")
  print("9", "Sagitario")
  print("10", "Capricornio")
  print("11", "Acuario")
  print("12", "Piscis")
  print("exit", "Para salir")

def read_file(signo):
   file = open('signo,"r"')
   for line in file:
     print(line)
user_input = ""
while user_input != "exit":
   menu()
   user_input = input()
   if user_input == "1":
      read_file("Aries.txt")
   elif user_input == "2":
      read_file("Tauro.txt")
   elif user_input == "3":
      read_file("Geminis.txt")
   elif user_input == "4":
      read_file("Cancer.txt")
   elif user_input == "5":
      read_file("Leo.txt")
   elif user_input == "6":
      read_file("Virgo.txt")
   elif user_input == "7":
      read_file("Libra.txt") 
   elif user_input == "8":
      read_file("Escorpio.txt")
   elif user_input == "9":
      read_file("Sagitario.txt")
   elif user_input == "10":
      read_file("Capricornio.txt")
   elif user_input == "11":
      read_file("Acuario.txt")
   elif user_input == "12":
      read_file("Piscis.txt")

   elif user_input == "exit":
      print("Hasta la proxima")
      exit()
   else:
      print("opción incorrecta")