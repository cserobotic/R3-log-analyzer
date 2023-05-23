# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
from loganalyzer.Parser import *
from loganalyzer.Game import *
from loganalyzer.Analyzer import *

for myargs in sys.argv[1:]:
    is_first_iteration=True
    TEAM_NAME=''

    df = pd.DataFrame(columns=["name",
                       "status",   
                       "ally_goals",   
                       "opp_goals",    
                       "possession",   
                       "pass_accuracy",    
                       "correct_pass", 
                       "wrong_pass",   
                       "on_target_shoot:"])
    win_cnt=0
    ctr = 1
    # print(sys.argv)
    for filename in os.listdir(myargs):

        # if(filename[-3:]=='.gz'):
        #     print('filename=',myargs+'/'+filename[:-7])
        #     gunzip(myargs+'/*.gz')
        #     parser = Parser(myargs+'/'+filename[:-7])
        # else:    
        if(not ('.rcg' in filename)):
            continue

        print('file number:', ctr)

        print('filename= ',myargs+'/'+filename[:-4])
        parser = Parser(myargs+'/'+filename[:-4])

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

        if( is_first_iteration and len(sys.argv)<=2):
            TEAM_NAME = team_l['name']

        if( len(sys.argv)>2 and team_r['name']==sys.argv[2] ):
            team_l,team_r = team_r,team_l

        elif( team_r['name']==TEAM_NAME ):
            team_l,team_r = team_r,team_l

        if( not is_first_iteration ):
            df = pd.concat([df, pd.DataFrame(team_l, index=[ctr])], axis=0)
            # print(df)
            ctr += 1

        if( is_first_iteration ):
            is_first_iteration = False
            df = pd.DataFrame([team_l])
            ctr += 1

        # count wins
        if( team_l['status']=='Winner' ):
            win_cnt += 1

        # print("True Pass:"+str(analyzer.pass_r))
        # print("Wrong Pass:"+str(analyzer.intercept_l))
        # print("Right Team :"+analyzer.game.right_team.name + "\n")
        # print("Game result :"+analyzer.status_r)
        # print("Goals :"+str(analyzer.game.right_goal))
        # print("Possession:"+str(analyzer.possession_r))
        # print("Pass Accuracy:"+str(analyzer.pass_accuracy_r))
        # print("on_target_shoot:"+str(analyzer.on_target_shoot_r))
        # print('\n')

        # print("True Pass:"+str(analyzer.pass_l))
        # print("Wrong Pass:"+str(analyzer.intercept_r))
        # print("Left Team :"+analyzer.game.left_team.name+"\n")
        # print("Game result :"+analyzer.status_l)
        # print("Goals :"+str(analyzer.game.left_goal))
        # print("Possession:"+str(analyzer.possession_l))
        print("Pass Accuracy:"+str(analyzer.pass_accuracy_l))
        correct_pass_avg    = df['correct_pass' ].mean()
        wrong_pass_avg      = df['wrong_pass'   ].mean()
        pass_accuracy_avg   = df['pass_accuracy'].mean()
        print('correct_pass_avg  = ', correct_pass_avg )
        print('wrong_pass_avg    = ', wrong_pass_avg   )
        print('pass_accuracy_avg = ', pass_accuracy_avg)
        # print("on_target_shoot:"+str(analyzer.on_target_shoot_l))

    print(df)
    print('#################################################')
    print('directory finished and the report is as follows: ')

    our_goals_avg       = df['ally_goals'   ].mean()
    opp_goals_avg       = df['opp_goals'    ].mean()
    possession_avg      = df['possession'   ].mean()
    correct_pass_avg    = df['correct_pass' ].mean()
    wrong_pass_avg      = df['wrong_pass'   ].mean()
    pass_accuracy_avg   = df['pass_accuracy'].mean()
    our_goals_std       = df['ally_goals'   ].std()
    opp_goals_std       = df['opp_goals'    ].std()
    possession_std      = df['possession'   ].std()
    correct_pass_std    = df['correct_pass' ].std()
    wrong_pass_std      = df['wrong_pass'   ].std()
    pass_accuracy_std   = df['pass_accuracy'].std()
    
    winrate = win_cnt/ctr

    print('our_goals_avg     = ', our_goals_avg    )
    print('opp_goals_avg     = ', opp_goals_avg    )
    print('possession_avg    = ', possession_avg   )
    print('correct_pass_avg  = ', correct_pass_avg )
    print('wrong_pass_avg    = ', wrong_pass_avg   )
    print('pass_accuracy_avg = ', pass_accuracy_avg)
    print('our_goals_std     = ', our_goals_std    )
    print('opp_goals_std     = ', opp_goals_std    )
    print('possession_std    = ', possession_std   )
    print('correct_pass_std  = ', correct_pass_std )
    print('wrong_pass_std    = ', wrong_pass_std   )
    print('pass_accuracy_std = ', pass_accuracy_std)
    print('winrate           = ', winrate)

    df.to_csv(myargs+'/summary.csv')

    
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
