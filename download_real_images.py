
# download_real_images.py
# Usage: put your PEXELS_API_KEY or UNSPLASH_ACCESS_KEY below and run.
import os, requests, csv, shutil, sys

# Choose provider: 'pexels' or 'unsplash'
PROVIDER = 'pexels'
PEXELS_API_KEY = '<REPLACE_WITH_YOUR_PEXELS_API_KEY>'
UNSPLASH_ACCESS_KEY = '<REPLACE_WITH_YOUR_UNSPLASH_ACCESS_KEY>'

OUT_ASSETS = 'assets'
PRODUCTS_CSV = 'products.csv'

def download_from_pexels(query, dest_path):
    url = 'https://api.pexels.com/v1/search'
    headers = {'Authorization': PEXELS_API_KEY}
    params = {'query': query, 'per_page':1}
    r = requests.get(url, headers=headers, params=params, timeout=20)
    if r.status_code == 200:
        data = r.json()
        photos = data.get('photos') or []
        if photos:
            img_url = photos[0]['src']['large2x']
            r2 = requests.get(img_url, stream=True, timeout=30)
            if r2.status_code == 200:
                with open(dest_path, 'wb') as f:
                    for chunk in r2.iter_content(1024):
                        f.write(chunk)
                return True
    return False

def download_from_unsplash(query, dest_path):
    url = 'https://api.unsplash.com/search/photos'
    params = {'query':query, 'per_page':1, 'orientation':'landscape'}
    headers = {'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'}
    r = requests.get(url, headers=headers, params=params, timeout=20)
    if r.status_code == 200:
        data = r.json()
        results = data.get('results') or []
        if results:
            img_url = results[0]['urls']['full']
            r2 = requests.get(img_url, stream=True, timeout=30)
            if r2.status_code == 200:
                with open(dest_path, 'wb') as f:
                    for chunk in r2.iter_content(1024):
                        f.write(chunk)
                return True
    return False

def main():
    if not os.path.exists(OUT_ASSETS):
        os.makedirs(OUT_ASSETS)
    with open(PRODUCTS_CSV, newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_name = row['image']
            title = row['title']
            dest = os.path.join(OUT_ASSETS, image_name)
            print(f'Downloading for: {title} -> {image_name}')
            success = False
            if PROVIDER == 'pexels' and '<REPLACE_WITH_YOUR_PEXELS_API_KEY>' not in PEXELS_API_KEY:
                success = download_from_pexels(title + ' product lifestyle')
            if PROVIDER == 'unsplash' and '<REPLACE_WITH_YOUR_UNSPLASH_ACCESS_KEY>' not in UNSPLASH_ACCESS_KEY:
                success = download_from_unsplash(title + ' product lifestyle', dest)
            if not success:
                print(' -> Failed to download, keeping placeholder.')

if __name__ == '__main__':
    main()
