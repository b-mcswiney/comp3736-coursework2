import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def gen_line(x_labels, gold_medals, silver_medals, bronze_medals, graph_label, trial, graph_numb):
    """Function to generate line graphs"""
    plt.plot(x_labels, gold_medals, label="Gold", color="#FFD700")
    plt.plot(x_labels, silver_medals, label="Silver", color="#C0C0C0")
    plt.plot(x_labels, bronze_medals, label="Bronze", color="#CD7F32")

    plt.xlabel("Country name")
    plt.ylabel("number of medals")

    if trial == "years":
        plt.yticks([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

    elif trial == "country":
        plt.yticks([5, 10, 15, 20])

    plt.minorticks_on()
    plt.legend()
    plt.grid()
    if trial == "years":
        plt.title(f"{graph_label}Number of medals won per game in the USA")
    else:
        plt.title(f"{graph_label}Number of medals won")

    plt.savefig(f"assets/line-{trial}-trial-{graph_numb}.png", bbox_inches="tight")

    plt.clf()

def gen_area(x_labels, gold_medals, silver_medals, bronze_medals, graph_label, trial, graph_numb):
    """Function to generate area graphs"""
    plt.stackplot(x_labels, gold_medals, silver_medals, bronze_medals,
                  labels=["Gold", "Silver", "Bronze"], colors=["#FFD700", "#C0C0C0", "#CD7F32"])

    plt.xlabel("Country name")
    plt.ylabel("number of medals")

    plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

    plt.minorticks_on()

    plt.legend()
    plt.grid()
    if trial == "years":
        plt.title(f"{graph_label}Number of medals won per game in the USA")
    else:
        plt.title(f"{graph_label}Number of medals won")

    plt.savefig(f"assets/area-{trial}-trial-{graph_numb}.png", bbox_inches="tight")

    plt.clf()
