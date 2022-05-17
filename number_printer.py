"""
Digits and prefix dictionaries store english words for digits and prefixes (e.g. two, twen-(ty) both represented by integer 2)
"""

digits = {'0': ' ', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
prefix = {'2':'twen', '3':'thir', '4':'for', '5':'fif', '6':'six', '7':'seven', '8':'eigh', '9':'nine'}

def quad(num):
    """
    Computes quadrillions (1-999 quadrillion)
    """
    if num[-15:] == '000000000000000':
        return hund(num[:-15]) + 'quadrillion'
    elif num[-15:-2] == '0000000000000':
        return hund(num[:len(num)-15]) + 'quadrillion ' + 'and ' + hund(num[-2:])
    else:
        return hund(num[:len(num)-15]) + 'quadrillion ' + trill(num[-15:])

def trill(num):
    """
    Computes trillions (1-999 trillion)
    """
    if num[-12:] == '000000000000':
        return hund(num[:-12]) + 'trillion'
    elif num[-12:-2] == '0000000000':
        return hund(num[:len(num)-12]) + 'trillion ' + 'and ' + hund(num[-2:])
    elif num[:3] == '000':
        return bill(num[-12:]) 
    else:
        return hund(num[:len(num)-12]) + 'trillion ' + bill(num[-12:])

def bill(num):
    """
    Computes billions (1-999 billion)
    """
    if num[-9:] == '000000000':
        return hund(num[:-9]) + 'billion'
    elif num[-9:-2] == '0000000':
        return hund(num[:len(num)-9]) + 'billion ' + 'and ' + hund(num[-2:])
    elif num[:3] == '000':
        return mill(num[-9:]) 
    else:
        return hund(num[:len(num)-9]) + 'billion ' + mill(num[-9:])

def mill(num):
    """
    Computes millions (1-999 million)
    """
    if num[-6:] == '000000':
        return hund(num[:-6]) + 'million'
    elif num[-6:-2] == '0000':
        return hund(num[:len(num)-6]) + 'million ' + 'and ' + hund(num[-2:])
    elif num[:3] == '000':
        return thous(num[-6:]) 
    else:
        return hund(num[:len(num)-6]) + 'million ' + thous(num[-6:])

def thous(num):
    """
    Computes thousands (1-999 thousand)
    """
    if num[-3:] == '000':
        return hund(num[:-3]) + 'thousand'
    elif num[-3] == '0':
        return hund(num[:len(num)-3]) + 'thousand ' + 'and ' + hund(num[-3:])
    elif num[:3] == '000':
        return hund(num[-3:])
    else:
        return hund(num[:len(num)-3]) + 'thousand ' + hund(num[-3:])

def hund(num):
    """
    Computes any three digit number. If two-digit, pass to tens() function
    """
    if len(num) < 3:
        return tens(num)
    if num[0] == '0':
        return tens(num[1:])
    if num[1:] == '00':
        return digits[num[0]] + ' hundred '
    return digits[num[0]] + ' hundred' + ' and ' + tens(num[1:])

def tens(num):
    """
    Computes any two-digit number (0-999)
    """
    if num == '0' or num == '':
        return 'zero'
    if len(num) == 1:
        return digits[num] + ' '
    if len(num) == 2:
        if num[0] == '0':
            return digits[num[1]] + ' '
        elif num == '10':
            return 'ten '
        elif num == '11':
            return 'eleven '
        elif num == '12':
            return 'twelve '
        elif num == '14':
            return 'fourteen '
        elif num[0] == '1':
            return prefix[num[1]] + 'teen '
        elif num[1] == '0':
            return prefix[num[0]] + 'ty '
        else:
            return prefix[num[0]] + 'ty ' + digits[num[1]] + ' '


def run(num):
    """
    Prints number in range (0 - 999,999,999,999,999,999) to output in English
    """

    if len(num) < 4:
        print(hund(num))
    elif len(num) > 3 and len(num) <= 6: #thousands
        print(thous(num))
    elif len(num) > 6 and len(num) <= 9: #millions
        print(mill(num))
    elif len(num) > 9 and len(num) <= 12: #billions
        print(bill(num))
    elif len(num) > 12 and len(num) <= 15: #trillions
        print(trill(num))
    elif len(num) > 15 and len(num) <= 18: #trillions
        print(quad(num))
    else:
        print('\nMaximum size is 1x10^18 - 1 (quintillions are not supported)')


def main():
    while True:
        x = input("\nEnter a number:\n")
        if x.isnumeric():
            x = x.lstrip('0')
            try:
                run(x)
            except:
                print('An error occured. Please try again.')
        else:
            print("\nPlease enter an integer between 0 and 1x10^18 - 1\n")
            continue
main()