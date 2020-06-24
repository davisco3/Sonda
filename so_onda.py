D = 90
E = 90

movimento = ""
grau_atual = 0
posicao = ""
posicao_atual_y = 0
posicao_atual_x = 0



while movimento != "exit": 
  
  movimento = input ("digite a direcao: ")
  if (movimento.upper() == "E"):
    if (grau_atual == 0):
      grau_atual = 360
    grau_atual = grau_atual - E 
   
  elif(movimento.upper() == "D"):
    grau_atual = grau_atual + D
  elif(movimento.upper() == "F"):
      print(grau_atual)
      if (grau_atual == 0):
          posicao_atual_y += 1
      elif (grau_atual == 180):
          posicao_atual_y -= 1
      elif (grau_atual == 90):
          posicao_atual_x += 1
      elif (grau_atual == 270):
          posicao_atual_x -= 1

    

  print(grau_atual)
  if grau_atual == 360:
       grau_atual = 0
  print (posicao_atual_x)
  print (posicao_atual_y)