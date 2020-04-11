def modify(new_record):
    with open('record.txt', 'w') as f:
        for j in range(0, 10):
            f.write(str(new_record[j]))
            f.write('\n')

score = 1499
with open('record.txt', 'r+') as f:
    record_scores = f.readlines()
    
    record_score = int(record_scores[0])
    for i in range(0, 10):
        record_scores[i] = record_scores[i].strip("\n")

    for i in range(0, 10, 1):
        print(record_scores[i])
        if score >= int(record_scores[i]):
            for j in range(9, i-1, -1):
                record_scores[j] = record_scores[j-1]
            record_scores[i] = score
            modify(record_scores)
            break