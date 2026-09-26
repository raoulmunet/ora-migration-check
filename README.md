# ora-migration-check

[![tests](https://github.com/raoulmunet/ora-migration-check/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-migration-check/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
