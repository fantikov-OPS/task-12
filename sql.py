from sqlalchemy import create_engine, text



e = create_engine("sqlite:///test.sqlite")

with e.begin() as conn:
    res=conn.execute(text("""
insert into user (firstname, lastname)
values ('Alex3', 'Varkalov')
                      """))
    conn.rollback()