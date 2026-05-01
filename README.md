# 🚀 AI-Driven Data Pipeline: Google Play Store Market Analysis

### 📌 Overview
An end-to-end data engineering and analytics project that processes 2.2M+ Google Play Store records to uncover market trends and generate actionable insights. The system integrates Generative AI (Llama 3.3 via Groq) to automatically transform structured data into human-readable narratives and real-time “market intelligence” summaries.

### 🛠️ Tech Stack
- **Language:** Python (Pandas)
- **AI / LLM:** Groq API (Llama-3.3-70B)
- **Visualization:** Flourish (Bar Chart Race)
- **Tools:** Jupyter Notebooks, VS Code
- **Deployment Ready:** Modular pipeline design (Docker/AWS adaptable)

### 🧠 Key Features

**✅ Automated Insight Generation**
Processed market data is sent to the Groq API to generate real-time narrative summaries, simulating “Breaking News” style insights.

**✅ Large-Scale Data Processing**
- Handled 2.2M+ records efficiently
- Optimized Pandas operations to reduce memory overhead
- Built scalable workflows for batch processing

**✅ Data Transformation & Clustering**
- Cleaned and standardized raw data
- Clustered 50+ app categories into 6 strategic market segments
- Extracted patterns in ratings, installs, and pricing trends

**✅ Insight-Driven Analytics**
- Combined data analytics + GenAI to bridge technical outputs with business insights
- Enabled easier interpretation for non-technical stakeholders

### 📊 Final Visualization
🔗 [Interactive Bar Chart Race Visualization](https://public.flourish.studio/visualisation/27055894/)
- Displays evolving market trends over time
- Augmented with AI-generated narrative insights

### 📂 Data Source
Due to the large size (2.2M+ records), the raw dataset is not included in this repository. 

📥 **Download here:** [Google Play Store Apps Dataset on Kaggle](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps)

### 📁 Project Structure
```text
data/                  # (ignored) raw dataset
notebooks/             # Jupyter notebooks for EDA & processing
 ├── 01_eda.ipynb
 ├── 02_processing.ipynb
 └── 03_analysis.ipynb

src/                   # Core pipeline logic
 ├── config.py
 ├── data_processing.py
 ├── analysis.py
 └── ai_insights.py

outputs/               # Generated outputs
 ├── processed_data.csv
 ├── market_clusters.csv
 └── insights.json

visualization/         # Flourish assets
 └── flourish_template.json

requirements.txt
README.md
```

### 💡 What This Project Demonstrates
- End-to-end data pipeline design
- Handling and processing large-scale datasets (big data)
- Applying machine learning (clustering) for segmentation
- Integrating LLMs into real-world data workflows
- Translating technical results into business insights

### 🚀 Future Improvements
- Real-time streaming pipeline (Kafka / Spark)
- Dashboard integration (React / BI tools)
- Advanced ML models for predictive analytics
- Full cloud deployment (AWS Lambda + S3 + API Gateway)
