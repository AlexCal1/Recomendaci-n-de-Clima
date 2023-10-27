# Saludo inicial
print("Hola, soy Siri!")

# Mensajes de recomendación para diferentes climas
mensaje1 = "Si hace sol, usa protector solar y gafas de sol."
mensaje2 = "Si está nevando, abrígate y usa ropa abrigada."
mensaje3 = "Si está lloviendo, no olvides llevar un paraguas."
mensaje4 = "Si está nublado, es un buen día para caminar."
mensaje5 = "No es posible dar una recomendación. Inténtalo más tarde."

# Solicitar si el usuario desea una recomendación y el clima actual
pregunta = input("¿Deseas recibir una recomendación del clima?: ")
clima = input("Ingresa el clima: ")

# Evaluar las respuestas y proporcionar recomendaciones
if pregunta.lower() == "no":
    print("Gracias por usar Siri, ¡hasta pronto!")
elif pregunta.lower() == "si":
    if clima.lower() == "soleado":
        print(mensaje1)
    elif clima.lower() == "nevando":
        print(mensaje2)
    elif clima.lower() == "lluvioso":
        print(mensaje3)
    elif clima.lower() == "nublado":
        print(mensaje4)
    else:
        print(mensaje5)
else:
    print("Respuesta no válida. Debes responder 'si' o 'no'.")
