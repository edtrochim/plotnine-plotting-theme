"""Custom plotnine themes."""

from plotnine import *


def theme_lab_inspired():
    """
    Return a clean, minimal theme inspired by lab aesthetics.
    
    Features:
    - Clean white background
    - Subtle gray gridlines
    - Open Sans font family
    - Bold titles
    - Top legend position
    
    Returns
    -------
    plotnine.theme
        A plotnine theme object
        
    Examples
    --------
    >>> from plotnine import *
    >>> from colab_plotting import theme_lab_inspired
    >>> 
    >>> (ggplot(mtcars, aes('wt', 'mpg')) +
    ...  geom_point() +
    ...  theme_lab_inspired())
    """
    base_theme = theme_minimal(base_size=12, base_family="Open Sans")
    
    return base_theme + theme(
        plot_background=element_blank(),
        panel_background=element_blank(),
        panel_border=element_blank(),
        panel_grid_major_x=element_blank(),
        panel_grid_major_y=element_line(size=0.5, color="#cbcbcb"),
        panel_grid_minor=element_blank(),
        axis_ticks=element_blank(),
        axis_line=element_blank(),
        plot_title=element_text(size=14, face="bold", color="#757575", hjust=0.5),
        axis_title=element_text(colour="#757575"),
        legend_position="top",
        legend_background=element_blank(),
        legend_key=element_blank(),
        legend_title=element_text(size=10, colour="#757575"),
        legend_text=element_text(size=8, colour="#757575"),
        strip_background=element_rect(fill="none", colour=None),
        strip_text=element_text(size=12, face="bold", colour="#757575", hjust=0)
    )
