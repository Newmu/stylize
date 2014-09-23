stylize
=======

Regressor based image stylization.

Inspired by the [various](http://alteredqualia.com/visualization/evolve/) [projects](http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/) implementing polygonal stylization of images via blends of genetic algorithms and hill climbing and [Andrej Karpathy's](http://cs.stanford.edu/people/karpathy/convnetjs/demo/image_regression.html) rephrasing of the problem in a machine learning framework.

Usage:
```
from stylize import render
from scipy.misc import imread

img = imread('resources/iggy.jpg')
stylized = render(img)
```


![Iggy](/resources/iggy.jpg?raw=true "My cat Iggy looking confused")
![Iggy](/example_images/defaults.png?raw=true "Default stylization with stylize")
![Iggy](/resources/iggy.gif?raw=true "Visualizing how it works")

example.py demos various capabalities of stylize and example_images contains those results run on Iggy.
