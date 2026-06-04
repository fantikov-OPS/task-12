from sqlalchemy import create_engine, text



e = create_engine("sqlite:///test.sqlite")

with e.begin() as conn:
    conn.execute(text("""
                    create table user (
                    id integer primary key autoincrement,
                    firstname varchar,
                    lastname varchar
                    )
                      """))