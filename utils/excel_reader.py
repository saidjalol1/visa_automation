import pandas as pd
from config import FILE_PATH
from .db_commands import insert_into_table, read_from_table, create_users_table
from .tmp_email_gen import create_temp_email, generate_password


def write_users_to_database(data, log_callback, frame_call_back):
    """
    write users' data in to databse
    """
    for i in data:
        create_users_table()
        account = create_temp_email()
        insert_into_table(
        "users",
        category=i.get("Category"),
        subcategory=i.get("Subcategory"),
        city=i.get("City"),
        name=f"{i.get('Surname')} {i.get('Name')}",
        passport=i.get("Passport number"),
        birth_date=i.get("Birthdate (dd.mm.yyyy)"),
        passport_validity=i.get("Passport validity  (dd.mm.yyyy)"),
        gender=i.get("Gender (M/F)"),
        phone=i.get("Phone"),
        nation=i.get("Nationality"),
        book_data_from=i.get("Book date from  (dd.mm.yyyy)"),
        book_data_to=i.get("Book date to  (dd.mm.yyyy)"),
        candidate_number = i.get("MIGRIS number"),
        email=str(account.get("email")),
        password=str(generate_password()),
        registered=0,
        booked=0,
        token=str(account.get("token")),
        )
        log_callback(f"Email and password created for: {account.get('email')}")

    log_callback("All users have been processed.Start registering !!!")
    frame_call_back()
    return data


async def read_excel(file_path: str, sheet_name: str = None, log_callback = None, frame_call_back = None) -> list:
    """
    Reading excel file , returns list of dicts
    """
    excel_file = pd.ExcelFile(file_path)
    sheet = sheet_name or excel_file.sheet_names[0]
    df = excel_file.parse(sheet)

  
    required_columns = [
        "Category", "Subcategory", "City", "Nationality", "Gender (M/F)",
        "Book date from  (dd.mm.yyyy)", "Book date to  (dd.mm.yyyy)",
        "Surname", "Name", "Passport number", "Passport validity  (dd.mm.yyyy)","MIGRIS number"
    ]

    df = df.dropna(subset=required_columns, how='any')

    data = df.to_dict(orient='records')
    write_users_to_database(data, log_callback,frame_call_back)
    return data
