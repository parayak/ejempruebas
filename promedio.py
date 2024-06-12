def calcular_promedio_notas(notas, ponderaciones):
    if len(notas) != len(ponderaciones):
        return "Error: La cantidad de notas y ponderaciones no coincide"
    
    suma_ponderada = sum(nota * ponderacion for nota, ponderacion in zip(notas, ponderaciones))
    suma_ponderaciones = sum(ponderaciones)
    
    promedio = suma_ponderada / suma_ponderaciones
    
    return promedio

def main():
    n = int(input("Ingrese la cantidad de notas: "))
    notas = []
    ponderaciones = []
    
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
        
        ponderacion = float(input(f"Ingrese la ponderación para la nota {i+1}: "))
        ponderaciones.append(ponderacion)
    
    promedio = calcular_promedio_notas(notas, ponderaciones)
    
    print(f"Su Promedio Final de Nota es: {promedio}")

if __name__ == "__main__":
    print("Desarrollado por el Gran Gurú")
    main()
