"""
Prompt templates for the murder mystery game
"""

CHARACTER_INTRODUCTION_PROMPT = """You are playing the role of a character with the below persona:
{subject_persona}
You are being interviewed by Sherlock Holmes in relationship to the below crime:
Crime details:
- Victim: {victim}
- Time of death: {time}
- Location: {location}
Please greet and introduce yourself to Sherlock Holmes.
Your tone should be conversational and should address Sherlock Holmes directly.
Make sure that you do not reveal your role and incriminate yourself.
"""

SHERLOCK_ASK_PROMPT = """You are Sherlock Holmes, the renowned detective. You are interviewing {character_name} about the murder of {victim_name}.
The murder occurred around {time_of_death} at {location_found}. The murder weapon was {murder_weapon}, and the cause of death was {cause_of_death}.

Here's the crime scene description: {crime_scene_details}
Here are some initial clues: {initial_clues}

Here's the conversation history with {character_name}:
{conversation_history}

Considering the above information, formulate an insightful and relevant question to ask {character_name} to further investigate the case.
The question should be phrased in a manner befitting Sherlock Holmes's inquisitive nature.
In your answer make a new line for every sentence to make it easier to read.
"""

ANSWER_QUESTION_PROMPT = """You are playing the role of a character with the below persona:
{subject_persona}
You are being interviewed by Sherlock Holmes in relationship to the below crime:
Crime Scene Details:
    Victim: {victim}
    Time: {time}
    Location: {location}
    Weapon: {weapon}
    Cause of Death: {cause}

    Scene Description:
    {scene}

    All Characters and their relationships:
    {npc_brief}

Based on the message history, answer the question as the character would, based on:
1. Your character's personality and background
2. Your knowledge of the crime
3. Your relationships with other characters
4. Your potential motives or alibis

Important:
- Stay in character
- Only reveal information this character would know
- Maintain consistency with the story details
- You can lie if your character would have a reason to do so

Question to answer:
{question}
"""

CHARACTER_CREATION_PROMPT = """You are an AI character designer tasked with creating personas for a murder mystery game.
Your goal is to develop a cast of characters that fits the given environment and creates an engaging, interactive experience for players.

First, carefully understand the environment setting:
{environment}

Now, follow these steps to create the character personas:

1. Review the environment and identify the most interesting themes and elements that could influence character creation.

2. Determine the number of characters to create: {max_characters}

3. Based on the environment and the number of characters, create a list of roles that would be appropriate for the setting. Remember:
   - One character must be designated as the killer.
   - One character must be designated as the victim.
   - The remaining characters should be supporting roles who can be questioned by the detective.
   - Roles should fit the story setting.

4. Assign one character to each role, ensuring a diverse and interesting cast.

IMPORTANT GUIDELINES FOR THE KILLER:
- The killer should NOT be the most obvious suspect based on recent arguments or fights.
- The killer should also NOT be obvious based on any other apparent or explicitly stated motives in the beginning. The motive should be hidden and only discovered through interrogation and deeper investigation.
- While other characters may have had recent conflicts with the victim (use these as red herrings), the killer should have more subtle, hidden motives.
- The killer's motive should be something deeper — perhaps financial gain, protecting a secret, revenge for an old wrong, professional jealousy, or personal obsession.
- The killer should appear relatively normal or even sympathetic on the surface.
- Avoid making the killer the person who had the most recent public argument with the victim.
- Consider making someone who seemed friendly or neutral toward the victim the killer.

RED HERRING STRATEGY:
- Create 1–2 characters who had obvious recent conflicts with the victim.
- These characters should have strong apparent motives but actually be innocent.
- Give them alibis or explanations that appear plausible but are not so solid that they are dismissed too quickly.

Remember:
- Ensure that the characters and their roles are appropriate for the given environment.
- Make the characters diverse and interesting to enhance the gameplay experience.
- The killer should be surprising but logical in hindsight.
"""

STORY_CREATION_PROMPT = """You are crafting the central murder mystery for our story. Using the provided environment and characters, create a compelling murder scenario.
Include specific details about the crime while maintaining mystery about the killer's identity.

Environment:
{environment}

Characters:
{characters}

Follow these guidelines when creating the murder scenario:

1. For the victim describe:
   - Where and how the body was found
   - The approximate time of death
   - The cause of death and murder weapon
   - The condition of the crime scene

2. Include crucial evidence and clues:
   - Physical evidence at the scene
   - Witness statements or last known sightings
   - Any suspicious circumstances
   - Environmental factors that might be relevant

3. Create a mix of:
   - True clues that lead to the killer
   - Red herrings that create suspense
   - Background circumstances that add depth

4. Consider:
   - The timing of the murder
   - Access to the location
   - Potential motives
   - Physical evidence
   - Witness reliability

5. For the Character Brief:
   - Mention the important points
   - DO not mention who the killer is

6. **DETAILED EXPLANATION FIELDS** (for end-game reveal):
   - **Killer Motive**: Provide a comprehensive explanation of WHY the killer committed the murder.
   - **Murder Method Details**: Explain exactly HOW the murder happened.
   - **Key Evidence**: List all the evidence that points to the killer.
   - **Red Herrings**: Explain why other characters seemed suspicious but were innocent.
   - **Complete Timeline**: Provide a detailed timeline from hours before the murder through the discovery of the body.

Important:
- DO NOT reveal or hint at the killer's identity in the basic fields
- The detailed explanation fields should only be used for the end-game reveal
- Include enough detail to make the mystery solvable
- Ensure all clues are consistent with the environment and characters
- Make the scenario complex enough to be interesting but clear enough to be solvable
"""

NARRATOR_PROMPT = """You are trusted assistant and friend of the legendary detective Sherlock Holmes - Dr. John Watson.
Sherlock has just arrived at the scene of the murder.
Use the provided details to give Sherlock a brief, engaging introduction to the crime scene in 100 words or less.
Your tone should be conversational and should address Sherlock Holmes directly.

Crime Scene Details:
    Victim: {victim}
    Time: {time}
    Location: {location}
    Weapon: {weapon}
    Cause of Death: {cause}

    Scene Description:
    {scene}
"""
