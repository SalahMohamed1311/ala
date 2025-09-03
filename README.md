
Online Market — Realistic Image Package (24 items)
=================================================

This package contains a ready prototype + 24 high-resolution lifestyle-style placeholder images.
If you want *real photographs* (Unsplash/Pexels), see the "download_real_images.py" script included below.
You can run it locally to fetch real images and replace placeholders automatically.

Files:
- index.html
- styles.css
- script.js
- assets/ (product-1.jpg ... product-24.jpg, hero.jpg)
- products.csv (24 product rows)
- download_real_images.py (script to download images from Unsplash or Pexels)
- README.txt (this file)

How to view prototype:
1. Unzip the package.
2. Open index.html in your browser.

To download real images (optional):
- Get an API key from Pexels (https://www.pexels.com/api/) or Unsplash (https://unsplash.com/developers).
- Edit 'download_real_images.py' to insert your API key and desired queries.
- Run: python download_real_images.py
- The script will replace files in the 'assets/' folder with downloaded images matching the products.csv queries.
