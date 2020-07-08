import csv
D = 90
E = 90

movimentos = ""
grau_atual = 0
posicao = ""
posicao_atual_y = 0
posicao_atual_x = 0


with open ("so_onda.csv", "w", newline="") as csv_file:
  csv_reader = csv.writer(csv_file)
  csv_reader.writerow(
    ["movimento", "grau_atual", "posicao_atual_y", "posicao_atual_x"])
  print(csv_reader) 

  nao_eh_um_exit = True
  while nao_eh_um_exit:
      movimentos = input ("digite a direcao: ")
      nao_eh_um_exit = movimentos.upper () != "EXIT" 
      if nao_eh_um_exit:
        for movimento in movimentos:

          if (movimento.upper() == "E"):
            if (grau_atual == 0):
                grau_atual = 360
                grau_atual = grau_atual - E 
          
          elif(movimento.upper() == "D"):
            grau_atual = grau_atual + D
          elif(movimento.upper() == "F"):
              
              if (grau_atual == 0):
                  posicao_atual_y += 1
              elif (grau_atual == 180):
                  posicao_atual_y -= 1
              elif (grau_atual == 90):
                  posicao_atual_x += 1
              elif (grau_atual == 270):
                  posicao_atual_x -= 1

        csv_reader.writerow([movimento, grau_atual, posicao_atual_y, posicao_atual_x]) 

  print(grau_atual)
  if grau_atual == 360:
      grau_atual = 0
  print (posicao_atual_x)
  print (posicao_atual_y)