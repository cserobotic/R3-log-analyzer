# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
from sh import gunzip
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
                        "used_stamina_agents",
                        "team_moved_distance",
                        "average_distance_10p",
                        "average_stamina_10p",
                        "av_st_per_dist_10p",
                        "used_per_distance"])
                          
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
            "our_goals"            : analyzer.game.right_goal,
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
            "used_stamina_agents"   : analyzer.used_stamina_agents_r,
            "team_moved_distance"   : analyzer.team_moved_distance_r,
            "average_distance_10p"  : analyzer.average_distance_10p_r,
            "average_stamina_10p"   : analyzer.average_stamina_10p_r,
            "av_st_per_dist_10p"    : analyzer.av_st_per_dist_10p_r,
            "used_per_distance"     : analyzer.used_per_distance_r,
        }

        team_l = {
            "name"                  : analyzer.game.left_team.name,
            "status"                : analyzer.status_l,
            "our_goals"            : analyzer.game.left_goal,
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
            "used_stamina_agents"   : analyzer.used_stamina_agents_l,
            "team_moved_distance"   : analyzer.team_moved_distance_l,
            "average_distance_10p"  : analyzer.average_distance_10p_l,
            "average_stamina_10p"   : analyzer.average_stamina_10p_l,
            "av_st_per_dist_10p"    : analyzer.av_st_per_dist_10p_l,
            "used_per_distance"     : analyzer.used_per_distance_l,
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


        our_goals_avg            = df['our_goals'            ].mean()
        opp_goals_avg            = df['opp_goals'            ].mean()
        possession_avg           = df['possession'           ].mean()
        correct_pass_avg         = df['correct_pass'         ].mean()
        wrong_pass_avg           = df['wrong_pass'           ].mean()
        pass_accuracy_avg        = df['pass_accuracy'        ].mean()
        pass_in_length_avg       = df['pass_in_length'       ].mean()
        pass_in_width_avg        = df['pass_in_width'        ].mean()
        on_target_shoot_avg      = df['on_target_shoot'      ].mean()
        off_target_shoot_avg     = df['off_target_shoot'     ].mean()
        shoot_in_length_avg      = df['shoot_in_length'      ].mean()
        shoot_in_width_avg       = df['shoot_in_width'       ].mean()
        shoot_accuracy_avg       = df['shoot_accuracy'       ].mean()
        used_stamina_agents_avg  = df['used_stamina_agents'  ].mean()
        team_moved_distance_avg  = df['team_moved_distance'  ].mean()
        average_distance_10p_avg = df['average_distance_10p' ].mean()
        average_stamina_10p_avg  = df['average_stamina_10p'  ].mean()
        av_st_per_dist_10p_avg   = df['av_st_per_dist_10p'   ].mean()
        used_per_distance_avg    = df['used_per_distance'    ].mean()
        
        our_goals_std            = df['our_goals'            ].std()
        opp_goals_std            = df['opp_goals'            ].std()
        possession_std           = df['possession'           ].std()
        correct_pass_std         = df['correct_pass'         ].std()
        wrong_pass_std           = df['wrong_pass'           ].std()
        pass_accuracy_std        = df['pass_accuracy'        ].std()
        pass_in_length_std       = df['pass_in_length'       ].std()
        pass_in_width_std        = df['pass_in_width'        ].std()
        on_target_shoot_std      = df['on_target_shoot'      ].std()
        off_target_shoot_std     = df['off_target_shoot'     ].std()
        shoot_in_length_std      = df['shoot_in_length'      ].std()
        shoot_in_width_std       = df['shoot_in_width'       ].std()
        shoot_accuracy_std       = df['shoot_accuracy'       ].std()
        used_stamina_agents_std  = df['used_stamina_agents'  ].std()
        team_moved_distance_std  = df['team_moved_distance'  ].std()
        average_distance_10p_std = df['average_distance_10p' ].std()
        average_stamina_10p_std  = df['average_stamina_10p'  ].std()
        av_st_per_dist_10p_std   = df['av_st_per_dist_10p'   ].std()
        used_per_distance_std    = df['used_per_distance'    ].std()

        winrate = win_cnt/ctr
        
        print('################### AVERAGES')
        print('our_goals_avg            = ' , our_goals_avg            )
        print('opp_goals_avg            = ' , opp_goals_avg            )
        print('possession_avg           = ' , possession_avg           )
        print('correct_pass_avg         = ' , correct_pass_avg         )
        print('wrong_pass_avg           = ' , wrong_pass_avg           )
        print('pass_accuracy_avg        = ' , pass_accuracy_avg        )
        print('pass_in_length_avg       ='  , pass_in_length_avg       )
        print('pass_in_width_avg        ='  , pass_in_width_avg        )
        print('on_target_shoot_avg      ='  , on_target_shoot_avg      )
        print('off_target_shoot_avg     ='  , off_target_shoot_avg     )
        print('shoot_in_length_avg      ='  , shoot_in_length_avg      )
        print('shoot_in_width_avg       ='  , shoot_in_width_avg       )
        print('shoot_accuracy_avg       ='  , shoot_accuracy_avg       )
        print('used_stamina_agents_avg  ='  , used_stamina_agents_avg  )
        print('team_moved_distance_avg  ='  , team_moved_distance_avg  )
        print('average_distance_10p_avg ='  , average_distance_10p_avg )
        print('average_stamina_10p_avg  ='  , average_stamina_10p_avg  )
        print('av_st_per_dist_10p_avg   ='  , av_st_per_dist_10p_avg   )
        print('used_per_distance_avg    ='  , used_per_distance_avg    )

        print('################### stdIANCES')
        print('our_goals_std            = ' , our_goals_std            )
        print('opp_goals_std            = ' , opp_goals_std            )
        print('possession_std           = ' , possession_std           )
        print('correct_pass_std         = ' , correct_pass_std         )
        print('wrong_pass_std           = ' , wrong_pass_std           )
        print('pass_accuracy_std        = ' , pass_accuracy_std        )
        print('pass_in_length_std       = ' , pass_in_length_std       )
        print('pass_in_width_std        = ' , pass_in_width_std        )
        print('on_target_shoot_std      = ' , on_target_shoot_std      )
        print('off_target_shoot_std     = ' , off_target_shoot_std     )
        print('shoot_in_length_std      = ' , shoot_in_length_std      )
        print('shoot_in_width_std       = ' , shoot_in_width_std       )
        print('shoot_accuracy_std       = ' , shoot_accuracy_std       )
        print('used_stamina_agents_std  = ' , used_stamina_agents_std  )
        print('team_moved_distance_std  = ' , team_moved_distance_std  )
        print('average_distance_10p_std = ' , average_distance_10p_std )
        print('average_stamina_10p_std  = ' , average_stamina_10p_std  )
        print('av_st_per_dist_10p_std   = ' , av_st_per_dist_10p_std   )
        print('used_per_distance_std    = ' , used_per_distance_std    )

        print('winrate           = ', winrate)

    print(df)
    print('#################################################')
    print('directory finished and the report is as follows: ')

    our_goals_avg            = df['our_goals'            ].mean()
    opp_goals_avg            = df['opp_goals'            ].mean()
    possession_avg           = df['possession'           ].mean()
    correct_pass_avg         = df['correct_pass'         ].mean()
    wrong_pass_avg           = df['wrong_pass'           ].mean()
    pass_accuracy_avg        = df['pass_accuracy'        ].mean()
    pass_in_length_avg       = df['pass_in_length'       ].mean()
    pass_in_width_avg        = df['pass_in_width'        ].mean()
    on_target_shoot_avg      = df['on_target_shoot'      ].mean()
    off_target_shoot_avg     = df['off_target_shoot'     ].mean()
    shoot_in_length_avg      = df['shoot_in_length'      ].mean()
    shoot_in_width_avg       = df['shoot_in_width'       ].mean()
    shoot_accuracy_avg       = df['shoot_accuracy'       ].mean()
    used_stamina_agents_avg  = df['used_stamina_agents'  ].mean()
    team_moved_distance_avg  = df['team_moved_distance'  ].mean()
    average_distance_10p_avg = df['average_distance_10p' ].mean()
    average_stamina_10p_avg  = df['average_stamina_10p'  ].mean()
    av_st_per_dist_10p_avg   = df['av_st_per_dist_10p'   ].mean()
    used_per_distance_avg    = df['used_per_distance'    ].mean()
    
    our_goals_std            = df['our_goals'            ].std()
    opp_goals_std            = df['opp_goals'            ].std()
    possession_std           = df['possession'           ].std()
    correct_pass_std         = df['correct_pass'         ].std()
    wrong_pass_std           = df['wrong_pass'           ].std()
    pass_accuracy_std        = df['pass_accuracy'        ].std()
    pass_in_length_std       = df['pass_in_length'       ].std()
    pass_in_width_std        = df['pass_in_width'        ].std()
    on_target_shoot_std      = df['on_target_shoot'      ].std()
    off_target_shoot_std     = df['off_target_shoot'     ].std()
    shoot_in_length_std      = df['shoot_in_length'      ].std()
    shoot_in_width_std       = df['shoot_in_width'       ].std()
    shoot_accuracy_std       = df['shoot_accuracy'       ].std()
    used_stamina_agents_std  = df['used_stamina_agents'  ].std()
    team_moved_distance_std  = df['team_moved_distance'  ].std()
    average_distance_10p_std = df['average_distance_10p' ].std()
    average_stamina_10p_std  = df['average_stamina_10p'  ].std()
    av_st_per_dist_10p_std   = df['av_st_per_dist_10p'   ].std()
    used_per_distance_std    = df['used_per_distance'    ].std()

    winrate = win_cnt/ctr
    
    print('################### AVERAGES')
    print('our_goals_avg            = ' , our_goals_avg            )
    print('opp_goals_avg            = ' , opp_goals_avg            )
    print('possession_avg           = ' , possession_avg           )
    print('correct_pass_avg         = ' , correct_pass_avg         )
    print('wrong_pass_avg           = ' , wrong_pass_avg           )
    print('pass_accuracy_avg        = ' , pass_accuracy_avg        )
    print('pass_in_length_avg       ='  , pass_in_length_avg       )
    print('pass_in_width_avg        ='  , pass_in_width_avg        )
    print('on_target_shoot_avg      ='  , on_target_shoot_avg      )
    print('off_target_shoot_avg     ='  , off_target_shoot_avg     )
    print('shoot_in_length_avg      ='  , shoot_in_length_avg      )
    print('shoot_in_width_avg       ='  , shoot_in_width_avg       )
    print('shoot_accuracy_avg       ='  , shoot_accuracy_avg       )
    print('used_stamina_agents_avg  ='  , used_stamina_agents_avg  )
    print('team_moved_distance_avg  ='  , team_moved_distance_avg  )
    print('average_distance_10p_avg ='  , average_distance_10p_avg )
    print('average_stamina_10p_avg  ='  , average_stamina_10p_avg  )
    print('av_st_per_dist_10p_avg   ='  , av_st_per_dist_10p_avg   )
    print('used_per_distance_avg    ='  , used_per_distance_avg    )

    print('################### STANDARD DEVIATIONS')
    print('our_goals_std            = ' , our_goals_std            )
    print('opp_goals_std            = ' , opp_goals_std            )
    print('possession_std           = ' , possession_std           )
    print('correct_pass_std         = ' , correct_pass_std         )
    print('wrong_pass_std           = ' , wrong_pass_std           )
    print('pass_accuracy_std        = ' , pass_accuracy_std        )
    print('pass_in_length_std       = ' , pass_in_length_std       )
    print('pass_in_width_std        = ' , pass_in_width_std        )
    print('on_target_shoot_std      = ' , on_target_shoot_std      )
    print('off_target_shoot_std     = ' , off_target_shoot_std     )
    print('shoot_in_length_std      = ' , shoot_in_length_std      )
    print('shoot_in_width_std       = ' , shoot_in_width_std       )
    print('shoot_accuracy_std       = ' , shoot_accuracy_std       )
    print('used_stamina_agents_std  = ' , used_stamina_agents_std  )
    print('team_moved_distance_std  = ' , team_moved_distance_std  )
    print('average_distance_10p_std = ' , average_distance_10p_std )
    print('average_stamina_10p_std  = ' , average_stamina_10p_std  )
    print('av_st_per_dist_10p_std   = ' , av_st_per_dist_10p_std   )
    print('used_per_distance_std    = ' , used_per_distance_std    )

    print('winrate                  = ', winrate)

    df.to_csv(myargs+'/details.csv')

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
