import os

stages = {
    "dev": "https://dev-gs.qa-playground.com/api/v1",
    "release": "https://release-gs.qa-playground.com/api/v1"
}

def get_stage():
    stage_key = os.getenv("STAGE")
    return stages[stage_key]

