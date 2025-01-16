import csv

def get_documents_from_csv():
    documents = []

    with open('./data/data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            sentence = row['question']
            intent = row['answer']
            doc = {'question': sentence, 'answer': intent}
            documents.append(doc)

    return documents

def get_prepared_docs():
    documents = get_documents_from_csv()

    preparedDocs = []
    for doc in documents:
        prepared = f'question: {doc['question']} answer: {doc['answer']}'
        preparedDocs.append(prepared)

    return preparedDocs