# Code Review
Datum: 2023-10-22
Autor: Markus Wals, Wals.pro

## Allgemein
### Rechtschreibung
- Der Code und das gesamte Projekt ist voller Rechtschreibfehler, was ihn unprofessionell wirken lässt.
- Auch die Readme ist voller Rechtschreibfehler.
- Fehler im Wort Schema im Ordner Namen ./shemaExamples

### Generelle Form und Namenskonvention
- Es werden generell keine Naming Guidelines für Python verwendet und kein Schema konsistent eingehalten. Snake Case und Camel Case ist wild gemischt, obwohl es in PEP8 klare Regeln gibt, wann was anzuwenden ist. Siehe dazu im File ./naming.md für eine Zusammenfassung dazu.
- Die eigentlich klar vorgegebene Anzahl an Leerzeilen und Spaces ist inkonsistent über das ganze Projekt hinweg.
- Nimm bitte einfach den Problems Tab unten in Pycharm her. Vorher bitte noch das "Grammatik und Spellcheck" Modul für Deutsch herunterladen. So findest du im laufenden Betrieb schneller alle Fehler.
- Vielerorts im Code finden sich "Magic Numbers" die nicht weiter erkärt sind, das ist eine problematische Praktik.

### Herstellung
- Es scheint, als ob die Liste, welche Endpoints unterstützt werden, in vielen Files definiert ist, anstatt zentral in einer Konfigurationsdatei oder besser noch aus der OpenAPI Spezifikation.
- Wenn es um eine reine Connector klasse geht, würde ich eher in Richtung des OpenAPI Generators tendieren und die Klassen aus der OpenAPI Spezifikation zu generieren: https://openapi-generator.tech/.

### Funktionsumfang
- Aus der Readme geht nicht hervor, wie Aktionen an Entitäten ausgeführt werden können, z.B. /salesOrder/id/{id}/createShipment

### Dokumentation
- Die Readme.md ist ok formuliert, hat aber viele Rechtschreibfehler und folgt nicht zu 100% den Best-Practices für eine Readme.md. Hier ein Link zu einem guten Beispiel: https://tianhaozhou.medium.com/readme-best-practices-7c9ad6c2303
- So gut wie überall im Code fehlen die Docstrings der Methoden.
- Die Beispiele im Examples Ordner lassen zu Wünschen übrig. Hier ist nicht auf Anhieb klar, wie das Modul in den vielen Anwendungsfällen eingesetzt werden muss.

### Konsistenz
- Im Code sind einfache und double quotes gemischt. Es sollte nur ein Typ verwendet werden.

### Code
- Ein Review pro Source-File befindet sich jeweils im Ordner der Datei unter <Dateiname>.review.md