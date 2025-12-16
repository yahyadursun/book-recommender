# Semantik Kitap Öneri Sistemi 📚

Bu proje, yapay zeka destekli bir kitap öneri sistemidir. Kullanıcının girdiği metin tabanlı açıklamalara, seçilen kategorilere ve istenen duygu durumuna (ton) göre en uygun kitapları önerir.

## 🚀 Özellikler

- **Semantik Arama:** Kullanıcının doğal dilde yazdığı açıklamalara göre (örn: "uzayda geçen macera") kitapları bulur.
- **Duygu Analizi (Sentiment Analysis):** Kitapları "Mutlu", "Üzgün", "Korku", "Şaşırtıcı" gibi duygu durumlarına göre filtreler.
- **Kategori Filtreleme:** Belirli kitap kategorilerine göre arama yapma imkanı sunar.
- **Görsel Arayüz:** Gradio tabanlı kullanıcı dostu bir web arayüzü.

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

4. **Çevresel Değişkenleri Ayarlayın:**
   `.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:
   ```
   OPENAI_API_KEY=sk-proj-...
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
- **ChromaDB**: Vektör veritabanı.
- **OpenAI Embeddings**: Metinleri vektörlere dönüştürmek için.
- **Gradio**: Web arayüzü oluşturmak için.
- **Pandas & NumPy**: Veri işleme için.

## 📂 Veri Seti

Proje, kitap açıklamaları, kategoriler ve duygu etiketlerini içeren zenginleştirilmiş bir veri seti kullanır (`books_with_emotions.csv`).
