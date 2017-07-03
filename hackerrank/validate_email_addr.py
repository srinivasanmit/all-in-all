import re

def fun(s):
    # return True if s is a valid email, else return False
    #return filter(lambda x : re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", x), s)
    #return re.match(r'[a-zA-z0-9_-]+\@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', s)
    return True if re.match(r'^[a-zA-Z0-9_-]+\@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', s) else False

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
