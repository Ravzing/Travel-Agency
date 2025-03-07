from PIL import Image

image = Image.open("alex-azabache-8L7mOETNgHA-unsplash.jpg")

new_size = (720, 1280)
resized_image = image.resize(new_size)

resized_image.save("itza.jpg")