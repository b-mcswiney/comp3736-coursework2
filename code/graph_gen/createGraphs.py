from graphGen import gen_line, gen_area

def generate_graphs():
    country_list = ["USA", "Great Britain", "Australia", "Japan", "Germany"]
    country_list_short = ["Great Britain", "Australia", "Japan", "Germany"]
    years_list = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

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
        [30, 12, 10, 10, 14],
        "A - ",
        "max",
        3
    )
    gen_area(
        country_list,
        [37, 16, 14, 7, 15],
        [22, 20, 15, 13, 13],
        [37, 13, 16, 19, 13],
        "B - ",
        "max",
        4
    )

    # Question 9 and 10
    gen_line(
        years_list,
        [38, 48, 45, 46, 43],
        [33, 24, 34, 22, 30],
        [37, 36, 31, 36, 37],
        "B - ",
        "years",
        2
    )
    gen_line(
        years_list,
        [32, 48, 45, 46, 43],
        [36, 24, 34, 22, 30],
        [44, 36, 31, 36, 37],
        "A - ",
        "years",
        1
    )

    # Question 11 and 12
    gen_area(
        years_list,
        [45, 42, 45, 38, 38],
        [29, 25, 35, 24, 24],
        [38, 35, 34, 31, 33],
        "A - ",
        "years",
        1
    )
    gen_area(
        years_list,
        [46, 36, 41, 41, 37],
        [29, 22, 30, 24, 23],
        [37, 35, 33, 37, 38],
        "B - ",
        "years",
        2
    )

    # Question 13
    gen_line(
        years_list,
        [32, 38, 35, 36, 47],
        [31, 39, 32, 36, 37],
        [33, 24, 34, 22, 30],
        "A - ",
        "years",
        3
    )
    gen_line(
        years_list,
        [44, 36, 31, 36, 37],
        [32, 38, 35, 46, 43],
        [36, 24, 34, 22, 30],
        "B - ",
        "years",
        4
    )

    # Question 14
    gen_area(
        years_list,
        [32, 38, 35, 36, 47],
        [31, 39, 32, 36, 37],
        [33, 24, 34, 22, 30],
        "A - ",
        "years",
        3
    )
    gen_area(
        years_list,
        [44, 36, 31, 36, 37],
        [32, 38, 35, 46, 43],
        [36, 24, 34, 22, 30],
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
        [14, 8, 7, 13],
        [17, 8, 8, 5],
        [9, 10, 9, 10],
        "",
        "country",
        2
    )

    # Question 17 and 18
    gen_area(
        country_list_short,
        [16, 12, 7, 13],
        [14, 15, 11, 14],
        [12, 15, 13, 13],
        "",
        "country",
        1
    )
    gen_area(
        country_list_short,
        [18, 19, 16, 20],
        [12, 22, 14, 19],
        [10, 13, 18, 8],
        "",
        "country",
        2
    )

    # NOTE: Question 19 and 20 will compare pre-existing graphs


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