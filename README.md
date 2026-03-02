# Currency converter

## Dependencies:
- python3
- pip
- tk


## Starting av appen 

### 1. Installer avhengigheter

Kjør:

> pip install requests FreeSimpleGUI

---

### 2. Opprett virtuelt miljø

Kjør:

> python3 -m venv .venv

Aktiver miljøet:

Mac/Linux:
> source .venv/bin/activate

Windows:
> .venv\Scripts\activate

---

### 3. Start programmet

Kjør:

> python3 convert.py

Programmet vil nå starte.

## Hvordan bruke programmet

1. Start programmet ved å kjøre:

> python3 convert.py

2. Velg valuta du vil konvertere fra i første nedtrekksmeny.

3. Velg valuta du vil konvertere til i andre nedtrekksmeny.

4. Skriv inn beløpet du vil konvertere i input-feltet.

5. Trykk på "Convert".

6. Resultatet vises nederst i vinduet.

7. Trykk på "End" for å avslutte programmet.

## Funksjoner

### MakeList()

- Sender forespørsel til ExchangeRate-API.
- Henter tilgjengelige valutakurser.
- Lager en liste med alle gyldige valutakoder.
- Returnerer listen som brukes i GUI-ens dropdown-menyer.

### ValidCheck(Valuta1, Valuta2, Sum)

- Sjekker om valgt fra-valuta finnes i valutalisten.
- Sjekker om valgt til-valuta finnes i valutalisten.
- Sjekker om beløpet kan konverteres til float.
- Returnerer:
  - Bool for gyldig fra-valuta
  - Bool for gyldig til-valuta
  - Bool for gyldig beløp
  - Beløp som float (hvis gyldig)

### GetValue(key, GC, WRC, amount)

- Sender forespørsel til ExchangeRate-API med valgt base-valuta.
- Henter konverteringsrater.
- Regner ut:
  - Verdien i base-valuta
  - Verdien i ønsket valuta
- Returnerer begge beregnede verdier.

## Programflyt

1. Programmet starter og kaller `MakeList()` for å hente tilgjengelige valutaer.
2. GUI-vinduet opprettes med dropdown-menyer og inputfelt.
3. Når brukeren trykker "Convert":
   - `ValidCheck()` validerer input.
   - Hvis alt er gyldig, kalles `GetValue()`.
   - Resultatet vises i vinduet.
4. Programmet avsluttes når brukeren trykker "End".