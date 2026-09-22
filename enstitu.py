#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toplantıda Kafa Sallama Enstitüsü v0.0.7
Anlamadığın cümleye bilimsel kafa hareketi üretir.
"""

from __future__ import annotations

import random
import textwrap
from dataclasses import dataclass


# Gizli not (base64): R2l6bGkgbm90OiBveXVudSBraW1zZXllIHPttmxlbWUsIHNhbmTEsWsgc2Vzc2l6IMOnYWzEscWfxLFyLgo=
# Çözersen görürsün. Çözmezsen de hayat devam eder.

CUMLELER = [
    "Q4 hedeflerini Q3 ile senkronize ederken asenkron bir senkron yakaladık.",
    "Stakeholder alignment'ı holistik bir şekilde cascade ediyoruz.",
    "Aksiyon item'ını park edip offline'da circle back yapalım.",
    "Bu aslında bir win-win, hatta win-win-win; dördüncü win otoparkta.",
    "KPI'ları OKR'larla evlendirip bebek OKPI doğuracağız.",
    "Masa altından geçen kablo stratejik bir kablodur.",
]

TEPKILER = [
    "hmm evet kesinlikle",
    "tam olarak bunu düşünüyordum",
    "çok yerinde bir tespit",
    "ben de o taraftan bakmıştım aslında",
    "not aldım, yani alır gibi yaptım",
    "mükemmel, şimdi daha az anlıyorum",
]


@dataclass
class SallamaRaporu:
    cumle: str
    aci_derece: float
    inandiricilik: int
    soz: str
    karar: str

    def resmi_metin(self) -> str:
        return textwrap.dedent(
            f"""
            ================================================
            TOPLANTIDA KAFA SALLAMA ENSTİTÜSÜ
            Resmi Tutanak — Gizli Değil Ama Ciddi
            ================================================
            Duyulan cümle : {self.cumle}
            Sallama açısı  : {self.aci_derece:.1f} derece
            İnandırıcılık  : {self.inandiricilik}/100
            Ağızdan çıkan  : {self.soz}
            Enstitü kararı : {self.karar}
            ================================================
            """
        ).strip()


def olc() -> SallamaRaporu:
    cumle = random.choice(CUMLELER)
    aci = random.uniform(3.5, 22.7)
    inandiricilik = max(12, min(99, int(100 - aci * 2 + random.randint(-8, 15))))
    soz = random.choice(TEPKILER)
    if inandiricilik >= 70:
        karar = "Onaylandı. Kimse anlamadığını fark etmedi. Terfi yakın."
    elif inandiricilik >= 40:
        karar = "Şüpheli. Bir daha 'kesinlikle' deme, 'ilginç' de."
    else:
        karar = "İfşa riski. Kamerayı kapat, çay iste, konu değiştir."
    return SallamaRaporu(cumle, aci, inandiricilik, soz, karar)


def main() -> None:
    rapor = olc()
    print(rapor.resmi_metin())
    print()
    print("Damga: TKE-2026 / Kayyum Grok — Tentivory")
    print("Tarih: 22 Eylül 2026, salı, toplantı bitmek bilmedi.")


if __name__ == "__main__":
    main()
