import pandas as pd
from datetime import datetime
from pathlib import Path

def export_to_excel(data, filename='job_applications.xlsx'):
    """Export data to Excel with timestamp"""
    # convert string path to Path object if needed
    if not isinstance(filename, Path):
        filename = Path(filename)
    
    df = pd.DataFrame(data)
    
    # add metadata
    metadata = {
        'Report Generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Total Applications': len(df),
        'Status Counts': df['Status'].value_counts().to_dict()
    }
    
    with pd.ExcelWriter(filename) as writer:
        df.to_excel(writer, sheet_name='Applications', index=False)
        
        # add metadata sheet
        pd.DataFrame.from_dict(metadata, orient='index').to_excel(
            writer, sheet_name='Metadata'
        )
    
    print(f"Report saved to: {filename.absolute()}")
    return filename