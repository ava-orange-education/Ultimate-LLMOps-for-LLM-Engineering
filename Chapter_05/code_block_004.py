def semantic_chunking(document):
    """Split document by semantic boundaries (paragraphs, sections)"""
    chunks = document.split("\n\n")  # Split by paragraphs
    return [chunk.strip() for chunk in chunks if chunk.strip()]
    # Result: ["Introduction paragraph", "Methods section", "Results..."]