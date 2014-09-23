import sys
import os
from matplotlib import pyplot as plt
from scipy.misc import imread,imsave

from stylize import render

def show_img(img,title):
	plt.clf()
	plt.imshow(img)
	plt.xticks([])
	plt.yticks([])
	plt.title(title)
	plt.show()

if __name__ == "__main__":
	try:
		path = sys.argv[1]
	except:
		path = 'resources/iggy.jpg'

	print "Going to go through a few examples using the stylize.render"

	# Load an image into a numpy format and see it
	img = imread(path)
	plt.imshow(img)
	plt.xticks([])
	plt.yticks([])
	plt.title("Our source image, close to continue")
	plt.show()

	print "Please wait, rendering..."
	defaults = render(img,verbose=True)
	show_img(defaults,"Default stylization - polygonal")

	print "Please wait, rendering..."
	landmarks = render(img,features='landmarks',verbose=True)
	show_img(landmarks,"Landmark features for curved stylization")

	print "Please wait, rendering..."
	abstract = render(img,depth=4,verbose=True)
	show_img(abstract,"A depth of 4 results in an abstract representation")

	print "Please wait, rendering..."
	more_detail = render(img,ratio=0.00005,verbose=True)
	show_img(more_detail,"Ratio 0.00005 results greater detail")

	print "Please wait, rendering..."
	less_detail = render(img,ratio=0.001,verbose=True)
	show_img(less_detail,"Ratio 0.001 results in less detail")

	print "Please wait, rendering... this one's going to take a minute or so"
	smoother = render(img,iterations=25,verbose=True)
	show_img(smoother,"Averaging over 25 iterations to make it smoother")

	print "Please wait, rendering..."
	aa = render(img,anti_aliasing=True,verbose=True)
	show_img(aa,"Anti-aliasing to fight jaggies")
	
	print "Saved results are in the examples directory!"
	imsave('example_images/defaults.png',defaults)
	imsave('example_images/landmarks.png',landmarks)
	imsave('example_images/abstract.png',abstract)
	imsave('example_images/more_detail.png',more_detail)
	imsave('example_images/less_detail.png',less_detail)
	imsave('example_images/smoother.png',smoother)
	imsave('example_images/aa.png',aa)
