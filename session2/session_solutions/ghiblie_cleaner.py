from bda.session2.session_solutions.data_loader import load_csv_as_dicts

data = load_csv_as_dicts("studio_ghibli_movies.csv")

print(f"Loaded rows: {data} .")