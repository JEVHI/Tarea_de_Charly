"""
    Jesús Emanuel Verástegui Hernández
    2630324
    IM 1-1
"""
"""
    RESUMEN EJECUTIVO
        Las colecciones en Python permiten almacenar y organizar conjuntos de datos. Una 
        lista es una colección ordenada y mutable que permite modificar, agregar o eliminar 
        elementos dinámicamente. Una tupla es ordenada pero inmutable, ideal para datos 
        fijos que no deben alterarse a lo largo de la ejecución. Un diccionario almacena 
        pares clave-valor, facilitando la búsqueda rápida de información mediante una clave 
        única.

        Este documento abarca la implementación de seis problemas prácticos utilizando 
        colecciones: operaciones básicas con listas de compras, representación de coordenadas 
        y distancias con tuplas, administración de catálogos de productos con diccionarios, 
        gestión de calificaciones mediante un diccionario de listas, conteo de frecuencias 
        de palabras y la creación de una agenda de contactos con operaciones CRUD. Cada 
        problema detalla sus entradas, salidas, validaciones rigurosas y casos de prueba.
"""
"""
    PRINCIPIOS Y BUENAS PRÁCTICAS
        - Utilizar listas cuando se requiera modificar el tamaño o contenido de la colección con frecuencia.
        - Utilizar tuplas para agrupar datos relacionados que deben permanecer inmutables (ej. coordenadas 2D).
        - Utilizar diccionarios para búsquedas eficientes basadas en claves únicas descriptivas.
        - Evitar modificar la estructura de una lista mientras se itera sobre ella.
        - Validar siempre la existencia de claves en un diccionario antes de acceder directamente o utilizar el método .get().
        - Diseñar validaciones previas para evitar errores de índice fuera de rango o el procesamiento de datos vacíos.
"""

# PROBLEM 1: Shopping list basics (list operations)
"""
Crea una lista inicial de productos a partir de un texto separado por comas, 
agrega un nuevo elemento a la lista, calcula el número total de elementos 
y verifica si un producto específico existe en la lista.

Inputs:
- initial_items_text (string; ej. "apple,banana,orange")
- new_item (string; producto a agregar)
- search_item (string; producto a buscar)

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- Verificar que initial_items_text no esté vacío después de aplicar strip().
- Separar la cadena por comas y eliminar espacios extra de cada elemento.
- Verificar que new_item y search_item no estén vacíos después de aplicar strip().

Test cases:
1) Normal: initial_items_text = "apple, banana, orange", new_item = "grape", search_item = "banana"
   -> Items list: ['apple', 'banana', 'orange', 'grape'], Total items: 4, Found item: true
2) Borde: initial_items_text = "apple", new_item = "apple", search_item = "orange"
   -> Items list: ['apple', 'apple'], Total items: 2, Found item: false
3) Error: initial_items_text = "   ", new_item = "grape", search_item = "banana"
   -> Error: invalid input
"""

items_list_text = input('\nProblem 1. Lista de productos: ')
new_item = input('Pruducto nuevo: ')
serch_item = input('Buscar producto: ')

if not items_list_text.strip() or not new_item.strip() or not serch_item.strip():
    print('Error: invalid input')
else:
    items_list = [item.strip() for item in items_list_text.split(",") if item.strip()]
    if not items_list:
        print("Error: invalid input")
    else:
        new_item = new_item.strip()
        search_item = serch_item.strip()
        
        items_list.append(new_item)
        len_list = len(items_list)
        is_in_list = search_item in items_list
        
        print(f'Items list: {items_list}, Total items: {len_list}, Found item: {str(is_in_list).lower()}')

# PROBLEM 2: Points and distances with tuples
"""
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). 
Calcula la distancia euclidiana entre ellos y construye una nueva tupla 
que representa el punto medio.

Inputs:
- x1, y1, x2, y2 (float; coordenadas de los puntos)

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validations:
- Verificar que las 4 coordenadas ingresadas se puedan convertir a float.

Test cases:
1) Normal: x1 = 0.0, y1 = 0.0, x2 = 3.0, y2 = 4.0
   -> Point A: (0.0, 0.0), Point B: (3.0, 4.0), Distance: 5.0, Midpoint: (1.5, 2.0)
2) Borde: x1 = 2.5, y1 = 2.5, x2 = 2.5, y2 = 2.5
   -> Point A: (2.5, 2.5), Point B: (2.5, 2.5), Distance: 0.0, Midpoint: (2.5, 2.5)
3) Error: x1 = "abc", y1 = 0.0, x2 = 3.0, y2 = 4.0
   -> Error: invalid input
"""
x1 = input('\nProblem 2. x1 = ').strip
y1 = input('\t\t   y1 = ').strip
x2 = input('\t\t   x2 = ').strip
y2 = input('\t\t   y2 = ').strip
point_A = (x1, y1)
point_B = (x2, y2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2)/2, (y1 + y2)/2)

if not float(x1) or not float(y1) or not float(x2) or not float(y2):
    print('Error: invalid input')
else:
    print(f'Pont A: {point_A}, Point B: {point_B}, Distance: {distance}, Midpoint: {midpoint}')

# PROBLEM 3: Product catalog with dictionary
"""
Administra un catálogo de productos usando un diccionario que asocia los nombres 
de los productos con sus precios unitarios. Calcula el costo total en función del 
producto solicitado y la cantidad, si este existe.

Inputs:
- product_name (string)
- quantity (int; cantidad a comprar)

Outputs:
- Si el producto existe:
  "Unit price:" <unit_price>
  "Quantity:" <quantity>
  "Total:" <total_price>
- Si el producto no existe o la entrada es inválida:
  "Error: product not found" o "Error: invalid input"

Validations:
- quantity > 0 y debe ser un entero.
- product_name no debe estar vacío después de aplicar strip().
- Verificar que product_name exista como clave en product_prices.

Test cases:
1) Normal: product_name = "apple", quantity = 3
   -> Unit price: 10.0, Quantity: 3, Total: 30.0
2) Borde: product_name = "banana", quantity = 1
   -> Unit price: 5.5, Quantity: 1, Total: 5.5
3) Error: product_name = "laptop", quantity = 2
   -> Error: product not found
"""

product_price = {'milk':25.0, 'chocolate':20.0, 'rice':22.0}
product_name = input('\nProblem 3. Nombre del producto: ').strip().lower()
quantity = int(input('\t\t   Cantidad:'))

if not product_name or quantity<=0:
    print('Error: invalid input')
elif not product_name in product_price:
    print('Error: product not found')
else:
    unit_price = product_name[product_price]
    print(f'Unit price: {unit_price}, Quantity: {quantity}, Toatal: {unit_price*quantity}')

# PROBLEM 4: Student grades with dict and list
"""
Administra el rendimiento académico de los estudiantes usando un diccionario donde 
las claves son nombres de estudiantes y los valores son listas de calificaciones (float). 
Calcula el promedio y evalúa si el estudiante aprobó.

Inputs:
- student_name (string)

Outputs:
- Si el estudiante existe:
  "Grades:" <grades_list>
  "Average:" <average>
  "Passed:" true|false
- Si el estudiante no existe:
  "Error: student not found"

Validations:
- student_name no debe estar vacío después de aplicar strip().
- Verificar que student_name exista en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Test cases:
1) Normal: student_name = "Alice"
   -> Grades: [90.0, 85.0, 88.0], Average: 87.67, Passed: true
2) Borde: student_name = "Charlie"
   -> Grades: [70.0, 70.0], Average: 70.0, Passed: true
3) Error: student_name = "David"
   -> Error: student not found
"""

student_grades = {'Jesus': [90.0, 85.0, 88.0], 'Alexis': [60.0, 65.0, 58.0], 'Leonardo': [70.0, 70.0]}
student_names = input('\nProblem 4. Nombre del estudiante: ').strip()

if not student_names:
    print('Error: student not found')
elif not student_names in student_grades:
    print('Error: student not found')
else:
    average = sum(student_grades) / len(student_grades)
    print(f'Grades: {student_grades}. Averange: {average}, Passed: {average>=70.0}')

# PROBLEM 5: Word frequency counter (list + dict)
"""
Lee una oración de texto, la normaliza a minúsculas, la divide en palabras, 
construye un diccionario de frecuencias e identifica la palabra más común.

Inputs:
- sentence (string)

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validations:
- sentence no debe estar vacía después de aplicar strip().
- Estandarizar la eliminación de signos de puntuación reemplazando comas, puntos y signos de exclamación.
- Verificar que la lista de palabras resultante no esté vacía.

Test cases:
1) Normal: sentence = "apple banana apple orange banana apple"
   -> Words list: ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'], Frequencies: {'apple': 3, 'banana': 2, 'orange': 1}, Most common word: apple
2) Borde: sentence = "Hello hello HELLO"
   -> Words list: ['hello', 'hello', 'hello'], Frequencies: {'hello': 3}, Most common word: hello
3) Error: sentence = "   "
   -> Error: invalid input
"""

sentence = input('\nProblem 5. Escribe tu oracion: ').strip()

if not sentence:
    print("Error: invalid input")
else:
    
    for char in [".", ",", "!", "?", ";", ":"]:
        sentence = sentence.replace(char, "")
    
    words_list = sentence.lower().split()
    
    if not words_list:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            freq_dict[word] = freq_dict.get(word, 0) + 1
            
        most_common_word = max(freq_dict, key=freq_dict.get)
        
        print(f'Words list: {words_list}, Frequencies: {freq_dict}, Most common word: {most_common_word}')

# PROBLEM 6: Simple contact book (dictionary CRUD)
"""
Implementa una agenda de contactos básica usando un diccionario que asocia nombres 
de contactos con números telefónicos. Admite las acciones: "ADD", "SEARCH" y "DELETE".

Inputs:
- action_text (string; "ADD", "SEARCH" o "DELETE")
- name (string)
- phone (string; requerido para "ADD")

Outputs:
- Para "ADD": "Contact saved:" name, phone
- Para "SEARCH": "Phone:" <phone> (o "Error: contact not found")
- Para "DELETE": "Contact deleted:" name (o "Error: contact not found")

Validations:
- Normalizar action_text a mayúsculas y asegurar que sea una opción válida.
- name no debe estar vacío después de aplicar strip().
- Para "ADD", phone no debe estar vacío después de aplicar strip().

Test cases:
1) Normal: action_text = "ADD", name = "Alice", phone = "1234567890"
   -> Contact saved: Alice, 1234567890
2) Borde: action_text = "SEARCH", name = "Bob"
   -> Phone: 9876543210
3) Error: action_text = "DELETE", name = "NonExistent"
   -> Error: contact not found
"""

contacts = {'Minerva': '83111205309', 'Rodolfo': '8311319412'}
actions = {'ADD', 'SEARCH', 'DELETE'}

action = input('\nProblem 6. Escribir accion: ').strip().upper()
name = input('\t\t   Escribir nombre: ').strip()
phone = input('\t\t   Escribir numero: ').strip()


if action not in actions:
    print('Error: invalid input')
elif not name:
    print('Error: invalid input')
else:
    if action == 'ADD':
        if not phone:
            print('Error: invalid input')
        else:
            contacts[name] = phone
            print(f'Contact saved: {name}, {phone}')
            
    elif action == 'SEARCH':
        if name in contacts:
            print(f'Phone: {contacts[name]}')
        else:
            print('Error: contact not found')
            
    elif action == 'DELETE':
        if name in contacts:
            contacts.pop(name)
            print(f'Contact deleted: {name}')
        else:
            print('Error: contact not found')

"""
CONCLUSIONES / CONCLUSIONS
Las colecciones en Python representan herramientas esenciales para estructurar datos 
de manera eficiente. Las listas destacan por su mutabilidad y versatilidad al agregar, 
modificar o eliminar elementos. Las tuplas garantizan la integridad de datos fijos 
e inmutables, evitando alteraciones accidentales durante la ejecución. Los 
diccionarios optimizan la recuperación de datos mapeando claves únicas a sus 
respectivos valores. La combinación de estas colecciones, como un diccionario de 
listas, permite abordar modelos de datos complejos presentes en aplicaciones reales.
"""
"""
REFERENCIAS / REFERENCES
1) Python Software Foundation. Built-in Types: list, tuple, dict. 
   Official Python Documentation.
2) Lutz, Mark. Learning Python. O'Reilly Media. (Chapter on Collections and Data Structures).
3) Downey, Allen B. Think Python: How to Think Like a Computer Scientist. O'Reilly Media.
4) Hetland, Magnus Lie. Beginning Python: From Novice to Professional. Apress.
5) Class Lecture Notes on Python Data Structures, Collections, and Algorithmic Logic.
"""
