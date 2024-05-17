#Ejercicio#1
#def ordenar_y_mostrar_lista(precios):
    #precios_ordenados = precios.copy()
    #precios_ordenados.sort()
    #print("Lista ordenada de precios (de menor a mayor):", precios_ordenados)
    
    #menor_precio = precios_ordenados.pop(0)
    #print("El menor precio es:", menor_precio)
    
    #mayor_precio = precios_ordenados.pop()
    #print("El mayor precio es:", mayor_precio)


#precios = [50, 75, 46, 22, 80, 65, 8]

#ordenar_y_mostrar_lista(precios)

#Ejercicio No.3
#def contar_palabra(lista_palabras, palabra):
    #conteo = 0
    #for p in lista_palabras:
        #if p == palabra:
            #conteo += 1
    #return conteo

#lista_palabras = input("Ingrese una lista de palabras separadas por espacio: ").split()

#palabra_buscada = input("Ingrese la palabra que desea buscar: ")

#cantidad = contar_palabra(lista_palabras, palabra_buscada)

#if cantidad == 0:
    #print(f"La palabra '{palabra_buscada}' no aparece en la lista.")
#else:
    #print(f"La palabra '{palabra_buscada}' aparece {cantidad} veces en la lista.")

#Ejercicio No.2
#abecedario = [chr(i) for i in range(ord('a'), ord('z') + 1)]

#indice = 2  
#while indice < len(abecedario):
    #abecedario.pop(indice)
    #indice += 2  


#print("Lista resultante después de eliminar las letras en posiciones múltiplos de 3:")
#print(abecedario)

