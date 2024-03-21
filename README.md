# OJD DAPS Company Description Classifier

OJD DAPS Company Description Classifier is a Python library powered by a fine-tuned BERT model, designed to determine whether a given sentence describes what a company does. It's particularly useful in parsing job advertisements to extract sentences that outline company descriptions, providing a score from 0 to 1 that reflects the model's confidence in the identification.

## Installation

This library can be installed using pip. Ensure you have Python 3.10 or newer installed on your system before proceeding.

```bash
pip install git+https://github.com/nestauk/ojd_daps_company_descriptions.git
```

## Usage

### Basic Usage

To use the extract_company_description function, you simply need to pass a sentence to it. The function returns a dictionary with a score indicating how likely the sentence is to be describing a company.

```python
from ojd_daps_company_descriptions import extract_company_description

sentence = "We are a manufacturing company specializing in innovative solutions."
result = extract_company_description(sentence)

print(result)
[{'label': 'LABEL_1', 'score': 0.9953641891479492}]
```

The output will be a dictionary, where the score ranges from 0 to 1. A higher score suggests a higher likelihood that the sentence is a company description.

### Working with Job Adverts

When dealing with job adverts, which typically consist of multiple sentences with only some referring to the company description, you can utilize the library in conjunction with pandas to efficiently process and extract relevant descriptions.

Assuming you have a pandas DataFrame `job_ads` with a column `description` that contains the text of the job adverts, you can apply the extract_company_description function to each row to identify and score sentences related to company descriptions.


```python
import pandas as pd
from company_description_extractor import extract_company_description

# Assuming `job_ads` is your DataFrame and `description` is the column with job descriptions
def extract_description_scores(description_text):
    sentences = description_text.split('.')
    scores = []
    for sentence in sentences:
        score = extract_company_description(sentence)[0]['score']
        scores.append((sentence, score))
    return scores

job_ads['description_scores'] = job_ads['description'].apply(extract_description_scores)

print(job_ads['description_scores'])
```

This approach splits the job description into sentences and applies the extract_company_description function to each, collecting the scores. You can then use these scores to filter or highlight descriptions that are likely to be about the company.

## Methodology

To see how we trained our model, details on its performance, and code relating to producing our training set, please refer to our doumentation [here](https://github.com/nestauk/ojd_daps_language_models/company_descriptions/README.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
