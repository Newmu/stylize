stylize
=======

Regressor based image stylization.

Inspired by the [various](http://alteredqualia.com/visualization/evolve/) [projects](http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/) implementing polygonal stylization of images via blends of genetic algorithms and hill climbing and [Andrej Karpathy's](http://cs.stanford.edu/people/karpathy/convnetjs/demo/image_regression.html) rephrasing of the problem in a machine learning framework.

Usage (example.py had more detail - see results on iggy in example_images/): 
```
from stylize import render
from scipy.misc import imread

img = imread('resources/iggy.jpg')
defaults = render(img)
```

## Our Test Subject
![Iggy](/resources/iggy_small.jpg?raw=true "My cat Iggy looking confused")
## Default stylization with stylize
![Iggy](/resources/iggy_defaults.png?raw=true "Default stylization with stylize")
## Visualizing how it works
![Iggy](/resources/iggy.gif?raw=true "Visualizing how it works")
