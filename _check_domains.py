import socket, json, time, urllib.request, urllib.error, concurrent.futures

# Högfrekventa sökord i kombinationer
se_candidates = ["flygresor", "flygresa", "resejakten", "flygprisjakt", "resabilligt",
                 "resbilligt", "flygbiljetter", "sistaminutenresor", "charterresor",
                 "semesterresor", "weekendresor", "flygerbjudande", "flygbäst", "ressmart",
                 "flygsok", "billigaflygresor", "flygprisjakt.nu"]

nu_candidates = ["billigaflyg", "flygpriser", "flygresor", "flygbiljetter", "billigaresor",
                 "flygfynd", "hittaflyg", "flygdeals", "sistaminuten", "flygjakten",
                 "uppochflyg", "resejakten", "flygprisjakt", "resabilligt", "flygspanaren",
                 "smartaflyg", "flygkoll", "hej", "nic"]

def whois_iis(domain):
    try:
        s = socket.create_connection(("whois.iis.se", 43), timeout=12)
        s.sendall((domain + "\r\n").encode())
        data = b""
        while True:
            c = s.recv(8192)
            if not c: break
            data += c
        s.close()
        t = data.decode("latin-1", errors="replace").lower()
        if "no match" in t or "not found" in t: return "LEDIG"
        if "state: active" in t or "holder:" in t: return "TAGEN"
        return "?" + t[-50:].replace("\n", " ")
    except Exception as e:
        return "ERR"

def check_nu(domain):
    """.nu: DNS-NS-heuristik + försök whois.nic.nu"""
    # DNS
    try:
        req = urllib.request.Request("https://dns.google/resolve?name=" + domain + "&type=NS",
                                     headers={"User-Agent": "check/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
        dns = "LEDIG" if data.get("Status") == 3 else ("TAGEN" if data.get("Answer") else "?")
    except Exception:
        dns = "ERR"
    return dns

print("=== .se (whois.iis.se) ===")
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    se = dict(ex.map(lambda d: (d, whois_iis(d + ".se")), [c for c in se_candidates if not c.endswith(".nu")]))
for n, v in sorted(se.items()):
    print(f"{n}.se: {v}")

print()
print("=== .nu (dns.google NS-heuristik; sanity: hej.nu & nic.nu borde vara tagna) ===")
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    nu = dict(ex.map(lambda d: (d, check_nu(d + ".nu")), nu_candidates))
for n, v in sorted(nu.items()):
    print(f"{n}.nu: {v}")
