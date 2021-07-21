
def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

@decorator
def sports(input_text):
    print(input_text)



sports('Monster Ryu')