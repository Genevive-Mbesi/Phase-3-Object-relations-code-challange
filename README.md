# Yelp-style Domain Implementation

This repository contains a Python implementation of a Yelp-style domain with three main models: `Restaurant`, `Customer`, and `Review`. These models interact to simulate a simplified version of the Yelp platform for restaurant reviews. The implementation includes various methods to manage customers, restaurants, and reviews, as well as aggregate and association methods to provide insightful information.

## Classes

### Review

- `Review __init__(self, customer, restaurant, rating)`
  - Initializes a review with a customer, a restaurant, and a rating.
- `Review rating(self)`
  - Returns the rating for a restaurant in this review.
- `Review all()`
  - Returns a list of all reviews.
- `Review customer(self)`
  - Returns the customer object for that review.
- `Review restaurant(self)`
  - Returns the restaurant object for that given review.

### Customer

- `Customer __init__(self, given_name, family_name)`
  - Initializes a customer with a given name and a family name.
- `Customer given_name(self)`
  - Returns the customer's given name.
- `Customer family_name(self)`
  - Returns the customer's family name.
- `Customer full_name(self)`
  - Returns the full name of the customer (given name + family name).
- `Customer all()`
  - Returns a list of all customer instances.
- `Customer restaurants(self)`
  - Returns a unique list of all restaurants a customer has reviewed.
- `Customer add_review(self, restaurant, rating)`
  - Adds a new review associated with this customer and a given restaurant.
- `Customer num_reviews(self)`
  - Returns the total number of reviews that a customer has authored.
- `Customer find_by_name(name)` (class method)
  - Given a full name, returns the first customer whose full name matches.
- `Customer find_all_by_given_name(name)` (class method)
  - Given a given name, returns a list containing all customers with that given name.

### Restaurant

- `Restaurant __init__(self, name)`
  - Initializes a restaurant with a name.
- `Restaurant name(self)`
  - Returns the restaurant's name.
- `Restaurant all()`
  - Returns a list of all restaurant instances.
- `Restaurant reviews(self)`
  - Returns a list of all reviews for this restaurant.
- `Restaurant customers(self)`
  - Returns a unique list of all customers who have reviewed this restaurant.
- `Restaurant average_star_rating(self)`
  - Returns the average star rating for this restaurant based on its reviews.

## Getting Started

To use this implementation, you can clone the repository and explore the provided classes and methods. You can integrate these classes into your own projects or extend the functionality according to your requirements.

## Example Usage

Here's an example of how you can create instances and interact with the Yelp-style domain:

```python

# Create customers and restaurants
alice = Customer("Alice", "Johnson")
bob = Customer("Bob", "Smith")
restaurant1 = Restaurant("Delicious Eats")
restaurant2 = Restaurant("Tasty Bites")

# Customers add reviews
alice.add_review(restaurant1, 4)
bob.add_review(restaurant1, 5)
alice.add_review(restaurant2, 3)

# Retrieve information
print(restaurant1.average_star_rating())  # Output: 4.5
print(alice.restaurants())                # Output: [Restaurant("Delicious Eats"), Restaurant("Tasty Bites")]
print(bob.num_reviews())                  # Output: 1

## Contribution
Feel free to contribute to this repository by suggesting improvements, reporting issues, or submitting pull requests.

## License
This project is licensed under the MIT License.