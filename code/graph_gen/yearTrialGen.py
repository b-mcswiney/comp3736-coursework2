import matplotlib.pyplot as plt
from dataGen import get_year_list, get_5_american_years

year_names = get_year_list()
years = get_5_american_years()
gold_medals = years[0]
silver_medals = years[1]
bronze_medals = years[2]


# plt.plot(year_names, gold_medals, label="Gold")
# plt.plot(year_names, silver_medals, label="Silver")
# plt.plot(year_names, bronze_medals, label="Bronze")

# plt.xlabel("Game number")
# plt.ylabel("number of medals won")
# plt.legend()
# plt.title("B - Number of medals won per game for the USA")

# plt.savefig("assets/line-years-trial-2.png", bbox_inches="tight")

count = 0
while(count < 5):
    print("total: ", gold_medals[count] + silver_medals[count] + bronze_medals[count])
    count=count+1


plt.stackplot(year_names, gold_medals, silver_medals, bronze_medals,
               labels=["Gold", "Silver", "Bronze"])

plt.xlabel("Game name")
plt.ylabel("number of medals")
plt.legend()
plt.title("B - Number of medals won per game for the USA")

plt.savefig("assets/area-years-trial-2.png", bbox_inches="tight")
