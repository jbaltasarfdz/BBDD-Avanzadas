from xml.dom import minidom

documento = minidom.parse('XML\CategoriasFiltradoFinal.xml')

elementos = documento.getElementsByTagName('maincat')

contadorBusiness = 0
contadorCars = 0
contadorComputer = 0
contadorEntertainment = 0

for elem in elementos:
    if(elem.firstChild.data == 'Business & Finance'):
        contadorBusiness = contadorBusiness + 1
    if(elem.firstChild.data == 'Cars & Transportation'):
        contadorCars = contadorCars + 1
    if(elem.firstChild.data == 'Computers & Internet'):
        contadorComputer = contadorComputer + 1
    if(elem.firstChild.data == 'Entertainment & Music'):
        contadorEntertainment = contadorEntertainment + 1

print ("el numero de preguntas de Business & Finance es: ", contadorBusiness)
print ("el numero de preguntas de Cars & Transportation es: ", contadorCars)
print ("el numero de preguntas de Computers & Internet es: ", contadorComputer)
print ("el numero de preguntas de Entertainment & Music es: ", contadorEntertainment)