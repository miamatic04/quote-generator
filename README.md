# Generate a Random Quote with Python and ZenQuotes API

## Introduction

Need a little inspiration? What if you could get a brand new motivational quote delivered to your terminal every time you ran a Python script?

In this project tutorial, you'll learn how to fetch a real quote from the internet using just **6 lines of Python code**. We'll use a library called `requests` to talk to a free API (Application Programming Interface) - think of it as knocking on a door and asking for data.

Here's a preview of what you'll see when you run the program:

```
The only way to do great work is to love what you do.
— Steve Jobs
```

Pretty cool, right? Let's build it. 

---

## What is an API?

An API is a way for two programs to talk to each other. In our case, we'll be asking a website called **ZenQuotes** for a random quote, and it will send one back to us.

You don't need to sign up or create an account - ZenQuotes is completely free and open to use. Perfect for beginners!

---

## The requests library

`requests` is a popular Python library that makes it easy to send messages to websites and get data back. It's one of the most downloaded Python libraries in the world.

To install it, run this command in your Terminal (Mac) or Command Prompt (Windows):
```
pip install requests
```
or:
```
pip3 install requests
```
You should see a message like:

```
Successfully installed requests-2.28.0
```

You can verify the install worked by opening Python and running `import requests`. If no error appears, you're good to go! 

---

## Writing the Program

Open your code editor (like VS Code) and create a new file called `quote.py`.

**Step 1: Import the library**

At the top of the file, import the `requests` library:

```python
import requests
```

This gives our program access to all of `requests`'s features.

**Step 2: Fetch a quote from the internet**

Now let's send a request to the ZenQuotes API:

```python
response = requests.get('https://zenquotes.io/api/random')
```

`requests.get()` visits a URL, just like your browser does, and stores whatever comes back in the `response` variable. The URL we're visiting is ZenQuotes' API endpoint for a random quote.

**Step 3: Parse the response**

The API sends data back in a format called **JSON** (JavaScript Object Notation). It looks a lot like a Python list of dictionaries. We can convert it like this:

```python
data = response.json()
```

Now `data` holds the quote information. Here's what it looks like behind the scenes:

```json
[{"q": "The only way to do great work is to love what you do.", "a": "Steve Jobs"}]
```

- `"q"` is the quote text
- `"a"` is the author

**Step 4: Print the quote**

Let's pull out the quote and author and display them nicely:

```python
print(data[0]['q'])
print('—', data[0]['a'])
```

`data[0]` grabs the first (and only) item in the list. Then `['q']` and `['a']` pull out the quote and author.

---

## The Full Program

Here's everything together:

```python
import requests

response = requests.get('https://zenquotes.io/api/random')
data = response.json()

print(data[0]['q'])
print('—', data[0]['a'])
```

That's it, 6 lines! 

---

## Running the Program

In your terminal, navigate to the folder where you saved `quote.py`:

```
cd Desktop
```

Then run it:

```
python3 quote.py
```

You should see a random quote printed out, like:

```
In the middle of every difficulty lies opportunity.
— Albert Einstein
```

Run it again and you'll get a completely different quote. Every time! 

---

## Make It Your Own

Ready to take things further? Try these challenges:

**Challenge 1**

Print a divider line above and below the quote to make it look nicer:

```
--------------------------------------------------
The only way to do great work is to love what you do.
— Steve Jobs
--------------------------------------------------
```

**Challenge 2**

Save your quote to a file!

Instead of `print()`, try writing the quote to a `.txt` file. Look up Python's built-in `open()` function to get started.

**Challenge 3**

Print 3 quotes at once

Hint: You'll need to visit a different endpoint. Try replacing `/api/random` with `/api/quotes` — it returns 50 quotes at a time. Use a `for` loop to print the first three.

---

## Wrapping Up

Congrats! You just wrote a Python program that talks to the internet and fetches real data. You learned how to:

- Install and import a third-party library
- Make an API request with `requests.get()`
- Parse a JSON response
- Display the results in the terminal

This is the foundation of how apps, bots, and tools across the internet work. From here, you can fetch weather data, news headlines, sports scores - the sky's the limit. 

---

## More Resources

- [requests Documentation](https://requests.readthedocs.io/)
- [ZenQuotes API Docs](https://zenquotes.io/)
- [Python JSON Docs](https://docs.python.org/3/library/json.html)
