# Simple ETL Pipeline Assignment

Name: Tridiktya Hardani Putra

Click [here](./main.ipynb) to view the notebook.

## Steps to run the notebook

1. Install the required packages using uv.
```bash
uv sync
```

2. Add an .env file in the root directory with the following content:
```env
DATABASE_URL="postgresql+psycopg2://USER:PASSWORD@HOST:PORT/DATABASE_NAME"
```
Make sure to replace `USER`, `PASSWORD`, `HOST`, `PORT`, and `DATABASE_NAME` with your actual PostgreSQL database credentials. Also, ensure that the PostgreSQL database is running and accessible.

3. Run the notebook using Jupyter Notebook via uv.
```bash
uv run --with jupyter jupyter notebook
```
