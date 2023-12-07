from graphGen import gen_line, gen_area

def generate_graphs():
    country_list = ["USA", "Great Britain", "Australia", "Japan", "Germany"]
    country_list_short = ["Great Britain", "Australia", "Japan", "Germany"]
    years_list = ["Year 1", "Year 2", "Year 3"]

    # x_labels, gold_medals, silver_medals, bronze_medals, graph_label, trial, graph_numb
    # Question 1 and 2
    gen_line(
        country_list,
        [45, 22, 8, 7, 16],
        [36, 16, 12, 8, 17],
        [34, 17, 10, 13, 14],
        "A - ",
        "max",
        1
    )
    gen_line(
        country_list,
        [43, 10, 5, 4, 11],
        [26, 8, 11, 8, 7],
        [32, 11, 10, 13, 8],
        "B - ",
        "max",
        2
    )

    # Question 3 and 4
    gen_area(
        country_list,
        [43, 18, 17, 16, 18],
        [22, 15, 14, 12, 19],
        [38, 10, 12, 18, 8],
        "A - ",
        "max",
        1
    )
    gen_area(
        country_list,
        [38, 16, 8, 7, 16],
        [27, 23, 13, 8, 11],
        [30, 18, 15, 12, 14],
        "B - ",
        "max",
        2
    )

    # Question 5 and 6
    gen_line(
        country_list,
        [42, 21, 8, 11, 11],
        [23, 16, 14, 14, 11],
        [32, 18, 15, 15, 14],
        "A - ",
        "max",
        3
    )
    gen_line(
        country_list,
        [39, 8, 3, 7, 9],
        [32, 4, 12, 6, 14],
        [32, 11, 6, 12, 8],
        "B - ",
        "max",
        4
    )

    # Question 7 and 8
    gen_area(
        country_list,
        [45, 20, 8, 7, 13],
        [31, 23, 14, 9, 15],
        [30, 18, 10, 10, 14],
        "A - ",
        "max",
        3
    )
    gen_area(
        country_list,
        [37, 16, 14, 7, 15],
        [22, 20, 15, 13, 13],
        [37, 7, 16, 19, 13],
        "B - ",
        "max",
        4
    )

    # Question 9
    gen_line(
        years_list,
        [38, 48, 46 -7],
        [33, 24, 22 - 4],
        [37, 36, 36 - 10 ],
        "B - ",
        "years",
        2
    )
    # Question 10
    gen_line(
        years_list,
        [32, 48 + 5, 45],
        [36, 24 + 10, 34],
        [44, 36 + 10, 31],
        "A - ",
        "years",
        1
    )

    # Question 11 and 12
    gen_area(
        years_list,
        [45, 41, 39],
        [29, 25, 25],
        [38, 35, 34],
        "A - ",
        "years",
        1
    )
    gen_area(
        years_list,
        [46, 36, 41],
        [29, 22, 30],
        [37, 35, 33],
        "B - ",
        "years",
        2
    )

    # Question 13
    gen_line(
        years_list,
        [32, 38, 35],
        [31, 39, 32],
        [33, 24, 34],
        "A - ",
        "years",
        3
    )
    gen_line(
        years_list,
        [44, 36, 31],
        [32, 38, 35],
        [36, 24, 34],
        "B - ",
        "years",
        4
    )

    # Question 14
    gen_area(
        years_list,
        [32, 38, 35],
        [31, 39, 32],
        [33, 24, 34],
        "A - ",
        "years",
        3
    )
    gen_area(
        years_list,
        [44, 36, 31],
        [32, 38, 35],
        [36, 24, 34],
        "B - ",
        "years",
        4
    )

    # Question 15 and 16
    gen_line(
        country_list_short,
        [16, 12, 7, 13],
        [14, 15, 11, 14],
        [12, 15, 13, 13],
        "",
        "country",
        1
    )
    gen_line(
        country_list_short,
        [14, 18, 7, 13],
        [17, 17, 8, 5],
        [7, 9, 8, 10],
        "",
        "country",
        2
    )

    # Question 17 and 18
    gen_area(
        country_list_short,
        [16, 12, 14, 18],
        [14, 15, 11, 14],
        [12, 15, 13, 13],
        "",
        "country",
        1
    )
    gen_area(
        country_list_short,
        [18, 19, 16, 20],
        [12, 28, 14, 19],
        [6, 13, 18, 8],
        "",
        "country",
        2
    )

    # Question 19
    gen_area(
        country_list,
        [39, 8, 3, 7, 9],
        [32, 4, 12, 6, 14],
        [32, 11, 6, 12, 8],
        "",
        "same",
        1
    )
    gen_line(
        country_list,
        [39, 8, 3, 7, 9],
        [32, 4, 12, 6, 14],
        [32, 11, 6, 12, 8],
        "",
        "same",
        1
    )

    # NOTE: Question 20 will compare pre-existing graphs


# gen_line(
#         country_list,
#         country_list,
#         [, , , , ],
#         [, , , , ],
#         [, , , , ],
#         "B - ",
#         "max",
        
#     )

generate_graphs()