---
title: "Datenschutzerklärung"
lang: de
permalink: /privacy/de/
---

# Datenschutzerklärung von Ætherna

_Zuletzt aktualisiert: 24. November 2026_

Ætherna ist eine App zum Hören von Audiogesprächen über Werke. Diese Erklärung beschreibt, was die App und der Ætherna-Server speichern und warum.

## Was wir erheben

- **Kennung deines Apple Accounts.** Wenn du dich mit Apple anmeldest, erhalten wir eine anonyme Kennung, die Apple für diese App erstellt. Wir speichern nur einen verschlüsselten Hash (HMAC) davon, um dein Konto zu erkennen. **Wir fragen weder nach deinem Namen noch nach deiner E-Mail-Adresse und speichern sie nicht.**
- **Gerätesitzung.** Ein Sitzungscode liegt im Schlüsselbund des Geräts; auf dem Server speichern wir nur seinen Hash (SHA-256).
- **Abonnement.** Wenn du Premium abonnierst, speichern wir das Produkt, die Kaufumgebung, das Ablaufdatum und einen verschlüsselten Hash der Apple-Transaktionsnummer, um die bezahlten Funktionen freizuschalten. **Karten- oder Zahlungsdaten erhalten wir nie:** Die Abrechnung übernimmt Apple.
- **Laufende Folge.** Im kostenlosen Tarif merkt sich der Server, welche Folge du gerade hörst, um die Regel „eine Folge nach der anderen“ anzuwenden.

## Was wir nicht erheben

Die App hat keine Werbung, nutzt keine Analyse- oder Tracking-SDKs und verkauft oder teilt keine Daten mit Dritten zu Werbezwecken. Hörverlauf, Positionen und Einstellungen bleiben **auf dem Gerät**.

## Daten auf dem Gerät

Das Sitzungstoken bleibt im Schlüsselbund, nur auf diesem Gerät. Heruntergeladene Folgen liegen im Speicher der App, ausgenommen von Backups. Wiedergabepositionen und Einstellungen liegen im Speicher der App. Wenn du die App löschst, werden diese Daten vom Gerät entfernt.

## Netzwerk und Dienstleister

Die App kommuniziert mit dem Ætherna-Server über HTTPS via Cloudflare, das die IP-Adressen der Verbindungen verarbeitet, um den Datenverkehr zuzustellen und den Dienst zu schützen. Der Server nutzt die IP-Adresse wenige Minuten lang, nur im Arbeitsspeicher, um Missbrauch bei der Registrierung zu begrenzen.

## Konto löschen

Unter Einstellungen → Konto → **Mein Konto löschen** löscht die App auf dem Server dein Konto, deine Sitzungen, das gespeicherte Abonnement und die laufende Folge. Um Abbuchungen zu beenden, kündige das Abo zusätzlich in den Einstellungen deines Apple Accounts.

## Kinder

Ætherna richtet sich nicht an Kinder unter 13 Jahren und erhebt nicht wissentlich Daten von Kindern.

## Kontakt und Änderungen

Fragen zum Datenschutz: Eröffne ein Issue unter https://github.com/JoaoZaokk/aetherna-app/issues. Änderungen dieser Erklärung erscheinen auf dieser Seite, mit dem Datum oben.
