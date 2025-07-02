class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot modify the title after it has been set")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be 5-50 characters in length")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of the Author class")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of the Magazine class")
        
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot modify the name after it has been set")
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be longer than 0 characters")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique_magazines = {article.magazine for article in Article.all if article.author == self}
        return list(unique_magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class")
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        contributed_magazines = {article.magazine for article in Article.all if article.author == self}
        if not contributed_magazines:
            return None
        unique_topic_areas = {magazine.category for magazine in contributed_magazines}
        return list(unique_topic_areas)

class Magazine:
    all=[]

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be 2-16 characters in length")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise ValueError("Category must be longer than 0 characters")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_contributors = {article.author for article in Article.all if article.magazine == self}
        return list(unique_contributors)

    def article_titles(self):
        magazine_articles = [article.title for article in Article.all if article.magazine == self]
        if not magazine_articles:
            return None
        return magazine_articles

    def contributing_authors(self):
        author_article_count = {}
        authors_with_more_than_two_articles = []

        for article in Article.all:
            if article.magazine == self:
                author = article.author
                if isinstance(author, Author):
                    if author in author_article_count:
                        author_article_count[author] += 1
                    else:
                        author_article_count[author] = 1
        
        for author, count in author_article_count.items():
            if count > 2:
                authors_with_more_than_two_articles.append(author)
        
        return authors_with_more_than_two_articles if authors_with_more_than_two_articles else None