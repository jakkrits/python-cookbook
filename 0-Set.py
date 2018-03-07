# UNORDERED, NO DUPLICATES
# USEFUL TO CHECK INTERSECTION, DIFFERENCE

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print('Art' in art_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

