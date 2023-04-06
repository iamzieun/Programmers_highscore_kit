def solution(genres, plays):
    '''
    장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 리스트 만들기
    
    Args:
        genres: 노래의 장르를 나타내는 문자열 배열
        plays: 노래별 재생 횟수를 나타내는 정수 배열
    
    Returns:
        answer: 베스트 앨범에 들어갈 노래의 고유 번호 리스트
        
    '''
    answer = []
    
    genres_dict = dict.fromkeys(set(genres), 0)
    
    for g, p in zip(genres, plays):
        genres_dict[g] += p
    genres_list = [key for (key, value) in sorted(genres_dict.items(), key = lambda item: item[1], reverse=True)]
    #print("genres_dict :", genres_dict)
    #print("genres_list :", genres_list)

    plays_dict = {}
    for g in genres_list: 
        plays_dict[g] = []
    for idx, (g, p) in enumerate(zip(genres, plays)):
        plays_dict[g].append((idx, p))
    for key, val in plays_dict.items():
        plays_dict[key] = sorted(val, key = lambda item: (item[1], -item[0]), reverse=True)
    
    for key, val in plays_dict.items():
        answer.append(val[0][0])
        if len(val) >= 2:
            answer.append(val[1][0])
    #print("plays_dict :", plays_dict)
    #print("answer :", answer)
    return answer