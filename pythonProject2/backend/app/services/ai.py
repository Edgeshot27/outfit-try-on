from transformers import pipeline

# Initialize the text-generation pipeline
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

def generate_compliance_insights(data: dict) -> str:
    """
    Generate compliance insights using GPT-Neo.
    :param data: Compliance data containing issues or patterns.
    :return: AI-generated insights or suggestions.
    """
    prompt = (
        "Analyze the following supplier compliance issues and provide actionable suggestions: "
        f"{data}"
    )
    response = generator(prompt, max_length=100)
    return response[0]["generated_text"]
