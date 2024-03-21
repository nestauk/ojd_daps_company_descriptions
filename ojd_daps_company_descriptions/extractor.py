# Description: This function extracts company descriptions from a given text using the jobbert-base-cased-compdecs model.

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def extract_company_descriptions(text):
    """Extract company descriptions from a given text using the jobbert-base-cased-compdecs model.
    Args:
        text (str): The input text.

    Returns:
        list[dict]: A list of dicts containing the confidence score of whether the sentence describes a company.
    """
    model = AutoModelForSequenceClassification.from_pretrained("nestauk/jobbert-base-cased-compdecs")
    tokenizer = AutoTokenizer.from_pretrained("nestauk/jobbert-base-cased-compdecs")
    comp_desc = pipeline('text-classification', model=model, tokenizer=tokenizer)
    return comp_desc(text)
