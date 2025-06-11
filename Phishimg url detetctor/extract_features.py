import re
from urllib.parse import urlparse

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_https'] = int(url.startswith('https'))
    features['has_ip'] = int(bool(re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url)))
    features['has_at_symbol'] = int('@' in url)
    features['has_dash'] = int('-' in url)
    
    parsed = urlparse(url)
    features['num_subdomains'] = len(parsed.netloc.split('.')) - 2
    
    return features