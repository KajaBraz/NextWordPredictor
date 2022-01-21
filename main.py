from src import next_word

if __name__=='__main__':
    sample_text = """Italy, officially the Italian Republic, is a country consisting of a peninsula delimited by the Alps and several islands surrounding it, whose territory largely coincides with the homonymous geographical region. Italy is located in the centre of the Mediterranean Sea, in Southern Europe; it is also considered part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city, the country covers a total area of 301,340 km2 (116,350 sq mi) and shares land borders with France, Switzerland, Austria, Slovenia, as well as the enclaved microstates of Vatican City and San Marino. Italy has a territorial exclave in Switzerland (Campione) and a maritime exclave in Tunisian waters (Lampedusa). With around 60 million inhabitants, Italy is the third-most populous member state of the European Union.
    Due to its central geographic location in Southern Europe and the Mediterranean, Italy has historically been home to myriad peoples and cultures. In addition to the various ancient peoples dispersed throughout what is now modern-day Italy, the most predominant being the Indo-European Italic peoples who gave the peninsula its name, beginning from the classical era, Phoenicians and Carthaginians founded colonies mostly in insular Italy, Greeks established settlements in the so-called Magna Graecia of Southern Italy, while Etruscans and Celts inhabited central and northern Italy respectively. An Italic tribe known as the Latins formed the Roman Kingdom in the 8th century BC, which eventually became a republic with a government of the Senate and the People. The Roman Republic initially conquered and assimilated its neighbours on the Italian peninsula, eventually expanding and conquering parts of Europe, North Africa and Asia. By the first century BC, the Roman Empire emerged as the dominant power in the Mediterranean Basin and became a leading cultural, political and religious centre, inaugurating the Pax Romana, a period of more than 200 years during which Italy's law, technology, economy, art, and literature developed.
    During the Early Middle Ages, Italy endured the fall of the Western Roman Empire and the Barbarian Invasions, but by the 11th century numerous rival city-states and maritime republics, mainly in the northern and central regions of Italy, became prosperous through trade, commerce, and banking, laying the groundwork for modern capitalism. These mostly independent statelets served as Europe's main trading hubs with Asia and the Near East, often enjoying a greater degree of democracy than the larger feudal monarchies that were consolidating throughout Europe; however, part of central Italy was under the control of the theocratic Papal States, while Southern Italy remained largely feudal until the 19th century, partially as a result of a succession of Byzantine, Arab, Norman, Angevin, Aragonese, and other foreign conquests of the region. The Renaissance began in Italy and spread to the rest of Europe, bringing a renewed interest in humanism, science, exploration, and art. Italian culture flourished, producing famous scholars, artists, and polymaths. During the Middle Ages, Italian explorers discovered new routes to the Far East and the New World, helping to usher in the European Age of Discovery. Nevertheless, Italy's commercial and political power significantly waned with the opening of trade routes that bypassed the Mediterranean. Centuries of foreign meddling and conquest, and the rivalry and infighting between the Italian city-states, such as the Italian Wars of the 15th and 16th centuries, left Italy politically fragmented, and it was further conquered and divided among multiple foreign European powers over the centuries."""
    # source: Wikipedia (https://en.wikipedia.org/wiki/Italy)

    next_word.predict_next_word(sample_text)
