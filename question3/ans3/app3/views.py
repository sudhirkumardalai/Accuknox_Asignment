# books/views.py
from django.shortcuts import HttpResponse
from django.db import transaction
from .models import Book

def signal_test(request):
    # Initialize the output variable
    output = ""
    
    # Initialize the book variable
    book = None
    
    # Start a transaction
    try:
        with transaction.atomic():
            # Create a new Book instance (this triggers the signal)
            book = Book.objects.create(title="Original Title")
            
            # Prepare the output showing the title after the signal
            output = f"During transaction (after signal): {book.title}<br>"

            # Schedule on_commit task (to be run after transaction commits)
            transaction.on_commit(lambda: print(f"After commit: {book.title}"))

            # Force an exception to rollback the transaction
            raise Exception("Force rollback")

    except Exception as e:
        # Add the exception message to the output
        output += f"Transaction rolled back due to: {e}<br>"

    # Check if the book was rolled back (it should not exist in the DB)
    if book and not Book.objects.filter(id=book.id).exists():
        output += "Book was rolled back, including signal changes."
    elif book:
        output += "Book was saved, signal changes persisted."
    else:
        output += "No book was created."

    return HttpResponse(output)
