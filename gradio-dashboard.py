import pandas as pd
import numpy as np
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

import gradio as gr

load_dotenv()

books = pd.read_csv("books_with_emotions.csv")
books["large_thumbnail"]= books["thumbnail"] + "&fife=w800"
books["large_thumbnail"]= np.where(
    books["large_thumbnail"].isna(),
    "cover-not-found.jpg",
    books["large_thumbnail"]
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1,
    chunk_overlap=0,
    separators="\n"
)
raw_documents = TextLoader(
    ".\\tagged_description.txt",
    encoding="utf-8"
).load()

documents = text_splitter.split_documents(raw_documents)

print("🚀 ChromaDB başlatılıyor...")

# ChromaDB client
chroma_client = chromadb.Client()

# Eski collection'ı sil
try:
    chroma_client.delete_collection(name="db_books")
    print("✅ Eski collection silindi")
except:
    print("✅ Yeni collection oluşturuluyor")

# Collection oluştur (default embedding - ekstra kurulum gerektirmez)
db_books = chroma_client.create_collection(
    name="db_books"
)

print("✅ Collection hazır")

# *** BURADA EKSİK OLAN KISIM: VERİLERİ EKLEME ***
print("📚 Dokümanlar ekleniyor...")

# Dokümanları hazırla
doc_texts = [doc.page_content for doc in documents]
doc_ids = [f"doc_{i}" for i in range(len(documents))]

# Verileri ekle
db_books.add(
    documents=doc_texts,
    ids=doc_ids
)

print(f"✅ {len(documents)} doküman başarıyla eklendi\n")


def retrieve_semantic_recommendations(
        query: str,
        category: str=None,
        tone: str = None,
        initial_top_k: int=50,
        final_top_k: int=16,
)-> pd.DataFrame:
    # similarity_search yerine query kullanın
    recs = db_books.query(
        query_texts=[query],
        n_results=initial_top_k
    )
    
    # Debug için
    print(f"Query: {query}")
    print(f"Bulunan sonuç sayısı: {len(recs['documents'][0]) if recs['documents'] else 0}")
    
    # Sonuçları işleyin - tüm tırnak işaretlerini kaldır
    books_list = []
    for doc in recs['documents'][0]:
        try:
            # Tüm tırnak işaretlerini kaldır ve ilk kelimeyi al
            isbn_str = doc.replace('"', '').replace("'", '').split()[0]
            books_list.append(int(isbn_str))
        except (ValueError, IndexError) as e:
            print(f"⚠️ ISBN parse hatası: {doc[:50]}... - Hata: {e}")
            continue
    
    book_recs = books[books["isbn13"].isin(books_list)].head(final_top_k)

    if category != "All":
        book_recs = book_recs[book_recs["simple_categories"]==category][:final_top_k]
    else:
        book_recs = book_recs.head(final_top_k)
        
    if tone == "Happy":
        book_recs.sort_values(by="joy", ascending=False, inplace=True)
    elif tone == "Surprising":  # Yazım hatası düzeltildi
        book_recs.sort_values(by="surprise", ascending=False, inplace=True)
    elif tone == "Angry": 
        book_recs.sort_values(by="anger", ascending=False, inplace=True)
    elif tone == "Suspenseful": 
        book_recs.sort_values(by="surprise", ascending=False, inplace=True)
    elif tone == "Sad": 
        book_recs.sort_values(by="sadness", ascending=False, inplace=True)
    
    return book_recs


def recommend_books(
        query: str,
        category: str,
        tone: str
):
    recommendations = retrieve_semantic_recommendations(query, category, tone)
    results = []
    for _, row in recommendations.iterrows():
        description = row["description"]
        truncated_desc_split = description.split()
        truncated_description = " ".join(truncated_desc_split[:30]) + "..."

        authors_split = row["authors"].split(";")
        if len(authors_split) == 2:
            authors_str = f"{authors_split[0]} and {authors_split[1]}"
        elif len(authors_split) > 2:
            authors_str = f"{', '.join(authors_split[:-1])}, and {authors_split[-1]}"
        else:
            authors_str = row["authors"]

        caption = f"{row['title']} by {authors_str}: {truncated_description}"
        results.append((row["large_thumbnail"], caption))
    return results

categories = ["All"] + sorted(books["simple_categories"].unique())
tones = ["All", "Happy", "Sad", "Angry", "Suspenseful", "Surprising"]  # "Suprising" yazım hatası düzeltildi

with gr.Blocks(theme=gr.themes.Glass()) as dashboard:
    gr.Markdown("# Semantik Kitap Öneri Sistemi 📚")

    with gr.Row():
        user_query = gr.Textbox(
            label="Lütfen okumak istediğiniz kitap hakkında birkaç kelime yazın:",
            placeholder="Örneğin: Bir bilim kurgu romanı, uzay yolculuğu ve macera dolu...",
        )
        category_dropdown = gr.Dropdown(
            label="Kategori Seçin",
            choices=categories,
            value="All",
        )
        tone_dropdown = gr.Dropdown(
            label="Hangi Duyguya Sahip Kitaplar İstersiniz?",
            choices=tones,
            value="All")
        submit_button = gr.Button("Önerileri Getir 🚀")
    
    gr.Markdown("### Önerilen Kitaplar:")
    output = gr.Gallery(label="Önerilen Kitaplar", columns=8, rows=2)
    submit_button.click(fn=recommend_books,
                        inputs=[user_query, category_dropdown, tone_dropdown],
                        outputs=output
                        )

if __name__ == "__main__":
    dashboard.launch()