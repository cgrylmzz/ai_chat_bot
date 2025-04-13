# 🤖 AI Chat Bot

Bu proje, Python ile geliştirilmiş terminal tabanlı bir yapay zekâ sohbet botudur. Kullanıcıdan gelen sorulara veri tabanındaki cevapları döner, cevapsız kalan soruları kaydeder ve gerektiğinde kullanıcıdan yeni cevaplar alabilir.

---

## 📌 Özellikler

- 🧠 Soru-cevap veritabanı (`data.json`) kullanır  
- 🗣️ Yakın eşleşme algoritmasıyla benzer soruları tanır  
- ❌ Yasaklı kelime filtresiyle kötü içerikleri engeller (`banned_words.txt`)  
- 📝 Cevapsız soruları kaydeder (`unanswered.txt`) ve sonradan cevaplanmasını sağlar  
- 🧽 Soruları silebilir, listeleyebilir ve güncelleyebilir

---

## 🛠️ Gereksinimler

- Python 3.x (herhangi bir 3+ sürüm yeterli)
- Ekstra bir kütüphane gerektirmez (yalnızca `difflib`, `os`, `json`, `time` gibi yerleşik modüller kullanılmıştır)

---

## 💡 Örnek Kod Kullanımı

```python
from artificial_intelligence_bot import ArtificialIntelligenceBot

bot = ArtificialIntelligenceBot()

print(bot.ask_a_question("merhaba"))  # Sorulan soruya cevabı verir
```

Terminal arayüzünü çalıştırmak için doğrudan scripti başlatabilirsin:

```bash
python artificial_intelligence_bot.py
```

---

## 📁 Dosya Açıklamaları

| Dosya Adı                        | Açıklama                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| `artificial_intelligence_bot.py` | Ana uygulama dosyası, tüm bot fonksiyonlarını içerir                     |
| `data.json`                      | Kayıtlı soru-cevap veritabanı                                           |
| `banned_words.txt`               | Küfür ve uygunsuz içerikleri filtrelemek için kullanılan kelimeler      |
| `unanswered.txt`                 | Cevap verilemeyen soruların geçici olarak kaydedildiği metin dosyası    |

---

## 🔒 Yasaklı Kelime Listesi Hakkında

Bu projede bulunan `banned_words.txt` dosyası, kullanıcıdan gelen uygunsuz içerikleri **engellemek amacıyla** oluşturulmuştur.  
Bu kelimeler sistemin düzgün çalışması ve etik dışı kullanımın önüne geçilmesi için filtrelenir.  
**Proje içerisinde bu kelimelerin kullanılması teşvik edilmez.**

---

## 👨‍💻 Katkıda Bulun

Projeye katkıda bulunmak istersen:
- Yeni özellikler ekleyebilirsin
- Hataları bildirebilirsin
- PR (pull request) gönderebilirsin

---

## 📬 İletişim

> Her türlü geri bildirim ve öneri için GitHub üzerinden ulaşabilirsiniz.  
> Bu proje yalnızca öğrenim ve kişisel gelişim amaçlıdır.
