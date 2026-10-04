# with open("leaderboard.json", "r") as file:
#     leaderboard = json.load(file)

# leaderboard.append(player_result)

# with open("leaderboard.json", "w") as file:
#     json.dump(leaderboard, file, indent=4)



"""


                    ┌───────────────┐
                    │     START     │
                    └───────┬───────┘
                            ↓
                 ┌─────────────────────┐
                 │ Generate Game ID    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Display Welcome     │
                 │ Banner              │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Enter Player Name   │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Select Difficulty   │
                 │ Easy / Medium / Hard│
                 └──────────┬──────────┘
                            ↓
                   ┌────────────────┐
                   │ Valid Choice?  │
                   └───────┬────────┘
                       NO  │  YES
                    ┌──────┘    └────────┐
                    ↓                     ↓
          ┌─────────────────┐    ┌──────────────────┐
          │ Show Error &    │    │ Select Category  │
          │ Ask Again       │    └────────┬─────────┘
          └────────┬────────┘             ↓
                   └───────→ ┌────────────────┐
                             │ Valid Choice?   │
                             └───────┬────────┘
                                 NO  │  YES
                              ┌──────┘    └─────────┐
                              ↓                     ↓
                    ┌─────────────────┐   ┌──────────────────┐
                    │ Show Error &    │   │ Select Question  │
                    │ Ask Again       │   │ Bank             │
                    └────────┬────────┘   └────────┬─────────┘
                             └──────────────→       ↓
                                        ┌──────────────────┐
                                        │ Shuffle Questions│
                                        └────────┬─────────┘
                                                 ↓
                                        ┌──────────────────┐
                                        │ Display Question │
                                        │ + A/B/C/D        │
                                        └────────┬─────────┘
                                                 ↓
                                        ┌──────────────────┐
                                        │ Enter Answer     │
                                        │ A/B/C/D or Q     │
                                        └────────┬─────────┘
                                                 ↓
                                        ┌──────────────────┐
                                        │ Valid Input?     │
                                        └────────┬─────────┘
                                           NO   │   YES
                                        ┌───────┘    └──────────┐
                                        ↓                       ↓
                              ┌─────────────────┐       ┌──────────────┐
                              │ Show Error &    │       │ Q pressed?   │
                              │ Ask Again       │       └──────┬───────┘
                              └────────┬────────┘          YES │ NO
                                       └──────→                │
                                                               ↓
                                                      ┌─────────────────┐
                                                      │ Compare Answer  │
                                                      │ With Correct    │
                                                      └────────┬────────┘
                                                               ↓
                                                   ┌────────────────────┐
                                                   │ Correct Answer?    │
                                                   └────────┬───────────┘
                                                    YES     │      NO
                                             ┌──────────────┘      └──────────────┐
                                             ↓                                     ↓
                                  ┌──────────────────┐                  ┌──────────────────┐
                                  │ Add Points       │                  │ Wrong Answer     │
                                  │ Correct +1       │                  │ Show Correct Ans │
                                  │ Update Streak    │                  │ Reset Streak     │
                                  └─────────┬────────┘                  └─────────┬────────┘
                                            └──────────────┬──────────────────────┘
                                                           ↓
                                                  ┌─────────────────┐
                                                  │ More Questions? │
                                                  └────────┬────────┘
                                                   YES     │     NO
                                              ┌────────────┘      └──────────────┐
                                              ↓                                   ↓
                                    ┌──────────────────┐              ┌──────────────────┐
                                    │ Next Question    │              │ Calculate Score  │
                                    └────────┬─────────┘              │ & Percentage     │
                                             │                        └────────┬─────────┘
                                             └──────────────→                  ↓
                                                               ┌────────────────────────┐
                                                               │ Calculate Performance  │
                                                               │ Excellent / Good /     │
                                                               │ Average / Improvement  │
                                                               └───────────┬────────────┘
                                                                           ↓
                                                               ┌────────────────────────┐
                                                               │ Display Final          │
                                                               │ Scoreboard             │
                                                               └───────────┬────────────┘
                                                                           ↓
                                                               ┌────────────────────────┐
                                                               │ Save Result to         │
                                                               │ leaderboard.json       │
                                                               └───────────┬────────────┘
                                                                           ↓
                                                               ┌────────────────────────┐
                                                               │ Sort & Display         │
                                                               │ Top 5 Leaderboard      │
                                                               └───────────┬────────────┘
                                                                           ↓
                                                               ┌────────────────────────┐
                                                               │ Play Again?            │
                                                               │ Enter / Q              │
                                                               └───────────┬────────────┘
                                                                  ENTER    │    Q
                                                               ┌───────────┘    └───────┐
                                                               ↓                       ↓
                                                     ┌──────────────────┐       ┌────────────┐
                                                     │ Start New Game   │       │    END     │
                                                     │ New Game ID      │       └────────────┘
                                                     └────────┬─────────┘
                                                              │
                                                              └──────→ START
                                                              
"""