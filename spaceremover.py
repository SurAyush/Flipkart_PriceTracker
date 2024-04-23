#simple python program to remove multiple inbetween spaces from string
#this removes unwanted large white spaces from scraped product name
def clean(s):
    words = s.split()
    return ' '.join(words)

