import arxiv
import fitz  # PyMuPDF
import re
import random
import pandas as pd
separator = "\n---SEPARATOR---\n"

def get_summary_from_ids(id_list):
    # Initialize a list to store titles
    summary = []

    # Query arXiv for each arXiv ID and retrieve paper metadata
    for arxiv_id in id_list:
        try:
            paper = next(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
            print(paper.title)
            summary.append(paper.title+": "+paper.summary)
        except Exception as e:
            summary.append(f"Title not found for {arxiv_id}")

    return summary

def extract_references(text):
    # Find the references section
    references_start = re.search(r'References|Bibliography', text)
    if not references_start:
        return ""

    # Extract everything after the references section starts
    references_text = text[references_start.start():]
    
    return references_text

def extract_arxiv_ids(references_text):
    # Define the regex patterns for arXiv IDs
    new_arxiv_id_pattern = re.compile(r'\d{4}\.\d{5}')
    old_arxiv_id_pattern = re.compile(r'arXiv:\d{4}\d{2}\.\d{4}(v\d+)?')
    
    # Find all arXiv IDs in the references text
    new_arxiv_ids = new_arxiv_id_pattern.findall(references_text)
    old_arxiv_ids = old_arxiv_id_pattern.findall(references_text)
    
    # Combine both lists of IDs
    arxiv_ids = new_arxiv_ids + old_arxiv_ids
    
    return arxiv_ids

def fetch_paper_titles(arxiv_ids):
    # Initialize a list to store titles
    titles = []

    # Query arXiv for each arXiv ID and retrieve paper metadata
    for arxiv_id in arxiv_ids:
        try:
            paper = next(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
            titles.append(paper.title)
        except Exception as e:
            titles.append(f"Title not found for {arxiv_id}")

    return titles

def fetch_paper_dates(arxiv_ids):
    # Initialize a list to store titles
    dates = []

    # Query arXiv for each arXiv ID and retrieve paper metadata
    for arxiv_id in arxiv_ids:
        try:
            paper = next(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
            dates.append(paper.published)
        except Exception as e:
            dates.append(f"Date not found for {arxiv_id}")

    return dates

def get_full_text(pdf_path):
    document = fitz.open(pdf_path)

    # Extract text from each page
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text