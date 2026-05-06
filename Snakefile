rule run_all:
    input:
        "Affordable-Rental-Housing-Developments.csv",
        "libraries-json.csv",
        "Parks-Locations.csv"
rule reproduce_dataset:
    input:
        "Affordable-Rental-Housing-Developments.csv",
        "libraries-json.csv",
        "Parks-Locations.csv"
    output:
        "results/correlation.pdf",
        "results/aggregated_counts.csv"
    shell:
        "python script.py"

