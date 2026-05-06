rule reproduce_dataset:
    input:
        "Affordable-Rental-Housing-Developments.csv",
        "libraries-json.csv",
        "Parks-Locations.csv"
    output:
        "results/correlation.pdf",
        "results/correlation_results.txt"
    shell:
        "python script.py"
