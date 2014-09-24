stylize
=======

Regressor based image stylization.

Inspired by the [various](http://alteredqualia.com/visualization/evolve/) [projects](http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/) implementing polygonal stylization of images via blends of genetic algorithms and hill climbing and [Andrej Karpathy's](http://cs.stanford.edu/people/karpathy/convnetjs/demo/image_regression.html) rephrasing of the problem in a machine learning framework.

Whereas genetic algorithm and hill climbing approaches can take hours, stylize runs in seconds with much greater flexibility and higher fidelity when desired.

Usage (example.py has more detail): 
```
from stylize import render
from scipy.misc import imread

image = imread('resources/iggy_small.jpg')
defaults = render(image)
```

Our Test Subject, my cat Iggy  | Default stylization `render(image)`
------------- | -------------
![Iggy](/resources/iggy_small.jpg?raw=true "Iggy looking confused")  | ![Iggy](/resources/defaults_small.png?raw=true "Default stylization with stylize")

Abstract `render(image,depth=4)` | Smooth `render(image,iterations=25)`
------------- | -------------
![Iggy](/example_images/abstract.png?raw=true "Abstract Iggy")  | ![Iggy](/example_images/smoother.png?raw=true "Smooth Iggy")

More Detail `render(image,ratio=0.00005)` | Less Detail `render(image,ratio=0.001)`
------------- | -------------
![Iggy](/example_images/more_detail.png?raw=true "Iggy in all his glory")  | ![Iggy](/example_images/less_detail.png?raw=true "Iggy in low fidelity")

Visualizing how it works | Why
------------- | -------------
![Iggy](/resources/iggy.gif?raw=true "Visualizing how it works")  | stylize is currently based off of regression trees and an ensembled version of that model, the random forest regressor. Regression trees work by recursively partitoning ("splitting") their input feature space and assigning associations to those partitions (such as colors). At each frame the model splits every partition in half again until hitting its minimum partition size, click the gif to see a larger version!

