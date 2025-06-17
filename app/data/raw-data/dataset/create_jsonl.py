import json

file = "processed-files/FINAL-BOWNCE_2025.jsonl"

prompts_with_aliases = {
    "Bownce_Definition": [
        "Was ist Bownce?",
        "Erkläre Bownce",
        "Erkläre mir Bownce",
        "Was genau ist Bownce?",
        "Kannst du Bownce erklären?",
        "Was bedeutet Bownce?",
        "Was ist bownce",
        "Was ist Bownc?",
        "Was ist Bownze?",
        "Was ist Bowncce?",
        "Was ist Bownc e?",
        "Was ist das Bownce?",
        "Sag mir was über Bownce",
        "Was ist eigendlich Bownce?",
        "Was ist eigentlcih Bownce?",
        "Was ist eigentlcih bownce?"
    ],
    "Bownce_Benefits": [
        "Wie wirkt sich Bownce gesundheitlich aus?",
        "Wie wirkt Bownce auf die Gesundheit?",
        "Welche gesundheitlichen Effekte hat Bownce?",
        "Was macht Bownce mit meinem Körper?",
        "Wie gesund ist Bownce?",
        "Ist Bownce gesund?",
        "Wie wirkt sich bownce gesundheitlich aus?",
        "Wie wirkt sich Bownc gesundheitlich aus?",
        "Wie wirkt sich Bownze gesundheitlich aus?",
        "Wie wirkt sich Bownce gesunheitlich aus?",
        "Wie wirkt sich Bownce gesundheitlcih aus?",
        "Wie wirkt sich Bownce gesundheitlich aus",
        "Was passiert gesundheitlich bei Bownce?",
        "Was bringt Bownce für die Gesundheit?",
        "Welche gesundheitlichen Vorteile hat Bownce?",
        "Wie wirkt sich Bownce auf die Gesundheit aus?"
    ],
    "Bownce_Applications": [
        "Was sind die Anwendungsgebiete von Bownce?",
        "Wofür kann man Bownce nutzen?",
        "Welche Einsatzmöglichkeiten hat Bownce?",
        "Für wen ist Bownce geeignet?",
        "Wer kann Bownce benutzen?",
        "Was kann man mit Bownce machen?",
        "Was sind die Anwendungsgebiete von bownce?",
        "Was sind die Anwendungsgebiete von Bownc?",
        "Was sind die Anwendungsgebiete von Bownze?",
        "Was sind die Anwendungsgebiete von Bowncce?",
        "Was sind die Anwendungsgebiete von Bownc e?",
        "Was sind die Anwendungsgebite von Bownce?",
        "Was sind die Anwendungsgebiete von Bownce",
        "Welche Anwendungsgebiete hat Bownce?",
        "Für welche Zwecke ist Bownce gedacht?",
        "Anwendungsgebiete Bownce?"
    ]
}
completions = {
    "Bownce_Definition": [
        "**Bownce ist kein normales Sportgerät**, sondern ein neues Lebenskonzept."
        "- Es hilft **Körper und Seele** gleichzeitig.\n"
        "- Man bewegt sich sanft, hat Spaß dabei und fühlt sich besser.\n"
        "- Es geht nicht um Leistung oder Aussehen, sondern darum, sich **wohlzufühlen** und gemeinsam mit anderen "
        "etwas für die eigene Gesundheit zu tun - **ohne Druck, ohne Stress**.\n"
        "- Auch Menschen mit Krankheiten können mitmachen, ohne Angst vor Risiken.\n"
        "- Bownce will, dass alle Menschen sich wieder **lebendig, stark und verbunden** fühlen.\n###",
    ],
    "Bownce_Benefits": [
        "#1. Kurzzeitige Benutzung - geringe Belastung (z. B. unter 2 Minuten)\n"
        "##Was passiert im Körper?\n"
        "- Dein Körper arbeitet kurzfristig intensiv - er braucht schnell Energie, Sauerstoff und muss Abfallstoffe loswerden.\n"
        "- Dafür atmet man tiefer, das Herz schlägt schneller, und die Muskeln nutzen ihre schnellen Energiereserven.\n"
        "- Muskeln werden kurzfristig stärker belastet, was zu ersten Anpassungen führen kann - wie mehr Muskelvolumen und besserer Energie-Nutzung.\n"
        "- Deine Gelenke (z. B. Knie) profitieren kurzfristig auch: Sie saugen sich mit Flüssigkeit voll - das dämpft Stöße besser.\n"
        "- Wichtig: Bei häufiger oder zu intensiver Nutzung kann es zu Überlastung kommen, z. B. bei Leuten mit Gelenkproblemen oder Osteoporose.\n"
        "- Fazit: Kurzzeitig bringt es schon erste kleine Effekte, vor allem fürs Herz-Kreislauf-System. Aber zu viel oder zu oft kann bei empfindlichen Menschen Risiken haben.\n"
        ""
        ""
        "#2. Mittlere Nutzungsdauer - mittlere Belastung (z. B. 5-10 Minuten regelmäßig)\n"
        "##Was passiert im Körper?\n"
        "- Die Muskeln gewöhnen sich langsam - sie speichern mehr Energie, bilden mehr kleine „Kraftwerke“ (Mitochondrien) und werden besser durchblutet.\n"
        "- Die Beweglichkeit der Gelenke bleibt erhalten oder wird besser. Ideal z. B. für Menschen mit Gelenkbeschwerden oder im höheren Alter.\n"
        "- Auch dein Kreislauf profitiert: Das Herz wird stärker, die Ausdauer steigt, der Puls sinkt langfristig in Ruhe.\n"
        "- Deine Atmung wird effizienter - du bekommst mehr Luft pro Atemzug, was beim Stressabbau helfen kann.\n"
        "- Der Körper lernt außerdem besser, Energie aus Sauerstoff zu nutzen, statt sich „schnell zu verausgaben“.\n"
        "- **Insgesamt**: Die mittlere Nutzung ist für fast alle sicher und empfehlenswert - gute Effekte ohne Überlastung.\n"
        "#3. Lange Benutzung - hohe Belastung (z. B. über 10 Minuten, oft und intensiv)\n"
        "##Was passiert im Körper?\n"
        "- Jetzt beginnt echtes Training: Der Körper baut vor allem schnelle, kräftige Muskelfasern auf (die für kurze, starke Bewegungen da sind).\n"
        "- Die Koordination verbessert sich, also wie gut Muskeln und Nerven zusammenarbeiten.\n"
        "- Du kannst mit der Zeit mehr Leistung bringen, Bewegungen gezielter und effizienter ausführen.\n"
        "- Auch hier steigt die Zahl der Mitochondrien weiter - dein Körper wird ausdauernder und leistungsfähiger.\n"
        "- Deine Knochen und Knorpel (z. B. in den Gelenken) werden stärker, weil sie regelmäßig belastet werden.\n"
        "- Herz und Lunge werden optimal trainiert - langfristig hast du eine bessere Kondition, einen ruhigeren Puls und mehr Atemvolumen.\n"
        "- **Wichtig**: Diese Stufe eignet sich für Menschen mit Trainingsziel oder fortgeschrittenem Fitnesslevel. Anfänger sollten sich langsam hocharbeiten.\n"
        ""
        ""
        "#Fazit\n"
        "Wenn du das Ganze nur gelegentlich ausprobierst, kannst du erste positive Effekte bemerken - allerdings "
        "solltest du vorsichtig sein, wenn du es zu oft machst. "
        "Die mittlere Anwendung ist für die meisten Menschen sicher und gesund, besonders wenn du sie regelmäßig einsetzt. "
        "Wenn du gezielt trainieren und echte Fortschritte machen willst, bringt die längere Nutzung viel, "
        "erfordert aber auch, dass du dich daran gewöhnst.\n"
        "Am besten ist es, wenn du regelmäßig eine mittlere Dauer wählst - das ist sicher, bringt spürbare Vorteile "
        "und tut deiner Gesundheit gut.\n###",
    ],
    "Bownce_Applications": [
        "**Bownce kann von fast allen genutzt werden**, weil es sehr individuell anpassbar ist. "
        "Das bedeutet, dass es für verschiedene Altersgruppen, Geschlechter und Lebenssituationen geeignet ist.\n"
        "Junge Erwachsene (**18-30 Jahre**) profitieren zum Beispiel besonders von der Unterstützung "
        "bei psychischem Wohlbefinden und Gruppenzugehörigkeit. "
        "Menschen im mittleren Alter (**31-55 Jahre**) können Bownce zur Vorbeugung von Stress, "
        "Burnout und körperlichen Beschwerden nutzen. Ältere Nutzer (**56+**) profitieren von der Verbesserung der Lebensqualität, "
        "kardiovaskulären Gesundheit und sozialem Austausch.\n"
        "Auch spezielle Gruppen wie Kinder, Senioren, Menschen mit körperlichen oder geistigen Einschränkungen, "
        "sowie sozial ausgegrenzte oder sprachlich benachteiligte Personen können Vorteile erfahren.\n"
        ""
        ""
        "**Bownce hilft zudem bei verschiedenen Krankheiten**, indem es Symptome von Herz-Kreislauf-Problemen, "
        "Atemwegserkrankungen, Stoffwechselstörungen und neurologischen Erkrankungen lindert. "
        "Stressbedingte psychische und dermatologische Beschwerden können reduziert werden, "
        "was auch psychische Erkrankungen wie Angststörungen oder Depressionen positiv beeinflusst.\n"
        ""
        ""
        "Langfristig kann Bownce die Lebensqualität verbessern, soziale Isolation verringern, "
        "den Substanzkonsum senken und zu mehr Zufriedenheit führen. Es unterstützt dabei, "
        "das Leben bewusster und positiver zu erleben, besonders in späteren Lebensphasen.\n"
        ""
        ""
        "Kurz gesagt: **Bownce eignet sich für alle, die ihre Gesundheit, ihr Wohlbefinden** "
        "**und ihre Lebensqualität verbessern möchten - von jungen Erwachsenen bis hin zu älteren Menschen** "
        "**und besonderen Gruppen.**\n###"
    ]
}

count = 0
with open(file, "w", encoding="utf-8") as f:
    for key, prompt_list in prompts_with_aliases.items():
        if key not in completions:
            print(f"No completion found for {key}, skipping...")
            continue
        completion = completions[key][0]

        for prompt in prompt_list:
            entry = {
                "messages": [
                    {"role": "system", "content": "Du bist ein hilfreicher Assistent, der Informationen über Bownce bereitstellt."},
                    {"role": "user", "content": f"{prompt}\n\n###\n\n"},
                    {"role": "assistant", "content": completion}
                ]
            }
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            count += 1
print(f"{count} JSON lines created successfully!")

def print_jsonl():
    with open(file, "r") as f:
        print(f"JSONL file content: {f.read()}")

# print_jsonl()
