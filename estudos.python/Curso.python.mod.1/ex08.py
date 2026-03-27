#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros .
medida = float(input('Qual é a medida em metros: '))
km = medida /1000
hm = medida /100
dam = medida /10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida {medida}m correnponde a {km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')
