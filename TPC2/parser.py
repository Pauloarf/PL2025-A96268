def parseFile(filename):
    correctText = []
    correctLine = ""
    with open(filename, "r") as file:
        escape = False
        textCapture = False
        header = next(file)
        correctText.append(header)

        for line in file:
            for i, char in enumerate(line):
                if textCapture:
                    if char == ';':
                        continue
                    correctLine += char
                    if (char == '"'):
                        if escape:
                            escape = False
                        else:
                            if i + 1 < len(line) and line[i + 1] == '"':
                                escape = True
                            else:
                                textCapture = False
                    else:
                        escape = False
                else:
                    correctLine += char
                    if char == '"':
                        textCapture = True
            if not textCapture:
                correctText.append(correctLine)
                correctLine = ""
        if correctLine:
            correctText.append(correctLine)
    return correctText

def writeCSV(filename, correctText):
    with open(filename, "w+") as newCSV:
        for line in correctText:
            line = " ".join(line.split())
            newCSV.write(line);
            newCSV.write('\n')


def parseLines(text):
    allFields = []
    fields = []
    for line in text:
        fields = line.split(';')
        allFields.append(fields)
    return allFields

# Processa os records para retirar a informação pertendida
def processData(records):
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


text = parseFile("obras.csv")
#writeCSV("obrasNormalized.csv", text)
records = parseLines(text)
composers, period_count, period_titles = processData(records)
print_results(composers, period_count, period_titles)