import json
def carica_studenti(nome_file):
    try:
        with open(nome_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Errore: file '{nome_file}' non trovato.")
        return []
    except json.JSONDecodeError:
        print(f"Errore: il contenuto di '{nome_file}' non è un JSON valido.")
        return []
def calcola_media_materia(studente, materia):
    voti = studente.get("voti", {}).get(materia, [])
    if not voti:
        return 0.0
    return sum(voti) / len(voti)
def calcola_media_generale(studente):
    voti_materie = studente.get("voti", {})
    if not voti_materie:
        return 0.0
    medie = [calcola_media_materia(studente, m) for m in voti_materie]
    return sum(medie) / len(medie) if medie else 0.0
def aggiungi_voto(lista_studenti, id_studente, materia, voto):
    trovato = False
    for studente in lista_studenti:
        if studente["id"] == id_studente:
            trovato = True
            if materia in studente["voti"]:
                studente["voti"][materia].append(voto)
            else:
                studente["voti"][materia] = [voto]
            print(f"Voto {voto} aggiunto per {studente['nome']} {studente['cognome']} in {materia}.")
            return
    if not trovato:
        print(f"Errore: Studente con ID {id_studente} non trovato.")
def genera_report_studenti(lista_studenti):
    print("\n📝 Report Studenti:")
    for studente in lista_studenti:
        print(f"\n📌 {studente['nome']} {studente['cognome']} (ID: {studente['id']})")
        voti_studente = studente.get("voti", {})
        for materia, voti in voti_studente.items():
            media = calcola_media_materia(studente, materia)
            print(f"  - {materia}: Voti = {voti}, Media = {media:.2f}")
        media_generale = calcola_media_generale(studente)
        print(f"  ➤ Media Generale: {media_generale:.2f}")
def trova_miglior_studente(lista_studenti):
    if not lista_studenti:
        return None
    miglior = max(lista_studenti, key=calcola_media_generale)
    return f"{miglior['nome']} {miglior['cognome']}"
if __name__ == "__main__":
    studenti = carica_studenti("studenti.json")

    if studenti:
        genera_report_studenti(studenti)
        print("\n➡️ Aggiunta voto:")
        aggiungi_voto(studenti, "S103", "Matematica", 8)
        print("\n📊 Report aggiornato:")
        genera_report_studenti(studenti)
        miglior = trova_miglior_studente(studenti)
        print(f"\n🏆 Miglior studente: {miglior}")
