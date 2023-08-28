from customer import Customer
from restaurant import Restaurant

# Create customers and restaurants
alice = Customer("Alice", "Johnson")
bob = Customer("Bob", "Smith")
restaurant1 = Restaurant("Delicious Eats")
restaurant2 = Restaurant("Tasty Bites")

# Customers add reviews
alice_review1 = alice.add_review(restaurant1, 4)
bob_review1 = bob.add_review(restaurant1, 5)
alice_review2 = alice.add_review(restaurant2, 3)

# Retrieve information
print(restaurant1.average_star_rating())  # Output: 4.5
print(alice.restaurants())                # Output: [Restaurant("Delicious Eats"), Restaurant("Tasty Bites")]
print(bob.num_reviews())                  # Output: 1
