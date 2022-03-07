import math

can_sizes = [
        ["#1 Picnic", 6.83, 10.16],
        ["#1 Tall", 7.78, 11.91],
        ["#2", 8.73, 11.59],
        ["#2.5", 10.32, 11.91],
        ["#3 Cylinder", 10.79, 17.78],
        ["#5", 13.02, 14.29],
        ["#6Z", 5.4, 8.89],
        ["#8Z short", 6.83, 7.62],
        ["#10", 15.72, 17.78],
        ["#211", 6.83, 12.38],
        ["#300", 7.62, 11.27],
        ["#303", 8.1, 11.11]
    ]
# radius = float(dictionary['radius'])
# height = float(dictionary['height'])
def main():
    # radius = dictionary['radius']
    # height = dictionary['height']
    # storage_efficiency = compute_volume_area(radius, height) / compute_surface_area(radius, height)
    for name, radius, height in can_sizes:
    
        stor = compute_storage_efficiency(radius, height)
        print(f"{name} {stor:.1f}")

def compute_storage_efficiency(radius, height):
    volu = compute_volume_area(radius, height)
    surf = compute_surface_area(radius, height)
    stor_eff = volu / surf
    return stor_eff

def compute_volume_area(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area



main()