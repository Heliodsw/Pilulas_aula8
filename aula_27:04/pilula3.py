def atender(fila):
    
    if len(fila) == 0:
        print(" fila vazia")
        return fila
    paciente = fila.pop(0)
    print(f"Atendendo paciente: {paciente}")
    return fila


def main():
    fila = ["ana", "carlos", "beatriz", "joao"]
    print(f"Fila inicial: {fila}")  
    fila = atender(fila)
    print(f"Fila alterada: {fila}")
    
main()
    