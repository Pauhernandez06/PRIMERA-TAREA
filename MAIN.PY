meme_dict = {
            "CRINGE": "Algo excepcionalmente raro y embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "VINTAGE": "Algo que es nuevo pero tiene vibras de lago viejo",
            "AESTHETHIC": "Algo que es estetico, o sacado de pinterest",
            "DE MUJER" : "Se utiliza como para empoderar a la frase que se esta diciendo ",
            }
for i in list(meme_dict[len]):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        for i in(word):
            print(meme_dict.keys)
        
    else:
        print("NO SE ENCONTRO")
