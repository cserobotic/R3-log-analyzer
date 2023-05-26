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

    df = pd.DataFrame(columns=
                       ["name,"
                        "status",
                        "our_goals",
                        "opp_goals",
                        "possession",
                        "pass_accuracy",
                        "correct_pass",
                        "wrong_pass",
                        "pass_in_length",
                        "pass_in_width",
                        "on_target_shoot",
                        "off_target_shoot",
                        "shoot_in_length",
                        "shoot_in_width",
                        "shoot_accuracy",
                        "used_stamina_1",
                        "used_stamina_2",
                        "used_stamina_3",
                        "used_stamina_4",
                        "used_stamina_5",
                        "used_stamina_6",
                        "used_stamina_7",
                        "used_stamina_8",
                        "used_stamina_9",
                        "used_stamina_10",
                        "used_stamina_11",
                        "moved_distance_1",
                        "moved_distance_2",
                        "moved_distance_3",
                        "moved_distance_4",
                        "moved_distance_5",
                        "moved_distance_6",
                        "moved_distance_7",
                        "moved_distance_8",
                        "moved_distance_9",
                        "moved_distance_10",
                        "moved_distance_11",
                        "average_distance_10p",
                        "average_stamina_10p",
                        "av_st_per_dist_10p",
                        "used_per_distance_1",
                        "used_per_distance_2",
                        "used_per_distance_3",
                        "used_per_distance_4",
                        "used_per_distance_5",
                        "used_per_distance_6",
                        "used_per_distance_7",
                        "used_per_distance_8",
                        "used_per_distance_9",
                        "used_per_distance_10",
                        "used_per_distance_11"])
                          
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
            "name"                  : analyzer.game.right_team.name,
            "status"                : analyzer.status_r,
            "our_goals"             : analyzer.game.right_goal,
            "opp_goals"             : analyzer.game.left_goal,
            "possession"            : analyzer.possession_r,
            "pass_accuracy"         : analyzer.pass_accuracy_r,
            "correct_pass"          : analyzer.pass_r,
            "wrong_pass"            : analyzer.intercept_l,
            "pass_in_length"        : analyzer.pass_in_length_r,
            "pass_in_width"         : analyzer.pass_in_width_r,
            "on_target_shoot"       : analyzer.on_target_shoot_r,
            "off_target_shoot"      : analyzer.off_target_shoot_r,
            "shoot_in_length"       : analyzer.shoot_in_length_r,
            "shoot_in_width"        : analyzer.shoot_in_width_r,
            "shoot_accuracy"        : analyzer.shoot_accuracy_r,
            "used_stamina_1"        : analyzer.used_stamina_agents_r[0][0],
            "used_stamina_2"        : analyzer.used_stamina_agents_r[1][0],
            "used_stamina_3"        : analyzer.used_stamina_agents_r[2][0],
            "used_stamina_4"        : analyzer.used_stamina_agents_r[3][0],
            "used_stamina_5"        : analyzer.used_stamina_agents_r[4][0],
            "used_stamina_6"        : analyzer.used_stamina_agents_r[5][0],
            "used_stamina_7"        : analyzer.used_stamina_agents_r[6][0],
            "used_stamina_8"        : analyzer.used_stamina_agents_r[7][0],
            "used_stamina_9"        : analyzer.used_stamina_agents_r[8][0],
            "used_stamina_10"       : analyzer.used_stamina_agents_r[9][0],
            "used_stamina_11"       : analyzer.used_stamina_agents_r[10][0],
            "moved_distance_1"      : analyzer.team_moved_distance_r[0][0],
            "moved_distance_2"      : analyzer.team_moved_distance_r[1][0],
            "moved_distance_3"      : analyzer.team_moved_distance_r[2][0],
            "moved_distance_4"      : analyzer.team_moved_distance_r[3][0],
            "moved_distance_5"      : analyzer.team_moved_distance_r[4][0],
            "moved_distance_6"      : analyzer.team_moved_distance_r[5][0],
            "moved_distance_7"      : analyzer.team_moved_distance_r[6][0],
            "moved_distance_8"      : analyzer.team_moved_distance_r[7][0],
            "moved_distance_9"      : analyzer.team_moved_distance_r[8][0],
            "moved_distance_10"     : analyzer.team_moved_distance_r[9][0],
            "moved_distance_11"     : analyzer.team_moved_distance_r[10][0],
            "average_distance_10p"  : analyzer.average_distance_10p_r,
            "average_stamina_10p"   : analyzer.average_stamina_10p_r,
            "av_st_per_dist_10p"    : analyzer.av_st_per_dist_10p_r,
            "used_per_distance_1"   : analyzer.used_per_distance_r[0][0],
            "used_per_distance_2"   : analyzer.used_per_distance_r[1][0],
            "used_per_distance_3"   : analyzer.used_per_distance_r[2][0],
            "used_per_distance_4"   : analyzer.used_per_distance_r[3][0],
            "used_per_distance_5"   : analyzer.used_per_distance_r[4][0],
            "used_per_distance_6"   : analyzer.used_per_distance_r[5][0],
            "used_per_distance_7"   : analyzer.used_per_distance_r[6][0],
            "used_per_distance_8"   : analyzer.used_per_distance_r[7][0],
            "used_per_distance_9"   : analyzer.used_per_distance_r[8][0],
            "used_per_distance_10"  : analyzer.used_per_distance_r[9][0],
            "used_per_distance_11"  : analyzer.used_per_distance_r[10][0]
        }

        team_l = {
            "name"                  : analyzer.game.left_team.name,
            "status"                : analyzer.status_l,
            "our_goals"             : analyzer.game.left_goal,
            "opp_goals"             : analyzer.game.right_goal,
            "possession"            : analyzer.possession_l,
            "pass_accuracy"         : analyzer.pass_accuracy_l,
            "correct_pass"          : analyzer.pass_l,
            "wrong_pass"            : analyzer.intercept_r,
            "pass_in_length"        : analyzer.pass_in_length_l,
            "pass_in_width"         : analyzer.pass_in_width_l,
            "on_target_shoot"       : analyzer.on_target_shoot_l,
            "off_target_shoot"      : analyzer.off_target_shoot_l,
            "shoot_in_length"       : analyzer.shoot_in_length_l,
            "shoot_in_width"        : analyzer.shoot_in_width_l,
            "shoot_accuracy"        : analyzer.shoot_accuracy_l,
            "used_stamina_1"        : analyzer.used_stamina_agents_l[0][0],
            "used_stamina_2"        : analyzer.used_stamina_agents_l[1][0],
            "used_stamina_3"        : analyzer.used_stamina_agents_l[2][0],
            "used_stamina_4"        : analyzer.used_stamina_agents_l[3][0],
            "used_stamina_5"        : analyzer.used_stamina_agents_l[4][0],
            "used_stamina_6"        : analyzer.used_stamina_agents_l[5][0],
            "used_stamina_7"        : analyzer.used_stamina_agents_l[6][0],
            "used_stamina_8"        : analyzer.used_stamina_agents_l[7][0],
            "used_stamina_9"        : analyzer.used_stamina_agents_l[8][0],
            "used_stamina_10"       : analyzer.used_stamina_agents_l[9][0],
            "used_stamina_11"       : analyzer.used_stamina_agents_l[10][0],
            "moved_distance_1"      : analyzer.team_moved_distance_l[0][0],
            "moved_distance_2"      : analyzer.team_moved_distance_l[1][0],
            "moved_distance_3"      : analyzer.team_moved_distance_l[2][0],
            "moved_distance_4"      : analyzer.team_moved_distance_l[3][0],
            "moved_distance_5"      : analyzer.team_moved_distance_l[4][0],
            "moved_distance_6"      : analyzer.team_moved_distance_l[5][0],
            "moved_distance_7"      : analyzer.team_moved_distance_l[6][0],
            "moved_distance_8"      : analyzer.team_moved_distance_l[7][0],
            "moved_distance_9"      : analyzer.team_moved_distance_l[8][0],
            "moved_distance_10"     : analyzer.team_moved_distance_l[9][0],
            "moved_distance_11"     : analyzer.team_moved_distance_l[10][0],
            "average_distance_10p"  : analyzer.average_distance_10p_l,
            "average_stamina_10p"   : analyzer.average_stamina_10p_l,
            "av_st_per_dist_10p"    : analyzer.av_st_per_dist_10p_l,
            "used_per_distance_1"   : analyzer.used_per_distance_r[0][0],
            "used_per_distance_2"   : analyzer.used_per_distance_r[1][0],
            "used_per_distance_3"   : analyzer.used_per_distance_r[2][0],
            "used_per_distance_4"   : analyzer.used_per_distance_r[3][0],
            "used_per_distance_5"   : analyzer.used_per_distance_r[4][0],
            "used_per_distance_6"   : analyzer.used_per_distance_r[5][0],
            "used_per_distance_7"   : analyzer.used_per_distance_r[6][0],
            "used_per_distance_8"   : analyzer.used_per_distance_r[7][0],
            "used_per_distance_9"   : analyzer.used_per_distance_r[8][0],
            "used_per_distance_10"  : analyzer.used_per_distance_r[9][0],
            "used_per_distance_11"  : analyzer.used_per_distance_r[10][0]
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

        print("Right Team : "                               +analyzer.game.right_team.name + "\n")
        print("Game result: "                               +analyzer.status_r)
        print("Goals : "                                    +str(analyzer.game.right_goal))
        print("Possession: "                                +str(analyzer.possession_r))
        print("True Pass: "                                 +str(analyzer.pass_r))
        print("Wrong Pass: "                                +str(analyzer.intercept_l))
        print("Pass Accuracy: "                             +str(analyzer.pass_accuracy_r))
        print("Pass in Lenght: "                            +str(analyzer.pass_in_length_r))
        print("Pass in Width: "                             +str(analyzer.pass_in_width_r))
        print("On Target Shoot: "                           +str(analyzer.on_target_shoot_r))
        print("Off Target Shoot: "                          +str(analyzer.off_target_shoot_r))
        print("Shoot in Lenght: "                           +str(analyzer.shoot_in_length_r))
        print("Shoot in Width: "                            +str(analyzer.shoot_in_width_r))
        print("Shoot Accuracy: "                            +str(analyzer.shoot_accuracy_r))
        print("Stamina Usage: "                             +str(analyzer.used_stamina_agents_r))
        print("moved Distance: "                            +str(analyzer.team_moved_distance_r))
        print("Average Distance 10 Player: "                +str(analyzer.average_distance_10p_r))
        print("Average Stamina 10 Player: "                 +str(analyzer.average_stamina_10p_r))
        print("Average Stamina Per distance 10 Player: "    +str(analyzer.av_st_per_dist_10p_r))
        print("Stamina per Distance: "                      +str(analyzer.used_per_distance_r))
        print('\n')

        print("Left Team: "                                 +analyzer.game.left_team.name+"\n")
        print("Game result: "                               +analyzer.status_l)
        print("Goals :"                                     +str(analyzer.game.left_goal))
        print("Possession: "                                +str(analyzer.possession_l))
        print("Pass Accuracy: "                             +str(analyzer.pass_accuracy_l))
        print("True Pass: "                                 +str(analyzer.pass_l))
        print("Wrong Pass: "                                +str(analyzer.intercept_r))
        print("On Target Shoot:"                            +str(analyzer.on_target_shoot_l))
        print("Off Target Shoot: "                          +str(analyzer.off_target_shoot_l))
        print("Shoot in Lenght: "                           +str(analyzer.shoot_in_length_l))
        print("Shoot in Width: "                            +str(analyzer.shoot_in_width_l))
        print("Shoot Accuracy: "                            +str(analyzer.shoot_accuracy_l))
        print("Stamina Usage: "                             +str(analyzer.used_stamina_agents_l))
        print("moved Distance: "                            +str(analyzer.team_moved_distance_l))
        print("Average Distance 10 Player: "                +str(analyzer.average_distance_10p_l))
        print("Average Stamina 10 Player: "                 +str(analyzer.average_stamina_10p_l))
        print("Average Stamina Per distance 10 Player: "    +str(analyzer.av_st_per_dist_10p_l))
        print("Stamina per Distance: "                      +str(analyzer.used_per_distance_l))
        print('\n')

        for column in df.columns:
            if((column=='name') or (column=='status')):
                continue
            print(column,' AVG =\t\t',df[column].mean())
            print(column,' STD =\t\t',df[column].std())


        winrate = 100*win_cnt/ctr
        print('winrate           = ', winrate)

    print(df)
    print('#################################################')
    print('directory finished and the report is as follows: ')

    for column in df.columns:
            print(column,'AVG =\t\t\t',df[column].mean())
            print(column,'STD =\t\t\t',df[column].std())
            
    winrate = win_cnt/ctr
    print('winrate                  = ', winrate)

    df.to_csv(myargs+'/details.csv')
