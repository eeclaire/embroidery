import pandas as pd
import pydash
import tabula


def read_pdf(file_path: str) -> pd.DataFrame:
    left = 26
    # right = left + 545
    # top = 228
    # bottom = top + 230

    column_1 = left + 54
    column_1_color_codes = column_1 + 57
    column_1_skein_count = column_1_color_codes + 75

    column_2 = column_1_skein_count + 52
    column_2_color_codes = column_2 + 50
    column_2_skein_count = column_2_color_codes + 73

    column_3 = column_2_skein_count + 55
    column_3_color_codes = column_3 + 50
    # column_3_skein_count = column_3_color_codes + 76

    df = tabula.read_pdf(
        file_path,
        guess=False,
        pages=3,
        stream=True,
        columns=[
            column_1, column_1_color_codes, column_1_skein_count,
            column_2, column_2_color_codes, column_2_skein_count,
            column_3, column_3_color_codes
        ],
        pandas_options={'header': None}
    )

    return df[0]


def normalize_thread_row(row: dict) -> dict:
    return {
        "id": int(row["id"]),
        "code": row["code"],
        "count": int(row["count"][len("x "):]),
    }


def is_thread_row(row: dict) -> bool:
    valid_id = False
    if pd.isna(row["id"]):
        return False
    if isinstance(row["id"], bool):
        return False
    elif isinstance(row["id"], int):
        valid_id = True
    elif isinstance(row["id"], str):
        valid_id = True if row["id"].isdigit() else False

    # Check that thread count starts with "x "
    expected = "x "
    valid_thread_count = False
    if not isinstance(row["count"], str):
        return False
    elif row["count"][:(len(expected))] == expected:
        valid_thread_count = True

    if valid_id and valid_thread_count:
        return True

    return False


def parse_pdf_contents(df: pd.DataFrame):
    final = []
    (_, cols_len) = df.shape

    # Assumption that there are 3 columns to parse through
    for i in range(0, cols_len, 3):
        sub = df.iloc[:, i:i + 3].rename(
            columns={i: "id", i + 1: "code", i + 2: "count"})
        d = sub.to_dict("records")
        d = pydash.filter_(d, is_thread_row)
        d = pydash.map_(d, normalize_thread_row)
        final += d

    return final
