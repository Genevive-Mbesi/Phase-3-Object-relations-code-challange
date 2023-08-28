from review import Review

class Customer:
    _all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls._all_customers

    def restaurants(self):
        reviewed_restaurants = [review.restaurant() for review in Review.all() if review.customer() == self]
        return list(set(reviewed_restaurants))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        return new_review

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer() == self])

    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls._all_customers if customer.given_name() == name]
