import pandas as pd
from datetime import datetime

def export_to_excel(data, filename='job_applications.xlsx'):
    """Export data to Excel with timestamp"""
    df = pd.DataFrame(data)
    
    # Add metadata
    metadata = {
        'Report Generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Total Applications': len(df)
    }
    
    with pd.ExcelWriter(filename) as writer:
        df.to_excel(writer, sheet_name='Applications', index=False)
        
        # Add metadata sheet
        pd.DataFrame.from_dict(metadata, orient='index').to_excel(
            writer, sheet_name='Metadata'
        )
    
    return filename