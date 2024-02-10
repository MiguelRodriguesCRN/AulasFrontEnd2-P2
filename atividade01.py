homens = 0
mulheres = 0
altura_homens = []
altura_mulheres = []

for i in range(3):
    sexo = input("Digite seu sexo com M e F:")
    if(sexo == "F"):
        mulheres = mulheres + 1
        altura_mulheres = int(input('Digite sua altura:'))
    else:
        homens = homens + 1
        altura_homens = int(input('Digite sua altura:'))

media_homens = altura_homens / homens
altura_de_todos = altura_homens + altura_mulheres
maior = max(altura_de_todos)
min = min(altura_de_todos)

print(f'A media de altura dos hommens é de: {media_homens}')
print(f'A maior altura é {maior} e a menor {min}')
print(f'O total de mulhetes é de {mulheres}')