import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

modelname = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(modelname)
model = AutoModelForSequenceClassification.from_pretrained(modelname)

def sentimentanalyze(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
    predicted_label = model.config.id2label[predicted_class_id]    

    return predicted_label