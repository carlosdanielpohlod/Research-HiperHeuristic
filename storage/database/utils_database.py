

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
def extrairScoreHeuristica(heuristica):
    score = []
    for i in heuristica:
        score.append(i.score)
    return score
def codStringToNumber(tipoHeuristica_id):
    if(tipoHeuristica_id == "busca local"):
        return 2
    else:
        if(tipoHeuristica_id == "reproducao"):
            return 1
        else:
            if(tipoHeuristica_id == "mutacao"):
                return 3
            else: 
                return tipoHeuristica_id

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