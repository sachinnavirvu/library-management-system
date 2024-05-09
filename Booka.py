from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for books
books = [
    {'title': 'Book 1', 'author': 'Author 1', 'category': 'Fiction', 'available': True},
    {'title': 'Book 2', 'author': 'Author 2', 'category': 'Non-Fiction', 'available': False},
    {'title': 'Book 3', 'author': 'Author 3', 'category': 'Fiction', 'available': True}
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        query = request.form['query']
        # Implement book search logic based on query
        search_results = [book for book in books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
        return render_template('search_results.html', query=query, results=search_results)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
