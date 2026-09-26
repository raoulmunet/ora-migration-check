from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import scan

def main(argv=None):
    p=argparse.ArgumentParser(description="Check Oracle SQL migration hotspots.")
    p.add_argument("source")
    p.add_argument("--target",required=True,choices=("postgres","sqlserver"))
    p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv)
    findings=scan(Path(a.source).read_text(encoding="utf-8"),a.target)
    if a.format=="json":
        print(json.dumps([f.to_dict() for f in findings],indent=2))
    else:
        for f in findings:
            print(f"line {f.line}: {f.feature} [{f.risk}] -> {f.guidance}")
    return 1 if findings else 0
if __name__=="__main__": raise SystemExit(main())
