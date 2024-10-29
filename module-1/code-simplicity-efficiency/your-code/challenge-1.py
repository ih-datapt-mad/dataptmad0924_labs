"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""


def word_to_number(word):
    """Convert a number in words to its integer value."""          #definimos una funcion que lo primero que hace es convertir el srting que entra en un int 
    words = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5} #definimos un diccionario con las keys iguales al lo que queremos y que tenga el valor correspondiente 
    return words.get(word)                                                #pedimos que nos devuelva lo que contenga la clave del dicionario 


def calculate(num1, operator, num2):                                     #ahora hacemos otra funcion para hacer las operaciones ya teniendo encuenta que tendriamos los valores como int
    """Perform the calculation based on the operator."""
    if operator == 'plus':                                                #tenemos dos condiciones si suma o resta. definimos que si es plus sume y si es minus reste 
        return num1 + num2
    elif operator == 'minus':
        return num1 - num2
    else:
        pass                                                               
       
    
print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')                  #pedimos que el usuario ingrese lo que quiere
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')


num1 = word_to_number(a)                                                     #usamos la funcion para convertir los que el srting en numeros 
num2 = word_to_number(c)

if num1 is None:                                                             
    print("the first number is not valid")                                #indicamos en cada caso que si no esta dentro de los parametro establecidos de de un error
if num2 is  None:
    print("the second number is not valid") 
if b not in ["plus","minus"]:
    print("the operator not valid")   


result = calculate(num1, b, num2)                                        #llamamos a la funcion y pasamos los parametros si esta todo correcto deberia funcionar 

print("the answer",result,"¡¡¡")


print("Thanks for using this calculator, goodbye :)")
