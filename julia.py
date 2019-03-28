from PIL import Image

# driver function


def julia(cX, cY):
	width, height, zoom = 640, 480, 1

	# creating the new image in RGB mode
	bitmap = Image.new("RGB", (width, height), "white")

	# Allocating the storage for the image and
	# loading the pixel data.
	pix = bitmap.load()

	# setting up the variables according to
	# the equation to  create the fractal
	moveX, moveY = 0.0, 0.0
	maxIter = 255

	for x in range(width):
			for y in range(height):
				zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
				zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
				i = maxIter
				while zx * zx + zy * zy < 4 and i > 1:
					tmp = zx * zx - zy * zy + cX
					zy, zx = 2.0 * zx * zy + cY, tmp
					i -= 1

				# convert byte to RGB (3 bytes), kinda
				# magic to get nice colors
				pix[x, y] = (i << 21) + (i << 10) + i * 8

	return bitmap


julia(-0.4, 0.6).save('julia.png', 'PNG')
