from .db_manage import team_add, startup_add
import json


def add_new_team(json_data):
    json_data = json.loads(json_data)

    data = {
        "name": json_data['teamName'],
        "case": json_data['teamCase'],
        "solution": json_data['teamSolution'],
        "captain_name": json_data['captain']['captainName'],
        "captain_about": json_data['captain']['captainAbout'],
        "captain_email": json_data['captain']['captainEmail'],
        "captain_phone": json_data['captain']['captainPhone'],
        "member_name1": json_data['members']['memberName1'],
        "member_about1": json_data['members']['memberAbout1'],
        "member_email1": json_data['members']['memberEmail1'],
        "member_phone1": json_data['members']['memberPhone1'],
        "member_name2": json_data['members']['memberName2'],
        "member_about2": json_data['members']['memberAbout2'],
        "member_email2": json_data['members']['memberEmail2'],
        "member_phone2": json_data['members']['memberPhone2'],
        "member_name3": json_data['members']['memberName3'],
        "member_about3": json_data['members']['memberAbout3'],
        "member_email3": json_data['members']['memberEmail3'],
        "member_phone3": json_data['members']['memberPhone3']
    }

    team_add(data)


def add_new_startup(json_data):
    json_data = json.loads(json_data)

    data = {
        "name": json_data['teamName'],
        "site": json_data['teamSite'],
        "stage": json_data['teamStage'],
        "about": json_data['teamAbout'],
        "task_about": json_data['taskAbout'],
        "specs": json_data['teamSpecs'],
        "addition": json_data['teamAddition'],
        "presentation": json_data['teamPresentation'],
        "country": json_data['teamCountry'],
        "team_lead": json_data['teamLead'],
        "email": json_data['teamEmail'],
        "phone": json_data['teamPhone']
    }

    startup_add(data)
