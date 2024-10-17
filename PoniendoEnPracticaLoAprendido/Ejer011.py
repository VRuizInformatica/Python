salarios = [[700, 900, 1300] , [1000, 950, 1080], [1300, 930, 1200]]
empleados = ["Javier María", "Antonio Muñoz", "Isabel Allende"]

for i in range(len(empleados)):
    totalSalario = sum(salarios[i])
    salarioSuma = " + ".join(map(str,salarios[i]))
    empleadosDef = empleados[i]
    print(f"{empleadosDef} -> {salarioSuma} = {totalSalario}")
