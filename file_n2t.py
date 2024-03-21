import os
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
def file_read(file_name,o_n):
    os.remove(o_n)
    with open(file_name, 'r') as f:
        num_list = [int(num) for num in f.read().split(',')]
    return num_list

def write_file(output_filename, num_print):
    with open(output_filename, "a") as text_file:
        for items in num_print:
            text_file.write(items + '\n')
#main function
file_name = input('Enter file name: ')
o_n = 'num_outpts.txt'
numbers = file_read(file_name,o_n)
num_print=[]
for n in numbers:
    num_print.append(number_to_words(n))
write_file(o_n, num_print)
#print([num for num in num_print])