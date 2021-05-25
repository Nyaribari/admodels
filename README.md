# admodels

**Exploring Django new functionalities.**

Meta data and the Enum class for making choices easily and making the application fast fast.
Since Django 3.0, there is a Choices class that extends Python’s Enum types with extra constraints and functionality.


# UUID for ids unique.

Universally unique identifier is a 128-bit number, usually represented as 32 hexadecimal characters separated by four hyphens. The probability that a UUID will be duplicated is not zero, but it is close enough to zero to be negligible.

ID that Django uses out-of-the-box is incremented sequentially. That means that the 5th registered user has an id 5 and the 6th one has id 6. So, if I register and figure out that my id is 17, I know there were 16 people registered before me and I can try to get to their data by using their id. That makes your application very vulnerable.

That's where UUID comes in handy. UUID key is randomly generated, so it doesn't carry any information as of how many people are registered to the page or what their id might be.
