import re


def email_extractor(words):
    print(re.findall('\w+@\w+\.\w{3}', words))


email_extractor(
    "fghgjk,judom@ymail.com,gndvbdhsdhvc csv,chibuzor_760@email.org, 3526_yyy@gmail.com, olammakalu007@gmail.com,dhgsxzfgszdgcxzdzfg")
