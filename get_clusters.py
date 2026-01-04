import google.generativeai as genai
import pandas as pd
import json

# Paste your key here
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_market_clusters(categories):
    prompt = f"""
    I have these Google Play Store categories: {categories}
    Group them into exactly 6 'Market Clusters' (e.g., Entertainment, Tools, Lifestyle, Social, Productivity, Education).
    Return ONLY a JSON dictionary where the KEY is the original category and the VALUE is the cluster name.
    Example: {{"Dating": "Social", "Finance": "Productivity"}}
    """
    response = model.generate_content(prompt)
    # Cleans the response to ensure it's valid JSON
    clean_json = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(clean_json)

# Test it with a few categories
unique_categories = ['Dating', 'Finance', 'Weather', 'Action', 'Education', 'Business']
clusters = get_market_clusters(unique_categories)
print(clusters)