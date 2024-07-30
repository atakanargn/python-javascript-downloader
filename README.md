# Script Downloader

This script downloads all JavaScript files linked in an HTML file.

## Requirements

- Python 3.x
- requests
- beautifulsoup4

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/atakanargn/python-javascript-downloader.git
    cd python-javascript-downloader
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have an HTML file (e.g., `example.html`) with script tags you want to download.
2. Run the script:
    ```bash
    python download_script_files.py example.html
    ```
   This will download all JavaScript files to a folder named `downloaded_scripts`.

## Example

```html
<!-- example.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
</body>
</html>
```

Running the script with this example.html will download jquery-3.6.0.min.js and popper.min.js into the downloaded_scripts directory.