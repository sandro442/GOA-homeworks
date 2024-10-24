n=10
for i in range (1, n + 1):
    stars= '*'*i
    spaces = ' ' * (2*(n-i))
    print(stars+spaces+stars)