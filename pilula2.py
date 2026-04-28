def especialidadeTop(consultas):
    cont = {}
    for c in consultas:
        esp = c["especialidade"]
        if esp not in cont:
            cont[esp] = 0
        cont[esp] += 1
    maior_esp = ""
    max_valor = -1
    for esp in cont:
        if cont[esp] > max_valor:
            max_valor = cont[esp]
            maior_esp = esp
    return maior_esp




def main():
    consultar = [
        {"paciente": "Ana"    , "especialidade": "Cardiologia"},
        {"paciente": "Carlos" , "especialidade": "Ortopedia"  },
        {"paciente": "Beatriz", "especialidade": "Cardiologia"},
        {"paciente": "João"   , "especialidade": "Cardiologia"}
    ]
    print(especialidadeTop(consultar))

main()