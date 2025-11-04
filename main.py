from utils.transcript_loader import get_youtube_transcript
from utils.text_splitter import split_text
from utils.vector_store import create_vector_store
from rag.retriever import get_retriever
from rag.chat_chain import build_chat_chain
from config.settings import VECTOR_STORE_PATH, EMBEDDING_MODEL

def main():
    print("Enter YouTube video URL:")
    video_url = input("> ")

    print(" Fetching transcript...")
    transcript = get_youtube_transcript(video_url)

    print("Splitting text into chunks...")
    chunks = split_text(transcript)

    print("Creating vector store...")
    create_vector_store(chunks, VECTOR_STORE_PATH, EMBEDDING_MODEL)

    retriever = get_retriever()
    chat_chain = build_chat_chain(retriever)

    print("\n Ask questions about the video (type 'exit' to quit):\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        result = chat_chain({"question": query})
        print(f"Bot: {result['answer']}\n")

if __name__ == "__main__":
    main()
