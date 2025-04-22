# Calculadora de Costos de Envío

## Ingresar el peso del paquete y la tarifa de envío

peso = float(input("Ingrese el peso del paquete en kilogramos: "))

tarifa = float(input("Ingrese la tarifa de envío por kilogramo: "))

## Calcular el costo de envío

costo_envio = peso * tarifa

## Mostrar el resultado

print(f"Costo de Envío: {costo_envio} USD")
