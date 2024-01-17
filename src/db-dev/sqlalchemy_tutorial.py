from sqlalchemy import create_engine, text
import os

connectionstring_pg = os.environ["PYTHON_DEV_CONNECTION_STRING"]
print(connectionstring_pg)

# connectionstring_sqlite_mem = sqlite+pysqlite:///:memory:"

engine = create_engine(connectionstring_pg, echo=False)

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()

with engine.connect() as conn:
    result = conn.execute(text("select x, y from some_table"))
    for row in result:
        print(f"Row: {row.x} {row.y}")

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")


from sqlalchemy.orm import Session

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 1})
    for row in result:
        print(f"sesssion x: {row.x}  y: {row.y}")


with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
    )
    session.commit()

with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"sesssion x: {row.x}  y: {row.y}")

from sqlalchemy import MetaData

metadata_obj = MetaData()

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), nullable=False),
    Column("fullname", String, nullable=False),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

# create two tables, does not recreate the tables if present.
metadata_obj.create_all(engine)

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


bjoren = User(name="bjoren", fullname="bjorn joren")
bjoren_addr = Address(email_address="bjoren@blaat.be", user=bjoren)


# with Session(engine) as session:
#     result = session.ins(
#         text("UPDATE some_table SET y=:y WHERE x=:x"),
#         [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
#     )
#     session.commit()


from sqlalchemy import insert

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
compiled = stmt.compile()

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.inserted_primary_key)
    conn.commit()
