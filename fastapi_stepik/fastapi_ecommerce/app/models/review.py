from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, Boolean, Text, DateTime
from datetime import datetime

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rating_id = Column(Integer, ForeignKey('ratings.id'))
    comment = Column(Text)
    comment_date = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)