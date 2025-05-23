import json
from holidays import Turkey
from datetime import date

def tatilleri_json_olarak_kaydet(dosya_adi="tatiller.json", yil_araligi=10):
    mevcut_yil = date.today().year
    tum_tatiller = []

    for yil in range(mevcut_yil, mevcut_yil + yil_araligi):
        tr_tatiller = Turkey(years=yil)
        print(f"{yil} yılı için tatiller alınıyor...")

        for tarih, ad in sorted(tr_tatiller.items()):
            tatil = {
                "tarih": tarih.strftime("%Y-%m-%d"),
                "aciklama": ad
            }
            tum_tatiller.append(tatil)

    # JSON dosyasına yaz
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        json.dump(tum_tatiller, dosya, ensure_ascii=False, indent=4)

    print(f"Tüm tatiller başarıyla '{dosya_adi}' dosyasına yazıldı.")

if __name__ == "__main__":
    tatilleri_json_olarak_kaydet()
