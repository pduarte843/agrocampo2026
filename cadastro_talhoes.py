# AgroCampo - cadastro de talhoes
talhoes = []

def cadastrar_talhao(nome, area_ha, cultura):
    talhoes.append({"nome": nome, "area_ha": area_ha, "cultura": cultura})
    return talhoes[-1]

print(cadastrar_talhao("Talhao 1", 12.5, "Soja"))
