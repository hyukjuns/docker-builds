### SQL
```
# SELECT
SELECT * FROM table;

# INSERT
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

# ALTER
ALTER TABLE tablename MODIFY columnname INTEGER;

# DELETE
DELETE FROM table WHERE key = value;

# UPDATE
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### Init db
scheme.sql -> dockerfile's entrypoint.d