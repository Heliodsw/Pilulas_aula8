def especialidadeTop(consultas):
    cont = {}
    for c in consultas:
        esp = c["especialidade"]
        if esp in cont:
            cont[esp] = 0
            cont[esp] += 1
    
    maior_esp = ""
    max_valor = 1
    for esp in cont:
        if cont[esp] > max_valor:
            max_valor = cont[esp]
            maior_esp = esp
            
            return maior_esp 
        
def main():
    consultar = [
        {"nome": "Ana", "especialidade": "Cardiologia"},
        {"nome": "Carlos", "especialidade": "Ortopedia"},
        {"nome": "Beatriz", "especialidade": "Cardiologia"},
        {"nome": "Joao", "especialidade": "Cardiologia"}
    ]
    especialidadeTop(consultar)
    
    print(especialidadeTop(consultar))
    
main()    