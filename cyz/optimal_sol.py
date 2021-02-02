import gurobipy as grb
import numpy as np

capacity_list = [246,315,83,173,539,246,62,5]


def price_model(capacity):
    time_period = 14
    a = 88.4
    b = -0.009267
    theta = -0.005 
    model = grb.Model()
    F = model.addVars(time_period, lb=-100.0, vtype=grb.GRB.CONTINUOUS, name="Freight")
    b_F = model.addVars(time_period, lb=-100.0, vtype=grb.GRB.CONTINUOUS, name="b_Freight")
    exp_F = model.addVars(time_period, vtype=grb.GRB.CONTINUOUS, name="exp_b_Freight")

    model.addConstrs((b * F[i] - b_F[i] == 0 for i in range(time_period)), name="c1")

    for i in range(time_period):
        model.addGenConstrExp(b_F[i], exp_F[i])
    model.addConstr(grb.quicksum([a*exp_F[i] for i in range(time_period)]) = capacity, name="c2")
    # model.addConstr(grb.quicksum([a*exp_F[i] for i in range(time_period)]) >= 0.8*capacity, name="c2")

    model.setObjective(a*exp_F[0]*F[0] + grb.quicksum([a*exp_F[i]*F[i] + theta * F[i] * (F[i]-F[i-1]) for i in range(1,time_period)]), grb.GRB.MAXIMIZE)
    model.params.NonConvex = 2
    model.optimize()
    for v in model.getVars():
        print('%s %g' % (v.varName, v.x))
    # model.computeIIS()






def linear_price_model():
    time_period = 14
    theta = -0.01
    p1 = -0.00774
    p2 = 11.86
    capacity = 539
    model = grb.Model()
    F = model.addVars(time_period, lb=0.0, vtype=grb.GRB.CONTINUOUS, name="Freight")

    model.addConstrs((p1 * F[i] + p2 >= 0 for i in range(time_period)), name="c1")

    model.addConstr(grb.quicksum([p1 * F[i] + p2 for i in range(time_period)]) <= capacity, name="c2")

    model.addConstr(grb.quicksum([p1 * F[i] + p2 for i in range(time_period)]) >= 0.3*capacity, name="c3")

    model.setObjective(p1 * F[0]**2 + p2 * F[0] + grb.quicksum([p1 * F[i]**2 + p2 * F[i] + theta * F[i] * (F[i]-F[i-1]) for i in range(1,time_period)]), grb.GRB.MAXIMIZE)
    model.optimize()
    revenue = 0
    for v in model.getVars():
        print('%s %g' % (v.varName, v.x))
        revenue += p1 * v.x**2 + p2 * v.x
    return revenue


if __name__ =="__main__":
    # res = linear_price_model()
    # print(res)
    for cap in capacity_list[:1]:
        price_model(cap)