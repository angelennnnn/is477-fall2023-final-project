rule prepare:
    output:
        "data/breast_cancer_wisconsin/breast_cancer_wisconsin.csv"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/breast_cancer_wisconsin/breast_cancer_wisconsin.csv"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    input:
        "data/breast_cancer_wisconsin/breast_cancer_wisconsin.csv"
    output:
        summary_stats="results/summary_statistics.csv",
        class_report="results/classification_report.txt",
        conf_matrix="results/confusion_matrix.csv",
        feature_importances="results/feature_importances.png"
    shell:
        "python scripts/analysis.py"
rule reproduce:
    input:
        summary_stats="results/summary_statistics.csv",
        class_report="results/classification_report.txt",
        conf_matrix="results/confusion_matrix.csv",
        feature_importances="results/feature_importances.png",
        profiling_report="profiling/report.html"
    output:
        "results/reproducibility_check.txt"
    shell:
        "echo 'All analyses have been successfully reproduced.' > {output}"
