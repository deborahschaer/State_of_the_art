import json

def load_papers(split):
    file_path = 'dataset/'+split
    with open(file_path, 'r') as file:
        papers = file.read().strip().split('\n')  # Assuming papers are separated by double newlines
    abstracts = []
    texts = []
    for paper in papers:
        abstract = ''
        text = ''
        lines = paper.split('\n')
        for line in lines:        
            d = json.loads(line)
            abstract = "\n".join(d["abstract_text"])
            abstract= abstract.replace("<S>", "").replace("</S>", "")
            text = "\n".join(d["article_text"])
            text= text.replace("<S>", "").replace("</S>", "")
        abstracts.append(abstract)
        texts.append(text.strip())

        
    return abstracts, texts