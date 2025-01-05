# tuple
score_tuple = (2.45, 4.56, 4.00, 5.00)

score_list = [2.45, 4.56, 4.00, 5.00]

# tuple shi ar sheidzleba cvlilebis shetana is aris immutable monacemta tipi /data type
print(score_tuple)
print(score_list)



print('---------------------')

scores = (7, 9, 9, 8, 9)

print("count:",scores.count(9)) # 3 imitom rom 3 cali 9 aris 

print("length:",len(scores)) # 5 cali ragaca weria




print('-------------')


# zustad unda iyos imdeni elementi ramdenic aris mititebuli chvens tuple shi. tu ara errors gamoitans
birthday_date = (12, "August", 1993, "lomi", [1, 2, 3], "aeiou", "ya", "yo")
# -es aris rest----
day, month, year, lomi, ragac, rest = birthday_date

print(day)
print(month)
print(year)
print(lomi)
print(ragac)
print(rest) #an rac ginda is daarqvi 










fav_movies = ("se7en", "the notebook", "The batman", "" )
fav_movies = ("ragac1", "ragac2", "ragavc3", "ragac4", "ragac5","ragac6" )


first_movie,other_movies = fav_movies

print(first_movie)
print(other_movies)

print('---')

print(fav_movies[0])
print(fav_movies[5])









