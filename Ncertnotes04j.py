import telebot

API_TOKEN = '6370912820:AAGFw5oO5g933k7fz5fWQ9gWuw2GPOCPztU'
bot = telebot.TeleBot(API_TOKEN)

# Dummy data for subjects and chapters from class 9 NCERT
subjects = {
    "Mathematics": ["Number Systems", "Polynomials", "Coordinate Geometry", "Linear Equations in Two Variables",
                    "Introduction to Euclid's Geometry", "Lines and Angles", "Triangles", "Quadrilaterals",
                    "Areas of Parallelograms and Triangles", "Circles", "Constructions", "Heron's Formula"],
    "Science": ["Matter in Our Surroundings", "Is Matter Around Us Pure?", "Atoms and Molecules",
                "Structure of the Atom", "The Fundamental Unit of Life", "Tissues", "Diversity in Living Organisms",
                "Motion", "Force and Laws of Motion", "Gravitation", "Work and Energy", "Sound", "Why Do We Fall Ill?",
                "Natural Resources", "Improvement in Food Resources"],
    "History": ["The French Revolution", "Socialism in Europe and the Russian Revolution", "Nazism and the Rise of Hitler",
                "Forest Society and Colonialism", "Pastoralists in the Modern World", "Peasants and Farmers",
                "History and Sport: The Story of Cricket", "Clothing: A Social History", "India and the Contemporary World - I"],
    "Geography": ["India - Size and Location", "Physical Features of India", "Drainage", "Climate", "Natural Vegetation and Wildlife",
                  "Population", "India - People and Economy"],
    "English": ["Beehive", "Moments"],
    # Add more subjects and chapters here...
}

# Matter in Our Surroundings notes
matter_notes = """
Matter in Our Surroundings:

Introduction:
Matter is the substance that makes up everything around us. It exists in various forms, such as solids, liquids, and gases. The study of matter and its properties is an essential aspect of physics and chemistry. In this topic, we will explore the different states of matter, the properties they exhibit, and the changes they undergo under various conditions.

States of Matter:
Matter can exist in three primary states:

Solid: In the solid state, particles are tightly packed and have a fixed shape and volume. They vibrate around fixed positions. Examples include ice, wood, and metals.

Liquid: In the liquid state, particles are close together but have more freedom of movement than in solids. Liquids have a fixed volume but can take the shape of their container. Examples include water, oil, and milk.

Gas: In the gaseous state, particles are far apart and have high kinetic energy. Gases have neither a fixed shape nor a fixed volume. They expand to fill the entire available space. Examples include air, oxygen, and carbon dioxide.

Characteristics of States of Matter:
The states of matter exhibit various characteristics:

Density: It is the measure of mass per unit volume and varies for different states of matter. Solids have the highest density, followed by liquids and then gases.

Compressibility: The ability of matter to be compressed into a smaller volume. Gases are highly compressible, whereas liquids and solids are relatively incompressible.

Shape and Volume: Solids have a definite shape and volume, liquids have a definite volume but take the shape of the container, and gases have neither a definite shape nor a definite volume.

Changes of State:
Matter can undergo changes in its state under different conditions:

Melting: The change of a solid to a liquid at its melting point.

Freezing: The change of a liquid to a solid at its freezing point.

Evaporation: The change of a liquid to a gas at temperatures below its boiling point.

Boiling: The change of a liquid to a gas at its boiling point, with the formation of bubbles.

Condensation: The change of a gas to a liquid when it loses heat.

Sublimation: The change of a solid directly to a gas without passing through the liquid state.

Deposition: The change of a gas directly to a solid without passing through the liquid state.

Important Concepts:

Temperature and Pressure: The state of matter is influenced by temperature and pressure. An increase in temperature generally leads to a change from a solid to a liquid and then to a gas. An increase in pressure can also induce changes in states.

Kinetic Theory of Matter: This theory explains the behavior of matter based on the movement of particles. It states that particles in solids vibrate, particles in liquids move more freely, and particles in gases move randomly at high speeds.

Latent Heat: During changes of state, heat energy is absorbed or released without causing a change in temperature. The heat absorbed during melting and evaporation is called latent heat of fusion and latent heat of vaporization, respectively.

Humidity: It is the measure of the amount of water vapor present in the air.

Importance:
Understanding the properties and changes of states of matter is crucial in various aspects of daily life and scientific research. It helps in the design and operation of technologies, such as refrigeration, cooking, and industrial processes. It also forms the basis for the study of thermodynamics and the behavior of materials under different conditions.

In conclusion, the study of matter in our surroundings is fundamental to comprehend the nature of substances, their interactions, and the changes they undergo. Having a grasp of these concepts allows us to navigate the world around us and develop technologies that improve our quality of life.
"""

# Start command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Education Bot! Use /help to see the available commands.")

# Help command handler
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = "List of available commands:\n" \
                "/start - Start the bot\n" \
                "/help - Show this help message\n" \
                "/subject - Choose a subject\n" \
                "/chapter - Choose a chapter"
    bot.send_message(message.chat.id, help_text)

# Subject command handler
@bot.message_handler(commands=['subject'])
def subject(message):
    subject_list = list(subjects.keys())
    bot.send_message(message.chat.id, "Choose a subject:\n" + "\n".join(subject_list))

# Chapter command handler
@bot.message_handler(commands=['chapter'])
def chapter(message):
    subject = message.text.split()[-1]
    chapter_list = subjects.get(subject)
    if chapter_list:
        bot.send_message(message.chat.id, f"Choose a chapter for {subject}:\n" + "\n".join(chapter_list))
    else:
        bot.send_message(message.chat.id, "Invalid subject. Please choose a subject from /subject command.")

# Note command handler (for simplicity, let's assume it returns dummy notes)
@bot.message_handler(commands=['notes'])
def notes(message):
    subject = message.text.split()[1]
    chapter = message.text.split()[2]
    if subject and chapter:
        if subject == "Science" and chapter == "Matter in Our Surroundings":
            bot.send_message(message.chat.id, matter_notes)
        else:
            bot.send_message(message.chat.id, "Sorry, notes for this chapter are not available yet.")
    else:
        bot.send_message(message.chat.id, "Please choose a subject and chapter first using /subject and /chapter commands.")

# Main function to start the bot
def main():
    bot.polling()

if __name__ == '__main__':
    main()
