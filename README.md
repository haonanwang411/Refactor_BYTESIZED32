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
