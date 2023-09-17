# Vocabulary quiz

The Vocabulary Quiz Game is an interactive application that offers users the opportunity to enhance their vocabulary while enjoying an engaging gaming experience. The game is designed with a user-friendly graphical interface created using the Tkinter library in Python.

The program features three distinct game modes, each catering to different player preferences and skill levels:

In summary, the Vocabulary Quiz Game offers a versatile and entertaining platform for players to expand their vocabulary. With its multiple gameplay modes, it accommodates different preferences and skill levels, making it suitable for both learners and word enthusiasts. Whether you prefer the challenge of timed quizzes, the strategy of conserving lives, or a casual practice session, this game provides an engaging and educational experience for all.

## Game Modes

**1. Play with Lives:** In this mode, players have a limited number of lives. They are presented with word meanings or definitions and must choose the correct word from a list of options. Correct answers increase their score, while incorrect ones result in a loss of lives. The game continues until lives run out.

**2. Time Attack:** In Time Attack mode, players face the challenge of answering as many word meaning questions as possible within a fixed time limit. The clock is ticking, and players must think quickly to accumulate a high score before time runs out.

**3. Warmup:** Warmup mode is a practice mode without the pressure of lives or time limits. Players can familiarize themselves with word meanings and definitions in a stress-free environment, making it an ideal starting point for beginners.

# Files

### Quiz_advanced

_Terminal-Based Vocabulary Quiz Game:_

- **User Interface**: This version is entirely text-based and is played in a terminal or console.
- **Gameplay**: Users interact with the game through text inputs and outputs. They receive word meanings or definitions and input their answers by typing.
- **Features**: It includes the same gameplay modes (Play with Lives, Time Attack, Warmup) and vocabulary data as the GUI versions but without any graphical elements.
- **Usability**: Suited for users comfortable with command-line interfaces and text-based interactions.

### Quiz_advanced_with_GUI

_GUI Vocabulary Quiz Game (Non-OOP):_

- **User Interface**: This version provides a graphical user interface (GUI) created using the Tkinter library in Python.
- **Gameplay**: Users select their desired game mode via buttons and interact with the game through graphical elements such as buttons, labels, and entry fields.
- **Features**: It incorporates the same gameplay modes as the terminal version but offers a more visually appealing and user-friendly experience.
- **Usability**: Ideal for users who prefer a GUI-based interface and a more interactive gaming experience.

### Quiz_advanced_OOP

_GUI Vocabulary Quiz Game (OOP):_

- **User Interface**: Similar to the GUI version, this implementation features a GUI built with Tkinter.
- **Gameplay**: However, it follows an Object-Oriented Programming (OOP) approach, organizing the game's components into classes and objects for improved code structure and maintainability.
- **Features**: All gameplay modes and features from the GUI version are present, but the code is organized into classes and methods, enhancing code modularity and reusability.
- **Usability**: Suitable for users who appreciate well-structured, maintainable code and those interested in learning or applying OOP principles.

### Summary of Game Modes:

These three versions of the Vocabulary Quiz Game cater to different user preferences and technical backgrounds, offering a range of choices in how users can engage with and enjoy the game. Players can select the version that best suits their familiarity with terminal-based interfaces, their preference for graphical interaction, or their interest in exploring Object-Oriented Programming concepts in Python.

## Additional Info

The Vocabulary Quiz Game sources its word data from a CSV file, **"Vocabulary_list.csv,"** and stores it in a dictionary. This data provides the basis for the word meaning questions presented to players throughout the game.

As players engage with the game, their current status is displayed on the GUI. This includes information on the number of lives they have (in the case of the first mode), their score, and any messages or warnings presented via message boxes.
