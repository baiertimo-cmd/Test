#!/usr/bin/env python3
"""Erzeugt aus src/lernpfad.html die Schülerfassung (index.html) und die Lehrkraftfassung (lehrkraft.html).

Aufruf: python3 build.py

Schülerfassung:   alle mit <!--@T-->…<!--@/T--> bzw. /*@T*/…/*@/T*/ markierten Teile entfallen,
                  die Lösungen (/*@SOL*/…/*@/SOL*/) werden durch Prüfsummen ersetzt.
Lehrkraftfassung: alles bleibt erhalten, Lösungen sind beim Öffnen eingeblendet.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src" / "lernpfad.html"


def fnv1a36(text: str) -> str:
    """Muss hashStr() in der Seite entsprechen (FNV-1a, 32 Bit, Basis 36)."""
    h = 0x811C9DC5
    for b in ("haro|" + text).encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = ""
    while True:
        h, r = divmod(h, 36)
        out = digits[r] + out
        if h == 0:
            return out


def read_solutions(src: str) -> dict:
    block = re.search(r"/\*@SOL\*/var SOL = (\{.*?\}), SOLH = null;/\*@/SOL\*/", src, re.S)
    if not block:
        raise SystemExit("Lösungsblock /*@SOL*/ nicht gefunden")
    body = re.sub(r"(\w+):", r'"\1":', block.group(1))
    return json.loads(body)


def strip_markers(src: str) -> str:
    return re.sub(r"<!--@/?T-->|/\*@/?T\*/|/\*@/?SOL\*/|/\*@KEY\*/", "", src)


def build_student(src: str) -> str:
    sol = read_solutions(src)
    hashed = {k: fnv1a36(f"{k}|{v}") for k, v in sol.items()}
    src = re.sub(r"/\*@SOL\*/.*?/\*@/SOL\*/",
                 lambda _: "var SOL = null, SOLH = " + json.dumps(hashed) + ";", src, flags=re.S)
    src = re.sub(r"<!--@T-->.*?<!--@/T-->", "", src, flags=re.S)
    src = re.sub(r"/\*@T\*/.*?/\*@/T\*/", "", src, flags=re.S)
    src = src.replace("// In der Lehrkraft-Fassung im Klartext; build.py ersetzt den Block in der Schülerfassung durch Prüfsummen.\n", "")
    return strip_markers(src)


def build_teacher(src: str) -> str:
    src = src.replace('"haro-fuhrpark-v1"/*@KEY*/', '"haro-fuhrpark-lehrkraft-v1"')
    src = src.replace("<title>Fuhrpark HARO GmbH</title>", "<title>Fuhrpark HARO GmbH (Lehrkraft)</title>")
    return strip_markers(src)


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    student = build_student(src)
    leaks = [w for w in ("214.000", "235.200", "21.200", "50.800", "Musterlösung", "teacherToggle", "SOL.cheaper", "+SOL[")
             if w in student]
    if leaks:
        raise SystemExit(f"Schülerfassung enthält noch Lösungsspuren: {leaks}")
    (ROOT / "index.html").write_text(student, encoding="utf-8")
    (ROOT / "lehrkraft.html").write_text(build_teacher(src), encoding="utf-8")
    print("index.html (Schüler) und lehrkraft.html (Lehrkraft) erzeugt.")


if __name__ == "__main__":
    main()
