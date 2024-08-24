def create_pattern(i: int=5):
    
    num_of_stars = (2*i)-1
    star_counter = num_of_stars
    for j in range(1, i+1):
        stars = '*'*star_counter
        spaces = ' '*(int((num_of_stars-star_counter)/2))
        star_counter -= 2        
        print(f'{spaces}{stars}{spaces}')

create_pattern(10)
