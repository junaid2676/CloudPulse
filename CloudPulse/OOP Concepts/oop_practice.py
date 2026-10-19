# A class is a blueprint for creating service objects.
class Service:

    # __init__ runs when we create a new Service object.
    def __init__(self, name, url):
        # Store the supplied values on this object.
        self.name = name
        self.url = url


# Create two separate Service objects.
website = Service("Example Website", "https://example.com")
python_site = Service("Python Website", "https://www.python.org")

# Display the attributes stored in each object.
print(website.name)
print(website.url)

print(python_site.name)
print(python_site.url)
