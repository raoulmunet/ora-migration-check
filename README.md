# ora-migration-check

Scan Oracle SQL for constructs that deserve attention before migration to PostgreSQL or SQL Server.

> **Oracle source compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Common SQL/PLSQL constructs |
> | Oracle Database 23ai | ✅ Common SQL/PLSQL constructs |
> | Oracle AI Database 26ai | ✅ Common SQL/PLSQL constructs |
>
> Newer release-specific syntax that is not in the rule catalog is reported only when a matching rule exists. The tool does not claim full cross-database transpilation.

## Targets

- PostgreSQL
- SQL Server

## Checks currently include

- `NVL`
- `DECODE`
- `SYSDATE`
- `ROWNUM`
- `CONNECT BY`
- sequence `.NEXTVAL`
- `MERGE` review
- Oracle outer join `(+)`
- PL/SQL package constructs

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-migration-check.git"

ora-migration-check examples/oracle_query.sql --target postgres
ora-migration-check examples/oracle_query.sql --target sqlserver --format json
```

Example:

```text
NVL        -> review COALESCE semantics
ROWNUM     -> rewrite pagination/top-N logic
CONNECT BY -> recursive CTE or target-specific hierarchy logic
```

## Important

A suggested equivalent is a migration hint, not a guarantee of identical semantics. Datatypes, NULL behavior, optimizer behavior, date/time semantics and procedural code require testing on the target platform.

## License

MIT.
