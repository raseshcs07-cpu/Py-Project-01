"""
START
  ↓
main()
  ↓
play_game()
  ↓
Choose Difficulty
  ↓
Generate Secret Number
  ↓
Start Timer
  ↓
Show Hints
  ↓
Enter Guess
  ↓
Validate Input
  ↓
Check Duplicate
  ↓
Compare Guess
  ↓
 ┌───────────────┬───────────────┐
 ↓               ↓               ↓
Too High       Too Low         Correct
 ↓               ↓               ↓
Hint            Hint          Score + Time
 ↓               ↓               ↓
 └───────→ Try Again ←───────────┘
                ↓
        Attempts Finished?
          ↓           ↓
         YES          NO
          ↓           ↓
      Game Over     Try Again
          ↓
      Play Again?
       ↓       ↓
      YES      NO
       ↓        ↓
   New Game    END
"""