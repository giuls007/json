import json
def carica_inventario(nome_file):
    try:
        with open(nome_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Errore: File '{nome_file}' non trovato.")
        return []
    except json.JSONDecodeError:
        print(f"Errore: Il file '{nome_file}' non contiene un JSON valido.")
        return []

def trova_prodotto(inventario, codice_prodotto):
    for prodotto in inventario:
        if prodotto["codice"] == codice_prodotto:
            return prodotto
    return None

def calcola_valore_totale_inventario(inventario):
    return sum(p["prezzo_unitario"] * p["quantita_disponibile"] for p in inventario)

def lista_prodotti_per_categoria(inventario, categoria):
    return [p["nome"] for p in inventario if p["categoria"].lower() == categoria.lower()]

def aggiorna_quantita_prodotto(inventario, codice_prodotto, nuova_quantita):
    if nuova_quantita < 0:
        print("Errore: la quantità non può essere negativa.")
        return
    prodotto = trova_prodotto(inventario, codice_prodotto)
    if prodotto:
        prodotto["quantita_disponibile"] = nuova_quantita
        print(f"Quantità aggiornata per '{prodotto['nome']}' a {nuova_quantita}.")
    else:
        print(f"Prodotto con codice '{codice_prodotto}' non trovato.")

def trova_prodotti_esauriti(inventario):
    return [p["nome"] for p in inventario if p["quantita_disponibile"] == 0]

if __name__ == "__main__":
    inventario = carica_inventario("inventario.json")

    if inventario:
        print("\n📦 INVENTARIO CARICATO")
        valore_totale = calcola_valore_totale_inventario(inventario)
        print(f"\n💰 Valore totale dell'inventario: €{valore_totale:.2f}")
        codice = "P001"
        prodotto = trova_prodotto(inventario, codice)
        if prodotto:
            print(f"\n🔍 Prodotto trovato ({codice}): {prodotto['nome']} - €{prodotto['prezzo_unitario']} (Q: {prodotto['quantita_disponibile']})")
        else:
            print(f"\n❌ Prodotto con codice {codice} non trovato.")

        categoria = "Libri"
        libri = lista_prodotti_per_categoria(inventario, categoria)
        print(f"\n📚 Prodotti nella categoria '{categoria}': {libri}")
        aggiorna_quantita_prodotto(inventario, "L002", 18)
        esauriti = trova_prodotti_esauriti(inventario)
        print(f"\n⚠️ Prodotti esauriti: {esauriti}")
