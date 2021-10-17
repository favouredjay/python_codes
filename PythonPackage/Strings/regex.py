import re

pattern = '001125'
print('Match' if re.fullmatch(pattern, '001125') else 'no match')
print('Match' if re.fullmatch(pattern, '012345') else 'no match')
print('Valid' if re.fullmatch(r'\d{5}', '81234') else 'inValid')
print('valid' if re.fullmatch('[A-Z][a-z]+', 'Joy') else 'invalid')
print('valid' if re.fullmatch('[A-Z][a-z]+', 'joy') else 'invalid')
print('valid' if re.fullmatch('[^a-z]+', '.') else 'invalid')
print("the result is" + "  " + ('valid' if re.fullmatch('[^0-9]+', '.') else 'invalid'))
print('valid' if re.fullmatch('[*$.]+', '.') else 'invalid')
print('match' if re.fullmatch('labell?ed', 'labelled') else 'no match')
print('match' if re.fullmatch(r'\d{3,}', '12345656765') else 'no match')
print('match' if re.fullmatch(r'\d{3,6}', '1234') else 'no match')
print('match' if re.fullmatch(r'\d{3,6}', '1234567') else 'no match')
print (re.sub(r'\t', ',', '1\t2\t3\t4\t5', count=1))


result = re.search('fun', 'python is fun!')
print(result.group()if result else "wrong")
result3 = re.search('FUN', 'python is fun!', flags=re.IGNORECASE)
print(result3.group()if result3 else "not found")


result1 = re.search('^girl', 'Joy is a good girl', flags=re.IGNORECASE)
print(result1.group()if result1 else "wrong")


