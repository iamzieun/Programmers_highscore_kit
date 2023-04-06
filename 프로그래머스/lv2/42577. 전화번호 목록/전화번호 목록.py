def solution(phone_book):
    # 1. Hash map 생성
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾기
    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            # 3. 자기 자신 제외
            if prefix in hash_map and prefix != phone_number:
                return False
    return True