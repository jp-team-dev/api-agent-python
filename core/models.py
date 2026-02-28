from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import mapped_column, Mapped, declarative_base

Base = declarative_base()

class DocSection(Base):
    __tablename__ = "doc_sections"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    embedding: Mapped[Vector] = mapped_column(Vector(1536))
    content: Mapped[str] = mapped_column()
