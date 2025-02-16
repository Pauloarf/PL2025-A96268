import re

# Função que dá parse do texto retirado do csv, e tokeniza-o
def parse_music_data(text):
    pattern = re.compile(r'(.+?);"(.*?)";(\d+);(\w+);(.+?);(\d{2}:\d{2}:\d{2});(O\d+)', re.DOTALL)
    
    lines = text.strip().split('\n')
    headers = lines[0].split(';')
    data_text = '\n'.join(lines[1:]) 
    
    matches = pattern.findall(data_text)
    
    cleaned_records = []
    for match in matches:
        cleaned_record = [" ".join(field.split()) for field in match]
        cleaned_records.append(cleaned_record)
    
    return headers, cleaned_records

# Recebe o header e os records para criar o csv
def write_csv(filename, headers, records):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(';'.join(headers) + '\n')
        for record in records:
            file.write(';'.join(record) + '\n')

# Processa os records para retirar a informação pertendida
def process_music_data(records):
    composers = sorted(set(" ".join(reversed(record[4].split(','))) for record in records))
    
    period_count = {}
    period_titles = {}
    
    for record in records:
        period = record[3]
        title = record[0]
        
        if period in period_count:
            period_count[period] += 1
        else:
            period_count[period] = 1
        
        if period in period_titles:
            period_titles[period].append(title)
        else:
            period_titles[period] = [title]
    
    for period in period_titles:
        period_titles[period].sort()
    
    return composers, period_count, period_titles

# Faz print aos resultados
def print_results(composers, period_count, period_titles):
    print("\nLista ordenada dos compositores:")
    for composer in composers:
        print(composer)
    
    print("\nDistribuição das obras por período:")
    for period, count in period_count.items():
        print(f"{period}: {count}")
    
    print("\nObras por período:")
    for period, titles in period_titles.items():
        print(f"{period}:")
        for title in titles:
            print(f"  - {title}")


## "Main"
with open("TPC2/obras.csv", "r", encoding="utf-8") as f:
    text = f.read()

headers, records = parse_music_data(text)
write_csv("TPC2/music_data.csv", headers, records)
print("CSV file generated successfully!")

composers, period_count, period_titles = process_music_data(records)
print_results(composers, period_count, period_titles)
