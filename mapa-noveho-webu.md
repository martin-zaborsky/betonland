# BETONLAND — návrh nového webu

**Východisko:** kompletná štruktúra z `sitemap_index.xml` (20 URL). Nič sa nestráca, všetko sa presúva 1:1 alebo sa zlučuje s presmerovaním 301.

---

## 1. Mapa nového webu

### Hlavná navigácia

| # | Stránka | Nová URL | Pôvodná URL | Poznámka |
|---|---------|----------|-------------|----------|
| 1 | Domů | `/` | `/` | prepracovaný layout |
| 2 | Produkty (rozcestník) | `/produkty/` | `/produkty/` | mriežka 6 kategórií s cenami „od“ |
| 3 | Betonové jímky | `/produkty/jimky/` | `/produkty/jimky/` | **zlúčené** so 4 podstránkami – všetky cenníky na jednej stránke |
| 4 | Betonové sklepy | `/produkty/sklepy/` | `/produkty/sklepy/` | **zlúčené** s `/cenik-sklepy/` (7 cenníkových tabuliek) |
| 5 | Vodoměrné šachty | `/produkty/sachty/` | `/produkty/sachty/` | + cenník |
| 6 | Montážní jámy | `/produkty/montazni-jamy/` | `/produkty/montazni-jamy/` | + cenník M1–M5 |
| 7 | Nádrže na vodu | `/produkty/nadrze-na-vodu/` | `/produkty/nadrze-na-vodu/` | **zlúčené** s `/betonove-nadrze-na-vodu/`; opraviť rozbitú tabuľku `[wptb id=7867 not found]` |
| 8 | Příslušenství | `/produkty/prislusenstvi/` | `/produkty/prislusenstvi/` | 9 položiek + cenník |
| 9 | Ceník (súhrnný) | `/cenik/` | — | **nová stránka**: všetky cenníky na jednom mieste + filter |
| 10 | Reference / Realizace | `/reference/` | `/projects/` + `/recenze/` | fotogaléria realizácií + recenzie |
| 11 | Časté otázky | `/casto-kladene-otazky/` | `/faqs/` + `/casto-kladene-otazky/` | **zlúčené**, FAQ schema |
| 12 | Kontakt | `/kontakt/` | `/kontakt/` | formulár, mapa pôsobnosti, údaje výrobcu |
| 13 | Ochrana soukromí | `/ochrana-soukromi/` | `/ochrana-sukromia/` | oprava preklepu (SK slovo na CZ webe) |

### Cenníkové podstránky (zachované kvôli SEO)

Tieto URL majú vlastný vyhľadávací dopyt, preto zostávajú ako samostatné stránky a zároveň sú prelinkované z hlavnej stránky jímek:

| Stránka | URL | Obsah |
|---|---|---|
| Jednokomorové jímky | `/jednokomorove-betonove-jimky/` | 20 rozmerov, 21 000 – 74 000 Kč |
| Dvojkomorové jímky | `/dvojkomorove-betonove-jimky/` | 7 rozmerov, 27 500 – 46 000 Kč |
| Trojkomorové jímky | `/trojkomorove-betonove-jimky/` | 2 rozmery, 43 000 – 49 000 Kč |
| Vícekomorové jímky | `/vicekomorove-betonove-jimky/` | sestavy na mieru |
| Ceník sklepů | `/cenik-sklepy/` | 7 tabuliek (kopulové, rovná strecha, bez dna, s oporným múrom, modulové, so schodiskom) |
| Nádrže na vodu | `/betonove-nadrze-na-vodu/` | → 301 na `/produkty/nadrze-na-vodu/` |

### Nové stránky, ktoré odporúčam pridať

- **`/cenik/`** — jedna stránka so všetkými cenníkmi; najsilnejšia landing page pre „jímka cena“, „betonová jímka cena“
- **`/o-nas/`** — 30+ rokov, výrobca SałexPol, certifikáty, fotky výroby (buduje dôveru, dnes chýba)
- **`/jak-probiha-montaz/`** — príprava výkopu, usadenie, kolaudácia; rieši najčastejšiu obavu zákazníka
- **`/kalkulacka-objemu/`** — „koľko osôb → aký objem jímky“; zbiera kontakt
- **`/blog/`** (voliteľné) — „jímka vs. septik vs. ČOV“, „povolenie k jímke“, „ako často vyvážať“ — dopyty s vysokým objemom hľadania

---

## 2. Čo na súčasnom webe nefunguje

| Problém | Dopad | Riešenie v návrhu |
|---|---|---|
| Rozbitá tabuľka `[wptb id="7867" not found]` na nádržiach | stránka bez cien = stratený dopyt | ceny natvrdo v HTML tabuľke |
| Miešaná slovenčina a čeština („ochrana sukromia“, „po celé Českej republice“) | pôsobí neserióznne na CZ trhu | jednotná čeština |
| Duplicita FAQ (`/faqs/` aj `/casto-kladene-otazky/`) | kanibalizácia v Google | zlúčené + 301 |
| Ceny schované hlboko v štruktúre | užívateľ nenájde cenu do 10 s | cena „od“ pri každom produkte + súhrnný ceník v hlavnom menu |
| Chýba prepočet objemu | zákazník nevie, čo si vybrať | kalkulačka + odporúčania v FAQ |
| Slabá konverzná cesta | dopyt len cez kontaktnú stránku | formulár v hero, lepivá lišta na mobile, CTA po každom cenníku |
| Chýbajú fotky realizácií | nižšia dôvera | galéria referencií (potrebujem od vás fotky) |

---

## 3. Dizajnový smer — monochróm podľa loga

Paleta je odvodená priamo z farieb vášho loga, žiadna cudzia akcentová farba:

| Premenná | Hodnota | Odkiaľ |
|---|---|---|
| `--ink` | `#111213` | slovo **LAND** |
| `--steel` | `#515252` | slovo **BETON** |
| `--stone` | `#a9a8a8` | posunutý svetlosivý štvorec |
| `--paper-2` | `#f3f3f2` | svetlé plochy sekcií |

- **Typografia:** Barlow Condensed (nadpisy, verzálky — ladí s geometrickým groteskom loga) + Inter (text)
- **Textúra:** betónový vzor vyrezaný priamo zo štvorca v logu, použitý v hero, produktových kartách a CTA pruhu
- **Logo:** tmavá verzia na svetlom pozadí, invertovaná svetlá verzia v pätičke a na tmavých plochách
- **CTA:** čierne tlačidlo na svetlom pozadí, biele na tmavom — v monochróme má najvyšší kontrast
- **Fotografia:** reálne realizácie, usadzovanie hydraulickou rukou, detail betónu — nie stock
- **Mobil:** lepivá lišta „Zavolať / Poptávka“, vodorovne skrolovateľné cenníky

---

## 4. Prevod do WordPressu

Kód je pripravený tak, aby sa dal preklopiť do témy bez prepisovania:

- **Šablóny:** `front-page.php`, `single-produkt.php`, `page-cenik.php`, `page.php`, `archive-reference.php`
- **Custom post type:** `produkt` (nahrádza `rebuilto_service`), `reference` (nahrádza `rebuilto_project`)
- **ACF polia:** `cena_od`, `parametry` (repeater), `cenik_tabulka` (repeater: objem / d / š / v / cena), `co_je_v_cene`
- **Cenníky:** repeater v ACF namiesto pluginu WP Table Builder — ceny sa dajú upraviť bez rizika, že sa tabuľka „stratí“
- **CSS:** premenné v `:root`, žiadny build proces, žiadny Bootstrap
- **Formuláre:** WPForms alebo Contact Form 7, notifikácia na `info@betonland.cz`
- **SEO:** Rank Math / Yoast, FAQ + Product + LocalBusiness schema, sitemap
- **Presmerovania:** 301 pre zlúčené a premenované URL (tabuľka v sekcii 1)
- **Rýchlosť:** bez page builderu (Elementor/WPBakery) → cieľ LCP < 1,8 s

---

## 5. Súbory v balíku

| Súbor | Obsah |
|---|---|
| `index.html` | Domov |
| `produkty.html` | Rozcestník sortimentu |
| `jimky.html` | Betonové jímky + 3 cenníky |
| `sklepy.html` | Betonové sklepy + 7 cenníkov |
| `sachty.html` | Vodoměrné šachty + cenník |
| `montazni-jamy.html` | Montážní jámy M1–M5 |
| `nadrze-na-vodu.html` | Nádrže na vodu |
| `prislusenstvi.html` | Příslušenství + cenník |
| `cenik.html` | Súhrnný ceník (všetko na jednej stránke) |
| `reference.html` | Realizácie + recenzie |
| `faq.html` | Časté otázky (+ FAQ schema) |
| `kontakt.html` | Kontakt + poptávkový formulár |
| `ochrana-soukromi.html` | Zásady spracovania údajov (vzor) |
| `assets/style.css` | Celý dizajnový systém, jeden súbor |
| `assets/logo-*.png` | Logo (tmavá + svetlá verzia) |
| `assets/concrete.jpg` | Betónová textúra z loga |
| `build.py` | Generátor — prestavia web po zmene obsahu |

## 6. Ďalší postup

1. Prejsť si web, doladiť texty a ceny
2. Dodať fotky realizácií a logo vo vektore (SVG) — teraz sú v galérii zástupné plochy
3. Preklopenie do WordPressu + migrácia obsahu a presmerovania
4. Kontrola: rýchlosť, mobil, formuláre, indexácia

---

*Ceny v návrhu sú prevzaté z betonland.cz k 17. 8. 2026. Pred spustením treba overiť aktuálnosť — najmä pri nádržiach na vodu, kde cenník na súčasnom webe chýba.*
