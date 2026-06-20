from pypdf import PdfReader

from sentence_transformers import (
    SentenceTransformer
)

import faiss
import numpy as np

from services.llm_service import (
    initialize_llm
)


# Load embedding model once
embedding_model = (
    SentenceTransformer(
        "all-MiniLM-L6-v2"
    )
)


def extract_text_from_pdf(
    uploaded_file
):
    """
    Extract all text from PDF
    """

    pdf = PdfReader(
        uploaded_file
    )

    text = ""

    for page in pdf.pages:

        page_text = (
            page.extract_text()
        )

        if page_text:

            text += (
                page_text + "\n"
            )

    return text


def chunk_text(
    text,
    chunk_size=1000,
    overlap=200
):
    """
    Split text into chunks
    """

    chunks = []

    start = 0

    while start < len(text):

        end = (
            start + chunk_size
        )

        chunks.append(
            text[start:end]
        )

        start += (
            chunk_size - overlap
        )

    return chunks


def create_vector_store(
    chunks
):
    """
    Create FAISS index
    """

    embeddings = (
        embedding_model.encode(
            chunks
        )
    )

    embeddings = np.array(
        embeddings
    ).astype(
        "float32"
    )

    dimension = (
        embeddings.shape[1]
    )

    index = (
        faiss.IndexFlatL2(
            dimension
        )
    )

    index.add(
        embeddings
    )

    return (
        index,
        chunks
    )


def retrieve_context(
    question,
    index,
    chunks,
    top_k=3
):
    """
    Retrieve relevant chunks
    """

    question_embedding = (
        embedding_model.encode(
            [question]
        )
    )

    question_embedding = (
        np.array(
            question_embedding
        ).astype(
            "float32"
        )
    )

    distances, indices = (
        index.search(
            question_embedding,
            top_k
        )
    )

    retrieved_chunks = []

    for idx in indices[0]:

        if idx < len(chunks):

            retrieved_chunks.append(
                chunks[idx]
            )

    return retrieved_chunks


def answer_question(
    question,
    index,
    chunks
):
    """
    RAG Question Answering
    """

    context_chunks = (
        retrieve_context(
            question,
            index,
            chunks
        )
    )

    context = "\n\n".join(
        context_chunks
    )

    llm = initialize_llm()

    prompt = f"""
You are a financial analyst.

Answer ONLY using the
provided context.

Context:
{context}

Question:
{question}

Instructions:
- Use information only from context.
- If answer is unavailable,
  say it is not mentioned.
- Keep answer concise.
"""

    response = llm.invoke(
        prompt
    )

    return (
        response.content,
        context_chunks
    )