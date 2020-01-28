# Welcome to the VERBOSE OCTO LAMP API!

Here we navigate the shadowy worlds of API engineering.

# Basic Authentication

All web applications need strong security so our app features **Basic Authentication**, providing us with some nifty user safety.

> **A scheme :**  where the client sends **HTTP requests** the **Authorization header** with the word **Basic** followed by a space and a base64-encoded string username:password.


## Salted Hashing

We can store passwords securely using [salts](https://en.wikipedia.org/wiki/Salt_(cryptography)).

```mermaid
sequenceDiagram
User ->> Web Server: Hello Web Server, how is this password?
Web Server -->>Database Server: Oh you only have different salts?
Web Server--x User: I need to check the salt, please wait...
Web Server-x Database Server: Here is the salt for the password!
Note right of Database Server: Web Server thinks a long<br/>long time, so long<br/>because the password is strongly<br/>hashed with 14 rounds of Bcrypt.

Web Server-->User: Checking with Database Server...
User->Database Server: Yes... user, this salted password matches, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Plaintext Password] -- Random --> B((Nonce))
A --> C(Digest)
B --> D{Salted Password}
C --> D
```
# Welcome to the Unnamed API!

Here we navigate the shadowy worlds of API engineering.

# Basic Authentication

All web applications need strong security so our app features **Basic Authentication**, providing us with some nifty user safety.

> **A scheme :**  where the client sends **HTTP requests** the **Authorization header** with the word **Basic** followed by a space and a base64-encoded string username:password.


## Salted Hashing

We can store passwords securely using [salts](https://en.wikipedia.org/wiki/Salt_(cryptography)).

```mermaid
sequenceDiagram
User ->> Web Server: Hello Web Server, how is this password?
Web Server -->>Database Server: Oh you only have different salts?
Web Server--x User: I need to check the salt, please wait...
Web Server-x Database Server: Here is the salt for the password!
Note right of Database Server: Web Server thinks a long<br/>long time, so long<br/>because the password is strongly<br/>hashed with 14 rounds of Bcrypt.

Web Server-->User: Checking with Database Server...
User->Database Server: Yes... user, this salted password matches, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Plaintext Password] -- Random --> B((Nonce))
A --> C(Digest)
B --> D{Salted Password}
C --> D
```

