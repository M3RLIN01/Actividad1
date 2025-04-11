numero_acl = input("Ingrese el número de la ACL")

try:
    acl_numero = int(numero_acl)
    if 1 <= acl_numero <= 99 or 1300 <= acl_numero <= 1999:
        print("Es una ACL Estándar")
    elif 100 <= acl_numero <= 199 or 2000 <= acl_numero <= 2699:
        print("Es una ACL Extendida")
    else:
        print("El número ingresado no corresponde a una ACL IPV4 común.")
except ValueError:
    print("Por favor, ingrese un número válido")