import time
import random

# Countdown
for x in range(3, 0, -1):
    print(x)
    time.sleep(1)

print("Welcome to the 'Guess the Capital' Game!")
print("I will name a country, and you have to guess its capital.")


def guess_the_capital():

    countries_and_capitals = {
        "Afghanistan": "Kabul",
        "Albania": "Tirana",
        "Algeria": "Algiers",
        "Andorra": "Andorra la Vella",
        "Angola": "Luanda",
        "Antigua and Barbuda": "Saint John's",
        "Argentina": "Buenos Aires",
        "Armenia": "Yerevan",
        "Australia": "Canberra",
        "Austria": "Vienna",
        "Azerbaijan": "Baku",
        "Bahamas": "Nassau",
        "Bahrain": "Manama",
        "Bangladesh": "Dhaka",
        "Barbados": "Bridgetown",
        "Belarus": "Minsk",
        "Belgium": "Brussels",
        "Belize": "Belmopan",
        "Benin": "Porto-Novo",
        "Bhutan": "Thimphu",
        "Bolivia": "Sucre",
        "Bosnia and Herzegovina": "Sarajevo",
        "Botswana": "Gaborone",
        "Brazil": "Brasilia",
        "Brunei": "Bandar Seri Begawan",
        "Bulgaria": "Sofia",
        "Burkina Faso": "Ouagadougou",
        "Burundi": "Gitega",
        "Cabo Verde": "Praia",
        "Cambodia": "Phnom Penh",
        "Cameroon": "Yaoundé",
        "Canada": "Ottawa",
        "Central African Republic": "Bangui",
        "Chad": "N'Djamena",
        "Chile": "Santiago",
        "China": "Beijing",
        "Colombia": "Bogotá",
        "Comoros": "Moroni",
        "Congo (Congo-Brazzaville)": "Brazzaville",
        "Congo (Democratic Republic of the Congo)": "Kinshasa",
        "Costa Rica": "San José",
        "Croatia": "Zagreb",
        "Cuba": "Havana",
        "Cyprus": "Nicosia",
        "Czechia (Czech Republic)": "Prague",
        "Denmark": "Copenhagen",
        "Djibouti": "Djibouti",
        "Dominica": "Roseau",
        "Dominican Republic": "Santo Domingo",
        "Ecuador": "Quito",
        "Egypt": "Cairo",
        "El Salvador": "San Salvador",
        "Equatorial Guinea": "Malabo",
        "Eritrea": "Asmara",
        "Estonia": "Tallinn",
        "Eswatini": "Mbabane",
        "Ethiopia": "Addis Ababa",
        "Fiji": "Suva",
        "Finland": "Helsinki",
        "France": "Paris",
        "Gabon": "Libreville",
        "Gambia": "Banjul",
        "Georgia": "Tbilisi",
        "Germany": "Berlin",
        "Ghana": "Accra",
        "Greece": "Athens",
        "Grenada": "St. George's",
        "Guatemala": "Guatemala City",
        "Guinea": "Conakry",
        "Guinea-Bissau": "Bissau",
        "Guyana": "Georgetown",
        "Haiti": "Port-au-Prince",
        "Honduras": "Tegucigalpa",
        "Hungary": "Budapest",
        "Iceland": "Reykjavik",
        "India": "New Delhi",
        "Indonesia": "Jakarta",
        "Iran": "Tehran",
        "Iraq": "Baghdad",
        "Ireland": "Dublin",
        "Italy": "Rome",
        "Jamaica": "Kingston",
        "Japan": "Tokyo",
        "Jordan": "Amman",
        "Kazakhstan": "Astana",
        "Kenya": "Nairobi",
        "Kiribati": "Tarawa Atoll",
        "Korea (North)": "Pyongyang",
        "Korea (South)": "Seoul",
        "Kuwait": "Kuwait City",
        "Kyrgyzstan": "Bishkek",
        "Laos": "Vientiane",
        "Latvia": "Riga",
        "Lebanon": "Beirut",
        "Lesotho": "Maseru",
        "Liberia": "Monrovia",
        "Libya": "Tripoli",
        "Liechtenstein": "Vaduz",
        "Lithuania": "Vilnius",
        "Luxembourg": "Luxembourg City",
        "Madagascar": "Antananarivo",
        "Malawi": "Lilongwe",
        "Malaysia": "Kuala Lumpur",
        "Maldives": "Malé",
        "Mali": "Bamako",
        "Malta": "Valletta",
        "Marshall Islands": "Majuro",
        "Mauritania": "Nouakchott",
        "Mauritius": "Port Louis",
        "Mexico": "Mexico City",
        "Micronesia": "Palikir",
        "Moldova": "Chișinău",
        "Monaco": "Monaco",
        "Mongolia": "Ulaanbaatar",
        "Montenegro": "Podgorica",
        "Morocco": "Rabat",
        "Mozambique": "Maputo",
        "Myanmar ": "Naypyidaw",
        "Namibia": "Windhoek",
        "Nauru": "Yaren",
        "Nepal": "Kathmandu",
        "Netherlands": "Amsterdam",
        "New Zealand": "Wellington",
        "Nicaragua": "Managua",
        "Niger": "Niamey",
        "Nigeria": "Abuja",
        "North Macedonia (formerly Macedonia)": "Skopje",
        "Norway": "Oslo",
        "Oman": "Muscat",
        "Pakistan": "Islamabad",
        "Palau": "Ngerulmud",
        "Panama": "Panama City",
        "Papua New Guinea": "Port Moresby",
        "Paraguay": "Asunción",
        "Palestine": "Jerusalem",
        "Peru": "Lima",
        "Philippines": "Manila",
        "Poland": "Warsaw",
        "Portugal": "Lisbon",
        "Qatar": "Doha",
        "Romania": "Bucharest",
        "Russia": "Moscow",
        "Rwanda": "Kigali",
        "Saint Kitts and Nevis": "Basseterre",
        "Saint Lucia": "Castries",
        "Saint Vincent and the Grenadines": "Kingstown",
        "Samoa": "Apia",
        "San Marino": "San Marino",
        "Sao Tome and Principe": "São Tomé",
        "Saudi Arabia": "Riyadh",
        "Senegal": "Dakar",
        "Serbia": "Belgrade",
        "Seychelles": "Victoria",
        "Sierra Leone": "Freetown",
        "Singapore": "Singapore",
        "Slovakia": "Bratislava",
        "Slovenia": "Ljubljana",
        "Solomon Islands": "Honiara",
        "Somalia": "Mogadishu",
        "South Africa": "Pretoria",
        "South Sudan": "Juba",
        "Spain": "Madrid",
        "Sri Lanka": "Sri Jayawardenepura Kotte",
        "Sudan": "Khartoum",
        "Suriname": "Paramaribo",
        "Sweden": "Stockholm",
        "Switzerland": "Bern",
        "Syria": "Damascus",
        "Taiwan": "Taipei",
        "Tajikistan": "Dushanbe",
        "Tanzania": "Dodoma",
        "Thailand": "Bangkok",
        "Timor-Leste": "Dili",
        "Togo": "Lomé",
        "Tonga": "Nuku'alofa",
        "Trinidad and Tobago": "Port of Spain",
        "Tunisia": "Tunis",
        "Turkey": "Ankara",
        "Turkmenistan": "Ashgabat",
        "Tuvalu": "Funafuti",
        "Uganda": "Kampala",
        "Ukraine": "Kyiv",
        "United Arab Emirates": "Abu Dhabi",
        "United Kingdom": "London",
        "United States": "Washington D.C.",
        }



    countries = list(countries_and_capitals.keys())
    capitals = list(countries_and_capitals.values())
    score = 0

    rounds = int(input("How many rounds do you want to play? "))

    for _ in range(rounds):
        country = random.choice(countries)
        correct_capital = countries_and_capitals[country]

        # Generate three options (1 correct, 2 incorrect)
        options = random.sample(capitals, 3)

        # Ensure the correct capital is in the options
        if correct_capital not in options:
            options[random.randint(0, 2)] = correct_capital

        # Shuffle the options
        random.shuffle(options)

        # Display the question and options
        print(f"\nWhat is the capital of {country}?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        # Get the user's choice
        try:
            choice = int(input("Enter the number of your choice: "))
            if options[choice - 1].lower() == correct_capital.lower():
                print("Correct! 👍🏻")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_capital}.")
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")

    print(f"\nYou scored {score} points out of {rounds}.")
    restart = input("Do you want to play again? (yes/no): ").strip().lower()
    if restart == "yes":
        guess_the_capital()
    else:
        print("Thanks for playing! Goodbye!")


guess_the_capital()
