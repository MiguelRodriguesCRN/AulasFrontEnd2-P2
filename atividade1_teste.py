# UNIESP - CENTRO UNIVERSITARIO
# ALUNO: MIGUEL RODRIGUES CARNEIRO
# ATIVIDADE 1 - REQUISTOS DO SISTEMA: MAIOR E MENOR ALTURA, MÉDIA DE ALTURA DE PESSOAS DO SEXO MASCULINO E QUANTIDADE DE PESSOAS DO SEXO FEMININO

#QUANTIDADE DE PESSOAS DO SEXO F E M!!
pessoas_m = (8)
pessoas_f = (7)
pessoas_total = pessoas_f + pessoas_m

#DADOS DAS PESSOAS DO SEXO M
sexoM = ["M", "M", "M", "M", "M", "M", "M", "M"]
alturaM = [1.85,1.75, 1.76, 1.99, 1.22, 1.65, 1.75, 2.00]

#ALTURA DE TODAS AS PESSOAS
alturadetodos = [1.85,1.75, 1.76, 1.99, 1.22, 1.65, 1.75, 2.00, 1.83,1.33, 1.44, 1.39, 1.28, 1.34, 2.11]

#MEDIA DAS PESSOAS DO SEXO MASCILUNO
media_altura_m = sum(alturaM)/8

#DADOS DAS PESSOAS DO SEXO F
sexoF = ["F", "F", "F", "F", "F","F", "F"]
alturaF = [1.83,1.33, 1.44, 1.39, 1.28, 1.34, 2.10]

#CALCULO DE MAIOR ALTURA E MENOR
alturamaior = max(alturadetodos)
alturamenor = min(alturadetodos)


#RESULTADOS DAS QUESTOES!!!!
print(f'A quantidade de pessoas que responderam o questionario foram de: {pessoas_total}')
print(f'A maior altura é de {alturamaior}, | e a altura menor é e {alturamenor}!!')
print(f'A media de altura das pessoas do sexo masculino é de: {media_altura_m}!!!')
print(f'A quantidade de pessoas do sexo Feminino é de: {pessoas_f}!!!')
