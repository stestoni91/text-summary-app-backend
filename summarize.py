from transformers import pipeline

model = pipeline('summarization')

def summarize(text):
    summary = model(text)[0]['summary_text']
    return summary