def processar_consultas(registros):
    tempos = {}
    cont = {}
    status = {}
    for reg in registros:
        p = reg["paciente"]
        if p not in tempos:
            tempos[p] = 0
            cont[p] = 0
        tempos[p] += reg["tempo"]
        cont[p] += 1
    
    for p in tempos:
        t = tempos[p]
        if t < 2:
            status[p] = "leve"
        elif t < 5:
            status[p] = "moderado"
        else:
            status[p] = "crítico"

    for p in tempos:
        print({f"{p} | Tempo: {tempos[p]} | Qtd: {cont[p]} | Status: {status[p]}"})

def main():
    registros = [
        {"paciente": "Ana", "tempo":1},
        {"paciente": "Ana", "tempo":2},
        {"paciente": "Carlos", "tempo":4}
    ]
    processar_consultas(registros)

main()