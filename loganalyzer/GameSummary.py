# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
from loganalyzer.Parser import *
from loganalyzer.Game import *
from loganalyzer.Analyzer import *

flag=True
TEAM_NAME=''


df = pd.DataFrame()
win_cnt=0
ctr = 0
print(sys.argv)
for filename in os.listdir(sys.argv[1]):

    print(sys.argv[1]+filename[:-4])
    parser = Parser(sys.argv[1]+filename[:-4])
    game = Game(parser)
    analyzer = Analyzer(game)
    analyzer.analyze()

    team_r = {
        "name" : analyzer.game.right_team.name,
        "status" : analyzer.status_r,
        "ally_goals" : analyzer.game.right_goal,
        "opp_goals" : analyzer.game.left_goal,
        "possession" : analyzer.possession_r,
        "pass_accuracy" : analyzer.pass_accuracy_r,
        "correct_pass" : analyzer.pass_r,
        "wrong_pass" : analyzer.intercept_l,
        "on_target_shoot:" : analyzer.on_target_shoot_r
    }

    team_l = {
        "name" : analyzer.game.left_team.name,
        "status" : analyzer.status_l,
        "ally_goals" : analyzer.game.left_goal,
        "opp_goals" : analyzer.game.right_goal,
        "possession" : analyzer.possession_l,
        "pass_accuracy" : analyzer.pass_accuracy_l,
        "correct_pass" : analyzer.pass_l,
        "wrong_pass" : analyzer.intercept_r,
        "on_target_shoot" : analyzer.on_target_shoot_l
    }

    if( flag and len(sys.argv)<=2):
        TEAM_NAME = team_l['name']

    if( len(sys.argv)>2 and team_r['name']==sys.argv[2] ):
        team_l,team_r = team_r,team_l

    elif( team_r['name']==TEAM_NAME ):
        team_l,team_r = team_r,team_l

    if( not flag ):
        df.iloc[ctr] = pd.Series(team_l)
        ctr += 1

    if( flag ):
        flag = False
        df = pd.DataFrame([team_l])
        ctr += 1

    # count wins
    if( team_l['status']=='Winner' ):
        win_cnt += 1

    print("True Pass:"+str(analyzer.pass_r))
    print("Wrong Pass:"+str(analyzer.intercept_l))
    print("Right Team :"+analyzer.game.right_team.name + "\n")
    print("Game result :"+analyzer.status_r)
    print("Goals :"+str(analyzer.game.right_goal))
    print("Possession:"+str(analyzer.possession_r))
    print("Pass Accuracy:"+str(analyzer.pass_accuracy_r))
    print("on_target_shoot:"+str(analyzer.on_target_shoot_r))
    print('\n')

    print("True Pass:"+str(analyzer.pass_l))
    print("Wrong Pass:"+str(analyzer.intercept_r))
    print("Left Team :"+analyzer.game.left_team.name+"\n")
    print("Game result :"+analyzer.status_l)
    print("Goals :"+str(analyzer.game.left_goal))
    print("Possession:"+str(analyzer.possession_l))
    print("Pass Accuracy:"+str(analyzer.pass_accuracy_l))
    print("on_target_shoot:"+str(analyzer.on_target_shoot_l))

our_goals_avg  = df['ally_goals'].mean()
opp_goals_avg  = df['opp_goals' ].mean()
possession_avg = df['possession'].mean()
our_goals_var  = df['ally_goals'].var()
opp_goals_var  = df['opp_goals' ].var()
possession_var = df['possession'].var()
winrate = win_cnt/ctr

print('our_goals_avg  = ', our_goals_avg)
print('opp_goals_avg  = ', opp_goals_avg)
print('possession_avg = ', possession_avg)
print('our_goals_var  = ', our_goals_var)
print('opp_goals_var  = ', opp_goals_var)
print('possession_var = ', possession_var)
print('winrate        = ', winrate)

df.to_csv(sys.argv[1]+'\\summary.csv')

    
    # print("Pass in Lenght:"+str(analyzer.pass_in_length_r))
    # print("Pass in Width:"+str(analyzer.pass_in_width_r))
    
    # print("off_target_shoot:"+str(analyzer.off_target_shoot_r))
    # print("Shoot in Lenght:"+str(analyzer.shoot_in_length_r))
    # print("Shoot in Width:"+str(analyzer.shoot_in_width_r))
    # print("Shoot Accuracy:"+str(analyzer.shoot_accuracy_r))
    
    # print("Stamina Usage:"+str(analyzer.used_stamina_agents_r))
    # print("moved Distance:"+str(analyzer.team_moved_distance_r))
    # print("Average Distance 10 Player: "+str(analyzer.average_distance_10p_r))
    # print("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_r))
    # print("Average Stamina Per distance 10 Player: " +
    #       str(analyzer.av_st_per_dist_10p_r))
    # print("Stamina per Distance:"+str(analyzer.used_per_distance_r)+"\n"+"\n")


    # print("Wrong Pass:"+str(analyzer.intercept_r))
    # print("Pass in Lenght:"+str(analyzer.pass_in_length_l))
    # print("Pass in Width:"+str(analyzer.pass_in_width_l))
    
    # print("off_target_shoot:"+str(analyzer.off_target_shoot_l))
    # print("Shoot in Lenght:"+str(analyzer.shoot_in_length_l))
    # print("Shoot in Width:"+str(analyzer.shoot_in_width_l))
    # print("Shoot Accuracy:"+str(analyzer.shoot_accuracy_l))
    
    # print("Stamina Usage:"+str(analyzer.used_stamina_agents_l))
    # print("moved Distance:"+str(analyzer.team_moved_distance_l))
    # print("Average Distance 10 Player: "+str(analyzer.average_distance_10p_l))
    # print("Average Stamina 10 Player: "+str(analyzer.average_stamina_10p_l))
    # print("Average Stamina Per distance 10 Player: " +
    #       str(analyzer.av_st_per_dist_10p_l))
    # print("Stamina per Distance:"+str(analyzer.used_per_distance_l)+"\n")


    # for region in analyzer.regions:
    #     print("Ball in Region Percentage", region.name,
    #           " ", region.ball_in_region_cycles)

    # print("\nRight Team Regions Data")

    # Agent_regions
    # owner_cycles    : cycles player is ball owner in the region
    # position_cycles : cycles player is in the region
    # for agent in game.right_team.agents:
    #     for region in agent.regions:
    #         print(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: " +
    #               str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles))

    # print("\nLeft Team Regions Data")
    # for agent in game.left_team.agents:
    #     for region in agent.regions:
    #         print(region.name+" "+"Agent number "+str(agent.number)+" owner_cycles: " +
    #               str(region.owner_cycles) + "  " + "position_cycles: "+str(region.position_cycles))

    # Drawing Heatmap of the game
    # heatmap = analyzer.draw_heatmap(right_team=True, left_team=True)
