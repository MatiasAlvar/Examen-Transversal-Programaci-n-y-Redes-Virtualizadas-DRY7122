Numero_de_VLAN = int(input("Ingrese número de VLAN? "))
if Numero_de_VLAN >= 1 and Numero_de_VLAN <= 1005:
    print("Corresponde a VLAN de rango normal.")
elif Numero_de_VLAN >=1006 and Numero_de_VLAN <= 4094:
    print("Corresponde a VLAN de rango extendido")
else:
    print("Vlan no corresponde a rango normal ni tampoco a rango extendido .")
