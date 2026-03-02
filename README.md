# Currency converter

dependencies:

python3
pip
tk

 
## For bruker
For at appen skal fungere må du passe på at alle dependencies er lastet ned.

Når du er sikker kan du kjøre:
pip install requests FreeSimpleGUI

Dette er slutten av instalerings fasen.

Så kjører du:
Python3 -m venv .venv  

Dette definerer et virtuelt enviroment, som trengs for å kjøre appen.

Skriv deretter: 
source .venv/bin/activate

Da går du inn i envioromentet.

Når du da skriver: 
python3 convert.py

Så kjører du appen.

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