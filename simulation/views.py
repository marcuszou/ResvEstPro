# simulation/views.py
from django.shortcuts import render
import numpy as np

def simulate(request):
    if request.method == "POST":
        iterations = int(request.POST['iterations']) # number of darts to throw
        circle_radius = 1.0
        
        # Perform Monte Carlo simulation
        num_points_in_circle = 0
        for _ in range(iterations):
            x = np.random.uniform(-circle_radius, circle_radius) # x-coordinate of a random point within the square
            y = np.random.uniform(-circle_radius, circle_radius) # y-coordinate of a random point within the square
            if np.sqrt(x**2 + y**2) <= circle_radius:   # if this point is in the unit circle
                num_points_in_circle += 1  # increase the count of points that land inside the circle
        
        pi = 4 * num_points_in_circle / iterations # estimated value of pi using monte carlo simulation
        return render(request, 'simulation.html', {'pi': pi}) # return results in a response
    else:  # if request is GET method
        return render(request, 'form.html') # return the form for user input
    
def index_view(request):
    return render(request, 'form.html')
