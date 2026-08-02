# Checklista — Resesöksajt (Flygkoll)

**Live (test):** https://nidoxx.github.io/flygprisjakt/ — lösenord `flyg2026` (byt i `index.html` → `SITE_PASSWORD`). Repo: github.com/Nidoxx/flygprisjakt (publikt, noindex).

## 1. Beslut att ta (tänka på)

- [ ] **Namn/domän:** "Flygkoll" är TAGET (flygkoll.se är en aktiv konkurrentsajt). Lediga kandidater med högfrekventa sökord (kontrollerade 2026-08-02):

| Namn | Sökord i namnet | .se | .nu | .com |
|---|---|---|---|---|
| **Flygprisjakt** ⭐ | "flygpris" (flygpriser) | ✅ | ✅ | ✅ |
| **Flygpriser.nu** | "flygpriser" (exakt, toppsökord) | tagen | ✅ | tagen |
| **Flygjakten** | "flyg" + jakt | ✅ | ✅ | ✅ |
| **Hittaflyg** | "hitta flyg" | tagen | ✅ | ✅ |
| **Flygerbjudande** | "flygerbjudanden" | ✅ | – | ✅ |

  Alla rena toppsökord i .se (billigaflyg, flygresor, flygpriser, flygbiljetter) är tagna. Bästa kompromissen: **flygprisjakt.se** (+ .com för skydd, ~200 kr/år tillsammans).
- [ ] Kolla varumärket hos PRV + Google innan köp
- [ ] **Nisch:** Välj 3–5 sträckor/regioner att satsa på (t.ex. Stockholm → Balkan, lågprisbolag från Skavsta). Smalt är vinnbart — "flyg" är det inte.
- [ ] **Partner:** WayAway, Kiwi eller Travelpayouts (kolla att Travelpayouts fortfarande tar emot nya partners — sajten har varit nere).
- [ ] **Mål:** Sätt ett konkret 6-månadersmål (t.ex. 5 000 besökare/mån). Utan mål kan du inte avgöra om det funkar.

## 2. Göra den här veckan

- [ ] Registrera dig på **WayAway** (wayaway.io/en/for-partners) — gratis, ingen prenumeration
- [ ] Registrera dig på **Kiwi** (kiwi.com/partners) som reserv
- [ ] Kopiera widget-koden från partnern → klistra in i `index.html` under `PARTNER` (sätt `widgetReady = true`)
- [ ] Köp domänen (samma ställe som datorhjalpen.nu funkar)
- [ ] Koppla **GA4** (Google Analytics) + **Google Search Console** — görs via domänleverantören/Cloudflare
- [ ] Testa sajten själv: på datorn OCH mobilen (de flesta resesök är mobilt)

## 3. Nästa 1–3 månader (innehåll = trafik)

- [ ] Skriv **10–20 route-sidor**: "Billiga flyg från Stockholm till [stad]" — samma mall, ny stad
- [ ] Ansök till **Booking.com affiliate** (partner.booking.com) — hotell är 7× mer värt än flyg
- [ ] Skriv 4–6 guider: "Billigaste sättet att flyga till…", "Sista minuten-tips"
- [ ] Publicera minst 2–3 gånger/vecka — regelbundenhet slår allt annat
- [ ] Kolla Search Console varje vecka: vilka sökord ger visningar? Skriv mer om dem

## 4. Löpande (varje månad)

- [ ] Fyll i kalkylatorn (`rpm-kalkylator.html`) med riktiga siffror — följ trenden
- [ ] Om RPM under ~100 kr/1 000 besökare: byt nisch eller partner
- [ ] Håll koll på att affiliate-programmen inte ändrat villkor

## 5. Undvik (dyra misstag)

- [ ] **Köp INTE PHPTRAVELS/Adivaha** ($499+) förrän trafiken är bevisad (6 månaders data)
- [ ] **Betald annonsering (Google Ads)** = förlustaffär i början. Klickpriset överstiger utbetalningen
- [ ] Sluta inte publicera efter 3 månader — 90 % av liknande sajter dör så
- [ ] Glöm inte GDPR: cookie-banner + integritetspolicy + affiliate-avslöjande före lansering

## 6. Inför lansering (om ~3–6 månader)

- [ ] Integritetspolicy, villkor, om-oss-sida på båda språken
- [ ] sitemap.xml + robots.txt (för Google)
- [ ] Testa alla länkar och mobil-vyn
- [ ] Först då: utvärdera om en egen bokningsmotor (PHPTRAVELS/Adivaha) är värt det
