# phone_books = ["12","123","1235","567","88"]
# return false

def solution(phone_book):

    answer = True
    sorted_phone_book = sorted(phone_book)

    for i in range(1, len(sorted_phone_book)):
        if str(sorted_phone_book[i]).startswith(sorted_phone_book[i-1]):
            answer = False
    
    return answer


solution(["119", "97674223", "1195524421"])
