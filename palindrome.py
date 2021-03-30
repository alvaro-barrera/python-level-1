def palindrome(word):
    word = word.lower()
    word = word.replace(' ', '')

    word_inverted = word[::-1]
    if word == word_inverted:
        return True
    else:
        return False


def run():
    word = str(input('Escribe una palabra: '))
    is_palindrome = palindrome(word)

    if is_palindrome == True:
        resp = 'Es palíndromo'
    else:
        resp = 'NO es palíndromo'
    print(resp)


if __name__ == '__main__':
    run()
