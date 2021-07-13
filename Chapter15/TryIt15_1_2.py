import matplotlib.pyplot as plt
def cubes_to5():
    x_values = range(1,5)
    y_values = [x**3 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_values,y_values,c='red')

    ax.set_title("Cube Values",fontsize = 24)
    ax.set_xlabel("Value",fontsize = 14)
    ax.set_ylabel("Cubes of Value",fontsize = 14)

    ax.tick_params(axis='both',which='major',labelsize = 14)


    plt.show() 
    
def cubes_to5000():
    x_values = range(1, 5000)
    y_values = [x**3 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c='blue')

    ax.set_title("Cube Values to 5000", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cubes of Value")

    ax.tick_params(axis='both', which='major', labelsize=14)

    plt.show()

cubes_to5000()