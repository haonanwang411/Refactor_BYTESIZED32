# Refactored_BYTESIZED32
Byte-sized text games for code generation tasks on virtual environments,and In this refactoring process, the aim was to optimize the code for a collection of 32 games with similar structures and mechanics. The key focus areas were modularity, readability, reusability, extensibility, and performance. Each game followed a common pattern with variations in game-specific rules, objects, and actions, which provided an excellent opportunity to abstract shared logic and create a reusable framework.
## Key Optimization Highlights

### 1. Modular Design
Before Refactoring:
Each game contained a large amount of duplicated code, including classes like `GameObject`, `Container`, and `TextGame`.
Game-specific logic was intertwined with shared logic, making it difficult to isolate reusable components.
After Refactoring:
 Shared Module (`GameBasic`): Abstracted common classes (`GameObject`, `Container`, `TextGame`, etc.) into a shared library, reducing redundancy.
Game-Specific Classes: Individual games inherit from `TextGame`, focusing only on game-specific logic such as tasks, objects, and scoring.
Benefits:
Code reuse across all games.
We simplified game-specific implementation.
Centralized management of core functionalities, reducing maintenance effort.

—
### 2. Streamlined Action Handling
Before Refactoring:
Actions like `look around`, `take`, `put`, and game-specific commands were handled using repetitive `if-elif` blocks, leading to bloated code.
After Refactoring:
Introduced a **dictionary-based `action_map`** to handle actions dynamically. Each action is mapped to a corresponding method or lambda function:
    ```python
    action_map = {
        "look around": self.rootObject.makeDescriptionStr,
        "inventory": self.actionInventory,
        "take": lambda: self.actionTake(action[1]),
        "put": lambda: self.actionPut(action[1], action[2]),
        "answer": lambda: self.actionAnswer(action[1])
    }
    ```
Benefits:
Eliminated redundant `if-elif` statements.
Easy to add or modify actions for individual games by updating the `action_map`.
Improved readability and reduced code complexity.

---

### 3. Recursive Logic Optimization
Before Refactoring:
Recursive operations, such as retrieving all contained objects or calculating masses, used explicit loops with redundant code.
After Refactoring:
Used **list comprehensions** and **combined recursive calls**:
    ```python
    def getAllContainedObjectsRecursive(self):
        return self.left.getAllContainedObjectsRecursive() + self.right.getAllContainedObjectsRecursive() + [self.left, self.right]
    ```

    ```python
    def get_mass(self, contains):
        return sum(obj.getProperty("weight") for obj in contains.contains)
    ```

Benefits:
Cleaner, more concise implementations.Improved efficiency and maintainability.

---

### 4. Enhanced Object Description
Before Refactoring:
Descriptions for containers and their contents relied on verbose string concatenations and nested loops.
After Refactoring:
Simplified descriptions with list comprehensions:
    ```python
    def makeOneSideDescription(contains):
        effectiveContents = [obj.makeDescriptionStr() for obj in contains.contains]
        if effectiveContents:
            return "contains " + ", ".join(effectiveContents[:-1]) + (
                ", and " if len(effectiveContents) > 1 else "") + effectiveContents[-1]
        return "is empty"
    ```

Benefits:
Reduced verbosity and improved readability.
Consistent and elegant handling of object descriptions across games.

---

### 5. Unified Game Logic
Before Refactoring:
Game-specific logic (e.g., tasks, scoring) was mixed into a single monolithic class, making it hard to isolate and extend.
After Refactoring:
Game Logic Isolation: Each game is implemented as a subclass of `TextGame`, with methods overridden for tasks, scoring, and object initialization.
    ```python
    class BalanceScaleWeighGame(TextGame):
        def getTaskDescription(self):
            return "Your task is to figure out the weight of the cube."
        def calculateScore(self):
            self.score = 1 if self.cube_weight == self.answer_mass else 0
            self.gameOver = True
            self.gameWon = self.score > 0
    ```

Benefits:
Clear separation of shared and game-specific responsibilities. Easier to implement new games with minimal duplication.



### 6. Extended Features
Before Refactoring:
Limited gameplay mechanics with predefined actions and rigid rules.
After Refactoring:
Added dynamic action generation based on game state:
Actions like `answer` (specific to certain games) can be dynamically included.
generatePossibleActions build action sets tailored to the game environment:
      ```python
      for i in range(1, self.max_mass + 1):
          self.addAction(f"answer {i}g", ["answer", i])
      ```
  - Expanded scoring and feedback logic, allowing for more interactive and engaging gameplay.

Benefits:
Increased flexibility to define unique game rules and mechanics.
Enhanced player experience with dynamic interactions.

—
### 7. Centralized Testing and Execution
Before Refactoring:
Each game had its own main loop, often with duplicate logic for handling input, generating actions, and updating states.
After Refactoring:
Unified the main game loop in the shared `TextGame` class.
Games are instantiated and executed using the same `main(game)` function.
Benefits:
Standardized game execution. Simplified testing across multiple games.

---
## Intro to main code
### 1.library-GameBasic.py
This code is a general-purpose text-based game engine framework designed to provide a foundation for creating text adventure games. Using abstract classes and object-oriented programming, the framework modularly implements game objects' fundamental behaviors and logic (e.g., items, containers, devices). Developers can extend the framework to build specific game scenarios and logic.
Modules and Functionalities
#### 1. GameObject (Base Game Object)
**Description**: GameObject is the abstract base class for all game objects, defining fundamental attributes and operational logic such as container relationships, movability, and recursive object management.\\
**Key Features:**
Dynamic property management, e.g., isMoveable (movable), temperature (temperature), etc.
Container relationship management, supporting object addition, removal, and recursive traversal.
Provides a mapping between object names and references, facilitating player interactions.
#### 2. Container (Container)
Description:
Inherits from GameObject and represents objects that can contain other items (e.g., drawers, boxes, tables).
Key Features:
Supports container opening and closing operations.
Implements logic for storing and retrieving items, including validating the target container's availability and state.
#### 3. Device (Device)
Description:
Inherits from GameObject and represents devices that can be activated or deactivated (e.g., lights, fans).
Key Features:
Provides operations for turning devices on (turnOn) and off (turnOff).
Supports an interface for interacting with other objects.
#### 4. Substance (Substance)
Description:
Defines substances with physical properties (e.g., melting point, boiling point) and dynamically adjusts their states (solid, liquid, or gas) based on temperature.
Key Features:
Automatically switches the substance's physical state based on its temperature.
Provides descriptive information about the current state.
#### 5. World (World)
Description:
Inherits from Container and represents the game scene or environment, serving as the root container for all game objects.
Key Features:
Manages all objects within the scene and their states.
Generates natural language descriptions of the current scene.
#### 6. Agent (Agent)
Description:
Represents the player’s in-game proxy, responsible for managing the player’s items (e.g., inventory).
Key Features:
Implements logic for managing player items.
Provides readable descriptions of player items.
#### 7. TextGame (Text Game Logic)
Description:
Provides a general game logic framework, including world initialization, action registration, score calculation, and player interaction.
Key Features:
Defines abstract methods like initializeWorld() and getTaskDescription() for specific game logic implementation.
Supports parsing and executing player actions, such as picking up and placing items.
Manages game states, including game over and victory conditions.






