# EE103 Week 5 | Türkçe çalışma notları

Bu klasördeki kodlar 27 Ekim 2026 tarihli **Week 5 in-class exercise** dokümanındaki alıştırmalara göre yazılmıştır.

## 1. Sayıları çarpmak: `multiply-all.py`

10'dan 13'e kadar **10 × 11 × 12 × 13 = 17160**. `result_for = 1` olmalıdır çünkü çarpmada etkisiz eleman 1'dir. `range(start, end+1)` kullanılır çünkü `range` bitiş sayısını içermez. `while` çözümü her turda sayacı bir artırır ve aynı sonucu verir. Bu iki yöntemi karşılaştırmak **sanity check** olarak kullanılır.

## 2. Cupcake bulmacası: `cupcake-guess-check.py`

Verilen koşullar: Emma = David + 3, Frank = 3 × David, toplam = 28. Üç iç içe `for` döngüsü her kişi için olası cupcake sayılarını dener. Her üç koşulu da sağlayan tek çözüm **David = 5, Emma = 8, Frank = 15**. Matematiksel doğrulama: `D+(D+3)+3D=28` → `5D=25` → `D=5`.

## 3. Tam sayıyı ikiliye çevirme: `binary-integers.py`

13 ÷ 2 = 6 kalan 1; 6 ÷ 2 = 3 kalan 0; 3 ÷ 2 = 1 kalan 1; 1 ÷ 2 = 0 kalan 1. Kalanlar tersten okunur: **1101**. `%` kalanı, `//` tam bölüm sonucunu verir. Kod sıfırı ve negatif sayıları da ele alır.

## 4. Floating-point error: `floating-error.py`

On kere 0.1 eklendiğinde sonuç `0.9999999999999999` olur. Bunun nedeni 0.1'in ikilik kayan nokta gösteriminde tam karşılığının bulunmaması ve küçük yuvarlama hatalarının birikmesidir. Sayısal sonuçlarda yakınlığı sınamak için çoğu zaman `abs(a-b) < tolerance` kullanılır.

## 5. Kesirleri ikiliye çevirme: `binary-fractions.py`

Önce tam kısım **13 → 1101**. Kesirli kısım için 0.375×2=0.75 → bit 0; 0.75×2=1.5 → bit 1; 0.5×2=1.0 → bit 1. Böylece **0.375 → 0.011** ve **13.375 → 1101.011**. Doğrulama: 8+4+1+1/4+1/8 = 13.375. Sonsuza giden ikilik açılımlar için 32 bit sınırı uygulanır.

## 6. 0.1'i hata toleransıyla ikili yazmak: `binary-01.py`

0.1 ondalık sayısının ikilik gösterimi tekrar eder: `0.000110011001100...`. Her bulunan bitin ondalık katkısı `bit × 2**(-basamak)` biçimindedir. `abs(result - 0.1) < 0.00001` olduğunda durulur. 16 bit sonrası sonuç `0.0001100110011001`, ondalık değeri **0.0999908447265625**, hata **0.00000915527**.

## 7. Karekök yaklaşımı: `approximate-square-root.py`

`guess = 0` ile başlayıp her turda `increment = 0.0001` eklenir. `num_guesses` işlem sayısını tutar. PDF'nin 3. sayfasındaki döngü koşulu `abs(guess**2-number) >= epsilon` ve `epsilon = 0.01` şeklindedir; bu **karenin hatasıdır**, doğrudan karekökün hatası değildir. `DEBUG=True` yapıldığında her 1000 adımda bir tahmin yazılır.

36, 24, 2 ve 12345 değerlerinde varsayılan adım yeterlidir; ancak **54321 için hedef hata aralığı atlanır (overshoot)**. Yaklaşık 233 mertebesindeki bir tahmine 0.0001 eklemek karesini yaklaşık `2×233×0.0001 = 0.0466` değiştirir. Bu sıçrama 0.01'lik izin verilen hatayı aşabilir. `guess**2 <= number` koşulu sonsuz döngüyü önler; `increment = 0.00001` seçmek hassasiyeti artırır ama daha çok iterasyon gerektirir.

## 8. Bisection search: `bisection-pages.py`

148 sayfalık kitapta önce ortadaki sayfa **74** sorulur. Gizli sayfa daha büyükse alt sınır 75'e; daha küçükse üst sınır 73'e çekilir. Her adımda aralık yaklaşık yarılanır. Doğrusal arama en kötü durumda 148 tahmin kullanırken bisection en kötü durumda **8 tahmin** kullanır çünkü `2**7 < 148 <= 2**8`. Gizli sayfa 148 ise sıralama: **74, 111, 130, 139, 144, 146, 147, 148**.

## Çalıştırma ve test

VS Code terminalinde `Week5` dizinine girerek `python dosya-adi.py` komutuyla ilgili programı çalıştır. Hepsinin otomatik testini yapmak için `python -m unittest test_week5.py -v` yaz. GitHub'a yüklediğin klasör linkini dersin assignment alanına yapıştır.
