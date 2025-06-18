import pandas as pd
import cx_Oracle
import sys

def insert_excel_to_oracle(excel_path, db_config, table_name, excel_columns, db_columns=None):
    """
    Simple function to insert Excel data into Oracle database
    
    Parameters:
    - excel_path: Path to Excel file
    - db_config: Dictionary with DB connection info
    - table_name: Oracle table name
    - excel_columns: List of Excel column names to insert
    - db_columns: List of DB column names (if different from Excel columns)
    """
    
    try:
        # Read Excel file
        print(f"📖 Reading Excel file: {excel_path}")
        df = pd.read_excel(excel_path)
        print(f"✅ Found {len(df)} rows in Excel")
        
        # Filter only the columns we want
        df_filtered = df[excel_columns].copy()
        
        # If DB columns are different, rename them
        if db_columns:
            column_mapping = dict(zip(excel_columns, db_columns))
            df_filtered = df_filtered.rename(columns=column_mapping)
            target_columns = db_columns
        else:
            target_columns = excel_columns
        
        # Connect to Oracle
        print("🔌 Connecting to Oracle database...")
        dsn = cx_Oracle.makedsn(
            db_config['host'], 
            db_config['port'], 
            service_name=db_config['service_name']
        )
        connection = cx_Oracle.connect(
            db_config['username'], 
            db_config['password'], 
            dsn
        )
        print("✅ Connected to database")
        
        # Prepare INSERT statement
        placeholders = ', '.join([f':{i+1}' for i in range(len(target_columns))])
        column_names = ', '.join(target_columns)
        sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
        
        print(f"📝 SQL: {sql}")
        
        # Insert data
        cursor = connection.cursor()
        inserted_count = 0
        error_count = 0
        
        print("🚀 Starting insertion...")
        
        for index, row in df_filtered.iterrows():
            try:
                # Convert row to list, handling NaN values
                row_values = []
                for value in row.values:
                    if pd.isna(value):
                        row_values.append(None)
                    else:
                        row_values.append(value)
                
                cursor.execute(sql, row_values)
                inserted_count += 1
                
                if inserted_count % 100 == 0:
                    print(f"   Inserted {inserted_count} rows...")
                    
            except Exception as e:
                error_count += 1
                print(f"❌ Error in row {index + 1}: {e}")
                continue
        
        # Commit changes
        connection.commit()
        cursor.close()
        connection.close()
        
        # Summary
        print("\n" + "="*50)
        print("📊 SUMMARY")
        print("="*50)
        print(f"✅ Successfully inserted: {inserted_count} rows")
        print(f"❌ Errors: {error_count} rows")
        print(f"📊 Total processed: {len(df_filtered)} rows")
        
        return True
        
    except Exception as e:
        print(f"❌ General error: {e}")
        return False

# CONFIGURATION - MODIFY THESE VALUES
if __name__ == "__main__":
    
    # Database configuration
    DB_CONFIG = {
        'username': 'your_username',
        'password': 'your_password', 
        'host': 'localhost',
        'port': '1521',
        'service_name': 'your_service_name'
    }
    
    # File and table configuration
    EXCEL_PATH = 'your_file.xlsx'  # Path to your Excel file
    TABLE_NAME = 'your_table'      # Oracle table name
    
    # Column mapping
    EXCEL_COLUMNS = ['Column1', 'Column2', 'Column3']  # Excel column names
    DB_COLUMNS = ['COL1', 'COL2', 'COL3']             # DB column names (optional, if different)
    
    # Run the insertion
    print("🚀 Excel to Oracle Insertion Tool")
    print("="*50)
    
    success = insert_excel_to_oracle(
        excel_path=EXCEL_PATH,
        db_config=DB_CONFIG,
        table_name=TABLE_NAME,
        excel_columns=EXCEL_COLUMNS,
        db_columns=DB_COLUMNS  # Remove this line if Excel and DB columns have same names
    )
    
    if success:
        print("🎉 Process completed successfully!")
    else:
        print("💥 Process failed!")
