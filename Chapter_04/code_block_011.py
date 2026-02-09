# Full chain: NLU → mapping → SQL
chain = nlu_chain | to_sql_vars | sql_chain