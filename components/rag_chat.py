import streamlit as st

from services.rag_pipeline import (
    extract_text_from_pdf,
    chunk_text,
    create_vector_store,
    answer_question
)


def show_rag_chat():

    st.header("📄 Financial Report RAG")
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:
        if st.button(
            "📄 Process PDF"
        ):

            with st.spinner(
                "Processing..."
            ):

                ...

    if uploaded_file is not None:

        current_file = uploaded_file.name

        # Process only if new PDF uploaded
        if (
            "pdf_name" not in st.session_state
            or
            st.session_state.pdf_name != current_file
        ):

            with st.spinner(
                "Processing PDF..."
            ):

                text = extract_text_from_pdf(
                    uploaded_file
                )

                chunks = chunk_text(
                    text
                )

                index, chunks = (
                    create_vector_store(
                        chunks
                    )
                )

                st.session_state.index = index
                st.session_state.chunks = chunks
                st.session_state.pdf_name = current_file

            st.success(
                "PDF processed successfully!"
            )

        index = st.session_state.index
        chunks = st.session_state.chunks

        st.info(
            f"📚 Total Chunks: {len(chunks)}"
        )

        st.divider()

        question = st.text_input(
            "Ask a question about the report"
        )

        if st.button(
            "Ask Question"
        ):

            if not question:

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Generating answer..."
                ):

                    answer, sources = (
                        answer_question(
                            question,
                            index,
                            chunks
                        )
                    )

                st.subheader(
                    "🤖 Answer"
                )

                st.write(
                    answer
                )

                st.divider()

                st.subheader(
                    "📚 Source Chunks"
                )

                for i, source in enumerate(
                    sources,
                    start=1
                ):

                    with st.expander(
                        f"Source {i}"
                    ):

                        st.write(
                            source
                        )

    else:

        st.info(
            "Upload a PDF to start chatting."
        )