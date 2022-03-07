def execute(db, models):
    dept1 = models.Department(name="dept1")
    dept2 = models.Department(name="dept2")
    dept3 = models.Department(name="dept3")


    db.session.add(dept1)
    db.session.add(dept2)
    db.session.add(dept3)

    e1 = models.Employee(name="employee1", department_id=2)
    e2 = models.Employee(name="employee2", department_id=2)
    e3 = models.Employee(name="employee3", department_id=2)
    e4 = models.Employee(name="employee4", department_id=3)
    e5 = models.Employee(name="employee5", department_id=2)


    db.session.add(e1)
    db.session.add(e2)
    db.session.add(e3)
    db.session.add(e4)
    db.session.add(e5)

    d1 = models.Dependent(name="dependent1", employee_id=1)
    d2 = models.Dependent(name="dependent2", employee_id=1)

    db.session.add(d1)
    db.session.add(d2)

    db.session.commit()