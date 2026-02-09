# Orchestrate with try/except to catch unhandled errors
try:
    structured = safe_extract.invoke({"input": "Get employee names for product 'X' sold in January."})
    sql = safe_sql.invoke(structured)
    print(sql)
except Exception as e:
    print("Handled error:", str(e))