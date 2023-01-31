# https://www.youtube.com/watch?v=UEuXQjPUwcw&ab_channel=TechWithTim

# Lokal variabel - variabel som skapas i en funktion. Kan bara användas i den funktionen. Defined in the scope of a function.
# Global variabel - Defined in the scope of the file.

# Function - Should do one thing and do it very well
# Using global variables in a function makes it harder to search for errors and harder to use the function in another program

def add_7(x):
    return x + 7
    
result = 18

result = add_7(result)
print(result)