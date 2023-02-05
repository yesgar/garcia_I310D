#YG

def calculate_volume_of_sphere(radius):
    pi = 3.14159
    if (radius < 0):
        print("Radius can not be negative. Please provide value for radius")
    else:
        volume_of_sphere = 4/3 * pi * radius * radius * radius
        print(f"The volume of the sphere is {volume_of_sphere}")
    
calculate_volume_of_sphere(30)
calculate_volume_of_sphere(40)
