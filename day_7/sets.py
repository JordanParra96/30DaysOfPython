# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Length of it_companies:', len(it_companies))
it_companies.add('Twitter')
print('After adding Twitter:', it_companies)
it_companies.update(['LinkedIn', 'Snapchat', 'Pinterest'])
print('After updating with LinkedIn, Snapchat, Pinterest:', it_companies)
it_companies.remove('IBM')
print('After removing IBM:', it_companies)
it_companies.discard('IBM')

A_union_B = A.union(B)
print('A union B:', A_union_B)
A_intersection_B = A.intersection(B)
print('A intersection B:', A_intersection_B)
print('Is A subset of B?:', A.issubset(B))
print('Are A and B disjoint?:', A.isdisjoint(B))
A_sym_diff_B = A.symmetric_difference(B)
print('A symmetric difference B:', A_sym_diff_B)
del A
del B

age_set = set(age)
print('Age set:', age_set)

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print('Unique words in the sentence:', unique_words)
