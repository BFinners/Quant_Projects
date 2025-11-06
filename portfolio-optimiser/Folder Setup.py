import os

# ====== CONFIG ======
project_name = "portfolio-optimiser"
folders = [
    "notebooks",
    "src/portfolio_opt",
    "reports/figures",
    "tests"
]

files = {
    ".gitignore": """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env

# Jupyter
.ipynb_checkpoints

# VSCode / PyCharm
.vscode/
.idea/
""",
    "requirements.txt": """numpy
pandas
scipy
matplotlib
plotly
cvxpy
yfinance
scikit-learn
statsmodels
jupyterlab
numba
dash
pytest
flake8
""",
    "README.md": """# Portfolio Optimiser & Risk Visualiser

## Description
This project builds and visualises optimal portfolios using Python. Features include:
- Mean-variance optimisation (Markowitz)
- Risk metrics (VaR, CVaR)
- Interactive visualisations
- Optional backtesting and transaction-cost-aware rebalancing

## Folder structure
- `src/portfolio_opt/`: Python modules (data, stats, optimisation, backtest, viz)
- `notebooks/`: Example notebook with full walkthrough
- `reports/figures/`: Saved plots and figures
- `tests/`: Unit tests

## How to run
1. Install dependencies: conda install --file requirements.txt -c defaults -c conda-forge
2. Open `notebooks/portfolio_opt_explained.ipynb` to explore the workflow.
3. Optional: Run `dash_app.py` for an interactive dashboard.
""",
    "src/portfolio_opt/__init__.py": "# Makes this folder a Python package\n",
    "src/portfolio_opt/data.py": """# Placeholder for data fetching module
def get_prices(tickers, start, end):
    \"\"\"
    Fetch adjusted close prices for tickers from Yahoo Finance.
    \"\"\"
    pass
""",
    "src/portfolio_opt/stats.py": """# Placeholder for statistics functions
def compute_returns(prices):
    \"\"\"
    Compute daily returns from price DataFrame
    \"\"\"
    pass
""",
    "src/portfolio_opt/optim.py": """# Placeholder for optimisation functions
def mean_variance_optim(mu, sigma, target_return):
    \"\"\"
    Solve mean-variance optimisation problem
    \"\"\"
    pass
""",
    "src/portfolio_opt/backtest.py": """# Placeholder for backtesting module
def simulate_portfolio(weights, prices):
    \"\"\"
    Simulate portfolio performance over time
    \"\"\"
    pass
""",
    "src/portfolio_opt/viz.py": """# Placeholder for visualisation functions
def plot_efficient_frontier(frontier):
    \"\"\"
    Plot efficient frontier
    \"\"\"
    pass
""",
    "notebooks/portfolio_opt_explained.ipynb": "",  # empty notebook
    "dash_app.py": """# Placeholder for optional dashboard
if __name__ == "__main__":
    print("Dash app placeholder")
""",
    "tests/test_stats.py": """# Placeholder for unit tests
def test_compute_returns():
    assert True  # Replace with actual tests later
"""
}

# ====== CREATE FOLDERS ======
for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# ====== CREATE FILES ======
for path, content in files.items():
    full_path = os.path.join(project_name, path)
    with open(full_path, "w") as f:
        f.write(content)

print(f"Project '{project_name}' folder structure created successfully!")
