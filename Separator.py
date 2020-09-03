# Email list separator based on domains
# Input how you want to retrieve the emails
# Input the separator used in your mail list
# That's all :D
# Coded with love by Ali Baig <3

import urllib.error
import urllib.parse
import urllib.request
separated_emails = dict()

# Function to get emails as a string


def email_clipboard():
    input_clipboard = input('Paste the email list below: ').split(separator)
    return raw_result(input_clipboard)

# Function to get emails from a .txt file


def email_txt():
    input_file = input('Enter filename: ')
    try:
        file_open = open(input_file)
    except FileNotFoundError:
        print('File not found!')
        exit(0)
    for each_email in file_open:
        list_email = each_email.split(separator)
    return raw_result(list_email)

# Function to get emails from a url


def email_url():
    url_txt = input('Enter url: ')
    try:
        url_open = urllib.request.urlopen(url_txt)
    except ValueError:
        print('Not a valid url.')
        exit(0)
    except:
        print('Something went wrong.')
        exit(0)
    count = 0
    for line in url_open:
        count += 1
        return raw_result(line.decode().split(separator))

# Function to make a dictionary containing email separated on the behalf of domains


def raw_result(input_list):
    for emails in range(len(input_list)):
        input_list[emails] = input_list[emails].lstrip()
        domain_name = input_list[emails].find('@')
        if not input_list[emails][domain_name + 1:] in separated_emails:
            separated_emails[input_list[emails][domain_name + 1:]] = list()
        separated_emails[input_list[emails][domain_name + 1:]].append(input_list[emails])
    return separated_emails

# Function to print result on command line and store it in .txt file


def export_result_txt(sep_emails):
    for do, em in sep_emails.items():
        print(f'\n<==[[ {do} ]]==>\n')
        for e in em:
            print(e)
    export_data = input('Export to txt file? (y/n): ').lower()
    if export_data == 'y':
        result_txt = open('result.txt', 'w')
        for do, em in sep_emails.items():
            result_txt.write(f'\n<==[[ {do} ]]==>\n')
            for e in em:
                result_txt.write(f'{e}\n')
        result_txt.close()
        print('Done!')
    else:
        print('The program will exit now!')
        exit(0)


# Introduction screen nothing much here
print('*' * 51)
print('*', ' ' * 14, ' Email Separator', ' ' * 14, ' *')
print('*' * 51, end='')
try:
    choice = int(input(f'''
*   1. Enter emails via clipboard {' ' * 15} *
*   2. Enter emails via txt file {' ' * 16} *
*   3. Enter emails via txt file on a website {' ' * 3} *
{'*' * 51}
    
Enter your choice: '''))

    separator = input('Enter separator: ')

    if choice == 1:
        export_result_txt(email_clipboard())

    elif choice == 2:
        export_result_txt(email_txt())

    elif choice == 3:
        export_result_txt(email_url())

    else:
        print('Not a valid choice!')
        exit(0)

except ValueError:
    print('Error! The valid choices are from 1 to 4.')
    exit(0)
