stylize
=======

Regressor based image stylization.

Inspired by the [various](http://alteredqualia.com/visualization/evolve/) [projects](http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/) implementing polygonal stylization of images via blends of genetic algorithms and hill climbing and [Andrej Karpathy's](http://cs.stanford.edu/people/karpathy/convnetjs/demo/image_regression.html) rephrasing of the problem in a machine learning framework.

stylize currently implements two feature types 
Usage (example.py has more detail - see results on Iggy in example_images/): 
```
from stylize import render
from scipy.misc import imread

img = imread('resources/iggy.jpg')
defaults = render(img)
```

Our Test Subject, my cat Iggy  | Default stylization `render(img)`
------------- | -------------
![Iggy](/resources/iggy_small.jpg?raw=true "Iggy looking confused")  | ![Iggy](/resources/defaults_small.png?raw=true "Default stylization with stylize")

Abstract `render(img,depth=4)` | Smooth `render(img,iterations=25)`
------------- | -------------
![Iggy](/example_images/abstract.png?raw=true "Abstract Iggy")  | ![Iggy](/example_images/smoother.png?raw=true "Smooth Iggy")

More Detail `render(img,ratio=0.00005)` | Less Detail `render(img,ratio=0.001)`
------------- | -------------
![Iggy](/example_images/more_detail.png?raw=true "Iggy in all his glory")  | ![Iggy](/example_images/less_detail.png?raw=true "Iggy in low fidelity")

Visualizing how it works | Why
------------- | -------------
![Iggy](/resources/iggy.gif?raw=true "Visualizing how it works")  | stylize is currently based off of regression trees and an ensembled generalization of that model, the random forest regressor. Regression trees work by recursively partitoning ("splitting") their input feature space and assigning associations to those partitions (such as colors).