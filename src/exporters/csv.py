import pandas as pd
from pathlib import Path

def export_to_csv(data, filename='job_applications.csv'):
    """Export data to Excel with timestamp"""
    # convert string path to Path object if needed
    if not isinstance(filename, Path):
        filename = Path(filename)

    df = pd.DataFrame(data)

    df.to_csv(filename, header=True, index=False)

    print(f"Report saved to: {filename.absolute()}")
    return filename
