# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

# Get input of height and width
dimensions = input().split(' ')

height = int(dimensions[0])
width = int(dimensions[1])

# Validate values for height and width proportions
if height % 2 == 0:
    print("Height must be an odd number")
    
if width != (height * 3):
    print("Width must be 3 times the height")
    
# Generate top of the mat
design = ".|."
half_height = int((height - 1) / 2)
design_instance = 1

for line in range(half_height):
    design_width = design_instance * 3
    padding = int((width - design_width) / 2)
    
    print(( "-" * padding ) + (design * design_instance) + ( "-" * padding ))
    
    design_instance += 2

# generate center "WELCOME" line
welcome_padding = int((width - 7) / 2)
print(( "-" * welcome_padding ) + "WELCOME" + ( "-" * welcome_padding ))

# Generate bottom of the mat
design_instance -= 2

for line in range(half_height):
    design_width = design_instance * 3
    padding = int((width - design_width) / 2)
    
    print(( "-" * padding ) + (design * design_instance) + ( "-" * padding ))
    
    design_instance -= 2
