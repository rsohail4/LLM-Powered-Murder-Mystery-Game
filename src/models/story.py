"""
Story models for the murder mystery game
"""

from pydantic import BaseModel, Field


class StoryDetails(BaseModel):
    victim_name: str = Field(description="Name of the murder victim")
    time_of_death: str = Field(description="Approximate time when the murder occurred")
    location_found: str = Field(description="Where the body was discovered")
    murder_weapon: str = Field(description="The weapon or method used in the murder")
    cause_of_death: str = Field(description="Specific medical cause of death")
    crime_scene_details: str = Field(
        description="Description of the crime scene and any relevant evidence found"
    )
    witnesses: str = Field(
        description="Information about potential witnesses or last known sightings"
    )
    initial_clues: str = Field(
        description="Initial clues or evidence found at the scene"
    )
    npc_brief: str = Field(
        description="Brief description of the characters and their relationships"
    )

    # Detailed explanation fields for end-game reveal
    killer_motive: str = Field(
        description="Detailed explanation of why the killer committed the murder"
    )
    murder_method_details: str = Field(
        description="Detailed explanation of how the murder was carried out"
    )
    key_evidence: str = Field(
        description="List of key evidence that points to the killer"
    )
    red_herrings_explanation: str = Field(
        description="Explanation of the misleading clues and why innocent characters appeared suspicious"
    )
    complete_timeline: str = Field(
        description="Complete timeline of events leading up to and including the murder"
    )
