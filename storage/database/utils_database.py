def mediaScore(result):
    sum = 0
    i = 0
    for r in result:
        sum = sum + r.score
        i = i + 1
    return sum / i
def getNome(heuristica):
    nome = None
    for i in heuristica:
        nome = i.nome
    return nome
def getCodeHeuristica(heuristica):
    codHeuristica = None
    for i in heuristica:
        codHeuristica = i.codHeuristica
    return codHeuristica
def extrairHeuristicaUsada_id(result):
    resp = []
    for i in result:
        resp.append(i.heuristicaUsada_id)
    return resp