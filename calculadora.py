

UMBRAL = 4  


def tamano(u):
    return len(str(u))


def mult_clasica(u, v):
    """Multiplicacion de escuela, digito por digito (para n pequeno)."""
    a = [int(c) for c in reversed(str(u))]
    b = [int(c) for c in reversed(str(v))]
    res = [0] * (len(a) + len(b))
    for i, da in enumerate(a):
        acarreo = 0
        for j, db in enumerate(b):
            t = res[i + j] + da * db + acarreo
            res[i + j] = t % 10
            acarreo = t // 10
        res[i + len(b)] += acarreo
    return int("".join(map(str, reversed(res))))


def mult(u, v):
    """Multiplicacion de enteros grandes (u, v >= 0)."""
    n = max(tamano(u), tamano(v))
    if n <= UMBRAL:
        return mult_clasica(u, v)

    s = n // 2
    p = 10 ** s
    w, x = u // p, u % p
    y, z = v // p, v % p

    return (mult(w, y) * 10 ** (2 * s)
            + (mult(w, z) + mult(x, y)) * p
            + mult(x, z))


def mult_con_signo(u, v):
    signo = -1 if (u < 0) != (v < 0) else 1
    return signo * mult(abs(u), abs(v))


def leer_entero(msg):
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("  Entrada invalida, ingrese un entero.")


def main():
    print("=== Calculadora de enteros grandes ===")
    while True:
        print("\n1) Sumar   2) Restar   3) Multiplicar   0) Salir")
        op = input("Opcion: ").strip()
        if op == "0":
            break
        if op not in ("1", "2", "3"):
            print("  Opcion invalida.")
            continue
        u = leer_entero("Primer numero: ")
        v = leer_entero("Segundo numero: ")
        if op == "1":
            print("Resultado:", u + v)
        elif op == "2":
            print("Resultado:", u - v)
        else:
            print("Resultado:", mult_con_signo(u, v))


if __name__ == "__main__":
    main()