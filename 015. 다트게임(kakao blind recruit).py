def solution(dartResult):
    dart_target = {'S':1,'D':2,'T':3}
    special_target = ['*','#']
    score_arr = []
    arr = {} 
    
    for index, word in enumerate(dartResult):
        if word.isalpha() or word in special_target:
            arr[index] = word
    keys = arr.keys()
    
    prev_key_index = -1
    for word in keys:
        key = word
        value = arr[word]
        length = len(score_arr)
        
        if value in dart_target:
            score = int(dartResult[prev_key_index+1:key])**dart_target[value]
            score_arr.append(score)
        if value == '*':
            # 첫score 일때 처리    
            if length != 1:
                score_arr[length-2]*=2
            
            score_arr[length-1]*=2
            
        elif value == '#':
            score_arr[length-1]*=-1
        prev_key_index = key
    
    
    return sum(score_arr)

#TestData
#	['1S2D*3T','1D2S#10S','1D2S0T','1S*2T*3S','1D#2S*3S','1T2D3D#','1D2S3T*']
print(solution('1S2D*3T'))