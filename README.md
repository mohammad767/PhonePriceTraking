# Price Tracker — Python & BeautifulSoup

A small, modular **Price Tracker / Web Scraper** built with Python.

The project scrapes mobile product information from online stores, stores the collected data, and tracks price changes over time. It is also designed as a practical learning project for web scraping, Python project structure, JSON storage, testing, and Git/GitHub.

## Features

* Scrape mobile products from **Technolife**
* Scrape mobile products from **Digikala**
* Extract:

  * Product name
  * Current price
  * Product URL
  * Store source
* Clean and convert prices to integers
* Store product data in JSON
* Track previous and current prices
* Detect price increases and decreases
* Detect unchanged prices
* Handle common scraping and data errors
* Unit testing with `pytest`
* Modular project structure
* Git/GitHub-ready project

## Technologies

* Python
* `requests`
* `BeautifulSoup4`
* JSON
* `dataclasses`
* `pytest`
* Git
* GitHub

## Project Structure

```text
price-tracker/
│
├── app/
│   ├── scraper.py
│   ├── models.py
│   ├── storage.py
│   ├── tracker.py
│   └── utils.py
│
├── data/
│   ├── products.json
│   └── price_history.json
│
├── tests/
│   ├── test_scraper.py
│   ├── test_storage.py
│   └── test_tracker.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mohammad767/PhonePriceTraking.git
cd PhonePriceTraking
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application provides a simple command-line menu for scraping products, updating prices, and viewing price history.

Example product:

```python
Product(
    name="Example Mobile",
    price=74999000,
    url="https://example.com/product",
    source="technolife"
)
```

## Price Tracking

The tracker compares the current price with the previously stored price.

Example:

```text
Previous price: 70,000,000
Current price: 67,500,000
Change: -2,500,000
Status: Price decreased
```

It can also detect price increases and unchanged prices.

Price changes are stored in `data/price_history.json`.

## Web Scraping

The project uses `requests` to send HTTP requests and `BeautifulSoup` to parse returned HTML.

For Technolife, product information is extracted from the relevant HTML elements, including the product name, current price, and product link.

The project also supports collecting product data from Digikala through its available API response.

Scraping logic is separated from storage and price-tracking logic to keep each module focused on a specific responsibility.

## Data Model

Products are represented using a Python `dataclass`.

Each product contains:

```text
name
price
url
source
```

Example:

```python
Product(
    name="Samsung Galaxy S24",
    price=45000000,
    url="https://example.com/product",
    source="technolife"
)
```

## Testing

Run the test suite with:

```bash
pytest
```

The project includes tests for:

* Scraping
* HTTP request errors
* Data parsing
* JSON storage
* Product loading
* Price tracking
* Price comparison

## Limitations

* Website structures can change, which may require updating selectors or API handling.
* The initial version uses JSON rather than a database.
* Scraping behavior depends on the target website and its availability.
* This project is designed as a small learning and portfolio project rather than a production-scale scraping system.

## Future Improvements

Possible future improvements include:

* Add more online stores
* Use a database instead of JSON
* Schedule automatic price checks
* Add notifications for price changes
* Improve scraper resilience
* Add logging
* Add a web dashboard
* Use asynchronous scraping where appropriate

## Learning Goals

This project is intended to strengthen practical skills in:

* Python
* HTTP requests
* HTML parsing
* BeautifulSoup
* Data cleaning
* `dataclass`
* JSON and file I/O
* Error handling
* Testing with `pytest`
* Software architecture
* Git and GitHub

## Author

**Hassan**

This project was built as a practical Python/Web Scraping portfolio project.


