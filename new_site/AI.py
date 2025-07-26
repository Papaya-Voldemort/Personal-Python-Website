import requests
import random

# Base prompts for different quote styles
quote_prompts = [
    "Write a short motivational quote (max 20 words). Respond only with the quote, no extra text.",
    "Give me a short, deep quote that makes you think (under 20 words). Only the quote, no extra text.",
    "Create a short quote about imagination and ideas (under 20 words). Respond with the quote only.",
    "Give me a poetic life quote (max 15 words). Do not include anything except the quote itself.",
    "Write a short, tough quote about perseverance or discipline (under 20 words). Only the quote.",
    "Write a short, sarcastic quote about life (under 15 words). Respond only with the quote.",
    "Write a short, punchy quote about ambition or startups (15 words or less). No extras, only the quote.",
    "Give me a short motivational quote using video game metaphors (under 15 words). Just the quote.",
    "Write a mystical quote about fate (max 15 words). Respond only with the quote.",
    "Create a short quote about AI or the future (under 15 words). Only return the quote.",
    "Give me a short Zen-like quote about mindfulness or peace (max 12 words). Just the quote."
]

# Optional variations to slightly change prompts and add entropy
prompt_variations = [
    "",  # empty = use base prompt
    " Make it unique.",
    " Make it powerful.",
    " Make it original.",
    " Keep it vivid.",
    " Add some personality.",
    " With a twist."
]


def get_random_quote_prompt():
    base = random.choice(quote_prompts)
    twist = random.choice(prompt_variations)
    return base + twist


def generate_ai_quote():
    url = "https://ai.hackclub.com/chat/completions"
    headers = {"Content-Type": "application/json"}

    data = {
        "messages": [
            {"role": "user", "content": get_random_quote_prompt()}
        ],
        "temperature": round(random.uniform(0.9, 1.3), 2),  # Controlled chaos
        "top_p": round(random.uniform(0.85, 0.95), 2)  # Slight vocab diversity variation
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"


