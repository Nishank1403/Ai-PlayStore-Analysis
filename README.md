# 🚀 AI-Driven Data Pipeline: Google Play Store Market Analysis

### 📌 Overview

A data processing project that analyzes 2.2M+ Google Play Store records to find market trends. The pipeline cleans and clusters app category data, then uses Groq's API (Llama 3.3) to turn the clustered data into short, human-readable market insight summaries.

### 🛠️ Tech Stack

- **Language:** Python (Pandas)
- **AI / LLM:** Groq API (Llama 3.3) — used for generating narrative insights
- **Visualization:** Flourish (Bar Chart Race)
- **Tools:** Jupyter Notebook, VS Code

### 🧠 Key Features

**Large-Scale Data Processing**
- Processed 2.2M+ records from the Google Play Store dataset
- Cleaned and standardized raw category/rating/install data using Pandas

**Data Clustering**
- Grouped 50+ app categories into 6 broader market segments
- Used as a basis for trend analysis across category groups

**AI-Generated Insights**
- Sent processed/clustered data to the Groq API (Llama 3.3) to generate short narrative summaries of market trends
- Note: an earlier version of the clustering step (`get_clusters.py`) used Google's Gemini API. I switched to Groq after hitting rate limits on Gemini's free tier — Groq is the version actually used in the current pipeline.

### 📊 Final Visualization

🔗 [Interactive Bar Chart Race Visualization](https://public.flourish.studio/visualisation/27055894/)

### 📂 Data Source

Due to the large size (2.2M+ records), the raw dataset is not included in this repository.

📥 **Download here:** [Google Play Store Apps Dataset on Kaggle](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps)

### 📁 Project Structure

```
get_clusters.py              # Earlier Gemini-based clustering experiment (not the active pipeline)
process_data.ipynb           # Main notebook: cleaning, clustering, and Groq/Llama insight generation
playstore_FLOURISH_FINAL.csv # Processed data used for the Flourish visualization
playstore_race_ready.csv     # Intermediate processed dataset
```

### 💡 What This Project Demonstrates

- Processing and cleaning a large real-world dataset with Pandas
- Basic data clustering/categorization
- Integrating an LLM API (Groq/Llama 3.3) into a data workflow to generate readable summaries
- Comparing two LLM providers (Gemini vs. Groq) and choosing one based on practical constraints (rate limits)

### 🚀 Possible Future Improvements

- Move the API key handling to a `.env` file across both scripts (currently done in `get_clusters.py`)
- Consolidate the Gemini experiment and the Groq pipeline into one configurable script
- Add a requirements.txt for easier setup
