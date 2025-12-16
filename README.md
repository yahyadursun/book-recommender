# Semantik Kitap Öneri Sistemi 📚

Bu proje, yapay zeka destekli bir kitap öneri sistemidir. Kullanıcının girdiği metin tabanlı açıklamalara, seçilen kategorilere ve istenen duygu durumuna (ton) göre en uygun kitapları önerir.

**Önemli Not:** Bu proje tamamen **yerel** olarak çalışır ve herhangi bir harici API anahtarına (OpenAI vb.) ihtiyaç duymaz.

## 🚀 Özellikler

- **Semantik Arama:** Kullanıcının doğal dilde yazdığı açıklamalara göre (örn: "uzayda geçen macera") kitapları bulur.
- **Yerel Embeddingler:** ChromaDB'nin varsayılan gömme modellerini (Sentence Transformers) kullanarak metinleri vektörleştirir. Ücretsiz ve hızlıdır.
- **Duygu Analizi (Sentiment Analysis):** Kitapları "Mutlu", "Üzgün", "Korku", "Şaşırtıcı" gibi duygu durumlarına göre filtreler.
- **Kategori Filtreleme:** Belirli kitap kategorilerine göre arama yapma imkanı sunar.
- **Görsel Arayüz:** Gradio tabanlı kullanıcı dostu bir web arayüzü.

## 🧠 Yapay Zeka (AI) Kullanımı

Bu projede yapay zeka teknolojileri, kullanıcı deneyimini zenginleştirmek ve daha isabetli öneriler sunmak amacıyla iki temel alanda kullanılmıştır:

### 1. Embeddings (Vektör Gömme)
Metinleri (kitap açıklamaları ve kullanıcı sorguları) matematiksel vektörlere dönüştürmek için kullanılır.
- **Ne İçin Kullanıldı?** Klasik anahtar kelime eşleşmesi yerine **Semantik Arama (Anlamsal Arama)** yapabilmek için.
- **Faydası:** Kullanıcı "uzayda geçen bir macera" yazdığında; içinde "uzay" kelimesi geçmese bile, konusu yıldızlararası seyahat veya galaksiler olan kitapları anlayıp önerebilir. ChromaDB ve varsayılan gömme modelleri bu işlevi üstlenir.

### 2. LLM (Büyük Dil Modelleri)
Kitapların içeriklerini analiz etmek ve sınıflandırmak için kullanılmıştır (Veri hazırlık aşamasında).
- **Ne İçin Kullanıldı?** **Duygu Analizi (Sentiment Analysis)** ve metin sınıflandırma işlemleri için.
- **Faydası:** Kitap açıklamaları LLM'ler tarafından analiz edilerek her kitaba "Neşe", "Üzüntü", "Korku", "Gerilim" gibi duygu etiketleri atanmıştır. Bu sayede kullanıcılar sadece konuya göre değil, **okumak istedikleri kitabın hissettireceği duyguya (Mood)** göre de filtreleme yapabilirler.

## 🛠️ Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/KULLANICI_ADINIZ/book-recommender.git
   cd book-recommender
   ```

2. **Sanal ortam oluşturun (Önerilen):**
   ```bash
   python -m venv venv
   # Windows için:
   .\venv\Scripts\activate
   # Mac/Linux için:
   source venv/bin/activate
   ```

3. **Gereksinimleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Kullanım

Uygulamayı başlatmak için terminalde şu komutu çalıştırın:

```bash
python gradio-dashboard.py
```

Tarayıcınızda açılan yerel adres (genellikle `http://127.0.0.1:7860`) üzerinden arayüze erişebilirsiniz.

## 🏗️ Kullanılan Teknolojiler

- **Python**: Ana programlama dili.
- **LangChain**: LLM uygulamaları geliştirmek için framework.
- **ChromaDB**: Vektör veritabanı ve yerel embedding motoru.
- **Gradio**: Web arayüzü oluşturmak için.
- **Pandas & NumPy**: Veri işleme için.

## 📂 Veri Seti

Proje, kitap açıklamaları, kategoriler ve duygu etiketlerini içeren zenginleştirilmiş bir veri seti kullanır (`books_with_emotions.csv`).
