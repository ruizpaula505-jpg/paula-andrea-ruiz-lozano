usuarios = {
    10901: {"nombre": "catalina forero", "contraseña": "Qwe1rt#a", "pin": 613902, "saldo": 10000},
    11123: {"nombre": "miguel triana", "contraseña": "A123bx$n", "pin": 190100, "saldo": 20000}
}

print(" BIENVENIDO AL SISTEMA ")
print("Tiene 3 intentos para ingresar su documento")

intentos = 3

while intentos > 0:
    cedula = int(input("Ingrese su cédula: "))
    
    if cedula in usuarios:
        nombre = usuarios[cedula]["nombre"]
        print("Bienvenido(a)", nombre)
        break
    else:
        print("Documento no encontrado.")
        intentos -= 1
        print("Intentos restantes:", intentos)

if intentos == 0:
    print("Se acabaron los intentos. Saliendo del sistema")

else:
    contraseña_intentos = 3
    
    while contraseña_intentos > 0:
        contraseña = input("Ingrese su contraseña: ")
        
        if contraseña == usuarios[cedula]["contraseña"]:
            print("Contraseña correcta. Acceso permitido.")
            break
        else:
            print("Contraseña incorrecta.")
            contraseña_intentos -= 1
            print("Intentos restantes:", contraseña_intentos)
    
    if contraseña_intentos == 0:
        print("Se acabaron los intentos. Saliendo del sistema")
    
    else:
        print("MENU PRINCIPAL")
        print("1. Ver saldo")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Ver movimiento")
        print("5. Salir")
        
        opc = input("Seleccione una opción: ")

        if opc == "1":
            print(f"Su saldo actual es: {usuarios[cedula]['saldo']}")

        elif opc == "2":
            monto = float(input("Ingrese monto a consignar: "))
            usuarios[cedula]['saldo'] += monto
            print(f"Consignación exitosa. Nuevo saldo: {usuarios[cedula]['saldo']}")

        elif opc == "3":
            monto = float(input("Ingrese monto a retirar: "))
            if monto <= usuarios[cedula]['saldo']:
                usuarios[cedula]['saldo'] -= monto
                print(f"Retiro exitoso. Nuevo saldo: {usuarios[cedula]['saldo']}")
            else:
                print("Saldo insuficiente.")

        elif opc == "4":
            print("Movimientos registrados (aún no programados)")
        elif opc == "5":
            print("Saliendo del sistema...")

        else:
            print("Opción no válida.")