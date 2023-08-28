from review import Review

class Restaurant:
    _all_restaurants = []

    def __init__(self, name):
        self._name = name
        self._all_restaurants.append(self)

    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all_restaurants

    def reviews(self):
        return [review for review in Review.all() if review.restaurant() == self]

    def customers(self):
        reviewed_customers = [review.customer() for review in Review.all() if review.restaurant() == self]
        return list(set(reviewed_customers))

    def average_star_rating(self):
        restaurant_reviews = self.reviews()
        if not restaurant_reviews:
            return 0
        total_rating = sum([review.rating() for review in restaurant_reviews])
        return total_rating / len(restaurant_reviews)
