import spacy

# Cargar el modelo pre-entrenado en español
nlp = spacy.load("es_core_news_sm")

def reconocimiento_entidades(oraciones):

    entidades_total = []
    for oracion in oraciones:
        #se llama al modelo cargado y se le pasa como parametro la oracion 
        #se iguala a la variable doc
        doc = nlp(oracion)
        #se extraen entidades nombradas identificadas modelo spacy
        entidades = [(ent.text, ent.label_) for ent in doc.ents]
        entidades_dict = {'Oracion': oracion, 'entidades': entidades}
        entidades_total.append(entidades_dict)
    return(entidades_total)
