import pywhatkit
from datetime import datetime
from secrets_ import PHONE_NUMBER

now = datetime.now()
hour: int = now.hour
minute_delay: int = now.minute + 2

count: int = 0

random_facts_india = [
    "The cow is considered sacred in the Hindu religion in India. They believe that each cow contain 330 millions gods and goddesses",
    "The official religion of India is Hinduism, whose followers are adept to meditation and chanting mantras (words chanted in honor of specific deities). And did you know that Hinduism is the oldest religion on the world?",
    "The Taj Mahal is actually a tomb. Commissioned in 1632 by Emperor Shah Jahan to built the  Taj Mahal in honor of his late wife, Mumtaz Mahal,. Taj Mahal is among the Seven Wonders of the World, and is a stunning symbol of love and architectural brillance",
    "India was the first country to mine diamonds. India was the source of diamonds were in the world from the 4th century BC for around 1000 years. The pure diamonds were found in the Krishna River Delta, located in Andhra Pradesh.",
    "As one of the oldest civilizations in the world, Indians gave the worlds a lot of important inventions and discoveries. You may don't know, but chess is one of them, the king Balhait ordered an Indian brahmin to design a game to promote the intelligence of people.",
    "India is the most vegetarian country in the world. But still, only about 40% of the population is vegetarian. Many Indians eat chicken and fish. The only truth here is that you won't find beef to eat in any restaurant, and at most you will find buffalo meat in a few places.",
    "Did you know that India is the second largest country in the world that speaks English? So it is! English is the main language spoken in the country, apart from the 400 languages and dialects we have mentioned before."
]





pywhatkit.sendwhatmsg(PHONE_NUMBER, "DIT IS EEN TEST voor mijn automated messaging python script 🐍", hour, minute_delay, 35, True, )
