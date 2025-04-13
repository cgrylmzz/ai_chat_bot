import difflib  # Yakın eşleşme algoritmaları için
import time  # Zaman gecikmesi vermek için
import json  # Veri kaydetme ve okuma için
import os  # Dosya işlemleri için

# Yapay zekâ botunun temel sınıfı
class ArtificialIntelligenceBot:
    def __init__(self):     
        self.questions = {}  # Tüm soru-cevaplar burada tutulur
        self.load_data()  # Kaydedilmiş verileri yükler
        self.load_banned_words()  # Yasaklı kelimeleri yükler
        
    def load_data(self):
        # Soru-cevap veritabanını 'data.json' dosyasından okur
        if os.path.exists("data.json"):
            with open("data.json", "r", encoding="utf-8") as file:
                self.questions = json.load(file)
        else:
            self.questions = {}  # Dosya yoksa boş sözlük başlatılır
    
    def save_data(self):
        # Tüm verileri 'data.json' dosyasına kaydeder
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(self.questions, file, ensure_ascii=False, indent=4)
 
    def load_banned_words(self):
        # Yasaklı kelimeleri 'banned_words.txt' dosyasından okur
        if os.path.exists("banned_words.txt"):
            with open("banned_words.txt", "r", encoding="utf-8") as file:
                self.banned_words = [line.strip().lower() for line in file if line.strip()]         
        else:
            self.banned_words = []  # Dosya yoksa boş liste başlatılır

    def is_clean(self, text):
        # Verilen metin yasaklı kelime içeriyor mu kontrol eder
        return not any(word in text.lower() for word in self.banned_words)

    def log_unanswered_question(self, question):
        # Cevaplanamayan soruları 'unanswered.txt' dosyasına yazar
        with open("unanswered.txt", "a", encoding="utf-8") as file:
            file.write(question + "\n")

    def remove_from_unanswered(self, question):
        # Cevaplanan soruyu 'unanswered.txt' dosyasından siler
        if not os.path.exists("unanswered.txt"):
            return
        with open("unanswered.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip().lower() != question.lower()]
        with open("unanswered.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)

    def ask_a_question(self, question):
        # Bot'a soru sorulduğunda çalışır
        question = question.lower().strip()

        # Soru yasaklı kelime içeriyor mu kontrol edilir
        if not self.is_clean(question):
            return "Lütfen uygun bir dil kullan."

        # Soru doğrudan veritabanında varsa cevabı döner
        if question in self.questions:
            return self.questions[question]

        # Benzer (yakın) bir soru var mı kontrol edilir
        closest_matches = difflib.get_close_matches(question, self.questions.keys(), n=1, cutoff=0.6)
        if closest_matches:
            return f"Şunu mu demek istedin? '{closest_matches[0]}'\nCevap: {self.questions[closest_matches[0]]}"
        else:
            # Hiçbir eşleşme yoksa, soru cevapsızlar listesine eklenir
            self.log_unanswered_question(question)
            return "Bu soruya henüz yanıtım yok."

    def add_question_and_answer(self, question, answer):
        # Yeni soru-cevap eklemek için kullanılır
        question = question.lower().strip()

        # Yasaklı kelime kontrolü
        if not self.is_clean(question) or not self.is_clean(answer):
            return "Yasaklı kelime içerdiği için kayıt yapılmadı."

        if not answer.strip():
            return "Boş cevap kaydedilemez."

        self.load_data()  # Güncel verileri tekrar yükle, üzerine yazmayı önler

        if question in self.questions:
            return "Bu soru zaten kayıtlı."

        # Yeni soru ve cevabı kaydet
        self.questions[question] = answer
        self.save_data()
        self.remove_from_unanswered(question)
        return "Yeni bilgi başarıyla kaydedildi."

    def delete_question(self, question):
        # Kayıtlı bir soruyu silmek için
        question = question.lower().strip()
        if question in self.questions:
            del self.questions[question]
            self.save_data()
            return f"'{question}' sorusu başarıyla silindi."
        else:
            return "Böyle bir soru bulunamadı."

    def show_questions(self):
        # Kayıtlı tüm soru-cevapları listeler
        if not self.questions:
            print("Henüz kayıtlı bir soru yok.")
        else:
            for question, answer in self.questions.items():   
                print(f"{question} --> {answer}")

    def handle_unanswered_questions(self):
        # Cevapsız sorulara kullanıcıdan cevap almak için
        if not os.path.exists("unanswered.txt"):
            print("Cevapsız soru bulunmuyor.")
            return
        
        with open("unanswered.txt", "r", encoding="utf-8") as file:
            questions = list(set([line.strip() for line in file if line.strip()]))

        if not questions:
            print("Cevapsız soru bulunmuyor.")
            return
        
        # Her bir cevapsız soru için kullanıcıya sorma
        for question in questions:
            print(f"\nSoru: {question}")
            choice = input("Bu soruya cevap vermek ister misin? (e/h): ").lower()
            
            if choice == "e":
                answer = input("Cevabını yaz: ")
                print(self.add_question_and_answer(question, answer))
        
        # Artık cevaplananlar zaten tek tek siliniyor

# Terminal menüsü fonksiyonu
def menu():
    print("1- Soru sor")
    print("2- Soru ve cevap ekle")
    print("3- Soru sil")
    print("4- Kayıtlı soruları göster")
    print("5- Cevapsız soruları göster")
    print("q - Çıkmak için q tuşlayın")

# Bot nesnesi oluşturuluyor
bot = ArtificialIntelligenceBot()

# Ana uygulama döngüsü
def main():
    while True:
        print("\nYapay Zeka Botuna Hoş Geldiniz")
        menu()
        user_choice = input("Seçiminizi yapın (1-5 ya da q): ")
        
        if user_choice.lower() == "q":
            print("Uygulama kapatılıyor...")
            time.sleep(2)
            print("Uygulama kapandı.")
            break

        if user_choice == "1":
            question = input("Sorunuzu yazın: ")
            print(bot.ask_a_question(question))

        elif user_choice == "2":
            question = input("Eklemek istediğiniz soru: ")
            answer = input("Bu sorunun cevabı: ")
            print(bot.add_question_and_answer(question, answer))

        elif user_choice == "3":
            delete_question = input("Silmek istediğiniz soru: ")
            print(bot.delete_question(delete_question))

        elif user_choice == "4":
            bot.show_questions()

        elif user_choice == "5":
            bot.handle_unanswered_questions()

        else:
            print("Lütfen geçerli bir seçim yapın.")
            continue

# Uygulama buradan başlar
if __name__ == "__main__":
    main()
