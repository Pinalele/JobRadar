skills = [

    "python", "sql", "java", "scala", "typescript", "go", "rust",
    "pandas", "numpy", "scikit-learn", "spark", "databricks", "snowflake", "airflow",
    "pytorch", "tensorflow", "keras", "deep learning", "computer vision", "nlp",
    "llm", "llms", "large language model", "generative ai", "genai",
    "transformers", "hugging face", "huggingface", "openai", "prompt engineering",
    "fine-tuning", "rag", "retrieval augmented generation",
    "vector database", "embeddings",
    "langchain", "langgraph", "llamaindex", "ai agents", "agentic",
    "mlops", "mlflow", "docker", "kubernetes", "fastapi", "terraform", "git",
    "aws", "azure", "gcp", "sagemaker", "bedrock", "vertex ai",
]

ai_words = ["ai", "ml", "llm"]
ai_phrases = ["artificial intelligence", "machine learning"]


def is_ai_role(title: str) -> bool:
    """Return True if the title mentions AI or machine learning."""
    for keyword in ai_phrases:
        if keyword in title.lower():
            return True
    for keyword in ai_words:
        if keyword in title.lower().replace("/", " ").split():
            return True
    return False


def skills_in(description: str) -> set:
    """Return the skills from the skills list found in the description."""
    found = set()
    text = description.lower()
    words = text.replace(",", " ").replace(".", " ").replace("/", " ").split()

    for skill in skills:
        if " " in skill:
            if skill in text:
                found.add(skill)
        else:
            if skill in words:
                found.add(skill)
    return found

