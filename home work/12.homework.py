h = input("Введіть рядок для перетворення його в #: ")

nash = ''.join(i.capitalize() for i in h.split())
tag = ''.join(i for i in nash if i.isalnum())
hashtag = tag

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print('#', hashtag, sep='')
