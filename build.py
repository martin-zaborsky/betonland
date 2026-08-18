# -*- coding: utf-8 -*-
"""Generátor statického webu BETONLAND. Spustenie: python3 build.py"""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
TEL = "+420 797 812 444"
TELH = "+420797812444"
MAIL = "info@betonland.cz"

PRODUCTS = [
    ("jimky.html", "Betonové jímky", "Jedno-, dvoj-, troj- a vícekomorové"),
    ("sklepy.html", "Betonové sklepy", "Kopulové i s rovnou střechou"),
    ("sachty.html", "Vodoměrné šachty", "Přípojky, vodoměry, technologie"),
    ("montazni-jamy.html", "Montážní jámy", "Autoservisy, dílny, STK"),
    ("nadrze-na-vodu.html", "Nádrže na vodu", "Zavlažování i průmysl"),
    ("prislusenstvi.html", "Příslušenství", "Poklopy, komíny, desky"),
]
NAV = [("index.html", "Domů"), ("cenik.html", "Ceník"), ("reference.html", "Reference"),
       ("faq.html", "Časté otázky"), ("kontakt.html", "Kontakt")]

GLYPH = {
"jimky": '<svg width="82" height="82" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><path d="M3 8h18v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8Z"/><path d="M3 8l2-3h14l2 3"/><path d="M9 5V3h6v2"/><path d="M3 13h18"/></svg>',
"sklepy": '<svg width="82" height="82" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><path d="M3 20V11a9 9 0 0 1 18 0v9"/><path d="M3 20h18"/><path d="M10 20v-6h4v6"/></svg>',
"sachty": '<svg width="82" height="82" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><rect x="4" y="7" width="16" height="14" rx="1"/><path d="M4 11h16"/><circle cx="12" cy="16" r="2.2"/><path d="M12 7V3"/></svg>',
"jamy": '<svg width="82" height="82" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><path d="M2 12h20"/><path d="M6 12v8h12v-8"/><circle cx="8" cy="8" r="2"/><circle cx="16" cy="8" r="2"/><path d="M10 8h4"/></svg>',
"nadrze": '<svg width="82" height="82" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><path d="M12 3c3.5 4.2 6 7.3 6 10a6 6 0 0 1-12 0c0-2.7 2.5-5.8 6-10Z"/></svg>',
"prisl": '<svg width="82" height="82" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 4v3M12 17v3M4 12h3M17 12h3"/></svg>',
}

# ---------------------------------------------------------------- shell
def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{extra}</head>
<body>"""

def header(active):
    prod_items = "".join(
        f'<a href="{u}">{n}<small>{s}</small></a>' for u, n, s in PRODUCTS)
    def act(u):
        return ' class="active"' if active == u else ''
    nav = ""
    for u, n in NAV:
        if u == "index.html":
            nav += f'<a href="{u}"{act(u)}>{n}</a>'
    is_prod = active in [p[0] for p in PRODUCTS] + ["produkty.html"]
    nav += (f'<div class="dd{" active" if is_prod else ""}"><button>Produkty ▾</button>'
            f'<div class="dd-menu"><a href="produkty.html"><b>Všechny produkty</b><small>Přehled celého sortimentu</small></a>{prod_items}</div></div>')
    for u, n in NAV[1:]:
        nav += f'<a href="{u}"{act(u)}>{n}</a>'
    mnav = "".join(f'<a href="{u}">{n}</a>' for u, n in NAV[:1])
    mnav += '<div class="grpname">Produkty</div>'
    mnav += "".join(f'<a href="{u}">{n}</a>' for u, n, _ in PRODUCTS)
    mnav += '<div class="grpname">Informace</div>'
    mnav += "".join(f'<a href="{u}">{n}</a>' for u, n in NAV[1:])
    return f"""
<div class="topbar"><div class="wrap">
  <div class="grp hide-sm"><a href="tel:{TELH}">☎ {TEL}</a><a href="mailto:{MAIL}">✉ {MAIL}</a></div>
  <div class="grp"><span class="promo">AKCE: −50 % na přejezdovou desku</span><span>Působíme po celé ČR</span></div>
</div></div>

<header class="site"><div class="wrap">
  <a class="logo" href="index.html"><img src="assets/logo-192.png" alt="BETONLAND" width="605" height="192"></a>
  <nav class="main">{nav}</nav>
  <div class="hdr-cta">
    <span class="hdr-phone">{TEL}</span>
    <a class="btn btn-primary" href="kontakt.html#poptavka">Nezávazná poptávka</a>
    <button class="burger" aria-label="Menu" onclick="document.getElementById('mnav').classList.toggle('open')">☰</button>
  </div>
</div>
<div id="mnav"><div class="wrap">{mnav}</div></div>
</header>"""

def cta_band():
    return f"""
<div class="cta"><div class="tex"></div><div class="wrap">
  <div><h2>Řekněte nám rozměr, my řekneme cenu</h2>
  <p>Ozveme se do 24 hodin s pevnou cenou včetně dopravy a termínem montáže.</p></div>
  <div style="display:flex;gap:13px;flex-wrap:wrap">
    <a class="btn btn-light" href="tel:{TELH}">☎ {TEL}</a>
    <a class="btn btn-ghost" href="kontakt.html#poptavka">Nezávazná poptávka</a>
  </div>
</div></div>"""

def footer():
    prod = "".join(f'<li><a href="{u}">{n}</a></li>' for u, n, _ in PRODUCTS)
    return f"""
<footer class="site"><div class="wrap">
  <div class="f-grid">
    <div>
      <a class="logo" href="index.html"><img src="assets/logo-light-192.png" alt="BETONLAND" width="605" height="192"></a>
      <p>Výroba a montáž betonových jímek, sklepů, vodoměrných šachet, montážních jam a nádrží na vodu. Působíme po celé České republice.</p>
    </div>
    <div><h5>Produkty</h5><ul>{prod}</ul></div>
    <div><h5>Informace</h5><ul>
      <li><a href="cenik.html">Ceníky</a></li>
      <li><a href="faq.html">Časté otázky</a></li>
      <li><a href="reference.html">Reference</a></li>
      <li><a href="kontakt.html">Kontakt</a></li>
      <li><a href="ochrana-soukromi.html">Ochrana soukromí</a></li>
    </ul></div>
    <div><h5>Kontakt</h5><ul>
      <li><a href="tel:{TELH}">{TEL}</a></li>
      <li><a href="mailto:{MAIL}">{MAIL}</a></li>
      <li>Výrobce: SałexPol<br>Owadów 22A, 26-631 Jastrzębia</li>
      <li>DIČ: PL8121660308</li>
    </ul></div>
  </div>
  <div class="f-bottom"><span>© 2026 BETONLAND. Všechna práva vyhrazena.</span><span>Záruka je poskytována přímo výrobcem.</span></div>
</div></footer>

<div class="callbar">
  <a class="btn btn-light" href="tel:{TELH}">☎ Zavolat</a>
  <a class="btn btn-ghost" href="kontakt.html#poptavka">Poptávka</a>
</div>
</body></html>"""

def page(fn, title, desc, active, body, extra_head=""):
    doc = head(title, desc, extra_head) + header(active) + body + cta_band() + footer()
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(doc)
    return fn

# ---------------------------------------------------------------- parts
def hero_page(crumbs, eyebrow, h1, lead, actions, right=""):
    cr = " / ".join(crumbs)
    r = f'<div>{right}</div>' if right else ""
    grid_open = '<div class="hero-grid">' if right else '<div>'
    grid_close = '</div>' if right else '</div>'
    return f"""
<div class="hero"><div class="tex"></div><div class="veil"></div><div class="wrap hero-page">
  <div class="crumbs">{cr}</div>
  {grid_open}
    <div>
      <div class="eyebrow on-dark">{eyebrow}</div>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="hero-actions">{actions}</div>
    </div>
    {r}
  {grid_close}
</div></div>"""

def hero_simple(crumbs, eyebrow, h1, lead):
    cr = " / ".join(crumbs)
    return f"""
<div class="hero"><div class="tex"></div><div class="veil"></div><div class="wrap hero-simple">
  <div class="crumbs">{cr}</div>
  <div class="eyebrow on-dark">{eyebrow}</div>
  <h1 style="max-width:20ch">{h1}</h1>
  <p class="lead" style="max-width:62ch;margin-top:18px">{lead}</p>
</div></div>"""

def table(cap, headers, rows, price_idx=-1):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = ""
    for r in rows:
        tds = ""
        for i, c in enumerate(r):
            cls = ' class="cena"' if i == (len(r) - 1 if price_idx == -1 else price_idx) else ""
            tds += f"<td{cls}>{c}</td>"
        tb += f"<tr>{tds}</tr>"
    capd = f'<div class="cap">{cap}</div>' if cap else ""
    return (f'<div class="tblbox">{capd}<div class="scroll"><table class="p">'
            f'<thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div></div>')

def faq_items(items, open_first=True):
    out = ""
    for i, (q, a) in enumerate(items):
        o = " open" if (i == 0 and open_first) else ""
        out += f'<details class="faq"{o}><summary>{q}</summary><p>{a}</p></details>'
    return out

def prodcard(url, glyph, title, text, price, sub, more="Ceník a rozměry →", tag=""):
    tg = f'<span class="tag">{tag}</span>' if tag else ""
    return f"""<a class="card" href="{url}">
  <div class="ph">{tg}<span class="glyph">{GLYPH[glyph]}</span></div>
  <div class="body"><h3>{title}</h3><p>{text}</p>
  <div class="price">{price}<small>{sub}</small></div><span class="more">{more}</span></div></a>"""

def form_block(idattr="poptavka", flat=False, title="Nezávazná poptávka",
               sub="Ozveme se do 24 hodin s konkrétní cenou včetně dopravy."):
    cls = "card-form flat" if flat else "card-form"
    opts = "".join(f"<option>{n}</option>" for _, n, _ in PRODUCTS)
    return f"""<div class="{cls}" id="{idattr}">
  <h3>{title}</h3><p class="sm">{sub}</p>
  <form onsubmit="event.preventDefault();this.innerHTML='<p style=\\'padding:36px 0;text-align:center;font-weight:600\\'>Děkujeme, ozveme se do 24 hodin.</p>'">
    <div class="row2">
      <div class="field"><label>Jméno a příjmení *</label><input required></div>
      <div class="field"><label>Telefon *</label><input type="tel" required placeholder="+420"></div>
    </div>
    <div class="field"><label>E-mail *</label><input type="email" required></div>
    <div class="row2">
      <div class="field"><label>Co potřebujete?</label><select>{opts}<option>Nevím, poraďte mi</option></select></div>
      <div class="field"><label>Objem / rozměr</label><input placeholder="např. 10 m³"></div>
    </div>
    <div class="field"><label>Obec / PSČ montáže</label><input placeholder="např. 250 01 Brandýs nad Labem"></div>
    <div class="field"><label>Zpráva</label><textarea rows="3" placeholder="Termín, přístup na pozemek, doplňky…"></textarea></div>
    <button class="btn btn-primary" type="submit">Odeslat poptávku</button>
    <p class="note">Odesláním souhlasíte se <a href="ochrana-soukromi.html">zpracováním osobních údajů</a>.</p>
  </form></div>"""

# ---------------------------------------------------------------- data
JIMKY_1K = [
 ("2 m³","1,5 m","1,2 m","1,62 m","21 000 Kč"),("3 m³","3,0 m","2,40 m","0,60 m","21 000 Kč"),
 ("4 m³","2,5 m","2,0 m","1,12 m","22 000 Kč"),("5 m³","2,5 m","2,0 m","1,42 m","23 000 Kč"),
 ('6 m³ <span class="badge">nejprodávanější</span>',"2,5 m","2,0 m","1,62 m","24 500 Kč"),
 ("6 m³ (nízká)","4,0 m","2,4 m","0,95 m","26 000 Kč"),("7 m³","3,0 m","2,4 m","1,37 m","29 000 Kč"),
 ("8 m³","3,0 m","2,4 m","1,52 m","30 500 Kč"),("8 m³ (vysoká)","2,4 m","2,0 m","2,12 m","32 000 Kč"),
 ("9 m³","3,0 m","2,4 m","1,62 m","32 000 Kč"),
 ('10 m³ <span class="badge">nejprodávanější</span>',"3,0 m","2,4 m","1,82 m","34 000 Kč"),
 ("10 m³ (delší)","3,4 m","2,4 m","1,65 m","35 000 Kč"),("12 m³","4,0 m","2,4 m","1,65 m","38 000 Kč"),
 ("12 m³ (vysoká)","3,0 m","2,4 m","2,15 m","38 000 Kč"),("13 m³","3,0 m","2,4 m","2,32 m","41 000 Kč"),
 ("14 m³","4,0 m","2,4 m","1,91 m","43 000 Kč"),("14 m³ (vysoká)","3,4 m","2,4 m","2,20 m","43 000 Kč"),
 ("15 m³","3,0 m","2,4 m","2,65 m","47 000 Kč"),("18 m³","4,0 m","2,4 m","2,45 m","54 000 Kč"),
 ("22 m³","4,5 m","2,5 m","2,45 m","74 000 Kč"),
]
JIMKY_2K = [
 ("6 m³","2,5 m","2,0 m","1,62 m","27 500 Kč"),("7 m³","3,0 m","2,4 m","1,37 m","30 500 Kč"),
 ("8 m³","3,0 m","2,4 m","1,52 m","32 000 Kč"),("10 m³","3,0 m","2,4 m","1,82 m","36 000 Kč"),
 ("12 m³","4,0 m","2,4 m","1,65 m","40 000 Kč"),("12 m³ (vysoká)","3,0 m","2,4 m","2,15 m","40 000 Kč"),
 ("14 m³","4,0 m","2,4 m","1,90 m","46 000 Kč"),
]
JIMKY_3K = [("12 m³","4,0 m","2,4 m","1,65 m","43 000 Kč"),("14 m³","4,0 m","2,4 m","1,91 m","49 000 Kč")]
H_JIMKY = ["Objem","Délka","Šířka","Výška s deskou","Cena bez DPH"]

H_KUP = ["Délka","Šířka","Výška s kupolí","Výška bez kupole","Vnitřní d.","Vnitřní š.","Vnitřní v.","Cena bez DPH"]
H_ROV = ["Délka","Šířka","Výška vnější","Vnitřní d.","Vnitřní š.","Vnitřní v.","Cena bez DPH"]
SK_KUP = [
 ("3,0 m","2,4 m","2,4 m","1,4 m","2,8 m","2,2 m","2,2 m","42 000 Kč"),
 ("3,4 m","2,4 m","2,3 m","1,5 m","3,2 m","2,2 m","2,1 m","48 000 Kč"),
 ("3,4 m","2,4 m","2,5 m","1,5 m","3,2 m","2,2 m","2,3 m","51 000 Kč"),
 ("3,9 m","2,4 m","2,5 m","1,5 m","3,7 m","2,2 m","2,3 m","58 000 Kč"),
 ("4,5 m","2,5 m","2,45 m","1,5 m","4,3 m","2,3 m","2,25 m","74 000 Kč"),
]
SK_KUP_LONG = [("3,9 m","2,4 m","2,5 m","1,5 m","3,7 m","2,2 m","2,3 m","60 500 Kč")]
SK_ROV = [
 ("2,4 m","2,0 m","2,18 m","2,2 m","1,8 m","1,9 m","34 000 Kč"),
 ("3,0 m","2,4 m","2,18 m","2,8 m","2,2 m","1,9 m","41 000 Kč"),
 ("3,0 m","2,4 m","2,32 m","2,8 m","2,2 m","2,1 m","45 000 Kč"),
 ("3,4 m","2,4 m","2,25 m","3,2 m","2,2 m","2,0 m","46 000 Kč"),
]
SK_BEZDNA = [
 ("3,0 m","2,4 m","2,4 m","1,4 m","2,8 m","2,2 m","2,2 m","62 000 Kč"),
 ("3,4 m","2,4 m","2,3 m","1,5 m","3,2 m","2,2 m","2,1 m","68 000 Kč"),
 ("3,4 m","2,4 m","2,5 m","1,5 m","3,2 m","2,2 m","2,3 m","71 000 Kč"),
 ("3,9 m","2,4 m","2,5 m","1,5 m","3,7 m","2,2 m","2,3 m","78 000 Kč"),
 ("4,5 m","2,5 m","2,45 m","1,5 m","4,3 m","2,3 m","2,25 m","94 000 Kč"),
]
SK_OPORA = [
 ("3,0 m","2,4 m","2,18 m","2,8 m","2,2 m","1,9 m","43 500 Kč"),
 ("3,4 m","2,4 m","2,25 m","3,2 m","2,2 m","2,0 m","49 500 Kč"),
]
SK_MODUL = [
 ("3,9 m","2,4 m","2,55 m","3,7 m","2,2 m","2,3 m","55 000 Kč"),
 ("4,5 m","2,5 m","2,45 m","4,3 m","2,3 m","2,2 m","74 000 Kč"),
]
SK_SCHODY = SK_BEZDNA

SACHTY = [("2 m³","1,5 m","1,2 m","1,62 m","21 000 Kč"),("8 m³","2,4 m","2,0 m","2,12 m","32 000 Kč")]
JAMY = [("M1","350 × 120 × 170 cm","30 000 Kč"),("M2","400 × 120 × 170 cm","35 000 Kč"),
        ("M3","450 × 120 × 170 cm","39 000 Kč"),("M4","560 × 120 × 170 cm","45 000 Kč"),
        ("M5","600 × 120 × 170 cm","49 000 Kč")]
PRISL = [
 ("Litinový poklop do 3,5 t","pochozí i pojezdový do 3,5 t","2 500 Kč"),
 ('Přejezdová deska <span class="badge">akce −50 %</span>',"zpevnění nad jímkou pro přejezd","2 500 Kč"),
 ("TIR deska","pro zatížení nákladními vozidly","4 500 Kč"),
 ("Betonový komín 1 m","nástavba vstupu","3 000 Kč"),
 ("Betonový komín 0,5 m","nástavba vstupu","1 500 Kč"),
 ("Betonový komín 0,25 m","dorovnání výšky terénu","750 Kč"),
 ("Litinový poklop D125","zatížení do 12,5 t","5 500 Kč"),
 ("Litinový poklop D400","zatížení do 40 t","7 500 Kč"),
 ("Měřič hladiny kapaliny","signalizace naplnění jímky","3 000 Kč"),
]

FAQ_MONTAZ = [
 ("Co je potřeba připravit před instalací jímky?","Především je nutné zajistit přístup nákladního vozidla k výkopu, do kterého bude nádrž usazena. Výkop by měl být zhruba o půl metru větší než rozměry nádrže. Dno vhodně pokryjte 10cm vrstvou jemného kameniva (cca 3 mm). Zajistěte také přívod elektrické energie."),
 ("Je potřeba jeřáb?","Ne. Naši pracovníci usadí jímku pomocí hydraulického ramene z vozidla, a to bez dodatečných nákladů."),
 ("Jak dlouho trvá montáž jímky?","Montáž jímky trvá přibližně 45 minut."),
 ("Co je potřeba udělat po usazení jímky?","Počkejte asi 24 hodin, než zaschne lepidlo nebo montážní pěna. Poté můžete jímku obsypat zeminou – betonování není nutné."),
 ("Máte k jímce dokumentaci?","Ano. Certifikát ke kolaudaci i záruční list vám předáme ihned po montáži. Záruka je poskytována přímo výrobcem."),
]
FAQ_VYBER = [
 ("Jak velkou jímku potřebuji?","Orientačně se počítá zhruba 100–150 litrů na osobu a den. Pro čtyřčlennou domácnost s vyvážením přibližně jednou měsíčně proto obvykle doporučujeme jímku 10–14 m³. Rádi vám velikost spočítáme podle vaší konkrétní spotřeby vody."),
 ("Jaký je rozdíl mezi jedno-, dvoj- a tříkomorovou jímkou?","Jednokomorová jímka slouží k prostému shromažďování odpadní vody. Ve dvoukomorové se v první komoře usazují pevné látky a ve druhé se zachytí jemnější částice, čímž se prodlouží interval vyvážení kalu. Tříkomorová přidává třetí stupeň dočištění."),
 ("Je lepší beton, nebo plast?","Betonová jímka se díky své hmotnosti nemusí obetonovávat ani kotvit proti vztlaku spodní vody a odolává zatížení terénem. Plastová nádrž je lehčí na manipulaci, ale zpravidla vyžaduje obetonování."),
 ("Vyrobíte jímku na míru?","Ano. Vícekomorové nádrže lze propojit a vytvořit tak sestavu prakticky libovolné kapacity. Napište nám požadovaný objem a připravíme nabídku."),
]
FAQ_DOPRAVA = [
 ("Kam všude dovážíte?","Působíme po celé České republice. Cenu dopravy spočítáme podle místa montáže a sdělíme ji v nabídce."),
 ("Je montáž opravdu zdarma?","Ano, usazení hydraulickou rukou provádíme zdarma, pokud je k místu složení dostatečný přístup pro nákladní vozidlo."),
 ("Jak dlouho trvá dodání?","Standardně do 4 dnů od potvrzení objednávky."),
 ("Jsou ceny s DPH?","Ne. Všechny ceny v cenících jsou uvedeny bez DPH a bez ceny za dopravu."),
]

REVIEWS = [
 ("★★★★★","„Jímku 10 m³ přivezli třetí den po objednávce. Usazení trvalo necelou hodinu, papíry ke kolaudaci jsme dostali na místě.“","Jan P.","Kolín · jímka 10 m³"),
 ("★★★★★","„Vybírali jsme mezi plastem a betonem. Beton vyhrál cenou i tím, že se nemusí obetonovávat. Zatím naprostá spokojenost.“","Marie K.","Písek · dvoukomorová jímka 8 m³"),
 ("★★★★★","„Kopulový sklep vypadá skvěle, teplota drží stabilně po celý rok. Domluva i doprava bez problémů.“","Petr H.","Znojmo · sklep 3,4 × 2,4 m"),
 ("★★★★★","„Montážní jáma M3 do dílny. Přesně podle rozměrů, usazení hydraulickou rukou během dopoledne.“","Autoservis Vosáhlo","Hradec Králové · jáma M3"),
 ("★★★★★","„Vodoměrná šachta k novostavbě. Rychlá komunikace, cena přesně podle ceníku, žádné příplatky navíc.“","Lukáš M.","Beroun · šachta 2 m³"),
 ("★★★★★","„Objednávali jsme dvě jímky na chalupu a hospodářskou budovu. Obě usadili během jednoho dne.“","Rodina Nováková","Tábor · 2× jímka 8 m³"),
]

# ---------------------------------------------------------------- pages
def build_index():
    cards = (
      prodcard("jimky.html","jimky","Betonové jímky","Jedno-, dvoj-, troj- i vícekomorové jímky 2–22 m³ pro odpadní vody tam, kde není kanalizace.","od 21 000 Kč","bez DPH a dopravy",tag="nejprodávanější")
    + prodcard("sklepy.html","sklepy","Betonové sklepy","Kopulové i s rovnou střechou, se schodištěm nebo bez dna. Stabilní teplota pro víno, ovoce i zeleninu.","od 34 000 Kč","bez DPH a dopravy")
    + prodcard("sachty.html","sachty","Vodoměrné šachty","Prefabrikované šachty pro přípojky novostaveb, vodoměry a technologie bazénů či studní.","od 21 000 Kč","bez DPH a dopravy")
    + prodcard("montazni-jamy.html","jamy","Montážní jámy","Pět velikostí M1–M5 pro autoservisy, dílny a stanice STK. Délky 350 až 600 cm.","od 30 000 Kč","bez DPH a dopravy")
    + prodcard("nadrze-na-vodu.html","nadrze","Nádrže na vodu","Železobeton B35 odolný korozi i praskání. Od zahradního zavlažování až po průmyslové využití.","na dotaz","cenu spočítáme do 24 h","Zjistit cenu →")
    + prodcard("prislusenstvi.html","prisl","Příslušenství","Litinové poklopy do 3,5 t i D400, betonové komíny, přejezdové a TIR desky, měřiče hladiny.","od 750 Kč","bez DPH","Zobrazit ceník →",tag="akce −50 %"))

    revs = "".join(f'<div class="review"><div class="stars">{s}</div><p>{t}</p><b>{n}</b><small>{m}</small></div>'
                   for s,t,n,m in REVIEWS[:3])

    body = f"""
<div class="hero"><div class="tex"></div><div class="veil"></div><div class="wrap hero-home">
  <div>
    <div class="eyebrow on-dark">Výroba a montáž · více než 30 let zkušeností</div>
    <h1>Betonové jímky, sklepy a nádrže <em>usazené do 4 dnů</em></h1>
    <p class="lead">Vyrábíme z certifikovaného vibrovaného betonu C25/30 s ocelovou výztuží 8–10 mm. Nádrž přivezeme, hydraulickou rukou usadíme do výkopu a předáme certifikát ke kolaudaci – montáž je zdarma.</p>
    <div class="hero-actions">
      <a class="btn btn-light" href="#poptavka">Spočítat cenu zdarma →</a>
      <a class="btn btn-ghost" href="cenik.html">Zobrazit ceník</a>
    </div>
    <div class="trustline">
      <span><i>✓</i>Montáž hydraulickou rukou zdarma</span>
      <span><i>✓</i>Záruka 5 let od výrobce</span>
      <span><i>✓</i>Certifikát ke kolaudaci</span>
    </div>
  </div>
  {form_block("poptavka")}
</div></div>

<div class="usp"><div class="wrap">
  <div class="item"><span class="ic">Kč</span><div><b>Nejlepší cena</b><small>Garantujeme nejvýhodnější cenu na trhu</small></div></div>
  <div class="item"><span class="ic">⛟</span><div><b>Montáž zdarma</b><small>Usazení hydraulickou rukou bez příplatku</small></div></div>
  <div class="item"><span class="ic">4</span><div><b>Dodání do 4 dnů</b><small>Od potvrzení objednávky</small></div></div>
  <div class="item"><span class="ic">✓</span><div><b>Záruka 5 let</b><small>Přímo od výrobce, vč. certifikátu</small></div></div>
</div></div>

<section id="produkty">
  <div class="wrap">
    <div class="sec-head"><div class="txt">
      <div class="eyebrow">Sortiment</div><h2>Co pro vás vyrobíme</h2>
      <p class="lead">Šest produktových řad, všechny z vodonepropustného železobetonu s asfaltovou izolací. U každé najdete kompletní ceník s rozměry.</p>
    </div><a class="btn btn-outline" href="produkty.html">Všechny produkty →</a></div>
    <div class="prod-grid">{cards}</div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="sec-head"><div class="txt">
      <div class="eyebrow on-dark">Jak to probíhá</div><h2>Od poptávky k hotové jímce za 4 dny</h2>
      <p class="lead">Montáž samotné jímky trvá zhruba 45 minut. Jeřáb nepotřebujete – nádrž usadíme hydraulickým ramenem přímo z vozidla.</p>
    </div></div>
    <div class="steps">
      <div class="step"><h4>Poptávka</h4><p>Zavoláte nebo vyplníte formulář. Do 24 hodin dostanete pevnou cenu včetně dopravy a montáže.</p></div>
      <div class="step"><h4>Příprava výkopu</h4><p>Výkop o cca 0,5 m větší než nádrž, dno s 10cm vrstvou jemného kameniva a přístup pro nákladní vozidlo.</p></div>
      <div class="step"><h4>Dovoz a usazení</h4><p>Přivezeme a hydraulickou rukou usadíme. Montáž trvá přibližně 45 minut a je zdarma.</p></div>
      <div class="step"><h4>Předání</h4><p>Předáme certifikát ke kolaudaci a záruční list. Po 24 hodinách můžete jímku obsypat zeminou.</p></div>
    </div>
    <div class="stats">
      <div class="stat"><b>30+</b><span>let zkušeností s výrobou</span></div>
      <div class="stat"><b>4</b><span>dny průměrná dodací lhůta</span></div>
      <div class="stat"><b>5</b><span>let záruka od výrobce</span></div>
      <div class="stat"><b>C25/30</b><span>certifikovaný vibrovaný beton</span></div>
    </div>
  </div>
</section>

<section class="grey">
  <div class="wrap">
    <div class="sec-head"><div class="txt">
      <div class="eyebrow">Ceník</div><h2>Ceny máme veřejné</h2>
      <p class="lead">Ukázka nejžádanějších jednokomorových jímek. Kompletní ceníky všech produktů najdete na jedné stránce.</p>
    </div><a class="btn btn-outline" href="cenik.html">Celý ceník →</a></div>
    {table("", H_JIMKY, [JIMKY_1K[2],JIMKY_1K[4],JIMKY_1K[7],JIMKY_1K[10],JIMKY_1K[12]])}
    <p class="note">Ceny jsou uvedeny bez DPH a bez dopravy. Součástí každé jímky je horní deska 120 mm, komín 500 mm a betonové víko.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><div class="txt"><div class="eyebrow">Reference</div><h2>Co říkají zákazníci</h2></div>
      <a class="btn btn-outline" href="reference.html">Všechny reference →</a></div>
    <div class="reviews">{revs}</div>
  </div>
</section>

<section class="grey">
  <div class="wrap" style="max-width:920px">
    <div class="sec-head center"><div class="txt"><div class="eyebrow">Časté otázky</div><h2>Na co se ptáte nejčastěji</h2></div></div>
    {faq_items(FAQ_MONTAZ)}
    <div style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="faq.html">Všechny otázky a odpovědi →</a></div>
  </div>
</section>"""
    return page("index.html","BETONLAND – Betonové jímky, sklepy a nádrže na vodu | Montáž zdarma",
                "Výroba a montáž betonových jímek, sklepů, šachet, montážních jam a nádrží na vodu. Certifikovaný beton C25/30, dodání do 4 dnů, montáž zdarma, záruka 5 let. Působíme po celé ČR.",
                "index.html", body)

def build_produkty():
    cards = (
      prodcard("jimky.html","jimky","Betonové jímky","Jedno-, dvoj-, troj- i vícekomorové jímky 2–22 m³ z betonu C25/30 pro likvidaci odpadních vod.","od 21 000 Kč","bez DPH a dopravy")
    + prodcard("sklepy.html","sklepy","Betonové sklepy","Sedm provedení – kopulové, s rovnou střechou, modulové, se schodištěm i bez dna.","od 34 000 Kč","bez DPH a dopravy")
    + prodcard("sachty.html","sachty","Vodoměrné šachty","Pro přípojky novostaveb, umístění vodoměru mimo objekt a technologie bazénů či studní.","od 21 000 Kč","bez DPH a dopravy")
    + prodcard("montazni-jamy.html","jamy","Montážní jámy","Pět velikostí M1–M5 pro autoservisy, montážní dílny a stanice technické kontroly.","od 30 000 Kč","bez DPH a dopravy")
    + prodcard("nadrze-na-vodu.html","nadrze","Nádrže na vodu","Železobeton B35 pro shromažďování a skladování vody – zavlažování, hospodářství i průmysl.","na dotaz","cenu spočítáme do 24 h","Zjistit cenu →")
    + prodcard("prislusenstvi.html","prisl","Příslušenství","Litinové poklopy, betonové komíny, přejezdové a TIR desky, měřiče hladiny kapaliny.","od 750 Kč","bez DPH","Zobrazit ceník →"))
    body = hero_simple(['<a href="index.html">Domů</a>','<span style="color:#fff">Produkty</span>'],
        "Sortiment", "Betonové prefabrikáty pro dům, zahradu i dílnu",
        "Vše vyrábíme z certifikovaného vibrovaného betonu s ocelovou výztuží a asfaltovou izolací. Dopravu i usazení hydraulickou rukou zajišťujeme po celé České republice.") + f"""
<section><div class="wrap"><div class="prod-grid">{cards}</div>
<p class="note" style="margin-top:26px">Všechny ceny jsou uvedeny bez DPH a bez ceny za dopravu. Osazení provádíme zdarma, pokud je k místu složení dostatečný přístup.</p></div></section>

<section class="dark"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow on-dark">Společné pro celý sortiment</div><h2>Proč beton</h2></div></div>
  <div class="bens">
    <div class="ben"><div class="ic">1</div><h4>Dlouhá životnost</h4><p>Certifikovaný vibrovaný beton s ocelovou výztuží vydrží desítky let bez ztráty pevnosti.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Vodotěsnost</h4><p>Vodonepropustná konstrukce s asfaltovou izolací brání únikům i vnikání spodní vody.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Stabilita</h4><p>Vlastní hmotnost udrží nádrž na místě i při vysoké hladině spodní vody – betonování není nutné.</p></div>
  </div>
</div></section>"""
    return page("produkty.html","Produkty – betonové jímky, sklepy, šachty a jámy | BETONLAND",
                "Přehled sortimentu BETONLAND: betonové jímky, sklepy, vodoměrné šachty, montážní jámy, nádrže na vodu a příslušenství. Ceny, rozměry, montáž zdarma.",
                "produkty.html", body)

def build_jimky():
    spec = """<div class="spec-box"><h4>Parametry ve zkratce</h4>
      <div class="spec-row"><span>Objemy</span><b>2 – 22 m³</b></div>
      <div class="spec-row"><span>Beton</span><b>C25/30, vibrovaný, certifikovaný</b></div>
      <div class="spec-row"><span>Výztuž</span><b>ocelové pruty 8–10 mm</b></div>
      <div class="spec-row"><span>Izolace</span><b>asfaltový nátěr</b></div>
      <div class="spec-row"><span>Provedení</span><b>1-, 2-, 3- a vícekomorové</b></div>
      <div class="spec-row"><span>Montáž</span><b>zdarma, cca 45 minut</b></div>
      <div class="spec-row"><span>Dodání</span><b>do 4 dnů</b></div>
      <div class="spec-row"><span>Záruka</span><b>5 let od výrobce</b></div></div>"""
    body = hero_page(['<a href="index.html">Domů</a>','<a href="produkty.html">Produkty</a>','<span style="color:#fff">Betonové jímky</span>'],
        "Beton C25/30 · výztuž 8–10 mm", "Betonové jímky <em>od 2 do 22 m³</em>",
        "Jímky vyrábíme z vysoce kvalitního certifikovaného vibrovaného betonu C25/30 s ocelovou výztuží o průměru 8–10 mm a asfaltovou izolací. Vodonepropustné, odolné chemicky i biologicky, s minimální údržbou.",
        '<a class="btn btn-light" href="#cenik">Přejít na ceník ↓</a><a class="btn btn-ghost" href="kontakt.html#poptavka">Nezávazná poptávka</a>',
        spec) + f"""
<div class="jump"><div class="wrap">
  <a href="#typy">Typy jímek</a><a href="#cenik">Jednokomorové</a><a href="#cenik-2k">Dvoukomorové</a>
  <a href="#cenik-3k">Tříkomorové</a><a href="#vicekomorove">Vícekomorové</a><a href="#proc">Proč beton</a><a href="#faq">Časté otázky</a>
</div></div>

<section id="typy"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Provedení</div>
  <h2>Čtyři typy podle toho, co potřebujete</h2>
  <p class="lead">Čím více komor, tím lépe se odpadní voda přečistí a tím delší je interval mezi vyvážením.</p></div></div>
  <div class="types">
    <div class="type"><div class="chambers"><i class="on"></i></div><h3>Jednokomorové</h3>
      <p>Klasická akumulační jímka pro shromažďování odpadních vod tam, kde není kanalizace.</p>
      <div class="from">od 21 000 Kč</div><a class="more" href="#cenik">Ceník 2–22 m³ →</a></div>
    <div class="type"><div class="chambers"><i class="on"></i><i class="on"></i></div><h3>Dvoukomorové</h3>
      <p>V první komoře se usazují pevné látky, ve druhé se zachytí jemnější částice. Prodlužuje interval vyvážení kalu.</p>
      <div class="from">od 27 500 Kč</div><a class="more" href="#cenik-2k">Ceník 6–14 m³ →</a></div>
    <div class="type"><div class="chambers"><i class="on"></i><i class="on"></i><i class="on"></i></div><h3>Tříkomorové</h3>
      <p>Tři stupně filtrace. Poslední komora zajišťuje dočištění před vypouštěním do povrchových či podzemních vod.</p>
      <div class="from">od 43 000 Kč</div><a class="more" href="#cenik-3k">Ceník 12–14 m³ →</a></div>
    <div class="type"><div class="chambers"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></div><h3>Vícekomorové</h3>
      <p>Propojitelné nádrže umožňují libovolně navýšit kapacitu podle potřeby objektu.</p>
      <div class="from">na dotaz</div><a class="more" href="#vicekomorove">Spočítat sestavu →</a></div>
  </div>
</div></section>

<section class="grey" id="cenik"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Jednokomorové betonové jímky</h2>
  <p class="lead">V ceně je jímka, horní deska tloušťky 120 mm, komín 500 mm a betonové víko.</p></div></div>
  {table("", H_JIMKY, JIMKY_1K)}
  <p class="note">Ceny neobsahují dopravu a DPH. Montáž hydraulickou rukou je při dostatečném přístupu zdarma.</p>
  <div class="incl">
    <div><b>Jímka</b><span>vodonepropustný železobeton s asfaltovou izolací</span></div>
    <div><b>Horní deska</b><span>tloušťka 120 mm</span></div>
    <div><b>Komín 500 mm</b><span>betonový, součást ceny</span></div>
    <div><b>Betonové víko</b><span>součást ceny</span></div>
  </div>
</div></section>

<section id="cenik-2k"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Dvoukomorové jímky</h2>
  <p class="lead">Součástí je horní deska 120 mm, <b>dva</b> komíny 500 mm a <b>dvě</b> betonová víka. V první komoře se usazují pevné látky, ve druhé se zachytí jemnější částice.</p></div></div>
  {table("", H_JIMKY, JIMKY_2K)}
  <p class="note">Ceny neobsahují dopravu a DPH.</p>
</div></section>

<section class="grey" id="cenik-3k"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Tříkomorové jímky</h2>
  <p class="lead">Třístupňové čištění – kal se usazuje v první komoře, druhá zachytí jemnější částice a třetí zajišťuje dočištění vody.</p></div></div>
  {table("", H_JIMKY, JIMKY_3K)}
  <p class="note">Ceny neobsahují dopravu a DPH.</p>
</div></section>

<section id="vicekomorove"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Na míru</div><h2>Vícekomorové jímky</h2>
  <p class="lead">Jednotlivé nádrže lze vzájemně propojit a vytvořit sestavu prakticky libovolné kapacity – pro větší domácnosti, penziony, hospodářské objekty nebo provozy. Cenu sestavy připravíme podle požadovaného objemu a dispozice pozemku.</p></div>
  <a class="btn btn-primary" href="kontakt.html#poptavka">Poptat sestavu na míru →</a></div>
</div></section>

<section class="dark" id="proc"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow on-dark">Proč beton</div><h2>Proč si vybrat betonové jímky</h2>
  <p class="lead">Beton se na rozdíl od plastu nemusí obetonovávat ani kotvit proti vztlaku spodní vody.</p></div></div>
  <div class="bens">
    <div class="ben"><div class="ic">1</div><h4>Dlouhá životnost</h4><p>Certifikovaný vibrovaný beton C25/30 s ocelovou výztuží 8–10 mm vydrží desítky let bez ztráty pevnosti.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Vodotěsnost</h4><p>Vodonepropustná konstrukce s asfaltovou izolací brání únikům i vnikání spodní vody.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Chemická odolnost</h4><p>Odolává agresivnímu prostředí odpadních vod i biologickému rozkladu.</p></div>
    <div class="ben"><div class="ic">4</div><h4>Nízké náklady na údržbu</h4><p>Žádné nátěry, žádná revize plastových svarů. Prakticky bezúdržbový provoz.</p></div>
    <div class="ben"><div class="ic">5</div><h4>Stabilita a bezpečnost</h4><p>Vlastní hmotnost udrží jímku na místě i při vysoké hladině spodní vody – betonování není nutné.</p></div>
    <div class="ben"><div class="ic">6</div><h4>Ekologie</h4><p>Beton je přírodní, recyklovatelný materiál bez uvolňování látek do půdy.</p></div>
  </div>
</div></section>

<section id="faq"><div class="wrap" style="max-width:920px">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Časté otázky</div><h2>Montáž, výběr a příprava</h2></div></div>
  {faq_items(FAQ_MONTAZ + FAQ_VYBER[:2])}
  <div style="margin-top:24px"><a class="btn btn-outline" href="faq.html">Všechny otázky →</a></div>
</div></section>"""
    return page("jimky.html","Betonové jímky – ceník 2–22 m³ | Montáž zdarma | BETONLAND",
                "Betonové jímky jedno-, dvoj-, troj- a vícekomorové od 21 000 Kč. Beton C25/30, výztuž 8–10 mm, montáž hydraulickou rukou zdarma, dodání do 4 dnů, záruka 5 let.",
                "jimky.html", body)

def build_sklepy():
    spec = """<div class="spec-box"><h4>Parametry ve zkratce</h4>
      <div class="spec-row"><span>Provedení</span><b>7 variant</b></div>
      <div class="spec-row"><span>Vnější délka</span><b>2,4 – 4,5 m</b></div>
      <div class="spec-row"><span>Vnitřní výška</span><b>1,9 – 2,3 m</b></div>
      <div class="spec-row"><span>Ceny</span><b>34 000 – 94 000 Kč</b></div>
      <div class="spec-row"><span>Materiál</span><b>vodonepropustný železobeton</b></div>
      <div class="spec-row"><span>Montáž</span><b>zdarma při dostatečném přístupu</b></div>
      <div class="spec-row"><span>Dodání</span><b>do 4 dnů</b></div></div>"""
    body = hero_page(['<a href="index.html">Domů</a>','<a href="produkty.html">Produkty</a>','<span style="color:#fff">Betonové sklepy</span>'],
        "Sedm provedení · 34 000 – 94 000 Kč", "Betonové sklepy <em>hotové na klíč</em>",
        "Sklep z monolitického betonu udrží stabilní teplotu i vlhkost po celý rok – ideální pro víno, ovoce, zeleninu i zavařeniny. Vybírat můžete z kopulových i sklepů s rovnou střechou, se schodištěm odlitým zároveň se sklepem nebo v modulovém provedení.",
        '<a class="btn btn-light" href="#cenik">Přejít na ceník ↓</a><a class="btn btn-ghost" href="kontakt.html#poptavka">Nezávazná poptávka</a>',
        spec) + f"""
<div class="jump"><div class="wrap">
  <a href="#cenik">Kopulové</a><a href="#dlouha">Vstup na dlouhé straně</a><a href="#rovna">Rovná střecha</a>
  <a href="#opora">S opěrnou zdí</a><a href="#modul">Modulové</a><a href="#schody">Se schodištěm</a><a href="#bezdna">Bez dna</a>
</div></div>

<section id="cenik"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Kompletní ceník sklepů</h2>
  <p class="lead">Všechny ceny jsou bez DPH a bez ceny za dopravu. Usazení provádíme zdarma, pokud je k místu složení dostatečný přístup.</p></div></div>
  {table("Kopulové sklepy", H_KUP, SK_KUP)}
  <div id="dlouha"></div>
  {table("Kopulové sklepy – vstup na dlouhé straně", H_KUP, SK_KUP_LONG)}
  <div id="rovna"></div>
  {table("Sklepy s rovnou střechou", H_ROV, SK_ROV)}
  <div id="opora"></div>
  {table("Sklepy s rovnou střechou a opěrnou zdí na desce pro zadržení zeminy", H_ROV, SK_OPORA)}
  <div id="modul"></div>
  {table("Sklepy s rovnou střechou – modulové", H_ROV, SK_MODUL)}
  <div id="schody"></div>
  {table("Kopulové sklepy se schodištěm odlitým spolu se sklepem", H_KUP, SK_SCHODY)}
  <div id="bezdna"></div>
  {table("Sklepy bez dna", H_KUP, SK_BEZDNA)}
  <p class="note">Ceny neobsahují dopravu a DPH. Potřebujete jiný rozměr nebo úpravu na míru? <a href="kontakt.html#poptavka">Napište nám</a> a připravíme nabídku.</p>
</div></section>

<section class="grey"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">K čemu slouží</div><h2>Sklep, který drží teplotu celý rok</h2></div></div>
  <div class="bens light">
    <div class="ben"><div class="ic">1</div><h4>Stabilní klima</h4><p>Betonová konstrukce obsypaná zeminou udržuje po celý rok vyrovnanou teplotu i vlhkost bez elektřiny.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Hotový celek</h4><p>Sklep přivezeme jako jeden prefabrikovaný díl a usadíme hydraulickou rukou – žádné zdění na místě.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Varianty na míru</h4><p>Kopule i rovná střecha, schodiště odlité spolu se sklepem, modulové provedení či verze bez dna.</p></div>
  </div>
</div></section>

<section><div class="wrap" style="max-width:920px">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Časté otázky</div><h2>Ke sklepům se ptáte na</h2></div></div>
  {faq_items([
    ("Jaký je rozdíl mezi kopulovým sklepem a sklepem s rovnou střechou?","Kopulový sklep má klenutou střechu, která lépe přenáší zatížení zeminou a působí tradičněji – hodí se pod násyp či svah. Sklep s rovnou střechou má menší celkovou výšku a snáze se zapracuje do rovného terénu."),
    ("Co znamená sklep bez dna?","Nádrž se usazuje na připravený podklad bez betonového dna. Používá se tam, kde je požadována přirozená výměna vlhkosti s podložím – například pro skladování brambor či zeleniny."),
    ("Je součástí ceny schodiště?","Schodiště odlité spolu se sklepem je samostatná varianta – najdete ji v ceníku pod položkou „Kopulové sklepy se schodištěm“."),
    ("Musím sklep obetonovat?","Ne. Po usazení a zaschnutí spojů stačí sklep obsypat zeminou."),
  ])}
</div></section>"""
    return page("sklepy.html","Betonové sklepy – ceník od 34 000 Kč | BETONLAND",
                "Betonové sklepy kopulové i s rovnou střechou, se schodištěm, modulové i bez dna. Kompletní ceník 34 000 – 94 000 Kč, montáž zdarma, dodání do 4 dnů.",
                "sklepy.html", body)

def build_sachty():
    body = hero_simple(['<a href="index.html">Domů</a>','<a href="produkty.html">Produkty</a>','<span style="color:#fff">Vodoměrné šachty</span>'],
        "Prefabrikované šachty", "Vodoměrné šachty pro přípojky i technologie",
        "Pokud potřebujete připojit novostavbu k obecnímu vodovodu a zajistit celoroční snadný přístup k vodoměru, instalovat filtrační technologii k bazénu nebo čerpadlo ke studni, je vodoměrná šachta ideálním řešením.") + f"""
<section><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Využití</div><h2>Kde se šachta uplatní</h2></div></div>
  <div class="bens light">
    <div class="ben"><div class="ic">1</div><h4>Přípojky novostaveb</h4><p>Napojení objektu na obecní vodovod s celoročně přístupným vodoměrem.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Technologie bazénů a studní</h4><p>Prostor pro filtraci, čerpadlo a rozvody mimo obytný objekt.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Pojezdové plochy</h4><p>Betonová konstrukce snese instalaci i v místech s provozem – při použití odpovídajícího poklopu.</p></div>
  </div>
</div></section>

<section class="grey" id="cenik"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Ceník vodoměrných šachet</h2>
  <p class="lead">Všechny ceny jsou uvedeny bez DPH a bez ceny za dopravu. Osazení šachty provádíme zdarma, pokud je dostatečný přístup k místu složení.</p></div></div>
  {table("", ["Kapacita","Délka","Šířka","Výška s deskou","Cena bez DPH"], SACHTY)}
  <p class="note">Potřebujete jiný rozměr? <a href="kontakt.html#poptavka">Napište nám</a> – vyrobíme šachtu podle vašich požadavků.</p>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Doporučené doplňky</div><h2>K šachtě se hodí</h2></div>
  <a class="btn btn-outline" href="prislusenstvi.html">Celý ceník příslušenství →</a></div>
  {table("", ["Položka","Popis","Cena bez DPH"], [PRISL[0], PRISL[6], PRISL[7], PRISL[4]])}
</div></section>"""
    return page("sachty.html","Vodoměrné šachty – betonové prefabrikované | Ceník | BETONLAND",
                "Betonové prefabrikované vodoměrné šachty pro přípojky novostaveb, vodoměry a technologie bazénů či studní. Ceník od 21 000 Kč, osazení zdarma.",
                "sachty.html", body)

def build_jamy():
    body = hero_simple(['<a href="index.html">Domů</a>','<a href="produkty.html">Produkty</a>','<span style="color:#fff">Montážní jámy</span>'],
        "Pět velikostí M1 – M5", "Montážní jámy pro servisy a dílny",
        "Pokud chcete v dílně pracovat rychle a bezpečně, jsou betonové montážní jámy tou správnou volbou. Hodí se do autoservisů, montážních dílen i na stanice technické kontroly.") + f"""
<section class="grey" id="cenik"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Ceník montážních jam</h2>
  <p class="lead">Rozměry jsou uvedeny jako délka × šířka × hloubka. Ceny jsou bez DPH a bez ceny za dopravu.</p></div></div>
  {table("", ["Model","Rozměry (D × Š × H)","Cena bez DPH"], JAMY)}
  <p class="note">Osazení provádíme zdarma, pokud je k místu složení dostatečný přístup pro nákladní vozidlo s hydraulickou rukou.</p>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Pro koho</div><h2>Kde se montážní jáma vyplatí</h2></div></div>
  <div class="bens light">
    <div class="ben"><div class="ic">1</div><h4>Autoservisy</h4><p>Rychlý přístup ke spodní části vozidla bez nutnosti zvedáku.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Montážní dílny</h4><p>Trvalé pracoviště pro servis, svařování i údržbu techniky.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Stanice STK</h4><p>Prefabrikovaná jáma s přesnými rozměry a rovnými hranami.</p></div>
  </div>
</div></section>"""
    return page("montazni-jamy.html","Montážní jámy M1–M5 – betonové | Ceník od 30 000 Kč | BETONLAND",
                "Betonové montážní jámy pro autoservisy, dílny a stanice STK. Pět velikostí M1–M5 od 350 do 600 cm, ceník od 30 000 Kč, osazení zdarma.",
                "montazni-jamy.html", body)

def build_nadrze():
    body = hero_simple(['<a href="index.html">Domů</a>','<a href="produkty.html">Produkty</a>','<span style="color:#fff">Nádrže na vodu</span>'],
        "Železobeton B35", "Betonové nádrže na vodu",
        "Betonové nádrže na vodu jsou ideální pro shromažďování a skladování vody. Díky použití železobetonu B35 poskytují vysokou odolnost proti korozi i praskání. Uplatní se od zahradního zavlažování až po průmyslové potřeby.") + f"""
<section><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Využití</div><h2>Na co se nádrž hodí</h2></div></div>
  <div class="bens light">
    <div class="ben"><div class="ic">1</div><h4>Zahrada a zavlažování</h4><p>Zachytávání dešťové vody ze střech a její využití k závlaze.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Hospodářství</h4><p>Zásoba užitkové vody pro chov, mytí techniky nebo požární potřeby.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Průmysl</h4><p>Akumulace technologické vody s odolností proti korozi a chemickému zatížení.</p></div>
  </div>
</div></section>

<section class="grey" id="cenik"><div class="wrap">
  <div class="formgrid">
    <div>
      <div class="eyebrow">Ceník</div>
      <h2>Cenu spočítáme na míru</h2>
      <p class="lead" style="margin-top:14px">Nádrže na vodu vyrábíme v rozměrech odpovídajících našim jímkám, tedy zhruba od 2 do 22 m³. Konkrétní cena závisí na objemu, provedení a místě montáže – pošlete nám požadavek a do 24 hodin dostanete pevnou nabídku včetně dopravy.</p>
      <p class="note">Orientačně: nádrž 2 m³ od 21 000 Kč, 10 m³ od 34 000 Kč, 22 m³ od 74 000 Kč (bez DPH a dopravy). Přesnou cenu potvrdíme v nabídce.</p>
      <div style="margin-top:22px"><a class="btn btn-primary" href="tel:{TELH}">☎ {TEL}</a></div>
    </div>
    {form_block("poptavka", flat=True, title="Poptávka nádrže na vodu", sub="Napište objem a lokalitu, ozveme se do 24 hodin.")}
  </div>
</div></section>"""
    return page("nadrze-na-vodu.html","Betonové nádrže na vodu – železobeton B35 | BETONLAND",
                "Betonové nádrže na vodu ze železobetonu B35, odolné korozi i praskání. Pro zavlažování, hospodářství i průmysl. Cenová nabídka do 24 hodin, montáž zdarma.",
                "nadrze-na-vodu.html", body)

def build_prislusenstvi():
    body = hero_simple(['<a href="index.html">Domů</a>','<a href="produkty.html">Produkty</a>','<span style="color:#fff">Příslušenství</span>'],
        "Poklopy, komíny a desky", "Příslušenství k jímkám a šachtám",
        "Litinový poklop slouží k zakrytí vstupu do betonové jímky. Je vhodný všude tam, kde dochází k průchodu chodců nebo průjezdu automobilů či cyklistů.") + f"""
<section id="cenik"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Ceník</div><h2>Ceník příslušenství</h2>
  <p class="lead">Ceny jsou uvedeny bez DPH a bez ceny za dopravu. Příslušenství dodáváme spolu s nádrží i samostatně.</p></div></div>
  {table("", ["Položka","Popis","Cena bez DPH"], PRISL)}
  <p class="note">Na přejezdovou desku na žumpu právě probíhá akce se slevou 50 %.</p>
</div></section>

<section class="grey"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Jak vybrat</div><h2>Který poklop zvolit</h2></div></div>
  <div class="bens light">
    <div class="ben"><div class="ic">A</div><h4>Bez provozu</h4><p>Pokud přes jímku nikdo nejezdí, stačí betonové víko, které je součástí ceny nádrže.</p></div>
    <div class="ben"><div class="ic">B</div><h4>Osobní automobily</h4><p>Litinový poklop do 3,5 t, případně v kombinaci s přejezdovou deskou.</p></div>
    <div class="ben"><div class="ic">C</div><h4>Nákladní doprava</h4><p>Poklop D400 spolu s TIR deskou pro zatížení až 40 t.</p></div>
  </div>
</div></section>"""
    return page("prislusenstvi.html","Příslušenství k jímkám – poklopy, komíny, desky | Ceník | BETONLAND",
                "Litinové poklopy do 3,5 t i D400, betonové komíny 0,25–1 m, přejezdové a TIR desky, měřiče hladiny. Ceník od 750 Kč bez DPH.",
                "prislusenstvi.html", body)

def build_cenik():
    body = hero_simple(['<a href="index.html">Domů</a>','<span style="color:#fff">Ceník</span>'],
        "Aktuální ceny · srpen 2026", "Kompletní ceník na jednom místě",
        "Všechny ceny jsou uvedeny bez DPH a bez ceny za dopravu. Osazení hydraulickou rukou provádíme zdarma, pokud je k místu složení dostatečný přístup.") + f"""
<div class="jump"><div class="wrap">
  <a href="#j1">Jímky 1-komorové</a><a href="#j2">Jímky 2-komorové</a><a href="#j3">Jímky 3-komorové</a>
  <a href="#sklepy">Sklepy</a><a href="#sachty">Šachty</a><a href="#jamy">Montážní jámy</a><a href="#prisl">Příslušenství</a>
</div></div>

<section id="j1"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Betonové jímky</div><h2>Jednokomorové jímky</h2>
  <p class="lead">V ceně horní deska 120 mm, komín 500 mm a betonové víko.</p></div>
  <a class="btn btn-outline" href="jimky.html">Detail produktu →</a></div>
  {table("", H_JIMKY, JIMKY_1K)}
</div></section>

<section class="grey" id="j2"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Betonové jímky</div><h2>Dvoukomorové jímky</h2>
  <p class="lead">V ceně horní deska 120 mm, dva komíny 500 mm a dvě betonová víka.</p></div></div>
  {table("", H_JIMKY, JIMKY_2K)}
</div></section>

<section id="j3"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Betonové jímky</div><h2>Tříkomorové jímky</h2></div></div>
  {table("", H_JIMKY, JIMKY_3K)}
</div></section>

<section class="grey" id="sklepy"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Betonové sklepy</div><h2>Sklepy – všechna provedení</h2></div>
  <a class="btn btn-outline" href="sklepy.html">Detail produktu →</a></div>
  {table("Kopulové sklepy", H_KUP, SK_KUP)}
  {table("Kopulové sklepy – vstup na dlouhé straně", H_KUP, SK_KUP_LONG)}
  {table("Sklepy s rovnou střechou", H_ROV, SK_ROV)}
  {table("Sklepy s rovnou střechou a opěrnou zdí", H_ROV, SK_OPORA)}
  {table("Sklepy s rovnou střechou – modulové", H_ROV, SK_MODUL)}
  {table("Kopulové sklepy se schodištěm", H_KUP, SK_SCHODY)}
  {table("Sklepy bez dna", H_KUP, SK_BEZDNA)}
</div></section>

<section id="sachty"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Vodoměrné šachty</div><h2>Šachty</h2></div>
  <a class="btn btn-outline" href="sachty.html">Detail produktu →</a></div>
  {table("", ["Kapacita","Délka","Šířka","Výška s deskou","Cena bez DPH"], SACHTY)}
</div></section>

<section class="grey" id="jamy"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Montážní jámy</div><h2>Montážní jámy M1–M5</h2></div>
  <a class="btn btn-outline" href="montazni-jamy.html">Detail produktu →</a></div>
  {table("", ["Model","Rozměry (D × Š × H)","Cena bez DPH"], JAMY)}
</div></section>

<section id="prisl"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Doplňky</div><h2>Příslušenství</h2></div>
  <a class="btn btn-outline" href="prislusenstvi.html">Detail produktu →</a></div>
  {table("", ["Položka","Popis","Cena bez DPH"], PRISL)}
  <p class="note">Nádrže na vodu oceňujeme individuálně podle objemu a provedení – <a href="nadrze-na-vodu.html">poptejte cenu</a>.</p>
</div></section>"""
    return page("cenik.html","Ceník – jímky, sklepy, šachty, jámy a příslušenství | BETONLAND",
                "Kompletní ceník BETONLAND: betonové jímky 21 000–74 000 Kč, sklepy 34 000–94 000 Kč, vodoměrné šachty, montážní jámy M1–M5 a příslušenství. Bez DPH, montáž zdarma.",
                "cenik.html", body)

def build_reference():
    revs = "".join(f'<div class="review"><div class="stars">{s}</div><p>{t}</p><b>{n}</b><small>{m}</small></div>'
                   for s,t,n,m in REVIEWS)
    gal = "".join(f'<div class="it" data-t="{t}"></div>' for t in [
        "Jímka 10 m³ · Kolín","Kopulový sklep 3,4 × 2,4 m · Znojmo","Dvoukomorová jímka 8 m³ · Písek",
        "Montážní jáma M3 · Hradec Králové","Vodoměrná šachta 2 m³ · Beroun","Jímka 14 m³ · Tábor"])
    body = hero_simple(['<a href="index.html">Domů</a>','<span style="color:#fff">Reference</span>'],
        "Realizace a recenze", "Co jsme postavili a co na to zákazníci",
        "Přes tři desetiletí zkušeností a stovky usazených nádrží po celé České republice. Níže najdete ukázky realizací a hodnocení zákazníků.") + f"""
<section><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Realizace</div><h2>Vybrané zakázky</h2>
  <p class="lead">Fotografie z montáží – usazení hydraulickou rukou, příprava výkopu i hotové dílo.</p></div></div>
  <div class="gal">{gal}</div>
  <p class="note">Ukázková galerie. Po dodání vašich fotografií z realizací je zde nahradíme skutečnými snímky.</p>
</div></section>

<section class="grey"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Recenze</div><h2>Hodnocení zákazníků</h2></div></div>
  <div class="reviews">{revs}</div>
</div></section>

<section class="dark"><div class="wrap">
  <div class="stats" style="border-top:0;padding-top:0;margin-top:0">
    <div class="stat"><b>30+</b><span>let zkušeností s výrobou</span></div>
    <div class="stat"><b>14</b><span>krajů, kam dovážíme</span></div>
    <div class="stat"><b>45</b><span>minut průměrná montáž</span></div>
    <div class="stat"><b>5</b><span>let záruka od výrobce</span></div>
  </div>
</div></section>"""
    return page("reference.html","Reference a recenze zákazníků | BETONLAND",
                "Realizace betonových jímek, sklepů, šachet a montážních jam po celé ČR. Hodnocení zákazníků BETONLAND.",
                "reference.html", body)

def build_faq():
    body = hero_simple(['<a href="index.html">Domů</a>','<span style="color:#fff">Časté otázky</span>'],
        "Vše, co potřebujete vědět", "Časté otázky",
        "Nenašli jste odpověď? Zavolejte nám na {} nebo napište na {} – rádi poradíme.".format(TEL, MAIL)) + f"""
<section><div class="wrap" style="max-width:920px">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Montáž a příprava</div><h2>Než přijedeme</h2></div></div>
  {faq_items(FAQ_MONTAZ)}
</div></section>

<section class="grey"><div class="wrap" style="max-width:920px">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Výběr produktu</div><h2>Jak si vybrat</h2></div></div>
  {faq_items(FAQ_VYBER, open_first=False)}
</div></section>

<section><div class="wrap" style="max-width:920px">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Doprava, ceny a záruka</div><h2>Objednávka a dodání</h2></div></div>
  {faq_items(FAQ_DOPRAVA, open_first=False)}
</div></section>"""
    faqschema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[""" + ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (
            _json(q), _json(a)) for q, a in FAQ_MONTAZ + FAQ_VYBER + FAQ_DOPRAVA) + "]}</script>\n"
    return page("faq.html","Časté otázky – betonové jímky, sklepy a montáž | BETONLAND",
                "Odpovědi na časté otázky: příprava výkopu, montáž hydraulickou rukou, dokumentace ke kolaudaci, velikost jímky, doprava a záruka.",
                "faq.html", body, faqschema)

def _json(s):
    import json
    return json.dumps(s, ensure_ascii=False)

def build_kontakt():
    body = hero_simple(['<a href="index.html">Domů</a>','<span style="color:#fff">Kontakt</span>'],
        "Působíme po celé ČR", "Ozveme se do 24 hodin",
        "Napište nám rozměr nebo objem a lokalitu montáže. Připravíme pevnou cenu včetně dopravy a navrhneme termín. Poptávka je nezávazná a zdarma.") + f"""
<section><div class="wrap">
  <div class="formgrid">
    <div>
      <div class="eyebrow">Kontaktní údaje</div>
      <h2>Zavolejte nebo napište</h2>
      <div class="contact-list">
        <a href="tel:{TELH}"><span class="ic">☎</span>{TEL}</a>
        <a href="mailto:{MAIL}"><span class="ic">✉</span>{MAIL}</a>
        <div><span class="ic">⌖</span>Působíme po celé České republice</div>
      </div>
      <div class="infobox" style="margin-top:28px">
        <h4>Fakturační a výrobní údaje</h4>
        <dl>
          <dt>Značka</dt><dd>BETONLAND</dd>
          <dt>Výrobce</dt><dd>SałexPol – Sebastian Sałkiewicz</dd>
          <dt>Adresa výroby</dt><dd>Owadów 22A, 26-631 Jastrzębia, Polsko</dd>
          <dt>DIČ</dt><dd>PL8121660308</dd>
          <dt>Záruka</dt><dd>5 let, poskytuje přímo výrobce</dd>
        </dl>
      </div>
      <p class="note">Certifikát ke kolaudaci i záruční list předáváme ihned po montáži.</p>
    </div>
    {form_block("poptavka", flat=True)}
  </div>
</div></section>

<section class="grey"><div class="wrap">
  <div class="sec-head"><div class="txt"><div class="eyebrow">Než zavoláte</div><h2>Co si připravit</h2></div></div>
  <div class="bens light">
    <div class="ben"><div class="ic">1</div><h4>Objem nebo rozměr</h4><p>Kolik osob bude jímku využívat, případně jaký rozměr sklepa či jámy potřebujete.</p></div>
    <div class="ben"><div class="ic">2</div><h4>Lokalita</h4><p>Obec nebo PSČ místa montáže – podle toho spočítáme dopravu.</p></div>
    <div class="ben"><div class="ic">3</div><h4>Přístup na pozemek</h4><p>Zda se k výkopu dostane nákladní vozidlo s hydraulickou rukou.</p></div>
  </div>
</div></section>"""
    return page("kontakt.html","Kontakt – BETONLAND | +420 797 812 444",
                "Kontakt na BETONLAND: +420 797 812 444, info@betonland.cz. Nezávazná poptávka betonových jímek, sklepů, šachet a montážních jam. Působíme po celé ČR.",
                "kontakt.html", body)

def build_gdpr():
    body = hero_simple(['<a href="index.html">Domů</a>','<span style="color:#fff">Ochrana soukromí</span>'],
        "Zásady zpracování osobních údajů", "Ochrana soukromí",
        "Jak nakládáme s údaji, které nám pošlete přes kontaktní formulář nebo e-mailem.") + f"""
<section><div class="wrap"><div class="prose">
  <p><b>Vzorový text.</b> Před spuštěním webu jej nechte zkontrolovat a doplnit podle skutečného provozovatele a nastavení webu.</p>
  <h2>Kdo údaje zpracovává</h2>
  <p>Správcem osobních údajů je BETONLAND, kontaktní e-mail {MAIL}, telefon {TEL}. Výrobcem dodávaného zboží je SałexPol – Sebastian Sałkiewicz, Owadów 22A, 26-631 Jastrzębia, DIČ PL8121660308.</p>
  <h2>Jaké údaje zpracováváme</h2>
  <ul>
    <li>jméno a příjmení,</li>
    <li>telefonní číslo a e-mailová adresa,</li>
    <li>obec nebo PSČ místa montáže,</li>
    <li>obsah zprávy, kterou nám pošlete.</li>
  </ul>
  <h2>Proč údaje zpracováváme</h2>
  <p>Údaje z poptávkového formuláře používáme výhradně k tomu, abychom vám mohli připravit cenovou nabídku a domluvit dodání a montáž. Právním základem je jednání o smlouvě na vaši žádost a náš oprávněný zájem odpovědět na dotaz.</p>
  <h2>Jak dlouho je uchováváme</h2>
  <p>Poptávky uchováváme po dobu nezbytnou k vyřízení, nejdéle však 3 roky od posledního kontaktu. Údaje na daňových dokladech uchováváme po dobu stanovenou zákonem.</p>
  <h2>Komu je předáváme</h2>
  <p>Údaje předáváme pouze výrobci a dopravci v rozsahu nutném pro dodání a montáž, dále poskytovateli e-mailové schránky a webhostingu. Údaje neprodáváme a nepoužíváme k profilování.</p>
  <h2>Vaše práva</h2>
  <ul>
    <li>právo na přístup k údajům a jejich kopii,</li>
    <li>právo na opravu nepřesných údajů,</li>
    <li>právo na výmaz a na omezení zpracování,</li>
    <li>právo vznést námitku proti zpracování,</li>
    <li>právo podat stížnost u Úřadu pro ochranu osobních údajů.</li>
  </ul>
  <p>Uplatnit je můžete kdykoliv na {MAIL}.</p>
  <h2>Cookies</h2>
  <p>Web používá pouze technické cookies nezbytné pro jeho fungování. Pokud budou nasazeny analytické nebo marketingové nástroje, doplňte sem jejich seznam a zajistěte souhlasovou lištu.</p>
</div></div></section>"""
    return page("ochrana-soukromi.html","Ochrana soukromí | BETONLAND",
                "Zásady zpracování osobních údajů BETONLAND – jaké údaje zpracováváme, proč, jak dlouho a jaká máte práva.",
                "ochrana-soukromi.html", body)

if __name__ == "__main__":
    built = [build_index(), build_produkty(), build_jimky(), build_sklepy(), build_sachty(),
             build_jamy(), build_nadrze(), build_prislusenstvi(), build_cenik(),
             build_reference(), build_faq(), build_kontakt(), build_gdpr()]
    print("Vygenerováno %d stránek:" % len(built))
    for b in built:
        print("  ", b)
