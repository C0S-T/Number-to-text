def number_to_words(number):
    # Define dictionaries for mapping
    ones = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    teens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    if number < 10:
        print(ones[number])
    elif number < 20:
        print(teens[number])
    elif number < 100:
        print(f'{tens[number // 10]} {ones[number%10]}')

num = int(input('Enter a number : '))
number_to_words(num)
