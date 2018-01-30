SELECT_STATEMENT = "SELECT * FROM users"
c.execute(SELECT_STATEMENT)
print(c.fetchone())
print(c.fetchone())
