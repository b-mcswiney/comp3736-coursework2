import matplotlib.pyplot as plt
from dataGen import get_country_list, get_gold_medal_data, get_silver_medal_data, get_bronze_medal_data


country_names = get_country_list()
gold_medals = get_gold_medal_data()
silver_medals = get_silver_medal_data()
bronze_medals = get_bronze_medal_data()

# plt.plot(country_names, gold_medals, label="Gold")
# plt.plot(country_names, silver_medals, label="Silver")
# plt.plot(country_names, bronze_medals, label="Bronze")

# plt.xlabel("Country name")
# plt.ylabel("number of medals")
# plt.legend()
# plt.title("Number of medals won (random data generated)")

# plt.savefig("code/assets/line-max-trial-4.png", bbox_inches="tight")


plt.stackplot(country_names, gold_medals, silver_medals, bronze_medals, labels=["Gold", "Silver", "Bronze"])

plt.xlabel("Country name")
plt.ylabel("number of medals")
plt.legend()
plt.title("B - Number of medals won (random data generated)")

plt.savefig("code/assets/area-max-trial-4.png", bbox_inches="tight")
