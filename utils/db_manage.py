from .db import Teams, Startups, session


def team_add(data):
    s = session()
    rows = s.query(Teams).all()
    check = []

    for row in rows:
        check.append(row.name)
    print(data)
    print(check)
    if str(data["name"]) not in check:
        print(222)
        teams = Teams(
            name=data["name"],
            case=data["case"],
            solution=data["solution"],
            captain_name=data["captain_name"],
            captain_about=data["captain_about"],
            captain_email=data["captain_email"],
            captain_phone=data["captain_phone"],
            member_name1=data["member_name1"],
            member_about1=data["member_about1"],
            member_email1=data["member_email1"],
            member_phone1=data["member_phone1"],
            member_name2=data["member_name2"],
            member_about2=data["member_about2"],
            member_email2=data["member_email2"],
            member_phone2=data["member_phone2"],
            member_name3=data["member_name3"],
            member_about3=data["member_about3"],
            member_email3=data["member_email3"],
            member_phone3=data["member_phone3"],
        )
        print(data)
        print(teams)
        s.add(teams)
    s.commit()


def startup_add(data):
    s = session()
    rows = s.query(Startups).all()
    check = []

    for row in rows:
        check.append(row.name)

    if str(data["name"]) not in check:
        startups = Startups(
            name=data["name"],
            site=data["site"],
            stage=data["stage"],
            about=data["about"],
            task_about=data["task_about"],
            specs=data["specs"],
            addition=data["addition"],
            presentation=data["presentation"],
            country=data["country"],
            team_lead=data["team_lead"],
            email=data["email"],
            phone=data["phone"]
        )
        s.add(startups)
    s.commit()

