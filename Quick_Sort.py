def quick_sorting(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot = data_list[0]
        lesser = [x for x in data_list[1:] if x<=pivot]
        greater = [x for x in data_list[1:] if x>=pivot]
        result = quick_sorting(lesser)+[pivot]+quick_sorting(greater)
        return result
qs = quick_sorting([44,26,23,89,54,67,39,10])
print(qs)

#[10, 23, 26, 39, 44, 54, 67, 89]