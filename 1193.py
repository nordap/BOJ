i = int(input())

n = 1
end_point = 0

while (True):
    end_point += n
    
    if end_point >= i:
        end_point -= n
        break
    n += 1


numer = i - end_point
denumer = n - numer + 1

if n%2 == 1:
    numer, denumer = denumer, numer

print (str(numer) + '/' + str(denumer))
