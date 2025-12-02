
usuarios = {
    10901: {"nombre": "catalina forero", "contraseña": "Qwe1rt#a", "pin": 613902, "saldo": 10000},
    11123: {"nombre": "miguel triana", "contraseña": "A123bx$n", "pin": 190100, "saldo": 20000}
}

print("===== BIENVENIDO AL SISTEMA =====")
print("Tiene 3 intentos para ingresar su documento")

intentos = 3

while intentos > 0:
    cedula = int(input("Ingrese su cédula: "))
    
    if cedula in usuarios:
        nombre = usuarios[cedula]["nombre"]
        print(" Bienvenido(a)", nombre)
        break
    else:
        print(" Documento no encontrado.")
        intentos -= 1
        print("Intentos restantes:", intentos,)

if intentos == 0:
    print(" Se acabaron los intentos   Saliendo del sistema")
    
    





