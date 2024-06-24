from transformers import pipeline

model = pipeline('summarization', model='facebook/bart-large-cnn')

def summarize(text):
    summary = model(text)[0]['summary_text']
    return summary