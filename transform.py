from PIL import Image
import base64
from io import BytesIO
import time


def half_pixel(path):
    start_time = time.perf_counter()  # Start the timer
    img = Image.open(path)
    print(img.size)
    [xs, ys] = img.size  # width * height

    # Examine every pixel in the image
    for x in range(xs):
        for y in range(ys):
            # Get the RGB color of the pixel
            r, g, b = img.getpixel((x, y))
            # Increase RGB values by 100, with a max value of 255
            r = min(r + 100, 255)
            g = min(g + 100, 255)
            b = min(b + 100, 255)
            # Put the new pixel value back in the image
            img.putpixel((x, y), (r, g, b))

    # Save the modified image to a bytes buffer
    buffer = BytesIO()
    img.save(buffer, format='JPEG')

    # Encode the contents of the buffer to a Base64 string
    img_base64 = base64.b64encode(buffer.getvalue()).decode()

    # You can now use the Base64 string to save it to a file or use it as needed

    end_time = time.perf_counter()  # End the timer
    execution_time = end_time - start_time  # Calculate execution time

    print(f"The function took {execution_time} seconds to run.")
    return img_base64

# Call the function and get the Base64 string
base64_string = half_pixel("rothko.jpg")
# print(base64_string)

# Optionally, save the Base64 string to a file
# with open('image_base64.txt', 'w') as f:
#     f.write(base64_string)
