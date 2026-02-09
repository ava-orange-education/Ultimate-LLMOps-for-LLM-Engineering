# Simple chunking examples
def fixed_size_chunking(document, chunk_size=500):
    """Split document into fixed-size chunks"""
    words = document.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks
    # Result: ["chunk1 with 500 words...", "chunk2 with 500 words...", ...]