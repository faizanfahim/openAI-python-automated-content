import openai
import csv
import sys

openai.api_key = "YOUR_API_KEY"

def generate_article(prompt, model_engine):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.5,
    )

    article = response.choices[0].text
    return article.strip()

# ask for file path
file_path = input("Enter the file path: ")

# ask for column name
column_name = input("Enter the column name: ")

# ask for OpenAI API key
openai.api_key = input("Enter your OpenAI API key: ")

# ask for model engine
model_engine = input("Enter the OpenAI model engine: ")

# read the csv file
with open(file_path, 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        keyword = row[column_name]
        prompt = f"Write an informative and engaging article about {keyword} in 500 words."
        article = generate_article(prompt, model_engine)
        with open(f"{keyword}.txt", "w") as output_file:
            output_file.write(article)
            print(f"Article written for {keyword}")
