def get_company(email):
    
    try:
        return (email.split('@')[1].split('.com')[0])

    except:
        return 'Invalid email address'

if __name__ == '__main__':

    email_id = input("Enter email address: ")

    print(get_company(email_id))