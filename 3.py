dNumber = int(input())
data = [input() for _ in range(dNumber)]
search_dNumber = int(input())
search_data = [input() for _ in range(search_dNumber)]
for data_item in data:
    couneterInd = 0
    for search_data_item in search_data:
        couneterInd = data_item.find(search_data_item)
        if couneterInd == -1:
            break
    if couneterInd != -1:
        print(data_item)
