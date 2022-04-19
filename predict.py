


from flair.data import Sentence

def pridect(Model,Data):
    dict={"label":"Prediction"}

    import time
    start=time.time()
    for i in range(len(Data)-1):
     if(len(Data[i])!=0):
    
        sentence = Sentence(Data[i])
        Model.predict(sentence)
        list=sentence.to_dict(tag_type='ner')
        if(len(list['entities'])>0):
            for j in range(len(list['entities'])):
        
                dict[list['entities'][j]['text']]=str(list['entities'][j]['labels']) 

    print("le Temps d'execution est :"+str(time.time()-start))
    return (dict)