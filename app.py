# import streamlit as st
# from main import pipeline
# import tempfile
# import os

# st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
# st.title("Agentic RAG Chatbot")

# # Initialize session states
# if "history" not in st.session_state:
#     st.session_state.history = []

# if "file_paths" not in st.session_state:
#     st.session_state.file_paths = []

# # Save uploaded file
# def save_uploaded_file(uploaded_file):
#     temp_dir = tempfile.gettempdir()
#     file_path = os.path.join(temp_dir, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.read())
#     return file_path

# # File uploader
# uploaded_files = st.file_uploader(
#     "Upload Documents",
#     type=["pdf", "docx", "pptx", "csv", "txt", "md"],
#     accept_multiple_files=True
# )

# # Save files on upload only once
# if uploaded_files and not st.session_state.file_paths:
#     st.session_state.file_paths = [save_uploaded_file(f) for f in uploaded_files]
#     st.success("✅ Files uploaded and indexed!")

# # Display chat history
# if st.session_state.history:
#     st.subheader("🕘 Chat History")
#     for i, (q, a, sources) in enumerate(st.session_state.history[::-1]):
#         st.markdown(f"**Q{i+1}:** {q}")
#         st.markdown(f"**A:** {a}")
#         with st.expander("📄 Top 3 Source Chunks"):
#             chunks = sources.split("\n\n") if isinstance(sources, str) else sources
#             for idx, chunk in enumerate(chunks[:3]):
#                 st.markdown(f"**Chunk {idx+1}:**")
#                 st.code(chunk.strip(), language="markdown")

# # 📥 Chat input inside a form to fix double submit
# with st.form("chat_form", clear_on_submit=True):
#     query = st.text_input("Ask a question:", key="query_input")
#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         if query.strip() and st.session_state.file_paths:
#             with st.spinner("🤖 Thinking..."):
#                 result = pipeline(st.session_state.file_paths, query.strip())
#                 st.session_state.history.append((query.strip(), result["answer"], result["sources"]))
#         else:
#             st.warning("Please upload documents and enter a valid question.")




import streamlit as st
from main import pipeline
import tempfile
import os

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title(" Agentic RAG Chatbot")

# File uploader
uploaded_files = st.file_uploader(
    "📎 Upload Documents",
    type=["pdf", "docx", "pptx", "csv", "txt", "md"],
    accept_multiple_files=True
)

# Save files to temp dir
def save_uploaded_file(uploaded_file):
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

if "file_paths" not in st.session_state:
    st.session_state.file_paths = []

# Save uploaded files only once
if uploaded_files and not st.session_state.file_paths:
    st.session_state.file_paths = [save_uploaded_file(f) for f in uploaded_files]
    st.success("Files uploaded and indexed!")

# Display chat history
if st.session_state.history:
    st.subheader(" Chat History")
    for i, (q, a, sources) in enumerate(st.session_state.history[::-1]):
        st.markdown(f"**Q{i+1}:** {q}")
        st.markdown(f"**A:** {a}")
        with st.expander(" Top 3 Source Chunks"):
            chunks = sources if isinstance(sources, list) else sources.split("\n\n")
            for idx, chunk in enumerate(chunks[:3]):
                st.markdown(f"**Chunk {idx+1}:**")
                st.code(chunk.strip(), language="markdown")


st.markdown("---")
with st.form(key="chat_form", clear_on_submit=True):
    query = st.text_input(" Ask a question:")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if not st.session_state.file_paths:
            st.warning("Please upload documents first.")
        else:
            with st.spinner(" Thinking..."):
                result = pipeline(st.session_state.file_paths, query.strip())
                st.session_state.history.append((query.strip(), result["answer"], result["sources"]))
