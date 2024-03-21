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
    
    # Function to handle numbers from 1 to 999
    def num_to_words(n):
        if n == 0:
            return ''
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n]
        elif n < 100:
            return tens[n // 10] + (' ' + ones[n % 10] if n % 10 != 0 else '')
        else:
            return ones[n // 100] + ' hundred' + (' and ' + num_to_words(n % 100) if n % 100 != 0 else '')

    # Define scale words
    scales = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion']

    # Main function
    if number == 0:
        return 'zero'

    # Convert number to string to get its length
    number_str = str(number)
    length = len(number_str)

    # Break down the number into groups of three digits each
    groups = [(int(number_str[max(length - 3 * (i + 1), 0):length - 3 * i]), scales[i]) for i in range(length // 3 + (length % 3 > 0))][::-1]

    # Convert each group to words and append the scale word
    result = []
    for group, scale in groups:
        if group != 0:
            result.append(num_to_words(group))
            if scale:
                result.append(scale)

    return ' '.join(result)

# Get input from user
num = int(input("Enter a number: "))

# Convert and print the number in words
print("Output:", number_to_words(num))

                
                


