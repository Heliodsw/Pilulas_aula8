
def ranking(paciente):
    ranking_paciente = []
    for paciente in paciente:
        pontos =  0 
        if paciente["gravidade"] >4:
            pontos += 3
        elif paciente["gravidade"] > 2:
            pontos += 2
            
            if paciente["idade"] > 60:
                pontos += 2
                
        ranking_paciente.append({"nome": paciente["nome"], "pontos": pontos})
        
    #bubble sort para ordenar o ranking
    for i in range(len(ranking_paciente)):
        for j in range(i + 1, len(ranking_paciente)):
            if ranking_paciente[i]["pontos"] < ranking_paciente[j]["pontos"]:
                ranking_paciente[i], ranking_paciente[j] = ranking_paciente[j], ranking_paciente[i]

    #print(ranking_paciente)
    for i in range(len(ranking_paciente)):
        print(f"{ranking_paciente[i]['nome']} ,{ranking_paciente[i]['pontos']} pontos")
            

    
   

def main():
    paciente = [
        {"nome": "Ana", "idade": 70, "gravidade": 3},
        {"nome": "Carlos", "idade": 40, "gravidade": 5},
        {"nome": "Beatriz", "idade": 65, "gravidade": 2},
        {"nome": "Joao", "idade": 30, "gravidade": 1},
    ]
    ranking(paciente)
    #print(paciente[1]["nome"], paciente[1]["idade"])
   
main()