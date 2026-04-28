def atualizar_his(hist, paciente):
    
    if paciente in hist:
        hist.remove(paciente)
    hist.append(paciente)
    return hist


def main():
    hist = ['ana', 'carlos', 'beatriz',]
    novo = 'Carlos'
    print(f"Hist atual {hist}")
    hist = atualizar_his(hist, novo)
    print(f"Hist atualizado {hist}")
    
main()