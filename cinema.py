import json

def carica_configurazione_sala(nome_file):
    with open(nome_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def crea_mappa_sala(config):
    righe = config["dimensioni"]["righe"]
    colonne = config["dimensioni"]["colonne"]
    simbolo_libero = config["simbolo_libero"]

    mappa = [[simbolo_libero for _ in range(colonne)] for _ in range(righe)]

    for posto in config["posti_premium"]:
        r = posto["riga"]
        c = posto["colonna"]
        mappa[r][c] = posto["simbolo"]

    for posto in config["posti_occupati"]:
        r = posto["riga"]
        c = posto["colonna"]
        mappa[r][c] = posto["simbolo"]

    return mappa

def visualizza_sala(mappa_sala, config):
    print(config["nome_sala"])
    colonne = len(mappa_sala[0])
    print("  " + " ".join(str(i) for i in range(colonne)))
    for i, riga in enumerate(mappa_sala):
        print(f"{i} " + " ".join(riga))

def prenota_posto(mappa_sala, riga, colonna, config):
    if mappa_sala[riga][colonna] == config["simbolo_libero"]:
        mappa_sala[riga][colonna] = "X"
        return True
    else:
        return False

def conta_posti_liberi(mappa_sala, config):
    simbolo_libero = config["simbolo_libero"]
    return sum(r.count(simbolo_libero) for r in mappa_sala)

config = carica_configurazione_sala("sala_cinema.json")
mappa = crea_mappa_sala(config)

visualizza_sala(mappa, config)

prenota_posto(mappa, 1, 2, config)

visualizza_sala(mappa, config)

print("Posti liberi:", conta_posti_liberi(mappa, config))
