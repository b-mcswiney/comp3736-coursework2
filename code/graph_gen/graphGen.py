import matplotlib.pyplot as plt

def gen_line(x_labels, gold_medals, silver_medals, bronze_medals, graph_label, graph_numb):
    """Function to generate line graphs"""
    plt.plot(x_labels, gold_medals, label="Gold", color="#FFD700")
    plt.plot(x_labels, silver_medals, label="Silver", color="#C0C0C0")
    plt.plot(x_labels, bronze_medals, label="Bronze", color="#CD7F32")

    plt.xlabel("Country name")
    plt.ylabel("number of medals")
    plt.legend()
    plt.grid()
    plt.title(f"{graph_label}Number of medals won")

    plt.savefig(f"assets/line-max-trial-{graph_numb}.png", bbox_inches="tight")

def gen_area(x_labels, gold_medals, silver_medals, bronze_medals, graph_label, graph_numb):
    """Function to generate area graphs"""
    plt.stackplot(x_labels, gold_medals, silver_medals, bronze_medals, labels=["Gold", "Silver", "Bronze"])
    
    plt.xlabel("Country name")
    plt.ylabel("number of medals")
    
    plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
    
    plt.legend()
    plt.grid()
    plt.title("A - Number of medals won (random data generated)")
    
    plt.savefig("assets/area-max-trial-3.png", bbox_inches="tight")
