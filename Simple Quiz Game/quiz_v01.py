import random
import time

def show_banner():
    print("""
           ╔══════════════════════════════════════════════╗
           ║                                              ║
           ║              🎯 PYTHON QUIZ GAME             ║
           ║                                              ║
           ║           🧠 TEST YOUR KNOWLEDGE!            ║
           ║                                              ║
           ╚══════════════════════════════════════════════╝
           """)
show_banner()
time.sleep(1)

user_name = input("Enter your Name➡: ")
print(f"🔥 Welcome, {user_name} !")
print("Let's begin your quiz!\n")
time.sleep(0.25)





print("🎯 SELECT DIFFICULTY\n")
print("1. 🟢 Easy")
print("2. 🟡 Medium")
print("3. 🔴 Hard")

user_choose = input("\nChoose your difficulty:")


    
easy_general = [
    {
        "question": "What is the capital of Australia?",
        "A": "Sydney",
        "B": "Melbourne",
        "C": "Canberra",
        "D": "Perth",
        "answer": "C"
        
    },

    {
        "question" : "Which is the largest ocean on Earth",
        "A": "Atlantic Ocean",
        "B": "Pacific Ocean",
        "C": "Indian Ocean",
        "D": "Artic Ocean",
        "answer":"B"
        
    },

    {
        "question" : "What is the currency of Japan?",
        "A": "Won",
        "B": "Youn",
        "C": "Yen",
        "D": "Ringgit",
        "answer":"C"

    },

    {
        "question" : "Which country is known as the “Land of the Rising Sun”?",
        "A": "China",
        "B": "Japan",
        "C": "South Korea",
        "D": "Thailand",
        "answer":"B"

    },

    {
        "question" : "Which is the largest planet in our Solar System?",
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Neptune",
        "answer":"C"

    },

]

easy_science = [
    
    {
        "question" : "Which subatomic particle determines the atomic number of an element?",
        "A" : "Neutron",
        "B" : "Electron",
        "C" : "Proton",
        "D" : "Photon",
        "answer" : "C"

    },

    {
        "question" : "Which vitamin is primarily produced in the skin in response to sunlight?",
        "A" : "Vitamin A",
        "B" : "Vitamin B12",
        "C" : "Vitamin C",
        "D" : "Vitamin D",
        "answer" : "D"
    },

    {
        "question" : "Which blood group is known as the universal red-cell donor?",
        "A" : "AB+",
        "B" : "O-",
        "C" : "A+",
        "D" : "B-",
        "answer" : "B"
    },

    {
        "question" : "What is the SI unit of force?",
        "A" : "Joule",
        "B" : "Pascal",
        "C" : "Newton",
        "D" : "Watt",
        "answer" : "C"
    },

    {
        "question" : "Which layer of Earth's atmosphere contains most of the ozone layer?",
        "A" : "Troposphere",
        "B" : "Stratosphere",
        "C" : "Mesosphere",
        "D" : "Thermosphere",
        "answer" : "B"
    }

]

easy_programming = [
    
    {
        "question" : "What will this Python expression return: 7 // 2?",
        "A" : "3",
        "B" : "3.5",
        "C" : "4",
        "D" : "1",
        "answer" : "A"

    },

    {
        "question" : "Which Python data type is immutable?",
        "A" : "List",
        "B" : "Dictionary",
        "C" : "Set",
        "D" : "Tuple",
        "answer" : "D"
    },

    {
        "question" : "What does input() return by default in Python?",
        "A" : "Integer",
        "B" : "String",
        "C" : "Boolean",
        "D" : "Float",
        "answer" : "B"
    },

    {
        "question" : "Which keyword immediately exits a loop?",
        "A" : "Skip",
        "B" : "Continue",
        "C" : "Break",
        "D" : "exit",
        "answer" : "C"
    },

    {
        "question" : "What is the result of bool(0) in Python?",
        "A" : "True",
        "B" : "False",
        "C" : "0",
        "D" : "None",
        "answer" : "B"
    }

]

easy_history = [
    {
        "question" : "Who was the first Prime Minister of independent India?",
        "A" : "Sardar Patel",
        "B" : "Jawaharlal Nehru",
        "C" : "Mahatma Gandhi",
        "D" : "Rajendra Prasad",
        "answer" : "B"
    },

    {
        "question" : "In which year did India gain independence?",
        "A" : "1945",
        "B" : "1946",
        "C" : "1947",
        "D" : "1950",
        "answer" : "C"
    },

    {
        "question" : "Who built the Taj Mahal?",
        "A" : "Akbar",
        "B" : "Shah Jahan",
        "C" : "Aurangzeb",
        "D" : "Humayun",
        "answer" : "B"
    },

    {
        "question" : "Who founded the Maurya Empire?",
        "A" : "Ashoka",
        "B" : "Chandragupta Maurya",
        "C" : "Bindusara",
        "D" : "Harsha",
        "answer" : "B"
    },

    {
        "question" : "Who is known as the Iron Man of India?",
        "A" : "Bhagat Singh",
        "B" : "Subhas Chandra Bose",
        "C" : "Sardar Vallabhbhai Patel",
        "D" : "Bal Gangadhar Tilak",
        "answer" : "C"
    }
]

easy_language = [
    {
        "question" : "Which word is a synonym of 'rapid'?",
        "A" : "Slow",
        "B" : "Quick",
        "C" : "Weak",
        "D" : "Late",
        "answer" : "B"
    },

    {
        "question" : "Which word is an antonym of 'ancient'?",
        "A" : "Old",
        "B" : "Historic",
        "C" : "Modern",
        "D" : "Traditional",
        "answer" : "C"
    },

    {
        "question" : "Which sentence is grammatically correct?",
        "A" : "She go to college.",
        "B" : "She going to college.",
        "C" : "She goes to college.",
        "D" : "She gone to college.",
        "answer" : "C"
    },

    {
        "question" : "What is the plural form of 'criterion'?",
        "A" : "Criterions",
        "B" : "Criteria",
        "C" : "Criteriones",
        "D" : "Criterias",
        "answer" : "B"
    },

    {
        "question" : "Which word is a noun?",
        "A" : "Beautiful",
        "B" : "Quickly",
        "C" : "Honesty",
        "D" : "Run",
        "answer" : "C"
    }
]

easy_math = [
    {
        "question" : "What is 15 × 8?",
        "A" : "100",
        "B" : "110",
        "C" : "120",
        "D" : "125",
        "answer" : "C"
    },

    {
        "question" : "What is the square root of 144?",
        "A" : "10",
        "B" : "11",
        "C" : "12",
        "D" : "14",
        "answer" : "C"
    },

    {
        "question" : "What is 25% of 200?",
        "A" : "25",
        "B" : "40",
        "C" : "50",
        "D" : "75",
        "answer" : "C"
    },

    {
        "question" : "If x + 7 = 15, what is x?",
        "A" : "6",
        "B" : "7",
        "C" : "8",
        "D" : "9",
        "answer" : "C"
    },

    {
        "question" : "What is the value of 2³ + 3²?",
        "A" : "13",
        "B" : "15",
        "C" : "17",
        "D" : "18",
        "answer" : "B"
    }
]


medium_general = [
    {
        "question" : "Which country is completely surrounded by South Africa?",
        "A" : "Eswatini",
        "B" : "Lesotho",
        "C" : "Botswana",
        "D" : "Namibia",
        "answer" : "B"
    },

    {
        "question" : "Which Indian state has the highest literacy rate according to the 2011 Census?",
        "A" : "Kerala",
        "B" : "Goa",
        "C" : "Tamil Nadu",
        "D" : "Himachal Pradesh",
        "answer" : "A"
    },

    {
        "question" : "Which strait connects the Persian Gulf with the Gulf of Oman?",
        "A" : "Strait of Malacca",
        "B" : "Strait of Hormuz",
        "C" : "Bab-el-Mandeb",
        "D" : "Bosporus",
        "answer" : "B"
    },

    {
        "question" : "Which country has the most time zones when overseas territories are included?",
        "A" : "Russia",
        "B" : "United States",
        "C" : "France",
        "D" : "China",
        "answer" : "C"
    },

    {
        "question" : "Where is the headquarters of the International Court of Justice?",
        "A" : "Geneva",
        "B" : "New York",
        "C" : "Vienna",
        "D" : "The Hague",
        "answer" : "D"
    }
]

medium_science = [
    {
        "question" : "If the velocity of an object doubles, its kinetic energy becomes:",
        "A" : "2 times",
        "B" : "3 times",
        "C" : "4 times",
        "D" : "8 times",
        "answer" : "C"
    },

    {
        "question" : "Which molecule carries genetic information from DNA to ribosomes for protein synthesis?",
        "A" : "tRNA",
        "B" : "mRNA",
        "C" : "rRNA",
        "D" : "ATP",
        "answer" : "B"
    },

    {
        "question" : "Why does the sky appear blue?",
        "A" : "Reflection",
        "B" : "Refraction",
        "C" : "Rayleigh scattering",
        "D" : "Total internal reflection",
        "answer" : "C"
    },

    {
        "question" : "An object moving in a circular path at constant speed is accelerating because:",
        "A" : "Its mass changes",
        "B" : "Its speed changes",
        "C" : "Its direction of velocity changes",
        "D" : "Its kinetic energy becomes zero",
        "answer" : "C"
    },

    {
        "question" : "Which organelle is primarily responsible for ATP production in eukaryotic cells?",
        "A" : "Golgi apparatus",
        "B" : "Lysosome",
        "C" : "Mitochondrion",
        "D" : "Endoplasmic reticulum",
        "answer" : "C"
    }
]

medium_programming = [
    {
        "question" : "What is the output of `7 // 2` in Python?",
        "A" : "2",
        "B" : "3",
        "C" : "3.5",
        "D" : "4",
        "answer" : "B"
    },

    {
        "question" : "What does `range(2, 10, 2)` produce?",
        "A" : "2, 4, 6, 8",
        "B" : "2, 4, 6, 8, 10",
        "C" : "1, 3, 5, 7, 9",
        "D" : "2, 3, 4, 5, 6, 7, 8, 9",
        "answer" : "A"
    },

    {
        "question" : "What is the output of `bool([])` in Python?",
        "A" : "True",
        "B" : "False",
        "C" : "None",
        "D" : "Error",
        "answer" : "B"
    },

    {
        "question" : "Which data structure follows the FIFO principle?",
        "A" : "Stack",
        "B" : "Queue",
        "C" : "Tree",
        "D" : "Graph",
        "answer" : "B"
    },

    {
        "question" : "What is the purpose of a `return` statement inside a function?",
        "A" : "Repeat the function",
        "B" : "Stop the entire program",
        "C" : "Send a value back to the caller",
        "D" : "Create a loop",
        "answer" : "C"
    }
]

medium_history = [
    {
        "question" : "The Battle of Plassey was fought in which year?",
        "A" : "1757",
        "B" : "1764",
        "C" : "1857",
        "D" : "1772",
        "answer" : "A"
    },

    {
        "question" : "Who introduced the Permanent Settlement in Bengal?",
        "A" : "Lord Wellesley",
        "B" : "Lord Cornwallis",
        "C" : "Lord Curzon",
        "D" : "Lord Dalhousie",
        "answer" : "B"
    },

    {
        "question" : "Who introduced the Doctrine of Lapse?",
        "A" : "Lord Dalhousie",
        "B" : "Lord Canning",
        "C" : "Lord Ripon",
        "D" : "Lord Curzon",
        "answer" : "A"
    },

    {
        "question" : "Who wrote the Arthashastra?",
        "A" : "Kalidasa",
        "B" : "Chanakya",
        "C" : "Banabhatta",
        "D" : "Tulsidas",
        "answer" : "B"
    },

    {
        "question" : "The Non-Cooperation Movement was withdrawn after which incident?",
        "A" : "Jallianwala Bagh",
        "B" : "Chauri Chaura",
        "C" : "Dandi March",
        "D" : "Kakori Incident",
        "answer" : "B"
    }
]

medium_language = [
    {
        "question" : "Which sentence uses the correct form of the verb?",
        "A" : "Neither of the boys are ready.",
        "B" : "Neither of the boys is ready.",
        "C" : "Neither of the boys were ready.",
        "D" : "Neither boys is ready.",
        "answer" : "B"
    },

    {
        "question" : "Choose the correctly spelled word.",
        "A" : "Accomodation",
        "B" : "Accommodation",
        "C" : "Acommodation",
        "D" : "Accommadation",
        "answer" : "B"
    },

    {
        "question" : "What is the meaning of 'ambiguous'?",
        "A" : "Very clear",
        "B" : "Having more than one possible meaning",
        "C" : "Extremely short",
        "D" : "Completely false",
        "answer" : "B"
    },

    {
        "question" : "Which sentence is in the passive voice?",
        "A" : "The student solved the problem.",
        "B" : "The problem was solved by the student.",
        "C" : "The student is solving the problem.",
        "D" : "The student will solve the problem.",
        "answer" : "B"
    },

    {
        "question" : "Which word is an adverb?",
        "A" : "Careful",
        "B" : "Carefully",
        "C" : "Carefulness",
        "D" : "Care",
        "answer" : "B"
    }
]

medium_math = [
    {
        "question" : "If 3x + 7 = 22, what is x?",
        "A" : "3",
        "B" : "5",
        "C" : "7",
        "D" : "9",
        "answer" : "B"
    },

    {
        "question" : "What is the probability of getting an even number when rolling a fair six-sided die?",
        "A" : "1/6",
        "B" : "1/3",
        "C" : "1/2",
        "D" : "2/3",
        "answer" : "C"
    },

    {
        "question" : "What is the LCM of 12 and 18?",
        "A" : "24",
        "B" : "30",
        "C" : "36",
        "D" : "48",
        "answer" : "C"
    },

    {
        "question" : "A ₹800 item is discounted by 15%. What is its selling price?",
        "A" : "₹660",
        "B" : "₹680",
        "C" : "₹700",
        "D" : "₹720",
        "answer" : "B"
    },

    {
        "question" : "If a triangle has angles 45° and 65°, what is the third angle?",
        "A" : "60°",
        "B" : "70°",
        "C" : "80°",
        "D" : "90°",
        "answer" : "B"
    }
]


hard_general = [
    {
        "question" : "Which two countries share the longest international land border?",
        "A" : "Russia and Kazakhstan",
        "B" : "United States and Canada",
        "C" : "China and Mongolia",
        "D" : "Argentina and Chile",
        "answer" : "B"
    },

    {
        "question" : "Which is the only sea in the world with no coastline?",
        "A" : "Sargasso Sea",
        "B" : "Arabian Sea",
        "C" : "Coral Sea",
        "D" : "Tasman Sea",
        "answer" : "A"
    },

    {
        "question" : "Which Indian river is known as the Dakshin Ganga?",
        "A" : "Krishna",
        "B" : "Kaveri",
        "C" : "Godavari",
        "D" : "Narmada",
        "answer" : "C"
    },

    {
        "question" : "Which country has territory in both Europe and Asia and is separated by the Bosporus Strait?",
        "A" : "Georgia",
        "B" : "Turkey",
        "C" : "Azerbaijan",
        "D" : "Armenia",
        "answer" : "B"
    },

    {
        "question" : "Which country does NOT have a permanent seat on the UN Security Council?",
        "A" : "France",
        "B" : "Germany",
        "C" : "China",
        "D" : "United Kingdom",
        "answer" : "B"
    }
]

hard_science = [
    {
        "question" : "According to special relativity, as an object's speed approaches the speed of light, its relativistic energy:",
        "A" : "Approaches zero",
        "B" : "Remains constant",
        "C" : "Increases without bound",
        "D" : "Becomes negative",
        "answer" : "C"
    },

    {
        "question" : "Which quantum number determines the shape of an atomic orbital?",
        "A" : "Principal quantum number",
        "B" : "Azimuthal quantum number",
        "C" : "Magnetic quantum number",
        "D" : "Spin quantum number",
        "answer" : "B"
    },

    {
        "question" : "In an ideal Carnot engine, efficiency depends primarily on:",
        "A" : "Working substance",
        "B" : "Engine size",
        "C" : "Temperatures of the hot and cold reservoirs",
        "D" : "Pressure of surroundings",
        "answer" : "C"
    },

    {
        "question" : "Which particle is its own antiparticle?",
        "A" : "Electron",
        "B" : "Proton",
        "C" : "Photon",
        "D" : "Neutron",
        "answer" : "C"
    },

    {
        "question" : "What happens to the wavelength of a photon when its frequency increases?",
        "A" : "It increases",
        "B" : "It decreases",
        "C" : "It remains unchanged",
        "D" : "It becomes zero",
        "answer" : "B"
    }
]

hard_programming = [
    {
        "question" : "What is the average-case time complexity of searching for a key in a Python dictionary?",
        "A" : "O(1)",
        "B" : "O(log n)",
        "C" : "O(n)",
        "D" : "O(n²)",
        "answer" : "A"
    },

    {
        "question" : "Which algorithm has average-case O(n log n) time complexity and is based on divide and conquer?",
        "A" : "Bubble Sort",
        "B" : "Selection Sort",
        "C" : "Merge Sort",
        "D" : "Linear Search",
        "answer" : "C"
    },

    {
        "question" : "What is the output of `x=[1,2,3]; y=x; y.append(4); print(x)`?",
        "A" : "[1, 2, 3]",
        "B" : "[1, 2, 3, 4]",
        "C" : "[4, 1, 2, 3]",
        "D" : "Error",
        "answer" : "B"
    },

    {
        "question" : "Which traversal of a binary search tree produces values in sorted order?",
        "A" : "Preorder",
        "B" : "Postorder",
        "C" : "Inorder",
        "D" : "Level-order",
        "answer" : "C"
    },

    {
        "question" : "What is the worst-case time complexity of binary search on a sorted array?",
        "A" : "O(1)",
        "B" : "O(log n)",
        "C" : "O(n)",
        "D" : "O(n log n)",
        "answer" : "B"
    }
]

hard_history = [
    {
        "question" : "Which Ashokan inscription describes the effects of the Kalinga War and Ashoka's later policy?",
        "A" : "Allahabad Pillar Inscription",
        "B" : "Rock Edict XIII",
        "C" : "Junagadh Inscription",
        "D" : "Hathigumpha Inscription",
        "answer" : "B"
    },

    {
        "question" : "Who is traditionally regarded as the founder of the Gupta dynasty?",
        "A" : "Chandragupta I",
        "B" : "Samudragupta",
        "C" : "Sri Gupta",
        "D" : "Chandragupta II",
        "answer" : "C"
    },

    {
        "question" : "Which treaty ended the First Anglo-Maratha War?",
        "A" : "Treaty of Bassein",
        "B" : "Treaty of Salbai",
        "C" : "Treaty of Allahabad",
        "D" : "Treaty of Purandar",
        "answer" : "B"
    },

    {
        "question" : "Which Mughal emperor systematized the Mansabdari system?",
        "A" : "Babur",
        "B" : "Humayun",
        "C" : "Akbar",
        "D" : "Aurangzeb",
        "answer" : "C"
    },

    {
        "question" : "Which event led directly to the British Crown taking control of India from the East India Company?",
        "A" : "Battle of Plassey",
        "B" : "Revolt of 1857",
        "C" : "Formation of INC",
        "D" : "Partition of Bengal",
        "answer" : "B"
    }
]

hard_language = [
    {
        "question" : "Which sentence correctly uses the subjunctive mood?",
        "A" : "I wish I was taller.",
        "B" : "I wish I were taller.",
        "C" : "I wish I am taller.",
        "D" : "I wish I be taller.",
        "answer" : "B"
    },

    {
        "question" : "Which word is closest in meaning to 'ubiquitous'?",
        "A" : "Rare",
        "B" : "Present everywhere",
        "C" : "Uncertain",
        "D" : "Temporary",
        "answer" : "B"
    },

    {
        "question" : "Which sentence contains a dangling modifier?",
        "A" : "Walking to college, the rain started.",
        "B" : "Walking to college, I saw the rain.",
        "C" : "I walked to college in the rain.",
        "D" : "The rain started while I walked to college.",
        "answer" : "A"
    },

    {
        "question" : "Which word is an example of a contronym?",
        "A" : "Happy",
        "B" : "Sanction",
        "C" : "Quick",
        "D" : "Bright",
        "answer" : "B"
    },

    {
        "question" : "Which sentence has correct subject-verb agreement?",
        "A" : "The list of items are on the table.",
        "B" : "The list of items is on the table.",
        "C" : "The list of items were on the table.",
        "D" : "The lists of item is on the table.",
        "answer" : "B"
    }
]

hard_math = [
    {
        "question" : "If x + 1/x = 5, what is x² + 1/x²?",
        "A" : "21",
        "B" : "23",
        "C" : "25",
        "D" : "27",
        "answer" : "B"
    },

    {
        "question" : "What is the remainder when 2¹⁰ is divided by 7?",
        "A" : "1",
        "B" : "2",
        "C" : "4",
        "D" : "6",
        "answer" : "C"
    },

    {
        "question" : "If the roots of x² − 7x + 10 = 0 are α and β, what is α² + β²?",
        "A" : "19",
        "B" : "29",
        "C" : "39",
        "D" : "49",
        "answer" : "B"
    },

    {
        "question" : "How many distinct arrangements can be made using all letters of the word 'LEVEL'?",
        "A" : "20",
        "B" : "30",
        "C" : "60",
        "D" : "120",
        "answer" : "B"
    },

    {
        "question" : "If log₂(x) = 5, what is x?",
        "A" : "10",
        "B" : "16",
        "C" : "25",
        "D" : "32",
        "answer" : "D"
    }
]


if user_choose == "1":
    difficulty = "Easy🟢"
    ques = easy_general 
elif user_choose == "2":
    difficulty = "Medium🟡"
    ques = medium_general
elif user_choose == "3":
    difficulty = "Hard🔴"
    ques = hard_general

print(f"\nDifficulty selected»» {difficulty} Mode!")
time.sleep(0.5)


print("\n\n📚 SELECT CATEGORY\n")
print("1. 🌍 General Knowledge")
print("2. 🔬 Science")
print("3. 💻 Programming")
print("4. 🏛️ History")
print("5. 🗣️ Language")
print("6. 🧮 Mathematics")

category = input("\nChoose your category: ")

if category == "1":
    Category = "🌍 General Knowledge"

    if user_choose == "1":
        ques = easy_general
    elif user_choose == "2":
        ques = medium_general
    elif user_choose == "3":
        ques = hard_general

elif category == "2":
    Category = "🔬 Science"

    if user_choose == "1":
        ques = easy_science
    elif user_choose == "2":
        ques = medium_science
    elif user_choose == "3":
        ques = hard_science

elif category == "3":
    Category = "💻 Programming"

    if user_choose == "1":
        ques = easy_programming
    elif user_choose == "2":
        ques = medium_programming
    elif user_choose == "3":
        ques = hard_programming

elif category == "4":
    Category = "🏛️ History"

    if user_choose == "1":
        ques = easy_history
    elif user_choose == "2":
        ques = medium_history
    elif user_choose == "3":
        ques = hard_history

elif category == "5":
    Category = "🗣️ Language"

    if user_choose == "1":
        ques = easy_language
    elif user_choose == "2":
        ques = medium_language
    elif user_choose == "3":
        ques = hard_language

elif category == "6":
    Category = "🧮 Mathematics"

    if user_choose == "1":
        ques = easy_math
    elif user_choose == "2":
        ques = medium_math
    elif user_choose == "3":
        ques = hard_math

print(f"\nCategory selected »» {Category}")
time.sleep(0.5)


score = 0
streak = 0
best_streak = 0


random.shuffle(ques)

for number,question in enumerate(ques, start=1):

    print(f"\n🧠 QUESTION {number}/{len(ques)}")
    print(question["question"])
    
    print(f"A) {question['A']}")
    print(f"B) {question['B']}")
    print(f"C) {question['C']}")
    print(f"D) {question['D']}")


    correct_answer = question["answer"]
    user_answer = input("\nYour answer (A/B/C/D): ").upper().strip()

    while user_answer not in ["A", "B", "C", "D"]:
        print("⚠️ Invalid choice! Please choose A, B, C, or D.")
        user_answer = input("Your answer (A/B/C/D): ").upper().strip()

    print(f"\nCorrect Answer » {correct_answer}")
    
    if user_answer == correct_answer :
        print("Correct✅!")
        score+=1
        streak+=1
        print(f"🔥 Streak: {streak}")
        time.sleep(0.25)


        if streak > best_streak:
          best_streak = streak

    else :
        print("Wrong❌!")
        streak = 0
        print(f"🔥 Streak: {streak}")
        time.sleep(0.25)


        quit_game = False
        while True:
    
         continue_game = input(
            "\nPress Enter to continue playing | Q to quit: ").lower().strip()

         if continue_game == "":
            # round_number += 1
            break
    
         elif continue_game == "q":
             print("\nExiting game... 🫡")
             quit_game = True
             break
    
         else:
            print("\nInvalid choice! Press Enter to continue or Q to quit.")
    
         if quit_game:
          break
    

print(f"\n🏆 Best Streak: {best_streak}")
print(f"🏆 Score: {score}")
time.sleep(1)



input("\nPress Enter to continue....")