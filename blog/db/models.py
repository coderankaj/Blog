from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from blog import Base, engine


class Post(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    comments = relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'


class Comment(Base):
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    post_id = Column(Integer, ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'



