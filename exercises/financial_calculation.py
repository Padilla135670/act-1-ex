# financial_calculation.py
# Actividad 1 (extra) - Trabajo colaborativo con Git y GitHub
# Estudiante 2: Paolo Rodriguez

# FORMULA DEL INTERES COMPUESTO
#     valor_futuro = capital_inicial * (1 + tasa_anual) ** anios
# donde:
#   capital_inicial -> dinero que se invierte al inicio
#   tasa_anual      -> tasa de interes por anio en decimal (5% se escribe 0.05)
#   anios           -> numero de periodos que dura la inversion
#   valor_futuro    -> monto acumulado al terminar el plazo
# El exponente hace que los intereses de cada anio se reinviertan y a su vez
# generen mas intereses; por eso el crecimiento es exponencial y no lineal.


def calcular_valor_futuro(capital_inicial, tasa_anual, anios):
    """Calcula el valor futuro de una inversion con interes compuesto."""
    return capital_inicial * (1 + tasa_anual) ** anios


def mostrar_escenario(titulo, capital_inicial, tasa_anual, anios):
    """Imprime el detalle de un escenario y devuelve su valor futuro."""
    valor_futuro = calcular_valor_futuro(capital_inicial, tasa_anual, anios)
    interes_ganado = valor_futuro - capital_inicial

    print(titulo)
    print(f"  Capital inicial : $ {capital_inicial:,.2f}")
    print(f"  Tasa anual      : {tasa_anual * 100:.2f} %")
    print(f"  Plazo           : {anios} anios")
    print(f"  Valor futuro    : $ {valor_futuro:,.2f}")
    print(f"  Interes ganado  : $ {interes_ganado:,.2f}")
    print()

    return valor_futuro


def main():
    print("CALCULO DE INVERSION CON INTERES COMPUESTO")
    print("=" * 50)
    print()

    # Escenario 1: el calculo original de la Actividad 1
    valor_futuro_1 = mostrar_escenario(
        "Escenario 1 - Inversion original (plazo corto)",
        capital_inicial=10000.0,
        tasa_anual=0.05,
        anios=5,
    )

    # Escenario 2: segundo escenario, con mejor tasa y mayor plazo
    valor_futuro_2 = mostrar_escenario(
        "Escenario 2 - Inversion a largo plazo (mejor tasa)",
        capital_inicial=10000.0,
        tasa_anual=0.075,
        anios=10,
    )

    # COMPARACION ENTRE LOS DOS RESULTADOS
    diferencia = valor_futuro_2 - valor_futuro_1
    proporcion = valor_futuro_2 / valor_futuro_1

    print("COMPARACION DE LOS DOS ESCENARIOS")
    print("-" * 50)
    print(f"  Diferencia a favor del escenario 2 : $ {diferencia:,.2f}")
    print(f"  El escenario 2 rinde {proporcion:.2f} veces el escenario 1.")

    if valor_futuro_2 > valor_futuro_1:
        print("  Conviene mas el escenario 2: mayor plazo y mejor tasa.")
    else:
        print("  Conviene mas el escenario 1.")


if __name__ == "__main__":
    main()
