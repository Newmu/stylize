import numpy as np
from skimage.transform import resize,rescale
from sklearn.ensemble import RandomForestRegressor as RFR
from skimage.color import rgb2lab,lab2rgb
from scipy.spatial.distance import cdist

from time import time
from itertools import product

def coordinate_features(coordinates,n=4):
	x,y = coordinates[:,0],coordinates[:,1]
	features = coordinates
	m = 1
	for _ in range(n):
		features = np.hstack((features,np.column_stack((m*x+y,m*x-y,x+m*y,x-m*y))))
		m *= 2
	return features

def gen_x(w,h,landmarks=None):
	xx,yy = np.meshgrid(np.arange(w),np.arange(h))
	coordinates = np.column_stack((xx.reshape(-1,1),yy.reshape(-1,1)))
	scaled_coordinates = coordinates/np.asarray([[w,h]],dtype=float)

	if landmarks is None:
		features = coordinate_features(scaled_coordinates)	
	else:
		features = cdist(scaled_coordinates,landmarks)

	return np.hstack((coordinates,features))

def gen_xy(img,landmarks=None):
	w,h = img.shape[:2]
	X = gen_x(w,h,landmarks)
	x = X[:,0].astype(int)
	y = X[:,1].astype(int)
	Y = img[x,y]
	return X,Y

def pred_to_img(pred,X,w,h):
	pred_img = np.zeros((w,h,3))
	x = X[:,0].astype(int)
	y = X[:,1].astype(int)
	pred_img[x,y] = pred
	return pred_img

def pixel_scale(img,npxs):
	w,h = img.shape[:2]
	x = np.sqrt(npxs/(w*h*3.))
	img = resize(img,(int(round(w*x)),int(round(h*x))))
	return img

def render(img,
		   features='coordinates',
		   ratio=0.00025,
		   iterations=1,
		   lab=True,
		   depth=None,
		   npxs=5e5,
		   anti_aliasing=False,
		   verbose=False):
	"""
	Features decides the inputs for the model, current options are 'coordinates' for coordinate based features
	and 'landmarks' for distance to landmarks features. Render time and memory usage is about 2x using landmarks features.
	Default is 'coordinates'.

	ratio corresponds to the ratio of the size of the smallest details the model is allowed to use compared to the whole image.
	Default is 0.001, 1 would correspond to not fitting to anything while 0 would fit down to individual pixels.

	iterations is how many randomized runs of the base model to use for averaging in the final prediction.
	1 is default is corresponds to sharp boundaries. 10-100 would result in a much smoother more painterly result.
	Render time and memory usage increases linearly with number of iterations.

	lab decides whether to fit the model in lab color space instead of rgb color space. 
	Default is True.

	depth decides how many levels of splits the regressor is allowed to have.
	Default is None which corresponds to as many as needed.

	np decides how many pixels to resize the source image to internally for fitting.
	Default is 500,000. 

	anti_aliasing decides whether or not to use 2x grid super sampling.
	Default is False. Render time and memory usage will be increased over 2x.

	verbose controls whether to print info about a render
	Default is False.
	"""
	t = time()

	w,h = img.shape[:2]

	wrender,hrender = w,h
	if anti_aliasing:
		wrender,hrender = w*2,h*2

	img_o = pixel_scale(img,npxs)
	wfit,hfit = img_o.shape[:2]

	if lab:
		img = rgb2lab(img_o)

	if features == 'landmarks':
		locations = list(np.linspace(0,1,7))
		landmarks = list(product(locations,locations))
	else:
		landmarks = None

	X,Y = gen_xy(img,landmarks)
	xrender = gen_x(wrender,hrender,landmarks)

	min_samples = int(round(ratio*len(X)))
	model = RFR(n_estimators=iterations,n_jobs=-1,max_depth=depth,random_state=42,min_samples_leaf=min_samples)
	model.fit(X[:,2:],Y)

	pred = model.predict(xrender[:,2:])
	pred_img = pred_to_img(pred,xrender,wrender,hrender)

	if lab:
		pred_img = lab2rgb(pred_img)

	error = np.mean(np.square(resize(pred_img,(wfit,hfit))-img_o))*255.

	if anti_aliasing:
		pred_img = resize(pred_img,(w,h))

	if verbose:
		s =  "%08.3f seconds to render\n"%(time()-t)
		s += "%08.3f error (0-255 scaled)\n"%(error)
		s += "%08.3f min pixels considered\n"%(min_samples)
		print s

	return pred_img