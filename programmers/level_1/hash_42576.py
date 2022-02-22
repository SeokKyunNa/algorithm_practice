# participant : ["mislav", "stanko", "mislav", "ana"]	
# completion : ["stanko", "ana", "mislav"]	
# return : "mislav"
from collections import defaultdict, Counter

def solution(participant, completion):

    temp_dict = defaultdict(int)
    answer = ''

    temp_dict = Counter(participant)
    
    for name in completion:
        if name in temp_dict:
            temp_dict[name] -= 1
        else:
            answer = temp_dict[name]

    if answer == '':
        answer = temp_dict.most_common(1)[0][0]

    return answer