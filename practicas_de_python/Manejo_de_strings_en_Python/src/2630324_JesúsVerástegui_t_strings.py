"""
    Jesús Emanuel Verástegui Hernández
    2630324
    IM 1-1
"""
"""
RESUMEN EJECUTIVO
    Un string en Python es una secuencia inmutable de caracteres utilizada para 
    representar y almacenar texto. Las operaciones básicas incluyen concatenación, 
    obtención de longitud, extracción de subcadenas, búsqueda de patrones y reemplazo.
    Es crucial validar y normalizar las entradas de texto (como correos, nombres y contraseñas) 
    para garantizar la integridad de los datos, la seguridad y una buena experiencia de usuario. 
    Este documento cubre el desarrollo de seis problemas prácticos, detallando su 
    descripción, entradas, salidas, validaciones y el uso de métodos de string 
    implementados en Python.
"""
"""
PRINCIPIOS Y BUENAS PRACTICAS
    - Los strings son inmutables: cualquier modificación o 
      transformación genera un nuevo objeto de cadena en memoria.
    - Es una buena práctica normalizar la entrada usando strip() 
      y lower() antes de realizar comparaciones.
    - Evitar "números mágicos" en los índices; documentar 
      claramente qué extrae cada slice.
    - Aprovechar los métodos de string integrados de Python en lugar 
      de reescribir lógica de análisis de bajo nivel manualmente.
    - Diseñar validaciones estructuradas: verificar siempre primero
      si la entrada está vacía, seguido de los formatos estructurales.
    - Escribir código limpio y legible utilizando nombres de variables
      explícitos en lower_snake_case y mensajes de error comprensibles.
"""
# Problem 1: Full name formatter (name + initials)
"""
Description: Dado el nombre completo de una persona en una sola cadena, el programa normaliza el texto 
y muestra el nombre formateado en Title Case y sus iniciales.

Inputs:
- full_name (string; nombre completo con posibles espacios extra)

Outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validations:
- full_name no debe estar vacío tras strip().
- Debe contener al menos dos palabras.
- No aceptar cadenas que sean solo espacios.

Test cases:
1) Normal: "juan carlos tovar" -> Formatted: Juan Carlos Tovar, Initials: J.C.T.
2) Border: "  maria   del   carmen  " -> Formatted: Maria Del Carmen, Initials: M.D.C.
3) Error: "   " o "juan" -> Error: invalid input
"""

first_names = input('\nProblem 1. Ingresa tus nombres: ')
last_names = input('\t   Ingresa tus apellidos: ')
full_name = f'{first_names.strip()} {last_names.strip()}'.title()
full_name_list = full_name.split()
initials = '.'.join(word[0] for word in full_name_list)
if not first_names.strip() or not last_names.strip():
    print('Error: invalid input')
else:
    print(f'Formatted: {full_name}, Initials: {initials}')

# Problem 2: Simple email validator (structure + domain)
"""
Valida si una dirección de correo tiene un formato básico correcto (contiene un '@', 
al menos un '.' después del '@' y sin espacios). Si es válido, muestra el dominio.

Inputs:
- email_text (string)

Outputs:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validations:
- email_text no vacío tras strip().
- Contar exactamente un '@'.
- No contener espacios en blanco.

Test cases:
1) Normal: "test.user@example.com" -> Valid email: true, Domain: example.com
2) Border: "a@b.co" -> Valid email: true, Domain: b.co
3) Error: "invalid.email.com" o "user @domain.com" -> Valid email: false
"""

email = input('\nProblem 2. Ingresa tu email: ')
domain = email[email.find('@')+1:]
if not email.strip():
    print(False)
elif '@' not in email:
    print('@' in email)
elif ' ' in email.strip():
    print(' ' not in email.strip())
elif email.count('@') > 1:
    print(email.count('@') < 1)
else:
    print(f'Valid email: {email.count('@')==1}, Domain: {domain}')

# Problem 3: Palindrome checker (ignoring spaces and case)
"""
Determina si una frase es un palíndromo (se lee igual de izquierda a derecha y 
de derecha a izquierda), ignorando espacios y mayúsculas/minúsculas.

Inputs:
- phrase (string)

Outputs:
- "Is palindrome: true" o "Is palindrome: false"

Validations:
- phrase no vacía tras strip().
- Longitud mínima de 3 caracteres después de limpiar espacios.

Test cases:
1) Normal: "Anita lava la tina" -> Is palindrome: true
2) Border: "A man a plan a canal Panama" -> Is palindrome: true
3) Error: "ab" o "" -> Is palindrome: false
"""

phrase = input('\nProblem 3. Escribe tu palabra: ').strip().lower().replace(' ','')
reverse_phrase = phrase[::-1]
if phrase==reverse_phrase:
    print(f'Is palindrome: {phrase==reverse_phrase}')
else:
    print(f'Is palindrome: {phrase==reverse_phrase}')

# Problem 4: Sentence word stats (lengths and first/last word)
"""
Dada una oración, normaliza espacios, separa palabras y muestra el conteo total, 
la primera palabra, la última palabra, la más corta y la más larga.

Inputs:
- sentence (string)

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validations:
- Oración no vacía tras strip().
- Debe contener al menos una palabra tras split().

Test cases:
1) Normal: "Python string manipulation is powerful" -> Word count: 5, First: Python, Last: powerful
2) Border: "Hi" -> Word count: 1, First: Hi, Last: Hi
3) Error: "   " -> Error: invalid input
"""

sentence = input('\nProblem 4. Escribe tu oración: ')
words = sentence.strip().split()
shortest_word = words[0]
longest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word
    if len(word) > len(longest_word):
        longest_word = word

if sentence.strip() and sentence.split():
    print(f'Word count: {len(words)}, First: {words[0]}, Last: {words[-1]}, Shortest word: {shortest_word}, Longest word: {longest_word}')

# Problem 5: Password strength classifier
"""
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas 
de longitud y composición de caracteres.

Inputs:
- password_input (string)

Outputs:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validations:
- No aceptar contraseña vacía.

Test cases:
1) Normal: "Secret123!" -> Password strength: strong
2) Border: "password123" -> Password strength: medium
3) Error: "abc" -> Password strength: weak
"""
pasword_input = input('\nProblem 5 Ingrese su contraseña: ').strip()

if not pasword_input:
    print('Error: invalid input')
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

for caracter in pasword_input:
    if caracter.isupper():
        has_upper = True
    elif caracter.islower():
        has_lower = True
    elif caracter.isdigit():
        has_digit = True
    elif not caracter.isalnum():
        has_special = True

if len(pasword_input) >= 8 and has_upper and has_lower and has_digit and has_special:
    strength = 'strong'
elif len(pasword_input) >= 8 and (has_upper or has_lower or has_digit):
    strength = 'medium'
else:
    strength = 'weak'
print(f'Password strength: {strength}')

# Problem 6: Product label formatter (fixed-width text)
"""
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea 
con un ancho fijo exacto de 30 caracteres (rellenando con espacios o recortando si es necesario).

Inputs:
- product_name (string)
- price_value (string o número)

Outputs:
- "Label: <exactly 30 characters>"

Validations:
- product_name no vacío tras strip().
- price_value convertible a número positivo.

Test cases:
1) Normal: product="Coffee", price=4.50 -> "Label: 'Product: Coffee | Price: $4.5 '"
2) Border: nombre largo -> exactamente 30 caracteres
3) Error: nombre vacío o precio negativo -> Error: invalid input
"""
product_name = input('\nProblem 6. Ingresa el nombre del producto: ')
price_value = input('Ingresa el precio: ')
clean_name = product_name.strip()
num_price = abs(float(price_value))
    
if not clean_name or num_price==0:
    print('Error: invalid input')
else:
    base_label = f"Product: {clean_name} | Price: ${price_value}"
    final_label = base_label[:30].ljust(30)
    print(f'Label: {final_label}\n')

"""
CONCLUSIONES
    El manejo de strings es esencial para la entrada y salida de datos en cualquier aplicación. 
    El uso de métodos integrados como lower(), strip(), split() y join() facilita enormemente la normalización 
    de texto y garantiza comparaciones precisas. Implementar validaciones estructuradas evita fallos en tiempo 
    de ejecución y bloquea datos basura. Asimismo, comprender la inmutabilidad de las cadenas y el uso de slices 
    permite extraer subsegmentos de manera eficiente. En definitiva, un buen procesamiento de texto mejora 
    la seguridad y la calidad del software.
"""
"""
REFERENCIAS
    1) Python Software Foundation. (2026). Python Documentation - Built-in Types: Text Sequence Type — str. https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    2) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media.
    3) Ramalho, L. (2022). Fluent Python (2nd ed.). O'Reilly Media.
    4) McKinney, W. (2017). Python for Data Analysis (2nd ed.). O'Reilly Media.
    5) Real Python. (2025). Python String Methods and Manipulation Guide. https://realpython.com/python-strings/
"""