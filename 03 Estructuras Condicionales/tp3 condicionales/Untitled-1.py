edad_usuario = int(input("Por favor ingrese su edad: "))

if edad_usuario < 12:
    print("Eres un niño.")
elif 12 <= edad_usuario < 18:
    print("Eres un adolescente.")
elif 18 <= edad_usuario < 30:
    print("Eres un adulto joven.")
elif 30 <= edad_usuario < 60:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
