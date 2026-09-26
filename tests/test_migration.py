from ora_migration_check import scan

def test_postgres_rules():
    f=scan("select nvl(x,0) from t where rownum <= 10","postgres")
    assert {x.feature for x in f}=={"NVL","ROWNUM"}

def test_connect_by():
    assert scan("select * from t connect by prior id=parent_id","sqlserver")[0].feature=="CONNECT BY"
