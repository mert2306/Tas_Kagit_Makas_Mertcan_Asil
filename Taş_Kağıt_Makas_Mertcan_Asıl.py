import random
import sys

izinli_cevaplar = [
    'taş', 'kağıt', 'makas', 'anladım', 'anlamadım',
    'çıkış', 'dövdü', 'dövmedi', 'evet', 'hayır',
    'inelim', 'inmeyelim', 'yaşadım', 'yaşamadım'
]


def kullanıcıya_hakaret_et():
    print(
        f"{oyuncu_ismi}, bu oyunda o kelimeyi nereden buldun?"
        " Sanki her şeyi biliyormuşsun gibi davranma!"
    )


def kuralları_göster():
    print("\nTaş-Kağıt-Makas Oyun Kuralları:")
    print("1. Taş, makası yener.")
    print("2. Kağıt, taşı yener.")
    print("3. Makas, kağıdı yener.")
    print("4. Skoru 2 olan kişi kazanan olarak ilan edilir.")
    print("5. Oyunu istediğiniz zaman 'çıkış' yazarak sonlandırabilirsiniz.")
    print("6. Her oyunun sonunda toplam skoru tutacağız.")
    print("")


def kullanıcı_seçimi_al():
    seçim = input(f"{oyuncu_ismi}, Taş, Kağıt veya Makas seçin: ").lower()
    if seçim == 'çıkış':
        oyundan_çık()
    while seçim not in ['taş', 'kağıt', 'makas']:
        if seçim not in izinli_cevaplar:
            kullanıcıya_hakaret_et()
        seçim = input(
            f"{oyuncu_ismi}, geçersiz seçim. Taş, Kağıt veya Makas seçin: "
        ).lower()
        if seçim == 'çıkış':
            oyundan_çık()
    return seçim


def bilgisayar_seçimi_al():
    return random.choice(['taş', 'kağıt', 'makas'])


def kazananı_belirle(kullanıcı_seçimi, bilgisayar_seçimi, beraberlik_zorunlu=False):
    if beraberlik_zorunlu:
        return 'beraberlik'
    if kullanıcı_seçimi == bilgisayar_seçimi:
        return 'beraberlik'
    elif (
        (kullanıcı_seçimi == 'taş' and bilgisayar_seçimi == 'makas') or
        (kullanıcı_seçimi == 'kağıt' and bilgisayar_seçimi == 'taş') or
        (kullanıcı_seçimi == 'makas' and bilgisayar_seçimi == 'kağıt')
    ):
        return oyuncu_ismi
    else:
        return 'bilgisayar'


def skorları_yazdır(
    kullanıcı_skoru, bilgisayar_skoru, toplam_kullanıcı_skoru,
    toplam_bilgisayar_skoru
):
    print(f"\n{oyuncu_ismi} Skoru: {kullanıcı_skoru} | Bilgisayar Skoru: {bilgisayar_skoru}")
    print(f"Genel Toplam Skoru - {oyuncu_ismi}: {toplam_kullanıcı_skoru} | Bilgisayar: {toplam_bilgisayar_skoru}\n")


def oyundan_çık():
    print("Oyundan çıkış yapılıyor... Tekrar görüşmek üzere!")
    sys.exit()


def ana_oyun(kuralları_gösterilsin_mi, beraberlik_zorunlu):
    kullanıcı_skoru = 0
    bilgisayar_skoru = 0
    toplam_kullanıcı_skoru = 0
    toplam_bilgisayar_skoru = 0

    while True:
        kullanıcı_seçimi = kullanıcı_seçimi_al()
        bilgisayar_seçimi = bilgisayar_seçimi_al()
        print(f"Bilgisayarın seçimi: {bilgisayar_seçimi}")

        kazanan = kazananı_belirle(kullanıcı_seçimi, bilgisayar_seçimi, beraberlik_zorunlu)

        if kazanan == oyuncu_ismi:
            kullanıcı_skoru += 1
        elif kazanan == 'bilgisayar':
            bilgisayar_skoru += 1

        print(f"Bu elin kazananı: {kazanan}")
        print(f"Bu elde {oyuncu_ismi} Skoru: {kullanıcı_skoru} | Bilgisayar Skoru: {bilgisayar_skoru}")

        if kullanıcı_skoru == 2 or bilgisayar_skoru == 2:
            if kullanıcı_skoru == 2:
                toplam_kullanıcı_skoru += 1
            elif bilgisayar_skoru == 2:
                toplam_bilgisayar_skoru += 1
            skorları_yazdır(kullanıcı_skoru, bilgisayar_skoru, toplam_kullanıcı_skoru, toplam_bilgisayar_skoru)
            tekrar_oyna = input("Tekrar oynamak ister misiniz? (evet/hayır): ").lower()
            if tekrar_oyna not in izinli_cevaplar:
                kullanıcıya_hakaret_et()
            if tekrar_oyna == 'hayır':
                skorları_yazdır(kullanıcı_skoru, bilgisayar_skoru, toplam_kullanıcı_skoru, toplam_bilgisayar_skoru)
                oyundan_çık()
            kullanıcı_skoru = 0
            bilgisayar_skoru = 0


def oyunu_başlat():
    global oyuncu_ismi
    oyuncu_ismi = input("Lütfen isminizi girin: ")

    kuralları_gösterilsin_mi = True
    beraberlik_zorunlu = False
    kullanıcı_cevabı = input(
        f"{oyuncu_ismi}, oyun kurallarını okumak ister misiniz? (evet/hayır): "
    ).lower()
    if kullanıcı_cevabı == 'çıkış':
        oyundan_çık()
    elif kullanıcı_cevabı not in izinli_cevaplar:
        kullanıcıya_hakaret_et()
    elif kullanıcı_cevabı == 'evet':
        kuralları_göster()
        anladın_mı = input("Kuralları anladınız mı? (Anladım/Anlamadım): ").lower()
        if anladın_mı == 'çıkış':
            oyundan_çık()
        elif anladın_mı not in izinli_cevaplar:
            kullanıcıya_hakaret_et()
        elif anladın_mı == 'anladım':
            print("İyi o zaman rahat oldu.")
            kuralları_gösterilsin_mi = False
        else:
            print("Basit bir oyun bunda ne var hiç çocukluğunu yaşamadın mı?")
            çocukluk = input(
                "Çocukluğunu yaşadın mı? (yaşadım/yaşamadım): "
            ).lower()
            if çocukluk == 'çıkış':
                oyundan_çık()
            elif çocukluk not in izinli_cevaplar:
                kullanıcıya_hakaret_et()
            elif çocukluk == 'yaşadım':
                print("E o zaman biliyorsundur.")
            else:
                çocukluğuna_inelim_mi = input(
                    "Çocukluğuna inelim mi? (inelim/inmeyelim): "
                ).lower()
                if çocukluğuna_inelim_mi == 'çıkış':
                    oyundan_çık()
                elif çocukluğuna_inelim_mi not in izinli_cevaplar:
                    kullanıcıya_hakaret_et()
                elif çocukluğuna_inelim_mi == 'inmeyelim':
                    print("Beni ne uğraştırıyorsun.")
                else:
                    ceza = input(
                        "Baban seni hortumla dövüyor muydu? (dövdü/dövmedi): "
                    ).lower()
                    if ceza == 'çıkış':
                        oyundan_çık()
                    elif ceza not in izinli_cevaplar:
                        kullanıcıya_hakaret_et()
                    elif ceza == 'dövmedi':
                        print("Normal bi çocuklukmuş bende bir şey sandım.")
                    else:
                        ihbar = input("Polise haber vereyim mi? (evet/hayır): ").lower()
                        if ihbar == 'çıkış':
                            oyundan_çık()
                        elif ihbar not in izinli_cevaplar:
                            kullanıcıya_hakaret_et()
                        elif ihbar == 'hayır':
                            print("Askere gidince unutursun.")
                        else:
                            print(
                                "Anam burası Güzün Abla'nın yeri mi herkesin derdine"
                                " derman olalım."
                            )
            kuralları_gösterilsin_mi = False
    else:
        emin_misin = input("Emin misin? (evet/hayır): ").lower()
        if emin_misin == 'çıkış':
            oyundan_çık()
        elif emin_misin not in izinli_cevaplar:
            kullanıcıya_hakaret_et()
        elif emin_misin == 'evet':
            print("Günah benden gitti.")
            beraberlik_zorunlu = True
            kuralları_gösterilsin_mi = False

    ana_oyun(kuralları_gösterilsin_mi, beraberlik_zorunlu)


if __name__ == "__main__":
    oyunu_başlat()
