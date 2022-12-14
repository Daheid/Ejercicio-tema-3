#primera parte
def suma(valorA, ValorB): 
    resultado = valorA + ValorB
    print(resultado)


    

 #primera parte
suma(2, 3)

#segunda parte

class coche: 
    n_puertas = 2 #numero de puertas que tiene 
    def agg_puerta(n_puertas, puertas):
        n_puertas = puertas + n_puertas
        print(n_puertas)

   
miCoche = coche()

miCoche.agg_puerta(3)
miCoche.n_puertas(3)