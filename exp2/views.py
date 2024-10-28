from django.shortcuts import render

def index(request):
    context = {
        'result': '',
        'filtered_names': ['']
    }

    # List of names for filtering
    names_list = ['Alice', 'Andrew', 'Amelia', 'Aaron', 'Benjamin', 'Bella', 'Brian', 'Brittany', 'Christopher']

    # Check if the request is POST and determine which button was clicked
    if request.method == 'POST':
        # Handle the Odd or Even Checker
        if 'check_odd_even' in request.POST:
            try:
                number = int(request.POST.get('number'))
                if number % 2 == 0:
                    context['result'] = f'{number} is an even number'
                else:
                    context['result'] = f'{number} is an odd number'
            except ValueError:
                context['result'] = 'Please enter a valid number'

        # Handle the Name Filter
        if 'search_name' in request.POST:
            character = request.POST.get('character', '').lower()
            if character:  # Ensure the character input is not empty
                context['filtered_names'] = [name for name in names_list if name.lower().startswith(character)]

    return render(request, 'index.html', context)
