"""Font installation utilities for Google Colab."""

import os
import subprocess
import matplotlib.font_manager as fm


def setup_fonts(force_reinstall=False):
    """
    Install and setup Open Sans fonts for matplotlib/plotnine.
    
    Parameters
    ----------
    force_reinstall : bool, default False
        If True, removes existing opensans directory and reinstalls
        
    Returns
    -------
    bool
        True if fonts were successfully installed
    """
    opensans_dir = 'opensans'
    fonts_dir = '/tmp/fonts'
    
    # Clone Open Sans repository if needed
    if force_reinstall and os.path.exists(opensans_dir):
        subprocess.run(['rm', '-rf', opensans_dir], check=True)
    
    if not os.path.exists(opensans_dir):
        print("Cloning Open Sans font repository...")
        subprocess.run(
            ['git', 'clone', 'https://github.com/googlefonts/opensans.git'],
            check=True
        )
    
    # Prepare font directory
    subprocess.run(['rm', '-rf', fonts_dir], check=False)
    subprocess.run(['mkdir', fonts_dir], check=True)
    
    # Copy fonts
    font_files = [
        'opensans/fonts/ttf/OpenSans-Regular.ttf',
        'opensans/fonts/ttf/OpenSans-Bold.ttf',
        'opensans/fonts/ttf/OpenSans-Italic.ttf',
        'opensans/fonts/ttf/OpenSans-BoldItalic.ttf',
    ]
    
    for font_file in font_files:
        if os.path.exists(font_file):
            subprocess.run(['cp', font_file, fonts_dir], check=True)
    
    # Update font cache
    print("Updating font cache...")
    subprocess.run(['fc-cache', '-f', '-v'], check=True)
    
    # Load fonts into matplotlib
    for font_file in os.listdir(fonts_dir):
        font_path = os.path.join(fonts_dir, font_file)
        fm.fontManager.addfont(font_path)
    
    # Verify installation
    font_path = fm.findfont('Open Sans')
    print(f"Open Sans font installed at: {font_path}")
    
    return True
