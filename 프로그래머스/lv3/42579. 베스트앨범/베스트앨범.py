def solution(genres, plays):
    '''
    장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 리스트 만들기
    
    Args:
        genres: 노래의 장르를 나타내는 문자열 배열
        plays: 노래별 재생 횟수를 나타내는 정수 배열
    
    Returns:
        answer: 베스트 앨범에 들어갈 노래의 고유 번호 리스트
        
    '''
    genres_dict = {}
    plays_dict = {}

    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in genres_dict.keys():
            genres_dict[g] = p
        else:
            genres_dict[g] += p

        if g not in plays_dict.keys():
            plays_dict[g] = [(idx, p)]
        else:
            plays_dict[g].append((idx, p))
    
    answer = []

    for genres, plays in sorted(genres_dict.items(), key = lambda item: item[1], reverse=True):
        plays_dict[genres] = sorted(plays_dict[genres], key = lambda item: (item[1], -item[0]), reverse=True)
        if len(plays_dict[genres]) > 1:
            answer += [plays_dict[genres][0][0], plays_dict[genres][1][0]]
        else:
            answer += [plays_dict[genres][0][0]]
    
    return answer