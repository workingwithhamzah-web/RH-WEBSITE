from PIL import Image

img = Image.open('assets/beyond_borders_logo.png').convert('RGBA')
data = img.getdata()

new_data = []
for item in data:
    r, g, b, a = item
    # If the pixel is dark (e.g., background), make it fully transparent
    # If the background is dark gray, say brightness < 50
    avg = (r + g + b) / 3
    if avg < 50:
        new_data.append((255, 255, 255, 0)) # transparent
    else:
        # For the text, we want to keep anti-aliasing.
        # Let's map brightness [50, 255] -> alpha [0, 255]
        # and force color to white
        alpha = int((avg - 50) / (255 - 50) * 255)
        new_data.append((255, 255, 255, alpha))

img.putdata(new_data)
img.save('assets/beyond_borders_logo.png')
print("Image fixed!")
