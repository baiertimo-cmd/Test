# Juniorenfirma – Abrechnung

Abrechnungstool für eine Juniorenfirma an einer kaufmännischen Schule. Es besteht aus **einer einzigen Datei**
(`abrechnung.html`) und braucht weder Installation noch Internet. Alle Daten liegen in **einer Datendatei**
(z. B. `juniorenfirma-daten.json`) im gemeinsamen Ordner auf dem Schulserver.

## Funktionen

| Bereich | Was man damit macht |
| --- | --- |
| Übersicht | Kasse, Bankkonto, Einnahmen/Ausgaben und Überschuss des Jahres, offene Rechnungen, Lagerwarnungen, Schnellzugriffe |
| Verkauf & Rechnungen | Barverkauf (sofort bezahlt) oder Rechnung (Kunde zahlt später), Rabatt, Zahlungseingang buchen, stornieren, drucken/PDF |
| Angebote | Angebote erstellen und drucken, per Klick in eine Rechnung umwandeln |
| Einkauf | Wareneinkäufe erfassen (erhöht den Bestand), bezahlt/offen, neue Artikel direkt anlegen |
| Inventar | Artikel mit EK/VK-Preis, Rohgewinn, Bestand, Mindestbestand, Lagerwert, Bestandskorrektur (Inventur, Schwund …), Verlauf, Inventurliste |
| Einnahmen & Ausgaben | alle Zahlungen mit Filter; sonstige Einnahmen/Ausgaben (Spenden, Werbung, Gebühren …) direkt erfassen |
| Auswertung | Einnahmen-Überschuss-Rechnung mit Datumsfilter (Monat, Kalenderjahr, Schuljahr, frei wählbar), Kategorien, Monatsübersicht, verkaufte Artikel, offene Posten; Druck/PDF mit Unterschriftszeilen |
| Kunden & Lieferanten | Adressen, die beim Erstellen von Belegen übernommen werden |
| Einstellungen (nur Lehrkraft) | Firmendaten und Logo, Nummernkreise, Texte, Kategorien, Anfangsbestände Kasse/Bank, Benutzer, Datensicherung, Protokoll |

Alle Listen lassen sich als **CSV** für Excel exportieren. Rechnungen, Angebote, die Auswertung und die
Inventurliste werden über **Drucken / PDF** ausgegeben. Im Druckdialog „Als PDF speichern“ wählen.

### So hängt alles zusammen

- **Verkauf** (Barverkauf oder Rechnung) → Bestand sinkt sofort. Die **Einnahme** wird gebucht, sobald die Rechnung bezahlt ist.
  Ist nicht genug Ware da, verhindert das Tool den Verkauf.
- **Einkauf** → Bestand steigt. Die **Ausgabe** wird gebucht, sobald der Einkauf bezahlt ist.
- **Storno** einer Rechnung → Ware geht zurück ins Lager, die Einnahme entfällt; die Rechnung bleibt als „storniert“ sichtbar.
- **Auswertung** nach dem Zuflussprinzip: Es zählt das Zahlungsdatum. Offene Forderungen/Verbindlichkeiten und der
  Warenbestand werden zusätzlich angezeigt.
- Umsatzsteuer: Es wird von einer nicht umsatzsteuerpflichtigen Juniorenfirma ausgegangen (Hinweis nach § 19 UStG,
  Text in den Einstellungen änderbar).

## Einrichtung auf dem Schulserver

1. `abrechnung.html` in einen Ordner auf dem Schulserver kopieren, auf den Lehrkraft und Schülerfirma Zugriff haben.
2. Die Datei mit **Microsoft Edge** oder **Google Chrome** öffnen (Doppelklick oder Verknüpfung auf dem Desktop).
3. **Neue Datendatei anlegen …** wählen und die Datendatei im selben Ordner speichern.
4. Ersteinrichtung: Name der Juniorenfirma und Konto der Lehrkraft anlegen.
5. Unter **Einstellungen** Firmendaten, Logo, Bankverbindung und Anfangsbestände eintragen und Konten für die
   Schülerinnen und Schüler anlegen.

Danach öffnen alle die Datendatei über **Datendatei öffnen …**. Der Browser merkt sich die zuletzt verwendete Datei.
Jede Änderung wird sofort automatisch gespeichert. Den Speicherstatus zeigt die Seitenleiste links unten.

Mit **Mit Beispieldaten ausprobieren** lässt sich das Tool vorher gefahrlos testen
(Anmeldung `lehrer` / `demo` oder `schueler` / `demo`).

### Hinweise

- **Browser:** Direktes Speichern in die Datei klappt nur in Edge und Chrome. In anderen Browsern (z. B. Firefox)
  kann man arbeiten, muss die Datei aber über „Datei speichern (Download)“ herunterladen und wieder in den
  Ordner legen.
- **Mehrere Arbeitsplätze:** Mehrere Personen können die Datei gleichzeitig geöffnet haben. Änderungen anderer
  werden etwa alle 15 Sekunden übernommen. Speichern zwei Personen fast gleichzeitig, fragt das Tool nach,
  welcher Stand gelten soll.
- **Rollen:** Schülerinnen und Schüler können alles erfassen, bearbeiten, stornieren und drucken, aber nichts
  löschen. Einstellungen und Benutzerverwaltung sind nur für die Lehrkraft zugänglich. Das Protokoll zeigt,
  wer wann was geändert hat.
- **Datenschutz/Sicherheit:** Die Passwörter sind gehasht gespeichert. Die Anmeldung schützt aber nur die
  Bedienoberfläche. Wer Zugriff auf den Ordner hat, kann die Datendatei lesen. Der Ordner sollte daher nur
  für die Juniorenfirma freigegeben sein.
- **Datensicherung:** Unter „Einstellungen → Datensicherung“ regelmäßig eine Sicherung herunterladen,
  mindestens zum Monats- und zum Schuljahresende.
