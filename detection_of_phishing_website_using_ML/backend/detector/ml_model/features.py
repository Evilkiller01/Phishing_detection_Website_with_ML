def extract_features(url):
    return [
        1 if 'https' not in url else 0,
        len(url),
        1 if '@' in url else 0,
        1 if '//' in url[7:] else 0,
        url.count('.')
    ]