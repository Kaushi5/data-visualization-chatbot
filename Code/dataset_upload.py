import os
import shutil
import pandas as pd
import subprocess

# Paths
RAW_DATA_PATH = "datasets/raw/"
SUMMARY_OUTPUT_PATH = "datasets/summaries/"

# Ensure directories exist
os.makedirs(RAW_DATA_PATH, exist_ok=True)
os.makedirs(SUMMARY_OUTPUT_PATH, exist_ok=True)


def process_dataset_with_ollama(file_path, model="llama2"):
    """
    Process the dataset using the Ollama model to generate a summary.

    Args:
        file_path (str): Path to the uploaded dataset.
        model (str): Ollama model to use (default: "llama2").

    Returns:
        str: Summary generated by the LLM.
    """
    try:
        # Read dataset for preview
        dataset = pd.read_excel(file_path, engine="openpyxl")
        preview = dataset.head().to_string()

        # Prompt for the LLM
        prompt = (
            "Analyze the following dataset and generate a summary, including:\n"
            "- Key columns\n"
            "- Data types\n"
            "- Observations about its structure\n\n"
            f"Dataset preview:\n{preview}"
        )

        # Call Ollama CLI
        ollama_command = ["ollama", "run", model]
        process = subprocess.run(
            ollama_command,
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8",
        )

        # Check for errors
        if process.returncode != 0:
            raise Exception(f"Ollama Error: {process.stderr.strip()}")

        # Return the model's response
        llm_response = process.stdout.strip()
        return llm_response

    except Exception as e:
        raise Exception(f"Error interacting with Ollama or processing the dataset: {str(e)}")


def handle_uploaded_file(file_path):
    """
    Handles the uploaded dataset, saves it, and processes it for a summary.

    Args:
        file_path (str): Path to the uploaded file.

    Returns:
        str: The dataset summary generated by the LLM.
    """
    try:
        # Validate file type
        if not file_path or not file_path.endswith(".xlsx"):
            return "Please upload a valid Excel (.xlsx) dataset."

        # Save the file to the raw data directory
        raw_file_path = os.path.join(RAW_DATA_PATH, os.path.basename(file_path))
        shutil.copy(file_path, raw_file_path)

        # Generate a dataset summary using Ollama
        llm_summary = process_dataset_with_ollama(raw_file_path)

        # Save the summary to a file
        summary_file = os.path.join(SUMMARY_OUTPUT_PATH, "dataset_summary.txt")
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(llm_summary)

        # Return the summary
        return llm_summary

    except Exception as e:
        return f"An error occurred while processing the dataset: {str(e)}"

