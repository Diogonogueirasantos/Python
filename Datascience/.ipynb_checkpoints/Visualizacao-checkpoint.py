from matplotlib import pyplot as plt

'''anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(anos, pib, color='green', marker='o', linestyle='solid')
plt.title('Pib Nominal')
plt.xlabel('Anos')
plt.ylabel('Pib')
plt.show()'''


'''movies = ["AnnieHall", "Ben-Hur", "Casablanca", 'Gandhi', "West Side Story"]
oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), oscars)
plt.ylabel('Movies')
plt.xticks(range(len(movies)), movies)
plt.title("My Favorite Movies")
plt.show()'''

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")
plt.show()





