"""
    Jesús Emanuel Verástegui Hernández
    2630324
    IM 1-1
"""
"""
    RESUMEN EJECUTIVO
        Este documento cubre conceptos fundamentales de programación en Python, enfocándose 
        en tipos de datos numéricos (int y float) y booleanos (True/False). Los enteros 
        representan números enteros, mientras que los flotantes manejan decimales. Los 
        booleanos surgen de comparaciones relacionales e impulsan la toma de decisiones 
        lógicas. Validar entradas y prevenir la división por cero garantiza una ejecución 
        robusta y libre de errores en entornos de producción. Esta asignación incluye seis 
        problemas distintos que cubren conversión de temperatura, cálculo de nómina, 
        evaluación de descuentos, estadísticas numéricas, elegibilidad de préstamos y 
        análisis del Índice de Masa Corporal (IMC). Cada sección detalla entradas, 
        salidas, validaciones y casos de prueba claros.
"""
"""
    PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRÁCTICAS
        - Usar tipos de datos apropiados: int para contadores o cantidades enteras, float para medidas precisas.
        - Evitar duplicar expresiones almacenando resultados intermedios en variables descriptivas.
        - Validar siempre los datos crudos antes de realizar operaciones aritméticas (verificaciones de no negatividad, prevención de división por cero).
        - Usar convenciones de nombres descriptivas siguiendo lower_snake_case para variables y UPPER_SNAKE_CASE para constantes.
        - Documentar claramente cómo se interpretan las banderas booleanas dentro de cada contexto de aplicación.
"""
# PROBLEM 1: Temperature converter and range flag
"""
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, determina una bandera booleana
'is_high_temperature' que es true si Celsius es >= 30.0 y false en caso contrario.

Entradas:
- temp_c (float; temperatura en Celsius)

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validaciones:
- Verificar que temp_c se pueda convertir correctamente a float.
- No permitir temperaturas físicamente imposibles en Kelvin (temp_k < 0.0, es decir, temp_c < -273.15).

Casos de prueba:
1) Normal: temp_c = 25.5 -> Fahrenheit: 77.9, Kelvin: 298.65, High temperature: false
2) Borde: temp_c = 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
3) Error: temp_c = -300.0 -> Error: invalid input
"""

temp_c = float(input('\nEscribe la temperatura: '))
temp_f = 32 + (temp_c * (9 / 5))
temp_k = temp_c + 273.15
is_high_temperature = temp_c >= 30.0

if temp_k < 0.0:
  print('Error: invalid input')
else:
  print(
      f'Fahrenheit: {temp_f}, Kelvin: {temp_k}, High temperature: {str(is_high_temperature).lower()}')

# PROBLEM 2: Work hours and overtime payment
"""
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate. 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. 
Genera una bandera booleana 'has_overtime'.

Entradas:
- hours_worked (float)
- hourly_rate (float)

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguna validación falla, mostrar "Error: invalid input".

Casos de prueba:
1) Normal: hours_worked = 45.0, hourly_rate = 20.0 -> Regular pay: 800.0, Overtime pay: 150.0, Total pay: 950.0, Has overtime: true
2) Borde: hours_worked = 40.0, hourly_rate = 15.0 -> Regular pay: 600.0, Overtime pay: 0.0, Total pay: 600.0, Has overtime: false
3) Error: hours_worked = -5.0, hourly_rate = 20.0 -> Error: invalid input
"""

hours = float(input('Enter hours worked: '))
rate = float(input('Enter hourly rate: '))
hours_worked = float(hours)
hourly_rate = float(rate)
regular_hours = min(hours_worked, 40.0)
overtime_hours = max(0.0, hours_worked - 40.0)
regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5
total_pay = regular_pay + overtime_pay
has_overtime = hours_worked > 40.0

if hours_worked < 0 or hourly_rate <= 0:
  print('Error: invalid input')
else:
    print(f'Regular pay: {regular_pay}, Overtime pay: {overtime_pay}, Total pay: {total_pay}, Has overtime: {str(has_overtime).lower()}')

# PROBLEM 3: Discount eligibility with booleans
"""
Determina si un cliente recibe un descuento según su estado de estudiante, 
de adulto mayor o si el total de su compra es >= 1000.0. Aplica un 10% de descuento cuando es elegible.

Entradas:
- purchase_total (float)
- is_student_text (string: "YES" o "NO")
- is_senior_text (string: "YES" o "NO")

Salidas:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validaciones:
- purchase_total >= 0.0
- Normalizar texto a mayúsculas y convertir a booleanos.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Casos de prueba:
1) Normal: purchase_total = 500.0, is_student_text = "YES", is_senior_text = "NO" -> Discount eligible: true, Final total: 450.0
2) Borde: purchase_total = 1000.0, is_student_text = "NO", is_senior_text = "NO" -> Discount eligible: true, Final total: 900.0
3) Error: purchase_total = 200.0, is_student_text = "MAYBE", is_senior_text = "NO" -> Error: invalid input
"""

total = input('Escribir el total: ').strip()
is_student_text = input('Es estudiante (YES/NO): ').strip()
is_senior_text = input('Es senior (YES/NO): ').strip()
norm_student = is_student_text.upper()
norm_senior = is_senior_text.upper()
is_valid_purchase = total.replace('.', '', 1).lstrip('-').isdigit() and total.count('.') <= 1 and len(total) > 0

if not is_valid_purchase or norm_student not in ('YES', 'NO') or norm_senior not in ('YES', 'NO'):
    print('Error: invalid input')
else:
    total = float(total)
    if total < 0.0:
        print('Error: invalid input')
    else:
        is_student = norm_student == 'YES'
        is_senior = norm_senior == 'YES'
        discount_eligible = is_student or is_senior or (total >= 1000.0)
        final_total = total * 0.9 if discount_eligible else total
        print(f'Discount eligible: {str(discount_eligible).lower()}, Final total: {final_total}')

# PROBLEM 4: Basic statistics of three integers
"""
Lee tres enteros y calcula su suma, promedio (float), valor máximo, valor mínimo
y una bandera booleana 'all_even' que indica si los tres son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que todos los valores se puedan convertir a enteros.

Casos de prueba:
1) Normal: n1 = 4, n2 = 7, n3 = 10 -> Sum: 21, Average: 7.0, Max: 10, Min: 4, All even: false
2) Borde: n1 = 2, n2 = 4, n3 = 6 -> Sum: 12, Average: 4.0, Max: 6, Min: 2, All even: true
3) Error: n1 = "abc", n2 = 5, n3 = 2 -> Error: invalid input
"""

n1 = input('\nProblem 4. Enter first integer: ').strip()
n2 = input('\t\t   Enter second integer: ').strip()
n3 = input('\t\t   Enter third integer: ').strip()

if not n1 or not n2 or not n3:
    print('Error: invalid input')
else:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f'Sum: {sum_value}, Average: {average_value}, Max: {max_value}, Min: {min_value}, All even: {str(all_even).lower()}')

# PROBLEM 5: Loan eligibility (income and debt ratio)
"""
Determina la elegibilidad para un préstamo con base en el ingreso mensual, deuda mensual y puntaje crediticio.
 Calcula la relación de deuda y evalúa las reglas específicas de elegibilidad.

Entradas:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Salidas:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validaciones:
- monthly_income > 0.0 (evita división por cero)
- monthly_debt >= 0.0
- credit_score >= 0
- Si las validaciones fallan, mostrar "Error: invalid input".

Casos de prueba:
1) Normal: monthly_income = 9000.0, monthly_debt = 2000.0, credit_score = 700 -> Debt ratio: 0.222, Eligible: true
2) Borde: monthly_income = 8000.0, monthly_debt = 3200.0, credit_score = 650 -> Debt ratio: 0.4, Eligible: true
3) Error: monthly_income = 0.0, monthly_debt = 500.0, credit_score = 700 -> Error: invalid input
"""

income = input('Enter monthly income: ').strip()
debt = input('Enter monthly debt: ').strip()
credit = input('Enter credit score: ').strip()

if not income or not debt or not credit:
    print('Error: invalid input')
else:
    monthly_income = float(income)
    monthly_debt = float(debt)
    credit_score = int(credit)

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print('Error: invalid input')
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
        print(f'Debt ratio: {round(debt_ratio, 3)}, Eligible: {str(eligible).lower()}')

# PROBLEM 6: Body Mass Index (BMI) and category flag
"""
Calcula el Índice de Masa Corporal (IMC / BMI) y evalúa banderas booleanas de categoría para bajo peso, peso normal y sobrepeso.

Entradas:
- weight_kg (float)
- height_m (float)

Salidas:
- "BMI:" <rounded_bmi>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no es válido, mostrar "Error: invalid input".

Casos de prueba:
1) Normal: weight_kg = 70.0, height_m = 1.75 -> BMI: 22.86, Underweight: false, Normal: true, Overweight: false
2) Borde: weight_kg = 56.69, height_m = 1.75 -> BMI: 18.5, Underweight: false, Normal: true, Overweight: false
3) Error: weight_kg = -70.0, height_m = 1.75 -> Error: invalid input
"""

weight = input('Enter weight in kg: ').strip()
height = input('Enter height in meters: ').strip()

if not weight or not height:
    print('Error: invalid input')
else:
    weight_kg = float(weight)
    height_m = float(height)

    if weight_kg <= 0.0 or height_m <= 0.0:
        print('Error: invalid input')
    else:
        bmi = weight_kg / (height_m * height_m)
        rounded_bmi = round(bmi, 2)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0
        print(f'BMI: {rounded_bmi}, Underweight: {str(is_underweight).lower()}, Normal: {str(is_normal).lower()}, Overweight: {str(is_overweight).lower()}')

"""
CONCLUSIONES
    Los enteros y flotantes trabajan juntos de forma fluida para manejar tanto conteos 
    discretos como mediciones continuas en escenarios del mundo real. Las comparaciones 
    relacionales transforman valores de datos en bruto en banderas booleanas, impulsando 
    la ejecución condicional y el flujo lógico. Validar rangos y prevenir la división 
    por cero garantiza estabilidad y evita fallos en tiempo de ejecución. Diseñar 
    condiciones compuestas con operadores and, or y not agudiza las habilidades analíticas 
    de resolución de problemas, reflejando reglas fundamentales encontradas en sistemas 
    de nómina, préstamos financieros y análisis de salud.
"""
"""
REFERENCIAS
    1) Python Software Foundation. Built-in Types: Numeric Types — int, float, complex. 
    Official Python Documentation.
    2) Python Software Foundation. Truth Value Testing and Boolean Operations — bool. 
    Official Python Documentation.
    3) Lutz, Mark. Learning Python. O'Reilly Media. (Covers arithmetic, relational, and logical operators).
    4) Downey, Allen B. Think Python: How to Think Like a Computer Scientist. O'Reilly Media. 
    (Covers conditionals, functions, and data validation techniques).
    5) Class Lecture Notes on Data Validation, Error Handling, and Numerical Types in Python.
"""