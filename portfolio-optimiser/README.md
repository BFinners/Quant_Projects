# Portfolio Optimiser & Risk Visualiser

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
1. Install dependencies: `conda install --file requirements.txt -c defaults -c conda-forge`
2. Open `notebooks/portfolio_opt_explained.ipynb` to explore the workflow.
3. Optional: Run `dash_app.py` for an interactive dashboard.
