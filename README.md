# plotnine-plotting-theme
Custom plotting theme for Google Colab using plotnine with Open Sans fonts

## Installation

Install directly from GitHub in your Colab notebook:
```python
!pip install git+https://github.com/edtrochim/plotnine-plotting-theme.git

# 1. Setup fonts (run once per session)
from colab_plotting import setup_fonts
setup_fonts()

# 2. Use the theme
from plotnine import *
from colab_plotting import theme_lab_inspired

# Create your plot
(ggplot(mtcars, aes('wt', 'mpg', color='factor(cyl)')) +
 geom_point(size=3) +
 labs(title='MPG vs Weight by Cylinders',
      x='Weight (1000 lbs)',
      y='Miles per Gallon') +
 theme_lab_inspired())
