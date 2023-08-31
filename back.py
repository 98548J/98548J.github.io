from PIL import Image, ImageDraw
import math

# Constants
WIDTH, HEIGHT = 500, 500
output_filename = "C:\\Users\\carls\\OneDrive\\Documents\\GitHub\\98548J.github.io\\assets\\CAD_Background.png"
# red = 52
# green = 103
# blue = 235

red = 75
green = 150
blue = 255


def ease_in_out(x):
    scaled_x = (x - 50) * math.pi / 100
    sine_value = math.sin(scaled_x)
    scaled_sine = sine_value * 127.5 + 127.5
    return int(scaled_sine)

def distance(x, y, x2, y2):
    v = int(math.sqrt((x-x2)**2+(y-y2)**2))
    if v > 100:
        v = 100
    return v

# Create a new image with RGBA mode (with transparency)
image = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Set pixel colors based on location
for x in range(100, 400):
    for y in range(100, 400):

        alpha = 255
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(0, 100):
    for y in range(100, 400):

        alpha = ease_in_out(x)
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(400, 500):
    for y in range(100, 400):

        alpha = ease_in_out(100-(x-400))
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(100, 400):
    for y in range(0, 100):

        alpha = ease_in_out(y)
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(100, 400):
    for y in range(400, 500):

        alpha = ease_in_out(100-(y-400))
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(0, 100):
    for y in range(0, 100):

        alpha = ease_in_out(100-distance(x, y, 100, 100))
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(400, 500):
    for y in range(0, 100):

        alpha = ease_in_out(100-distance(x, y, 400, 100))
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(0, 100):
    for y in range(400, 500):

        alpha = ease_in_out(100-distance(x, y, 100, 400))
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

for x in range(400, 500):
    for y in range(400, 500):

        alpha = ease_in_out(100-distance(x, y, 400, 400))
        color = (red, green, blue, alpha)
        draw.point((x, y), fill=color)

# Save the image
image.save(output_filename, "PNG")

print(f"Image saved as {output_filename}")