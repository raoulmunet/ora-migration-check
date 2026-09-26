from __future__ import annotations
from dataclasses import dataclass,asdict
import re

@dataclass(frozen=True)
class Finding:
    feature:str
    line:int
    target:str
    guidance:str
    risk:str
    def to_dict(self): return asdict(self)

RULES={
"NVL": (r"\bNVL\s*\(", {"postgres":"Review COALESCE; verify datatype-resolution differences.","sqlserver":"Review COALESCE/ISNULL; verify datatype-resolution differences."},"medium"),
"DECODE": (r"\bDECODE\s*\(", {"postgres":"Rewrite as CASE.","sqlserver":"Rewrite as CASE."},"medium"),
"SYSDATE": (r"\bSYSDATE\b", {"postgres":"Review CURRENT_TIMESTAMP/CURRENT_DATE depending required datatype and timezone semantics.","sqlserver":"Review SYSDATETIME()/GETDATE() depending required precision."},"medium"),
"ROWNUM": (r"\bROWNUM\b", {"postgres":"Rewrite top-N/pagination using LIMIT/FETCH or window logic.","sqlserver":"Rewrite top-N/pagination using TOP/OFFSET-FETCH or window logic."},"high"),
"CONNECT BY": (r"\bCONNECT\s+BY\b", {"postgres":"Rewrite hierarchy using WITH RECURSIVE.","sqlserver":"Rewrite hierarchy using a recursive CTE."},"high"),
"SEQUENCE.NEXTVAL": (r"\b[A-Za-z][\w$#]*\.NEXTVAL\b", {"postgres":"Map to target sequence/identity design and nextval(...).","sqlserver":"Map to SEQUENCE NEXT VALUE FOR or identity design."},"high"),
"OUTER JOIN (+)": (r"\(\+\)", {"postgres":"Rewrite legacy Oracle outer join as ANSI JOIN.","sqlserver":"Rewrite legacy Oracle outer join as ANSI JOIN."},"high"),
"PACKAGE": (r"\bCREATE\s+(?:OR\s+REPLACE\s+)?PACKAGE\b", {"postgres":"No direct package equivalent; redesign procedural/API grouping.","sqlserver":"No direct package equivalent; redesign using schemas/procedures/functions."},"high"),
"MERGE": (r"\bMERGE\s+INTO\b", {"postgres":"Review target-version MERGE/upsert semantics and concurrency behavior.","sqlserver":"MERGE exists, but review target semantics and known concurrency/design considerations."},"medium"),
}

def scan(sql:str,target:str)->list[Finding]:
    if target not in {"postgres","sqlserver"}: raise ValueError("target must be postgres or sqlserver")
    out=[]
    for feature,(pat,guidance,risk) in RULES.items():
        for m in re.finditer(pat,sql,re.I):
            out.append(Finding(feature,sql.count("\n",0,m.start())+1,target,guidance[target],risk))
    return sorted(out,key=lambda x:(x.line,x.feature))
