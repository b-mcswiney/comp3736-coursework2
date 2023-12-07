from graphGen import gen_line, gen_area

def generate_graphs():
    country_list = ["USA", "Great Britain", "Australia", "Japan", "Germany"]

    # x_labels, gold_medals, silver_medals, bronze_medals, graph_label, graph_numb
    gen_line(
        country_list,
        [45, 22, 8, 7, 16],
        [36, 16, 12, 8, 17],
        [34, 17, 10, 13, 14],
        "A - ",
        1
    )

generate_graphs()