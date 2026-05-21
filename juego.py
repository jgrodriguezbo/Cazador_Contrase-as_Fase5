import random
import string


# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================

class LongitudInvalidaError(Exception):
    pass


class EntradaNoNumericaError(Exception):
    pass


class ContrasenaInvalidaError(Exception):
    pass


# =========================
# CLASE CONTRASEÑA
# =========================

class Contrasena:

    def __init__(self, longitud):
        self.longitud = longitud
        self.contrasena = ""

    def generar(self):

        letras = string.ascii_letters
        numeros = string.digits
        especiales = "!@#$%^&*()-_=+[]{};:,.<>?/"

        caracteres = letras + numeros + especiales

        while True:

            password = ""

            for i in range(self.longitud):
                password += random.choice(caracteres)

            if self.validar(password):
                self.contrasena = password
                return self.contrasena

    def validar(self, password):

        tiene_mayuscula = False
        tiene_minuscula = False
        tiene_numero = False
        tiene_especial = False

        especiales = "!@#$%^&*()-_=+[]{};:,.<>?/"

        for caracter in password:

            if caracter.isupper():
                tiene_mayuscula = True

            elif caracter.islower():
                tiene_minuscula = True

            elif caracter.isdigit():
                tiene_numero = True

            elif caracter in especiales:
                tiene_especial = True

        if len(password) < 8:
            raise ContrasenaInvalidaError(
                "La contraseña debe tener mínimo 8 caracteres"
            )

        if not tiene_mayuscula:
            raise ContrasenaInvalidaError(
                "La contraseña necesita una mayúscula"
            )

        if not tiene_minuscula:
            raise ContrasenaInvalidaError(
                "La contraseña necesita una minúscula"
            )

        if not tiene_numero:
            raise ContrasenaInvalidaError(
                "La contraseña necesita un número"
            )

        if not tiene_especial:
            raise ContrasenaInvalidaError(
                "La contraseña necesita un carácter especial"
            )

        repetidos = False

        for letra in password:
            if password.count(letra) > 1:
                repetidos = True

        if repetidos:
            raise ContrasenaInvalidaError(
                "La contraseña no debe tener caracteres repetidos"
            )

        return True


# =========================
# CLASE COFRE
# =========================

class Cofre:

    def __init__(self):

        opcion = random.randint(1, 3)

        if opcion == 1:
            self.tipo = "Común"
            self.puntos = 10

        elif opcion == 2:
            self.tipo = "Raro"
            self.puntos = 25

        else:
            self.tipo = "Legendario"
            self.puntos = 50

    def mostrar(self):

        return (
            "Cofre obtenido: "
            + self.tipo
            + " | Puntos: "
            + str(self.puntos)
        )


# =========================
# CLASE JUEGO
# =========================

class JuegoCazador:

    def __init__(self):
        self.puntaje = 0

    def jugar(self):

        continuar = "s"

        print("\n===== CAZADOR DE CONTRASEÑAS =====")

        while continuar.lower() == "s":

            try:

                entrada = input(
                    "\nIngrese la longitud de la contraseña: "
                )

                if not entrada.isdigit():
                    raise EntradaNoNumericaError(
                        "La entrada debe ser numérica"
                    )

                longitud = int(entrada)

                if longitud < 8:
                    raise LongitudInvalidaError(
                        "La longitud mínima es 8 caracteres"
                    )

                contrasena = Contrasena(longitud)

                password_generada = contrasena.generar()

                print(
                    "\nContraseña generada:",
                    password_generada
                )

                print(
                    "\nContraseña válida correctamente"
                )

                cofre = Cofre()

                self.puntaje += cofre.puntos

                print("\n" + cofre.mostrar())

                print(
                    "Puntaje acumulado:",
                    self.puntaje
                )

            except EntradaNoNumericaError as error:

                print("\nError:", error)

            except LongitudInvalidaError as error:

                print("\nError:", error)

            except ContrasenaInvalidaError as error:

                print("\nError:", error)

                print(
                    "\nCofre obtenido: Maldito | Puntos: -20"
                )

                self.puntaje -= 20

                print(
                    "Puntaje acumulado:",
                    self.puntaje
                )

            except Exception as error:

                print(
                    "\nOcurrió un error inesperado:",
                    error
                )

            finally:

                continuar = input(
                    "\n¿Desea seguir jugando? (s/n): "
                )

        print("\n===== FIN DEL JUEGO =====")

        print(
            "Puntaje final:",
            self.puntaje
        )


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

juego = JuegoCazador()
juego.jugar()