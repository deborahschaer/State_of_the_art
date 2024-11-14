# State_of_the_art
I like to evaluate if an LLM can create a state of the art text.

The project is divided into 3 task. 
- Task 1: Summarization
- Task 2: Selection of relevant papers
- Task 3: Combining articles to State of the art.


### Installation
The project was written on Ubuntu with Python 3.12.3.
To get all python packages install these requirements in your local virtual environment:

```bash
pip install -r requirements.txt
```

Further you can get Ollama installed with:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```
For installation on other systems check https://ollama.com/

Then you can pull the lastest version of mistral with:

```bash
ollama pull mistral
```

### Project Structure

```plaintext
project-root/
│
├── README.md                       # Overview of the project and installation
├── requirements.txt                # List of dependencies needed for the project
├── arxiv_tool.py                   # Some functions used to get papers from ArXiv and treat them.
├── create_dataset.ipynd            # This code was used to create the dataset for task 2 and 3.
|
├── task1/                          # Experiments of task 1
│   ├── dataset/                    # Dataset of ArXiv papers. Test part of scientific papers.
│   ├── results/                    # Filename indicates if these are BERTScore, ROUGE scores or selfevaluation.
                                      in each file are three columns: precision, recall and F1.
                                      The last 2 lines are mean and std.
│   ├── summaries/                  # All summaries. 'Complex' means that they were created with the complex prompt.
│   ├── create_summaries.ipynb      # Here summaries were created and stored in 'summaries/'
│   ├── data.py                     # Function to load the papers from dataset.
│   ├── evaluate_summaries.ipynb    # Calucaltions of scores, they are stored in 'results/'.
│   └── visualize_evaluation.ipynb  # Create a boxplot. 

|
├── task2/                          # Experiments of task 2
│   ├── dataset/                    # Dataset of ArXiv papers. The id is in the filename.
│   ├── results/                    # Results of task2
        ├── P_R_F1.txt              # precision, recall and F1 of
                                      in each file are three columns: .
                                      The last 2 lines are mean and std.
│   ├── create_summaries.ipynb      # Here summaries were created and stored in 'summaries/'
│   ├── data.py                     # Function to load the papers from dataset.
│   ├── evaluate_summaries.ipynb    # Calucaltions of scores, they are stored in 'results/'.
│   └── visualize_evaluation.ipynb  # Create a boxplot. 




├── data/                    # Data directory
│   ├── raw/                 # Raw, unprocessed data
│   ├── processed/           # Cleaned and processed data
│   └── ...                  # Other data folders as needed
│
├── config/                  # Configuration files
│   └── config.yaml          # Main configuration settings
│
├── notebooks/               # Jupyter notebooks for exploration and analysis
│   └── data_analysis.ipynb  # Example notebook for data analysis
│
└── tests/                   # Directory for test files
    ├── test_main.py         # Unit tests for main functionality
    └── ...                  # Other test files
