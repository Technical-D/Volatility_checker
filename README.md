# Volatility Checker

A web application to calculate daily and annualized volatility of financial datasets.
![image](https://github.com/Technical-D/Volatility_checker/assets/101353705/89e5d118-51a9-43e6-a6bc-605fe84f5603)


## Features

- Upload a financial dataset in CSV format.
- Calculate daily and annualized volatility using an API endpoint.
- View the results in a formatted JSON display.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/) installed

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/volatility-checker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd volatility-checker
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```
    
2. Open your browser and go to [http://localhost:5000](http://localhost:5000).

3. Upload a financial dataset in CSV format and click "Calculate Volatility."

4. View the calculated daily and annualized volatility in a formatted JSON display.

5. API Endpoint: (http://localhost:5000/compute_volatility)

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
