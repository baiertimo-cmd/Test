# Kaufen oder leasen? Der Fuhrpark der HARO GmbH

Interaktiver Lernpfad zur Unterrichtseinheit „Leasing vs. Kreditkauf“. Es gibt zwei Fassungen:

| Datei | Für wen | Inhalt |
| --- | --- | --- |
| `index.html` | Schülerinnen und Schüler | Lernpfad mit Selbstkontrolle, **ohne** Lösungen |
| `lehrkraft.html` | Lehrkraft | wie oben, plus Lösungen, Erwartungshorizonte, Musterlösung und „Lösung einsetzen“ |

Beide Dateien funktionieren ohne Installation direkt im Browser. Gib der Klasse nur `index.html` weiter.

## Änderungen vornehmen

Beide Fassungen werden aus **einer** Quelldatei erzeugt: `src/lernpfad.html`. Nach einer Änderung dort:

```
python3 build.py
```

Teile nur für die Lehrkraft sind in der Quelle mit `<!--@T-->…<!--@/T-->` (HTML) bzw. `/*@T*/…/*@/T*/` (JavaScript)
markiert. Die Lösungen stehen im Block `/*@SOL*/…/*@/SOL*/`; in der Schülerfassung werden sie durch Prüfsummen ersetzt,
sodass die Selbstkontrolle funktioniert, die Lösungen aber nicht im Quelltext stehen. `build.py` bricht ab, wenn
in der Schülerfassung noch Lösungswerte auftauchen.

## Stationen

| Station | Material | Inhalt |
| --- | --- | --- |
| Start | 02 (Situation, ergänzt) | Mitteilung der Geschäftsführung (Frau Herold, Herr Acar), Eckdaten |
| 01 | 01 + 02 (Infotext, ergänzt) | Infotext Leasingarten, interaktives Strukturraster mit Selbstkontrolle |
| 03 | 03 | Datenblatt beider Angebote, Infokarte Ratendarlehen, Lesecheck |
| 04 | 04 | Rechendossier mit Prüffunktion, Tipps und Ergebnisdiagramm |
| 05 | 05 (ergänzt) | Argumente zuordnen, Was-wäre-wenn-Rechner (Restwert, Zins, Wartung, Rate), Break-even |
| 06 | 06 | Empfehlungsschreiben mit Live-Checkliste, Satzbausteinen und Kopierfunktion |

## Ins Heft

Jede Station endet mit einer Box „Ins Heft“: Form des Hefteintrags, Arbeitsaufträge, ein Button zum Kopieren
von Überschrift und Auftrag sowie ein aufklappbarer Selbstcheck zum Abhaken.

## Lehrkraftfassung

`lehrkraft.html` öffnet mit eingeblendeten Lösungen. Der Schalter „Lösungen anzeigen“ blendet sie aus,
etwa wenn du die Seite am Beamer zuerst ohne Lösungen zeigen möchtest.

## Annahmen

- Fuhrpark: 8 Fahrzeuge à 30.000 € (= 240.000 € Anschaffungswert)
- Ergebnis: Kreditkauf 214.000 €, Leasing 235.200 € → Kreditkauf rechnerisch um 21.200 € günstiger
- Gleichstand bei einem Restwert von ca. 21,2 % (50.800 €)

Eingaben werden nur lokal im Browser gespeichert (localStorage).
