import os
import google.generativeai as genai
import json

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

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


# Note: This script was an early experiment using Gemini for category clustering.
# I later moved the active pipeline to Groq's API (Llama 3.3) after hitting
# rate limits on Gemini's free tier — see process_data.ipynb for the current version.
if __name__ == "__main__":
    unique_categories = ['Dating', 'Finance', 'Weather', 'Action', 'Education', 'Business']
    clusters = get_market_clusters(unique_categories)
    print(clusters)
