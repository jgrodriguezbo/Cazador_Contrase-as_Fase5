import random
import string


# ---------------------------------
# EXCEPCIONES PERSONALIZADAS
# ---------------------------------

class ErrorLongitud(Exception):
    pass


class ErrorContraseña(Exception):
    pass


# ---------------------------------
# CLASE CONTRASEÑA
# ---------------------------------

class Contraseña:

    especiales = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):

        if not str(longitud).isdigit():
            raise ErrorLongitud("La longitud debe ser numérica")

        self.longitud = int(longitud)

        if self.longitud < 8:
            raise ErrorLongitud(
                "La longitud mínima es 8 caracteres"
            )

    def generar(self):

        mayuscula = random.choice(string.ascii_uppercase)

        minuscula = random.choice(string.ascii_lowercase)

        numero = random.choice(string.digits)

        especial = random.choice(self.especiales)

        restantes = self.longitud - 4

        todos = (
            string.ascii_letters
            + string.digits
            + self.especiales
        )

        contraseña = [
            mayuscula,
            minuscula,
            numero,
            especial
        ]

        while len(contraseña) < self.longitud:

            caracter = random.choice(todos)

            if caracter not in contraseña:
                contraseña.append(caracter)

        random.shuffle(contraseña)

        return "".join(contraseña)

    def validar(self, contraseña):

        tiene_mayuscula = False
        tiene_minuscula = False
        tiene_numero = False
        tiene_especial = False

        for caracter in contraseña:

            if caracter.isupper():
                tiene_mayuscula = True

            elif caracter.islower():
                tiene_minuscula = True

            elif caracter.isdigit():
                tiene_numero = True

            elif caracter in self.especiales:
                tiene_especial = True

        if (
            tiene_mayuscula
            and tiene_minuscula
            and tiene_numero
            and tiene_especial
            and len(set(contraseña)) == len(contraseña)
        ):
            return True

        return False


# ---------------------------------
# CLASE COFRE
# ---------------------------------

class Cofre:

    def __init__(self, tipo, puntos):

        self.tipo = tipo
        self.puntos = puntos

    def mostrar(self):

        return (
            f"Cofre obtenido: {self.tipo}"
            f" | Puntos: {self.puntos}"
        )


# ---------------------------------
# CLASE JUEGO
# ---------------------------------

class JuegoCazador:

    def __init__(self):

        self.puntaje = 0

        self.cofres = [
            Cofre("Común", 10),
            Cofre("Raro", 25),
            Cofre("Legendario", 50)
        ]

        self.cofre_maldito = Cofre(
            "Maldito",
            -20
        )

    def jugar(self):

        continuar = "s"

        print("\n===== CAZADOR DE CONTRASEÑAS =====\n")

        while continuar.lower() == "s":

            try:

                longitud = input(
                    "Ingrese la longitud de la contraseña: "
                )

                contraseña_obj = Contraseña(longitud)

                contraseña = contraseña_obj.generar()

                print(
                    "\nContraseña generada:",
                    contraseña
                )

                if contraseña_obj.validar(contraseña):

                    cofre = random.choice(self.cofres)

                else:

                    raise ErrorContraseña(
                        "Contraseña inválida"
                    )

            except ErrorLongitud as e:

                print("\nError:", e)

                cofre = self.cofre_maldito

            except ErrorContraseña as e:

                print("\nError:", e)

                cofre = self.cofre_maldito

            else:

                print(
                    "\nContraseña válida correctamente"
                )

            finally:

                self.puntaje += cofre.puntos

                print("\n" + cofre.mostrar())

                print(
                    "Puntaje acumulado:",
                    self.puntaje
                )

                continuar = input(
                    "\n¿Desea seguir jugando? (s/n): "
                )

        print("\n===== FIN DEL JUEGO =====")
        print("Puntaje final:", self.puntaje)


# ---------------------------------
# EJECUCIÓN PRINCIPAL
# ---------------------------------

juego = JuegoCazador()

juego.jugar()