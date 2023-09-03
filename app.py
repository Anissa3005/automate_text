import pywhatkit
import os
from datetime import datetime
from secrets_ import PHONE_NUMBER

def get_var_value(filename="varstore.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

def send_message():
    if count > len(random_facts_india):
        return
    else:
        message = random_facts_india[count]


    pywhatkit.sendwhatmsg(PHONE_NUMBER, f"Random Fact {count}: {message}", hour, minute_delay, 35, True)


now = datetime.now()
hour: int = now.hour
minute_delay: int = now.minute + 2

varstore_path = os.path.join(os.path.dirname(__file__), "varstore.dat")
count: int = get_var_value(varstore_path)

message: str = ""

random_facts_india = [
    "",
    ""
    "The cow is considered sacred in the Hindu religion in India. They believe that each cow contain 330 millions gods and goddesses",
    "The official religion of India is Hinduism, whose followers are adept to meditation and chanting mantras (words chanted in honor of specific deities). And did you know that Hinduism is the oldest religion on the world?",
    "The Taj Mahal is actually a tomb. Commissioned in 1632 by Emperor Shah Jahan to built the  Taj Mahal in honor of his late wife, Mumtaz Mahal,. Taj Mahal is among the Seven Wonders of the World, and is a stunning symbol of love and architectural brillance",
    "India was the first country to mine diamonds. India was the source of diamonds were in the world from the 4th century BC for around 1000 years. The pure diamonds were found in the Krishna River Delta, located in Andhra Pradesh.",
    "As one of the oldest civilizations in the world, Indians gave the worlds a lot of important inventions and discoveries. You may don't know, but chess is one of them, the king Balhait ordered an Indian brahmin to design a game to promote the intelligence of people.",
    "India is the most vegetarian country in the world. But still, only about 40% of the population is vegetarian. Many Indians eat chicken and fish. The only truth here is that you won't find beef to eat in any restaurant, and at most you will find buffalo meat in a few places.",
    "Did you know that India is the second largest country in the world that speaks English? So it is! English is the main language spoken in the country, apart from the 400 languages and dialects we have mentioned before.",
    "Chenab Bridge is the highest rail bridge in the world. Not all of India's famous monuments are religious. The jaw-dropping bridge spanning the Chenab river in Jammu is 1,178 feet above the water.",
    "Rajasthan has a Temple of Rats. The animal wonders of India continue. Although rats might not be the first species you think of to worship, there is a temple in Rajasthan dedicated to rats."
]

send_message()





