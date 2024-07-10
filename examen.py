import random
import csv




trabajadores=[
    {
        "Nombre":"Juan Perez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Maria Garcia",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Carlos Lopez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Ana Martinez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Pedro Rodriguez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Laura Hernandez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Miguel Sanchez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Isabel Gomez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Francisco Diaz",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
    {
        "Nombre":"Elena Fernandez",
        "Sueldo": "0",
        "Desc.Salud": "0",
        "Desc.AFP": "0",
        "Sueldo Liquido": "0",
    },
]
try:
    def menu():
        menu=int(input("""
        1. Asignar sueldos
        2. Clasificar Sueldos
        3. Ver estadisticas
        4. Reporte de sueldos
        5. Salir del programa
        """))
        return menu
    
    def asignarsueldos():
        for des in trabajadores:
            sueldos=random.randint(300000,2500000)
            des['Sueldo']=sueldos
            print(f"Nombre: {des['Nombre']}    ${des['Sueldo']}")
    
    def clasificar():
        sueldosbajos=[]
        sueldosmedios=[]
        sueldosaltos=[]
        for des in trabajadores:
            if des['Sueldo']<800000:
                sueldosbajos.append(des)
            elif 800000<des['Sueldo'] and des['Sueldo']<2000000:
                sueldosmedios.append(des)
            elif 2000000<des['Sueldo']:
                sueldosaltos.append(des)
        print(f"Sueldos bajo $800.000          Sueldos Totales:{len(sueldosbajos)}")
        for des in sueldosbajos:
            print(f"""Nombre: {des['Nombre']}      Sueldo: ${des['Sueldo']}""")
        print(f"Sueldos entre $800.000 y $2.000.000          Sueldos Totales:{len(sueldosmedios)}")
        for des in sueldosmedios:
            print(f"""Nombre: {des['Nombre']}      Sueldo: ${des['Sueldo']}""")
        print(f"Sueldos sobre $2.000.000          Sueldos Totales:{len(sueldosaltos)}")
        for des in sueldosaltos:
            print(f"""Nombre: {des['Nombre']}      Sueldo: ${des['Sueldo']}""")
            
    def reporte():
        for des in trabajadores:
            des['Desc.Salud']=des['Sueldo'] * 0.7
            des['Desc.AFP']=des['Sueldo'] * 0.12
            descuentototal=des['Desc.AFP'] + des['Desc.Salud']
            des['Sueldo Liquido']=des['Sueldo'] - descuentototal
            print(f"""
            {des['Nombre']}   {des['Sueldo']} {des['Desc.Salud']}  {des['Desc.AFP']}  {des['Sueldo Liquido']}""")
            
            
        with open("Reporte_De_Sueldo.csv","w",newline="") as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(['Nombre'      ,'Sueldo'       ,'AFP',      'salud',     'liquido'])
            for i in trabajadores:
                escritor.writerows(
                [[i['Nombre'],        i['Sueldo'],      i['Desc.Salud'],     i['Desc.AFP'],      i['Sueldo Liquido']]
                ])
            print("listo")
            
            
    while True:
        op=menu()
        if op==1:
            print("Asignando sueldos...\n")
            asignarsueldos()
            print("\nLISTO")
        elif op==2:
            print("Clasificando sueldo...\n")
            clasificar()
            print("\nSueldos clasificados")
        elif op==3:
            print("Cargando estadisticas...")
            print("Estadisticas listas")
        elif op==4:
            print("Iniciando el reporte de sueldos...\n")
            reporte()
            print("\nReporte descargado con exito")
        elif op==5:
            print("Saliendo Programa\nDesarrollado por Leonardo Oñate\RUT:22.042.893-1\n")
        else:
            print("Elija una opcion valida")
        
          
        
except Exception as e:print(f"Hubo un error,{e}")