# **📊 Data Visualization Chatbot**

An interactive chatbot application for simplifying data analysis and visualization. This chatbot allows users to upload datasets, generate visualizations, and receive insights, all powered by advanced Large Language Models (LLMs) such as **Ollama**.

---

## **✨ Features**

- **📁 Dataset Upload**:
  - Upload Excel datasets (.xlsx) directly through the chatbot interface.
  - Uploaded datasets are securely stored in the `/datasets/raw/` directory.

- **📄 Dataset Summary**:
  - Automatic generation of dataset summaries, including:
    - Key columns and their data types.
    - Observations about the dataset structure.
  - Summaries are processed using **Ollama LLM** for natural language descriptions.

- **📈 Visualization Suggestions**:
  - Get tailored suggestions for visualizations based on the dataset's structure.
  - Supported chart types include:
    - **Bar Charts**
    - **Line Charts**
    - **Scatter Plots** and more.

- **🤖 Automated Visualization Generation**:
  - Generate visualizations automatically based on user requests.
  - Visualizations are stored in the `/visualizations/` directory for future reference.

- **🔍 Insights from Visualizations**:
  - Upload generated visualizations to receive insights such as:
    - Patterns and trends.
    - Key correlations and outliers.
    - Actionable business recommendations.

- **🔗 Combined Visualizations**:
  - Upload multiple visualizations to generate combined insights and visual outputs.
  - Get a holistic view of your data for in-depth analysis.

- **🖥️ Interactive Gradio Interface**:
  - A clean and user-friendly web interface for:
    - Dataset uploads.
    - Visualization requests and insights generation.

---

## **⚙️ Installation**

### **📋 Prerequisites**

- Python 3.8 or higher.
- [Pip](https://pip.pypa.io/en/stable/) for dependency management.
- [Gradio](https://gradio.app/) for the chatbot interface.
- [Ollama CLI](https://ollama.ai/) for LLM-based insights.

### **🔧 Setup Instructions**

1. **🛠️ Clone the repository**:
   ```bash
   git clone https://github.com/your-username/data-visualization-chatbot.git
   cd data-visualization-chatbot
🌐 Create and activate a virtual environment:
bash
Copy code
python -m venv venv

# For Windows: venv\Scripts\activate

# For macOS/Linux: source venv/bin/activate




📦 Install dependencies:
bash
Copy code
pip install -r requirements.txt
⚡ Ensure Ollama CLI is installed and configured:

Follow the official Ollama CLI installation guide.

📂 Create necessary directories:
bash
Copy code
mkdir -p datasets/raw datasets/summaries visualizations

🚀 Run the application:
bash
Copy code
python -m app.chatbot

🌐 Access the chatbot:
Open your browser and navigate to: http://127.0.0.1:7860.

📝 Usage
📤 Upload Dataset:
Upload an Excel file through the chatbot interface.
The chatbot confirms the upload and displays a dataset summary.

📊 Get Visualization Suggestions:
Request visualization suggestions tailored to your dataset.

🎨 Generate Visualizations:
Specify the type of chart and columns to visualize.
View and download generated visualizations.

🔍 Get Insights:
Upload a visualization to receive detailed insights powered by Ollama.

🔗 Combine Visualizations:
Upload multiple visualizations for combined insights and dynamic outputs.




##🔮**Future Scope**

📡 Real-Time Data Streaming:
Add support for real-time data ingestion and dynamic visualization updates.

📊 Advanced Analytics:
Integrate predictive analytics and anomaly detection capabilities.

🔗 Cross-Dataset Analysis:
Enable relationships between multiple datasets to uncover deeper insights.

🎨 Expanded Visualization Options:
Add support for advanced visualizations like heatmaps, treemaps, and geospatial maps.

📊 Business Intelligence Integration:
Integrate with tools like Power BI or Tableau for extended analytics.

🤖 Enhanced AI-Powered Recommendations:
Provide contextual business recommendations based on historical trends.

🤝 Contributing
We welcome contributions! Here's how you can help:

🐛 Report Issues:
Use GitHub issues to report bugs or suggest new features.

🔀 Submit Pull Requests:
Fork the repository, make changes, and submit a pull request.

📜 License
This project is licensed under the MIT License.

🙏 Acknowledgments
Ollama AI for LLM-powered dataset insights and recommendations.
Gradio for a seamless and interactive chatbot interface.
Open-source libraries like Matplotlib, Pandas, and Subprocess.
vbnet
Copy code
